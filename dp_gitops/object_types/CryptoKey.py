from jinja2 import Environment, StrictUndefined

class CryptoKey:
  __JINJA2_CFG_TEMPLATE = """crypto
  {% if description is defined %}# {{ description }}{% endif %}
  key "{{ name }}"
  admin-state {{ mAdminState }}
  "{{ Filename }}"
exit
"""

  __DEFAULT_PROPS = {
}

  def __init__(self):
    self.state = dict()

  def to_cfg(self):
    combined_state = CryptoKey.__DEFAULT_PROPS.copy()
    combined_state.update(self.state)
    env = Environment(undefined=StrictUndefined)
    t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
    return t.render(combined_state)

def main():
  crypto_key = CryptoKey()
  crypto_key.state = {
    "name": "test_key",
    "mAdminState": "enabled",
    "Filename": "cert:///key.pem"
  }
  print(crypto_key.to_cfg())

if __name__ == '__main__':
  main()