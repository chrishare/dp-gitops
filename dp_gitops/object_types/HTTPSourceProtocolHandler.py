from jinja2 import Environment, StrictUndefined

class HTTPSourceProtocolHandler:
  __JINJA2_CFG_TEMPLATE = """source-http "{{ name }}"
  {% if description is defined %}# {{ description }}{% endif %}
  local-address {{ LocalAddress }}
  port {{ LocalPort }}
  http-client-version {{ HTTPVersion }}
  allowed-features "{% set adder = joiner("+") %}{% for feature, status in AllowedFeatures.items() %}{% if status == 'on' %}{{ adder() }}{{ feature }}{% endif %}{% endfor %}" 
  {{ "no " if PersistentConnections != 'on' else "" }}persistent-connections 
  max-persistent-reuse {{ MaxPersistentConnectionsReuse }}
  {{ "no " if AllowCompression != 'on' else "" }}compression
  {{ "no " if AllowWebSocketUpgrade != 'on' else "" }}websocket-upgrade 
  websocket-idle-timeout {{ WebSocketIdleTimeout }}
  max-url-len {{ MaxURLLen }}
  max-total-header-len {{ MaxTotalHdrLen }}
  max-header-count {{ MaxHdrCount }}
  max-header-name-len {{ MaxNameHdrLen }}
  max-header-value-len {{ MaxValueHdrLen }}
  max-querystring-len {{ MaxQueryStringLen }}
  credential-charset {{ CredentialCharset }}
  http2-max-streams {{ HTTP2MaxStreams }}
  http2-max-frame {{ HTTP2MaxFrameSize }}
  {{ "no " if HTTP2StreamHeader != 'on' else "" }}http2-stream-header 
  {{ "no " if ChunkedEncoding != 'on' else "" }}chunked-encoding 
exit
"""

  __DEFAULT_PROPS = {
  "HTTPVersion": "HTTP/1.1",
  "AllowedFeatures": {
    "HTTP-1.0": "on",
    "HTTP-1.1": "on",
    "HTTP-2.0": "off",
    "POST": "on",
    "GET": "off",
    "PUT": "on",
    "PATCH": "off",
    "HEAD": "off",
    "OPTIONS": "off",
    "TRACE": "off",
    "DELETE": "off",
    "CONNECT": "off",
    "CustomMethods": "off",
    "QueryString": "on",
    "FragmentIdentifiers": "on",
    "DotDot": "off",
    "DotDotInPath": "off",
    "DotDotInQueryString": "off",
    "CmdExe": "off"
  },
  "PersistentConnections": "off",
  "MaxPersistentConnectionsReuse": 0,
  "AllowCompression": "off",
  "AllowWebSocketUpgrade": "off",
  "WebSocketIdleTimeout": 0,
  "MaxURLLen": 16384,
  "MaxTotalHdrLen": 128000,
  "MaxHdrCount": 0,
  "MaxNameHdrLen": 0,
  "MaxValueHdrLen": 0,
  "MaxQueryStringLen": 0,
  "CredentialCharset": "protocol",
  "HTTP2MaxStreams": 100,
  "HTTP2MaxFrameSize": 16384,
  "HTTP2StreamHeader": "off",
  "ChunkedEncoding": "on"
}

  def __init__(self):
    self.state = dict()

  def to_cfg(self):
    combined_state = HTTPSourceProtocolHandler.__DEFAULT_PROPS.copy()
    combined_state.update(self.state)
    env = Environment(undefined=StrictUndefined)
    t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
    return t.render(combined_state)

def main():
  http_source_protocol_handler = HTTPSourceProtocolHandler()
  http_source_protocol_handler.state = {
    "name": "test_http_handler",
    "mAdminState": "enabled",
    "LocalAddress": "0.0.0.0",
    "LocalPort": 80,
    "HTTPVersion": "HTTP/1.1",
    "AllowedFeatures": {
        "HTTP-1.0": "on",
        "HTTP-1.1": "on",
        "POST": "on",
        "PUT": "on",
        "QueryString": "on",
        "FragmentIdentifiers": "on"
    }
  }
  print(http_source_protocol_handler.to_cfg())

if __name__ == '__main__':
  main()