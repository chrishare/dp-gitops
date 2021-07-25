from jinja2 import Environment, StrictUndefined
from os import getcwd, path
from dp_gitops.object_types import HTTPSourceProtocolHandler
from pathlib import Path

def render_cfg(cfg_name, custom_configuration_dict):
  """ Perform jinja2 rendering using template from ./startup_cfg_templates/<cfg_name>
    and variables from custom_configuration_dict.
    custom_configuration_dict should be a dictionary with keys for any objects
    that should be represented in the auto_startup.cfg file. For instance, 
    custom_configuration_dict['HTTPSourceprotocolHandler'] should contain the 
    cfg-formatted text representation of the config to include. 
  """
  with open(path.join(getcwd(), 'startup_cfg_templates', cfg_name, 'auto-startup.cfg')) as reader:
    auto_startup_template = reader.read()
    env = Environment(undefined=StrictUndefined)
    t = env.from_string(auto_startup_template)
    return t.render(custom_configuration_dict)

def test():
  input_dict = {
    "name": "test_http_handler",
    "mAdminState": "enabled",
    "LocalAddress": "0.0.0.0",
    "LocalPort": 80
  }
  httpsourceprotocolhandler_cfg = HTTPSourceProtocolHandler.dict_to_cfg(input_dict)
  print(httpsourceprotocolhandler_cfg)
  custom_configuration_dict = dict()
  custom_configuration_dict['HTTPSourceProtocolHandler'] = httpsourceprotocolhandler_cfg
  result = render_cfg('insecure_bare_docker_10_0_3', custom_configuration_dict)
  Path('./tmp-data').mkdir(parents=True, exist_ok=True)
  with open(Path('./tmp-data/auto-startup.cfg'), 'a') as writer:
    writer.write(result)

def main():
  test()

if __name__ == '__main__':
  main()
