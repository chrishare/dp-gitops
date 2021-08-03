from collections import defaultdict
from jinja2 import Template, Environment, StrictUndefined
import yaml
from os import getcwd, path

default_dict = {
        "PolicyReferences": "on",
        "SLAEnforcementMode": "allow-if-no-sla"
    }

simple_example = {
    "name": "test_mpgw",
        "mAdminState": "enabled",
        "EnforcementMode": "enforce"
}

jinja2_cfg_template = """
policy-attachments "{{ name }}"
  admin-state {{ mAdminState }}
  enforcement-mode {{ EnforcementMode }}
  {{ "no " if PolicyReferences != 'on' else "" }}policy-references 
  sla-enforcement-mode {{ SLAEnforcementMode }}
exit
"""

def dict_to_cfg(input_dict):
  with open('./object-defaults/HTTPSourceProtocolHandler.yml') as reader:
    render_dict = yaml.safe_load(reader.read())
  print(render_dict)
  render_dict.update(input_dict)
  print(render_dict)
  env = Environment(undefined=StrictUndefined)
  t = env.from_string(jinja2_cfg_template)
  return t.render(render_dict)

def main():
  print(dict_to_cfg(short_example))

if __name__ == '__main__':
  main()