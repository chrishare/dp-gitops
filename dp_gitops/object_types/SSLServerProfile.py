from jinja2 import Environment, StrictUndefined


class SSLServerProfile:
    __JINJA2_CFG_TEMPLATE = """crypto
ssl-server "{{ name }}"
  {% if description is defined %}# {{ description }}{% endif %}
  protocols "{% set adder = joiner("+") %}{% for protocol, status in Protocols.items() %}{% if status == 'on' %}{{ adder() }}{{ protocol }}{% endif %}{% endfor %}" 
  {% for cipher in Ciphers %}ciphers {{ cipher }}
  {% endfor -%}
  idcred {{ Idcred.value }}
  {{ "no " if RequestClientAuth != 'on' else "" }}request-client-auth
  {{ "no " if RequireClientAuth != 'on' else "" }}require-client-auth
  {{ "no " if ValidateClientCert != 'on' else "" }}validate-client-cert 
  {{ "no " if SendClientAuthCAList != 'on' else "" }}send-client-auth-ca-list 
  {{ "no " if Caching != 'on' else "" }}caching 
  cache-timeout {{ CacheTimeout }}
  cache-size {{ CacheSize }}
  ssl-options "{% set adder = joiner("+") %}{% for option, status in SSLOptions.items() %}{% if status == 'on' %}{{ adder() }}{{ option }}{% endif %}{% endfor %}" 
  max-duration {{ MaxSSLDuration }}
  max-renegotiation-allowed {{ NumberOfRenegotiationAllowed }}
  {{ "no " if ProhibitResumeOnReneg != 'on' else "" }}prohibit-resume-on-reneg 
  {{ "no " if Compression != 'on' else "" }}compression 
  {{ "no " if AllowLegacyRenegotiation != 'on' else "" }}allow-legacy-renegotiation 
  {{ "no " if PreferServerCiphers != 'on' else "" }}prefer-server-ciphers
  {% for curve in EllipticCurves %}curves {{ curve }}
  {% endfor -%}
  {{ "no " if PrioritizeChaCha != 'on' else "" }}prioritize-chacha 
exit
"""

    __DEFAULT_PROPS = {
        "RequestClientAuth": "off",
        "RequireClientAuth": "on",
        "ValidateClientCert": "on",
        "SendClientAuthCAList": "on",
        "Caching": "on",
        "CacheTimeout": 300,
        "CacheSize": 20,
        "SSLOptions": {
            "max-duration": "off",
            "max-renegotiation": "off"
        },
        "MaxSSLDuration": 60,
        "NumberOfRenegotiationAllowed": 0,
        "ProhibitResumeOnReneg": "off",
        "Compression": "off",
        "AllowLegacyRenegotiation": "off",
        "PreferServerCiphers": "on",
        "EllipticCurves": [
            "secp521r1",
            "secp384r1",
            "secp256k1",
            "secp256r1"
        ],
        "PrioritizeChaCha": "off"
    }

    def __init__(self):
        self.state = dict()

    def to_cfg(self):
        combined_state = SSLServerProfile.__DEFAULT_PROPS.copy()
        combined_state.update(self.state)
        env = Environment(undefined=StrictUndefined)
        t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
        return t.render(combined_state)


def main():
    ssl_server_profile = SSLServerProfile()
    ssl_server_profile.state = {
        "name": "test_ssl_profile",
        "mAdminState": "enabled",
        "Idcred": {
            "value": "test_idcred"
        },
        "Protocols": {
            "SSLv3": "off",
            "TLSv1d0": "off",
            "TLSv1d1": "off",
            "TLSv1d2": "off",
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
        ]
    }
    print(ssl_server_profile.to_cfg())


if __name__ == '__main__':
    main()
