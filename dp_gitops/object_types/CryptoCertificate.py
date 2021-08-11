from jinja2 import Environment, StrictUndefined

class CryptoCertificate:
  __JINJA2_CFG_TEMPLATE = """crypto
  certificate "{{ name }}"
  admin-state {{ mAdminState }}
  "{{ Filename }}"
  {{ "ignore-expiration" if IgnoreExpiration == 'on' else "" -}}
exit
"""

  __DEFAULT_PROPS = {
    "IgnoreExpiration": "off"
}

  def __init__(self):
    self.state = dict()

  def to_cfg(self):
    combined_state = CryptoCertificate.__DEFAULT_PROPS.copy()
    combined_state.update(self.state)
    env = Environment(undefined=StrictUndefined)
    t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
    return t.render(combined_state)

def main():
  crypto_certificate = CryptoCertificate()
  crypto_certificate.state = {
    "name": "test_cer",
    "mAdminState": "enabled",
    "Filename": "cert:///cert.pem"
  }
  print(crypto_certificate.to_cfg())

if __name__ == '__main__':
  main()