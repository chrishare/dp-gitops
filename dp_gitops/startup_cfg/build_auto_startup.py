from jinja2 import Environment, StrictUndefined
from os import getcwd, listdir
from shutil import rmtree
from os.path import join, isfile
from dp_gitops.object_types.HTTPSourceProtocolHandler import HTTPSourceProtocolHandler
from dp_gitops.object_types.MultiProtocolGateway import MultiProtocolGateway
from dp_gitops.object_types.CryptoCertificate import CryptoCertificate
from dp_gitops.object_types.CryptoIdentCred import CryptoIdentCred
from dp_gitops.object_types.CryptoKey import CryptoKey
from dp_gitops.object_types.PolicyAttachment import PolicyAttachment
from dp_gitops.object_types.SSLClientProfile import SSLClientProfile
from dp_gitops.object_types.StylePolicy import StylePolicy
from dp_gitops.object_types.StylePolicyRule import StylePolicyRule
from dp_gitops.object_types.StylePolicyAction import StylePolicyAction
from pathlib import Path
import yaml

"""
Example run:

python3 -m dp_gitops.startup_cfg.build_auto_startup

"""
def render_cfg(cfg_name, custom_configuration_dict):
  """ Perform jinja2 rendering using template from ./startup_cfg_templates/<cfg_name>
    and variables from custom_configuration_dict.
    custom_configuration_dict should be a dictionary with keys for any objects
    that should be represented in the auto_startup.cfg file. For instance, 
    custom_configuration_dict['HTTPSourceprotocolHandler'] should contain the 
    cfg-formatted text representation of the config to include. 
  """
  with open(join(getcwd(), 'startup_cfg_templates', cfg_name, 'auto-startup.cfg')) as reader:
    auto_startup_template = reader.read()
    env = Environment(undefined=StrictUndefined)
    t = env.from_string(auto_startup_template)
    return t.render(custom_configuration_dict)

def add_custom_configuration(custom_configuration_dict, environment_variables, repository_path, dp_object_name, dp_object_class):
  custom_configuration_dict[dp_object_name] = ""
  object_directory = join(repository_path, dp_object_name)
  try:
    for entry in listdir(object_directory):
      entry_path = join(object_directory, entry)
      if isfile(entry_path):
        with open(entry_path) as entry_file:
          entry_string = entry_file.read()
          jinja2_env = Environment(undefined=StrictUndefined)
          t = jinja2_env.from_string(entry_string)
          rendered_string = t.render(environment_variables)
          #print(rendered_string)
          entry_dict = yaml.load(rendered_string, Loader=yaml.FullLoader)
          #print(entry_dict)
          dp_object = dp_object_class()
          dp_object.state = entry_dict
          dp_object_cfg = dp_object.to_cfg()
          custom_configuration_dict[dp_object_name] = custom_configuration_dict[dp_object_name] + '\r\n' + dp_object_cfg
  except FileNotFoundError as error:
    pass

def build_from_repository(configuration_data_path, environment, startup_cfg_template, build_output_path):
  repository_path = join(configuration_data_path, "repository")
  environment_path = join(configuration_data_path, "environment", environment)

  """
  - Get environment-specific yaml dict(s) to produce environment dict
  - List MPGW repository files
  - For each MPGW repo file
  -- Read the repo file as a string
  -- jinja2 render {{ }}
  -- Read to yaml
  -- Build MPGW object
  - Build auto_startup_cfg using objects
  """
  # Get all environment variables - read every yaml under the right environment folder, and merge into a single dict
  environment_variables = dict()
  for entry in listdir(environment_path):
    entry_path = join(environment_path, entry)
    if isfile(entry_path):
      with open(entry_path) as entry_file:
        entry_dict = yaml.load(entry_file, Loader=yaml.FullLoader)
        environment_variables.update(entry_dict)
  # We need a dict that contains config for all object types
  custom_configuration_dict = dict()
  # For each instance of each object type, read our custom configuration and update the environment specific parts
  # Order doesn't matter in the code - the order or objects is set by the config template
  add_custom_configuration(custom_configuration_dict, environment_variables, repository_path, 'MultiProtocolGateway', MultiProtocolGateway)
  add_custom_configuration(custom_configuration_dict, environment_variables, repository_path, 'StylePolicy', StylePolicy)
  add_custom_configuration(custom_configuration_dict, environment_variables, repository_path, 'CryptoCertificate', CryptoCertificate)
  add_custom_configuration(custom_configuration_dict, environment_variables, repository_path, 'CryptoIdentCred', CryptoIdentCred)
  add_custom_configuration(custom_configuration_dict, environment_variables, repository_path, 'CryptoKey', CryptoKey)
  add_custom_configuration(custom_configuration_dict, environment_variables, repository_path, 'HTTPSourceProtocolHandler', HTTPSourceProtocolHandler)
  add_custom_configuration(custom_configuration_dict, environment_variables, repository_path, 'SSLClientProfile', SSLClientProfile)
  add_custom_configuration(custom_configuration_dict, environment_variables, repository_path, 'PolicyAttachment', PolicyAttachment)
  add_custom_configuration(custom_configuration_dict, environment_variables, repository_path, 'StylePolicyRule', StylePolicyRule)
  add_custom_configuration(custom_configuration_dict, environment_variables, repository_path, 'StylePolicyAction', StylePolicyAction)
  add_custom_configuration(custom_configuration_dict, environment_variables, repository_path, 'StylePolicy', StylePolicy)

  # Render auto_startup.cfg
  startup_cfg_content = render_cfg(startup_cfg_template, custom_configuration_dict)
  # Write rendered output to build directory
  print("Here A")
  try:
    rmtree(build_output_path)
  except FileNotFoundError:
    pass
  print("Here B")
  Path(build_output_path).mkdir(parents=True, exist_ok=True)
  print(join(build_output_path, 'auto-startup.cfg'))
  with open(join(build_output_path, 'auto-startup.cfg'), 'w') as writer:
    writer.write(startup_cfg_content)

def main():
  configuration_data_path = './builds/simple_mpgw'
  environment = 'development'
  build_output_path = './builds/simple_mpgw/output/' + environment
  startup_cfg_template = 'insecure_bare_docker_10_0_3'
  build_from_repository(configuration_data_path, environment, startup_cfg_template, build_output_path)

if __name__ == '__main__':
  main()
