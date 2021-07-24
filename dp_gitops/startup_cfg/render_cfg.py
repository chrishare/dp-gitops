from jinja2 import Template, Environment, StrictUndefined
from os import getcwd, path
from dp_gitops.object_types.HTTPSourceProtocolHandler import dict_to_cfg

def render_cfg(cfg_name, custom_configuration_dict):
  with open(path.join(getcwd(), 'startup_cfg', cfg_name, 'auto-startup.cfg')) as reader:
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
  httpsourceprotocolhandler_cfg = dict_to_cfg(input_dict)
  print(httpsourceprotocolhandler_cfg)
  custom_configuration_dict = dict()
  custom_configuration_dict['custom_HTTPSourceProtocolHandler'] = httpsourceprotocolhandler_cfg
  result = render_cfg('bare_docker_10_0_3', custom_configuration_dict)
  print(result)

def main():
  test()

if __name__ == '__main__':
  main()
