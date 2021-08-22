from jinja2 import Environment, StrictUndefined

class SSLClientProfile:
  __JINJA2_CFG_TEMPLATE = """crypto
ssl-client "{{ name }}"
  {% if description is defined %}# {{ description }}{% endif %}
  admin-state {{ mAdminState }}
  protocols "{% set adder = joiner("+") %}{% for protocol, status in Protocols.items() %}{% if status == 'on' %}{{ adder() }}{{ protocol }}{% endif %}{% endfor %}" 
  {% for cipher in Ciphers %}ciphers {{ cipher }}
  {% endfor -%}
  idcred {{ Idcred.value }}
  {{ "no " if ValidateServerCert != 'on' else "" }}validate-server-cert
  {{ "no " if Caching != 'on' else "" }}caching
  cache-timeout {{ CacheTimeout }}
  cache-size {{ CacheSize }}
  ssl-client-features "{% set adder = joiner("+") %}{% for feature, status in SSLClientFeatures.items() %}{% if status == 'on' %}{{ adder() }}{{ feature }}{% endif %}{% endfor %}" 
  {% for curve in EllipticCurves %}curves {{ curve }}
  {% endfor -%}
  use-custom-sni-hostname {{ UseCustomSNIHostname }}
  {{ "no " if ValidateHostname != 'on' else "" }}validate-hostname 
  hostname-validation-flags "{% set adder = joiner("+") %}{% for flag, status in HostnameValidationFlags.items() %}{% if status == 'on' %}{{ adder() }}{{ flag }}{% endif %}{% endfor %}" 
  {{ "no " if HostnameValidationFailOnError != 'on' else "" }}hostname-validation-fail 
  {{ "no " if EnableTLS13Compat != 'on' else "" }}enable-tls13-compat 
exit
"""

  __DEFAULT_PROPS = {
    "Protocols": {
        "SSLv3": "off",
        "TLSv1d0": "off",
        "TLSv1d1": "off",
        "TLSv1d2": "on",
        "TLSv1d3": "on"
    },
    "Ciphers": [
        "AES_256_GCM_SHA384",
        "CHACHA20_POLY1305_SHA256",
        "AES_128_GCM_SHA256",
        "ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
        "ECDHE_RSA_WITH_AES_256_GCM_SHA384",
        "ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
        "ECDHE_RSA_WITH_AES_256_CBC_SHA384",
        "ECDHE_ECDSA_WITH_AES_256_CBC_SHA",
        "ECDHE_RSA_WITH_AES_256_CBC_SHA",
        "DHE_DSS_WITH_AES_256_GCM_SHA384",
        "DHE_RSA_WITH_AES_256_GCM_SHA384",
        "DHE_RSA_WITH_AES_256_CBC_SHA256",
        "DHE_DSS_WITH_AES_256_CBC_SHA256",
        "DHE_RSA_WITH_AES_256_CBC_SHA",
        "DHE_DSS_WITH_AES_256_CBC_SHA",
        "RSA_WITH_AES_256_GCM_SHA384",
        "RSA_WITH_AES_256_CBC_SHA256",
        "RSA_WITH_AES_256_CBC_SHA",
        "ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
        "ECDHE_RSA_WITH_AES_128_GCM_SHA256",
        "ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
        "ECDHE_RSA_WITH_AES_128_CBC_SHA256",
        "ECDHE_ECDSA_WITH_AES_128_CBC_SHA",
        "ECDHE_RSA_WITH_AES_128_CBC_SHA",
        "DHE_DSS_WITH_AES_128_GCM_SHA256",
        "DHE_RSA_WITH_AES_128_GCM_SHA256",
        "DHE_RSA_WITH_AES_128_CBC_SHA256",
        "DHE_DSS_WITH_AES_128_CBC_SHA256",
        "DHE_RSA_WITH_AES_128_CBC_SHA",
        "DHE_DSS_WITH_AES_128_CBC_SHA",
        "RSA_WITH_AES_128_GCM_SHA256",
        "RSA_WITH_AES_128_CBC_SHA256",
        "RSA_WITH_AES_128_CBC_SHA"
    ],
    "Caching": "on",
    "CacheTimeout": 300,
    "CacheSize": 100,
    "SSLClientFeatures": {
        "use-sni": "on",
        "permit-insecure-servers": "off",
        "compression": "off"
    },
    "EllipticCurves": [
        "secp521r1",
        "secp384r1",
        "secp256k1",
        "secp256r1"
    ],
    "UseCustomSNIHostname": "no",
    "ValidateHostname": "off",
    "HostnameValidationFlags": {
        "X509_CHECK_FLAG_ALWAYS_CHECK_SUBJECT": "off",
        "X509_CHECK_FLAG_NO_WILDCARDS": "off",
        "X509_CHECK_FLAG_NO_PARTIAL_WILDCARDS": "off",
        "X509_CHECK_FLAG_MULTI_LABEL_WILDCARDS": "off",
        "X509_CHECK_FLAG_SINGLE_LABEL_SUBDOMAINS": "off"
    },
    "HostnameValidationFailOnError": "off",
    "EnableTLS13Compat": "on"
}

  def __init__(self):
    self.state = dict()

  def to_cfg(self):
    combined_state = SSLClientProfile.__DEFAULT_PROPS.copy()
    combined_state.update(self.state)
    env = Environment(undefined=StrictUndefined)
    t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
    return t.render(combined_state)

def main():
  ssl_client_profile = SSLClientProfile()
  ssl_client_profile.state = {
    "name": "test_tls_client_profile",
    "mAdminState": "enabled",
    "Idcred": {
        "value": "test_idcred"
    },
    "ValidateServerCert": "off"
  }
  print(ssl_client_profile.to_cfg())

if __name__ == '__main__':
  main()