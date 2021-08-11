from jinja2 import Environment, StrictUndefined

class MultiProtocolGateway:
  __JINJA2_CFG_TEMPLATE = """mpgw "{{ name }}"
  no policy-parameters
  admin-state {{ mAdminState }}
  summary "{{ UserSummary }}"
  priority {{ Priority }}
  front-protocol {{ FrontProtocol.value }}
  xml-manager {{ XMLManager.value }}
  ssl-client-type {{ SSLClientConfigType }}
  default-param-namespace "{{ DefaultParamNamespace }}"
  query-param-namespace "{{ QueryParamNamespace }}"
  backend-url "{{ BackendUrl }}"
  {{ "no " if PropagateURI != 'on' else "" }}propagate-uri 
  monitor-processing-policy {{ MonitorProcessingPolicy }}
  request-attachments {{ RequestAttachments }}
  response-attachments {{ ResponseAttachments }}
  {{ "no " if RequestAttachmentsFlowControl != 'on' else "" }}request-attachments-flow-control 
  {{ "no " if ResponseAttachmentsFlowControl != 'on' else "" }}response-attachments-flow-control 
  root-part-not-first-action {{ RootPartNotFirstAction }}
  front-attachment-format {{ FrontAttachmentFormat }}
  back-attachment-format {{ BackAttachmentFormat }}
  {{ "no " if MIMEFrontHeaders != 'on' else "" }}mime-front-headers 
  {{ "no " if MIMEBackHeaders != 'on' else "" }}mime-back-headers 
  stream-output-to-back {{ StreamOutputToBack }}
  stream-output-to-front {{ StreamOutputToFront }}
  max-message-size {{ MaxMessageSize }}
  {{ "no " if GatewayParserLimits != 'on' else "" }}gateway-parser-limits 
  element-depth {{ ParserLimitsElementDepth }}
  attribute-count {{ ParserLimitsAttributeCount }}
  max-node-size {{ ParserLimitsMaxNodeSize }}
  {{ "forbid-external-references" if ParserLimitsExternalReferences == 'forbid' else "" }}
  external-references {{ ParserLimitsExternalReferences }}
  max-prefixes {{ ParserLimitsMaxPrefixes }}
  max-namespaces {{ ParserLimitsMaxNamespaces }}
  max-local-names {{ ParserLimitsMaxLocalNames }}
  attachment-byte-count {{ ParserLimitsAttachmentByteCount }}
  attachment-package-byte-count {{ ParserLimitsAttachmentPackageByteCount }}
  debugger-type internal
  debug-history {{ DebugHistory }}
  {{ "no " if FlowControl != 'on' else "" }}flowcontrol 
  soap-schema-url "{{ SOAPSchemaURL }}"
  front-timeout {{ FrontTimeout }}
  back-timeout {{ BackTimeout }}
  front-persistent-timeout {{ FrontPersistentTimeout }}
  back-persistent-timeout {{ BackPersistentTimeout }}
  {{ "no " if IncludeResponseTypeEncoding != 'on' else "" }}include-content-type-encoding 
  {{ "no " if PersistentConnections != 'on' else "" }}persistent-connections 
  {{ "no " if LoopDetection != 'on' else "" }}loop-detection 
  {{ "no " if DoHostRewriting != 'on' else "" }}host-rewriting 
  {{ "no " if DoChunkedUpload != 'on' else "" }}chunked-uploads 
  {{ "no " if ProcessHTTPErrors != 'on' else "" }}process-http-errors 
  http-client-ip-label "{{ HTTPClientIPLabel }}"
  http-global-tranID-label "{{ HTTPLogCorIDLabel }}"
  inorder-mode "{% set adder = joiner("+") %}{% for feature, status in InOrderMode.items() %}{% if status == 'on' %}{{ adder() }}{{ feature }}{% endif %}{% endfor %}"
  wsa-mode {{ WSAMode }}
  {{ "no " if WSARequireAAA != 'on' else "" }}wsa-require-aaa 
  {{ "no " if WSAStrip != 'on' else "" }}wsa-strip-headers
  wsa-default-replyto "{{ WSADefaultReplyTo }}"
  wsa-default-faultto "{{ WSADefaultFaultTo }}"
  {{ "no " if WSAForce != 'on' else "" }}wsa-force 
  wsa-genstyle {{ WSAGenStyle }}
  wsa-http-async-response-code {{ WSAHTTPAsyncResponseCode }}
  wsa-timeout {{ WSATimeout }}
  {{ "no " if WSRMEnabled != 'on' else "" }}wsrm 
  wsrm-sequence-expiration {{ WSRMSequenceExpiration }}
  {{ "no " if WSRMEnabled != 'on' else "" }}wsrm-destination-accept-create-sequence 
  wsrm-destination-maximum-sequences {{ WSRMDestinationMaximumSequences }}
  {{ "no " if WSRMDestinationInOrder != 'on' else "" }}wsrm-destination-inorder 
  wsrm-destination-maximum-inorder-queue-length {{ WSRMDestinationMaximumInOrderQueueLength }}
  {{ "no " if WSRMDestinationAcceptOffers != 'on' else "" }}wsrm-destination-accept-offers 
  {{ "no " if WSRMFrontForce != 'on' else "" }}wsrm-request-force 
  {{ "no " if WSRMBackForce != 'on' else "" }}wsrm-response-force 
  {{ "no " if WSRMBackCreateSequence != 'on' else "" }}wsrm-source-request-create-sequence 
  {{ "no " if WSRMFrontCreateSequence != 'on' else "" }}wsrm-source-response-create-sequence 
  {{ "no " if WSRMSourceMakeOffer != 'on' else "" }}wsrm-source-make-offer 
  {{ "no " if WSRMUsesSequenceSSL != 'on' else "" }}wsrm-source-sequence-ssl 
  wsrm-source-maximum-sequences {{ WSRMSourceMaximumSequences }}
  wsrm-source-retransmission-interval {{ WSRMSourceRetransmissionInterval }}
  {{ "no " if WSRMSourceExponentialBackoff != 'on' else "" }}wsrm-source-exponential-backoff 
  wsrm-source-retransmit-count {{ WSRMSourceMaximumRetransmissions }}
  wsrm-source-maximum-queue-length {{ WSRMSourceMaximumQueueLength }}
  wsrm-source-request-ack-count {{ WSRMSourceRequestAckCount }}
  wsrm-source-inactivity-close-interval {{ WSRMSourceInactivityClose }}
  {{ "no " if ForcePolicyExec != 'on' else "" }}force-policy-exec 
  {{ "no " if RewriteErrors != 'on' else "" }}rewrite-errors 
  {{ "no " if DelayErrors != 'on' else "" }}delay-errors 
  delay-errors-duration {{ DelayErrorsDuration }}
  http-server-version {{ BackHTTPVersion }}
  {{ "no " if HTTP2Required != 'on' else "" }}http2-required 
  request-type {{ RequestType }}
  response-type {{ ResponseType }}
  {{ "no " if FollowRedirects != 'on' else "" }}follow-redirects 
  {{ "no " if RewriteLocationHeader != 'on' else "" }}rewrite-location-header 
  stylepolicy {{ StylePolicy.value }}
  type {{ Type }}
  {{ "no " if AllowCompression != 'on' else "" }}compression 
  {{ "no " if EnableCompressedPayloadPassthrough != 'on' else "" }}enable-compressed-payload-passthrough 
  {{ "no " if AllowCacheControlHeader != 'on' else "" }}allow-cache-control 
  policy-attachments {{ PolicyAttachments.value }}
  {{ "no " if WSMAgentMonitor != 'on' else "" }}wsmagent-monitor 
  wsmagent-monitor-capture-mode {{ WSMAgentMonitorPCM }}
  {{ "no " if ProxyHTTPResponse != 'on' else "" }}proxy-http-response 
  transaction-timeout {{ TransactionTimeout }}
exit
"""

  __DEFAULT_PROPS = {
    "UserSummary": "",
    "Priority": "normal",
    "XMLManager": {
        "value": "default",
        "href": "/mgmt/config/default/XMLManager/default"
    },
    "SSLClientConfigType": "proxy",
    "DefaultParamNamespace": "http://www.datapower.com/param/config",
    "QueryParamNamespace": "http://www.datapower.com/param/query",
    "PropagateURI": "on",
    "MonitorProcessingPolicy": "terminate-at-first-throttle",
    "RequestAttachments": "strip",
    "ResponseAttachments": "strip",
    "RequestAttachmentsFlowControl": "off",
    "ResponseAttachmentsFlowControl": "off",
    "RootPartNotFirstAction": "process-in-order",
    "FrontAttachmentFormat": "dynamic",
    "BackAttachmentFormat": "dynamic",
    "MIMEFrontHeaders": "on",
    "MIMEBackHeaders": "on",
    "StreamOutputToBack": "buffer-until-verification",
    "StreamOutputToFront": "buffer-until-verification",
    "MaxMessageSize": 0,
    "GatewayParserLimits": "off",
    "ParserLimitsElementDepth": 512,
    "ParserLimitsAttributeCount": 128,
    "ParserLimitsMaxNodeSize": 33554432,
    "ParserLimitsExternalReferences": "forbid",
    "ParserLimitsMaxPrefixes": 1024,
    "ParserLimitsMaxNamespaces": 1024,
    "ParserLimitsMaxLocalNames": 60000,
    "ParserLimitsAttachmentByteCount": 2000000000,
    "ParserLimitsAttachmentPackageByteCount": 0,
    "DebugMode": "off",
    "DebugHistory": 25,
    "FlowControl": "off",
    "SOAPSchemaURL": "store:///schemas/soap-envelope.xsd",
    "FrontTimeout": 120,
    "BackTimeout": 120,
    "FrontPersistentTimeout": 180,
    "BackPersistentTimeout": 180,
    "IncludeResponseTypeEncoding": "off",
    "PersistentConnections": "on",
    "LoopDetection": "off",
    "DoHostRewriting": "on",
    "DoChunkedUpload": "off",
    "ProcessHTTPErrors": "on",
    "HTTPClientIPLabel": "X-Client-IP",
    "HTTPLogCorIDLabel": "X-Global-Transaction-ID",
    "InOrderMode": {
        "Request": "off",
        "Backend": "off",
        "Response": "off"
    },
    "WSAMode": "sync2sync",
    "WSARequireAAA": "on",
    "WSAStrip": "on",
    "WSADefaultReplyTo": "http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous",
    "WSADefaultFaultTo": "http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous",
    "WSAForce": "off",
    "WSAGenStyle": "sync",
    "WSAHTTPAsyncResponseCode": 204,
    "WSATimeout": 120,
    "WSRMEnabled": "off",
    "WSRMSequenceExpiration": 3600,
    "WSRMDestinationAcceptCreateSequence": "on",
    "WSRMDestinationMaximumSequences": 400,
    "WSRMDestinationInOrder": "off",
    "WSRMDestinationMaximumInOrderQueueLength": 10,
    "WSRMDestinationAcceptOffers": "off",
    "WSRMFrontForce": "off",
    "WSRMBackForce": "off",
    "WSRMBackCreateSequence": "off",
    "WSRMFrontCreateSequence": "off",
    "WSRMSourceMakeOffer": "off",
    "WSRMUsesSequenceSSL": "off",
    "WSRMSourceMaximumSequences": 400,
    "WSRMSourceRetransmissionInterval": 10,
    "WSRMSourceExponentialBackoff": "on",
    "WSRMSourceMaximumRetransmissions": 4,
    "WSRMSourceMaximumQueueLength": 30,
    "WSRMSourceRequestAckCount": 1,
    "WSRMSourceInactivityClose": 360,
    "ForcePolicyExec": "off",
    "RewriteErrors": "on",
    "DelayErrors": "on",
    "DelayErrorsDuration": 1000,
    "BackHTTPVersion": "HTTP/1.1",
    "HTTP2Required": "off",
    "RequestType": "preprocessed",
    "ResponseType": "preprocessed",
    "FollowRedirects": "on",
    "RewriteLocationHeader": "off",
    "Type": "static-backend",
    "AllowCompression": "off",
    "EnableCompressedPayloadPassthrough": "off",
    "AllowCacheControlHeader": "off",
    "WSMAgentMonitor": "off",
    "WSMAgentMonitorPCM": "all-messages",
    "ProxyHTTPResponse": "off",
    "TransactionTimeout": 0
}

  def __init__(self):
    self.state = dict()

  def to_cfg(self):
    combined_state = MultiProtocolGateway.__DEFAULT_PROPS.copy()
    combined_state.update(self.state)
    env = Environment(undefined=StrictUndefined)
    t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
    return t.render(combined_state)

def main():
  multi_protcol_gateway = MultiProtocolGateway()
  multi_protcol_gateway.state = {
    "name": "test_mpgw",
    "mAdminState": "enabled",
    "FrontProtocol": {
        "value": "test_http_handler"
    },
    "BackendUrl": "http://mybackend.com",
    "PolicyAttachments": {
        "value": "test_mpgw"
    },
    "StylePolicy": {
        "value": "test_policy"
    }
  }
  print(multi_protcol_gateway.to_cfg())

if __name__ == '__main__':
  main()