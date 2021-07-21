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


"""


TODO: Find equivalent rest form - maybe that is nice?