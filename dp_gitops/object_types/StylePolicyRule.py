from jinja2 import Environment, StrictUndefined

class StylePolicyRule:
  __JINJA2_CFG_TEMPLATE = """rule "{{ name }}"
  {% if description is defined %}# {{ description }}{% endif %}
  reset
    {% if Actions is mapping %}action "{{ Actions.value }}"{% else %}{% for item in Actions %}action "{{ item.value }}"{% if not loop.last %}
    {% endif %}{% endfor %}{% endif %}
  type {{ Direction }}
  input-filter {{ InputFormat }}
  output-filter {{ OutputFormat }}
  {{ "no " if NonXMLProcessing != 'on' else "" }}non-xml-processing
  {{ "no " if Unprocessed != 'on' else "" }}unprocessed
exit
"""

  __DEFAULT_PROPS = {
    "InputFormat": "none",
    "OutputFormat": "none",
    "NonXMLProcessing": "off",
    "Unprocessed": "off"
  }

  def __init__(self):
    self.state = dict()

  def to_cfg(self):
    combined_state = StylePolicyRule.__DEFAULT_PROPS.copy()
    combined_state.update(self.state)
    env = Environment(undefined=StrictUndefined)
    t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
    return t.render(combined_state)

def main():
  style_policy_rule = StylePolicyRule()
  style_policy_rule.state = {
    "name": "test_policy_rule",
    "mAdminState": "enabled",
    "Direction": "request-rule",
    "Actions": [{
      "value": "test_policy_rule_req_gatewayscript_0"
    }, {
      "value": "test_policy_2"
    }],
    "description": "This is a test"
  }
  print(style_policy_rule.to_cfg())

if __name__ == '__main__':
  main()