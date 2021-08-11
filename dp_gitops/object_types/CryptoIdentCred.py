from jinja2 import Environment, StrictUndefined

class CryptoIdentCred:
  __JINJA2_CFG_TEMPLATE = """crypto
  idcred "{{ name }}" "{{ Key.value }}" "{{ Certificate.value }}"
  admin-state {{ mAdminState }}
exit
"""

  __DEFAULT_PROPS = {
}

  def __init__(self):
    self.state = dict()

  def to_cfg(self):
    combined_state = CryptoIdentCred.__DEFAULT_PROPS.copy()
    combined_state.update(self.state)
    env = Environment(undefined=StrictUndefined)
    t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
    return t.render(combined_state)

def main():
  crypto_ident_cred = CryptoIdentCred()
  crypto_ident_cred.state = {
    "name": "test_idcred",
    "mAdminState": "enabled",
    "Key": {
        "value": "cert:///key.pem"
    },
    "Certificate": {
        "value": "cert:///cert.pem"
    }
  }
  print(crypto_ident_cred.to_cfg())

if __name__ == '__main__':
  main()