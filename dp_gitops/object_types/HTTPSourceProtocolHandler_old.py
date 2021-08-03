from collections import defaultdict
from jinja2 import Template, Environment, StrictUndefined
import yaml
from os import getcwd, path

"""
%if% available "source-http"

source-http "test_http_fsh"
  local-address 0.0.0.0
  port 80
  http-client-version HTTP/1.1
  allowed-features "HTTP-1.0+HTTP-1.1+POST+PUT+QueryString+FragmentIdentifiers" 
  persistent-connections 
  max-persistent-reuse 0
  no compression 
  no websocket-upgrade 
  websocket-idle-timeout 0
  max-url-len 16384
  max-total-header-len 128000
  max-header-count 0
  max-header-name-len 0
  max-header-value-len 0
  max-querystring-len 0
  credential-charset protocol
  http2-max-streams 100
  http2-max-frame 16384
  no http2-stream-header 
  chunked-encoding 
exit

source-http "test_http_fsh_two"
  local-address 0.0.0.0
  port 81
  http-client-version HTTP/1.1
  allowed-features "HTTP-1.0+HTTP-1.1+POST+PUT+QueryString+FragmentIdentifiers" 
  persistent-connections 
  max-persistent-reuse 0
  no compression 
  no websocket-upgrade 
  websocket-idle-timeout 0
  max-url-len 16384
  max-total-header-len 128000
  max-header-count 0
  max-header-name-len 200
  max-header-value-len 0
  max-querystring-len 0
  credential-charset protocol
  http2-max-streams 100
  http2-max-frame 16384
  http2-stream-header 
  chunked-encoding 
exit

%endif%


Equivalent SOMA XML:
<HTTPSourceProtocolHandler name="test_http_handler" xmlns:env="http://www.w3.org/2003/05/soap-envelope">
               <mAdminState>enabled</mAdminState>
               <LocalAddress>0.0.0.0</LocalAddress>
               <LocalPort>80</LocalPort>
               <HTTPVersion>HTTP/1.1</HTTPVersion>
               <AllowedFeatures>
                  <HTTP-1.0>on</HTTP-1.0>
                  <HTTP-1.1>on</HTTP-1.1>
                  <HTTP-2.0>off</HTTP-2.0>
                  <POST>on</POST>
                  <GET>off</GET>
                  <PUT>on</PUT>
                  <PATCH>off</PATCH>
                  <HEAD>off</HEAD>
                  <OPTIONS>off</OPTIONS>
                  <TRACE>off</TRACE>
                  <DELETE>off</DELETE>
                  <CONNECT>off</CONNECT>
                  <CustomMethods>off</CustomMethods>
                  <QueryString>on</QueryString>
                  <FragmentIdentifiers>on</FragmentIdentifiers>
                  <DotDot>off</DotDot>
                  <DotDotInPath>off</DotDotInPath>
                  <DotDotInQueryString>off</DotDotInQueryString>
                  <CmdExe>off</CmdExe>
               </AllowedFeatures>
               <PersistentConnections>on</PersistentConnections>
               <MaxPersistentConnectionsReuse>0</MaxPersistentConnectionsReuse>
               <AllowCompression>off</AllowCompression>
               <AllowWebSocketUpgrade>off</AllowWebSocketUpgrade>
               <WebSocketIdleTimeout>0</WebSocketIdleTimeout>
               <MaxURLLen>16384</MaxURLLen>
               <MaxTotalHdrLen>128000</MaxTotalHdrLen>
               <MaxHdrCount>0</MaxHdrCount>
               <MaxNameHdrLen>0</MaxNameHdrLen>
               <MaxValueHdrLen>0</MaxValueHdrLen>
               <MaxQueryStringLen>0</MaxQueryStringLen>
               <CredentialCharset>protocol</CredentialCharset>
               <HTTP2MaxStreams>100</HTTP2MaxStreams>
               <HTTP2MaxFrameSize>16384</HTTP2MaxFrameSize>
               <HTTP2StreamHeader>off</HTTP2StreamHeader>
               <ChunkedEncoding>off</ChunkedEncoding>
            </HTTPSourceProtocolHandler>


Equivalent HTTPHandler REST
"HTTPSourceProtocolHandler": {
        "name": "test_http_handler",
        "mAdminState": "enabled",
        "LocalAddress": "0.0.0.0",
        "LocalPort": 80,
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
        "PersistentConnections": "on",
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
"""

default_dict = {
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

short_example = {
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

simple_example = {
        "name": "test_http_handler",
        "mAdminState": "enabled",
        "LocalAddress": "0.0.0.0",
        "LocalPort": 80,
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
        "XMaxURLLen": 16384,
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

unused_jinja2_cfg_template_with_embedded_logic = """
source-http "{{ name }}"
  local-address {{ LocalAddress }}
  port {{ LocalPort }}
  http-client-version {{ HTTPVersion }}
  allowed-features "{% set adder = joiner("+") %}{% for feature, status in AllowedFeatures.items() %}{% if status == 'on' %}{{ adder() }}{{ feature }}{% endif %}{% endfor %}" 
  {{ "no " if PersistentConnections | default('off') != 'on' else "" }}persistent-connections 
  max-persistent-reuse {{ MaxPersistentConnectionsReuse | default(0) }}
  {{ "no " if AllowCompression != 'on' else "" }}compression
  {{ "no " if AllowWebSocketUpgrade != 'on' else "" }}websocket-upgrade 
  websocket-idle-timeout {{ WebSocketIdleTimeout | default(0) }}
  max-url-len {{ MaxURLLen | default(16384) }}
  max-total-header-len {{ MaxTotalHdrLen | default(128000) }}
  max-header-count {{ MaxHdrCount | default(0) }}
  max-header-name-len {{ MaxNameHdrLen | default(0) }}
  max-header-value-len {{ MaxValueHdrLen | default(0) }}
  max-querystring-len {{ MaxQueryStringLen | default(0) }}
  credential-charset {{ CredentialCharset | default(protocol) }}
  http2-max-streams {{ HTTP2MaxStreams | default(100) }}
  http2-max-frame {{ HTTP2MaxFrameSize | default(16384) }}
  {{ "no " if HTTP2StreamHeader != 'on' else "" }}http2-stream-header 
  {{ "no " if ChunkedEncoding != 'on' else "" }}chunked-encoding 
exit
"""

jinja2_cfg_template = """
source-http "{{ name }}"
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