from jinja2 import Environment, StrictUndefined

class StylePolicyAction:
  __JINJA2_CFG_TEMPLATE = """action "{{ name }}"
  {% if description is defined %}# {{ description }}{% endif %}
  reset
  type {{ Type }}
  input "{{ Input }}"
  parse-settings-result-type {{ ParseMetricsResultType }}
  transform-language {{ TransformLanguage }}
  gatewayscript-location "{{ GatewayScriptLocation }}"
  output "{{ Output }}"
  {{ "no " if NoTranscodeUtf8 != 'on' else "" }}charset-transparency
  named-inouts {{ NamedInOutLocationType }}
  ssl-client-type {{ SSLClientConfigType }}
  {{ "no " if Transactional != 'on' else "" }}transactional 
  soap-validation {{ SOAPValidation }}
  sql-source-type {{ SQLSourceType }}
  {{ "no " if JWSVerifyStripSignature != 'on' else "" }}strip-signature
  {{ "no " if Asynchronous != 'on' else "" }}asynchronous 
  results-mode {{ ResultsMode }}
  retry-count {{ RetryCount }}
  retry-interval {{ RetryInterval }}
  {{ "no " if MultipleOutputs != 'on' else "" }}multiple-outputs 
  iterator-type {{ IteratorType }}
  timeout {{ Timeout }}
  http-method {{ MethodRewriteType }}
  http-method-limited {{ MethodType }}
  http-method-limited2 {{ MethodType2 }}
exit
"""

  __DEFAULT_PROPS = {
        "ParseSettingsReference": {
            "URL": "",
            "Literal": "",
            "Default": ""
        },
        "ParseMetricsResultType": "none",
        "TransformLanguage": "none",
        "ActionDebug": "off",
        "NoTranscodeUtf8": "off",
        "NamedInOutLocationType": "default",
        "SSLClientConfigType": "proxy",
        "Transactional": "off",
        "SOAPValidation": "body",
        "SQLSourceType": "static",
        "JWSVerifyStripSignature": "on",
        "Asynchronous": "off",
        "ResultsMode": "first-available",
        "RetryCount": 0,
        "RetryInterval": 1000,
        "MultipleOutputs": "off",
        "IteratorType": "XPATH",
        "Timeout": 0,
        "MethodRewriteType": "GET",
        "MethodType": "POST",
        "MethodType2": "POST"
    }

  def __init__(self):
    self.state = dict()

  def to_cfg(self):
    combined_state = StylePolicyAction.__DEFAULT_PROPS.copy()
    combined_state.update(self.state)
    env = Environment(undefined=StrictUndefined)
    t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
    return t.render(combined_state)

def main():
  style_policy_action = StylePolicyAction()
  style_policy_action.state = {
        "name": "test_policy_rule_req_gatewayscript_0",
        "mAdminState": "enabled",
        "Type": "gatewayscript",
        "Input": "INPUT",
        "GatewayScriptLocation": "local:///simple.js",
        "Output": "PIPE"
    }
  print(style_policy_action.to_cfg())

if __name__ == '__main__':
  main()