from jinja2 import Environment, StrictUndefined

class PolicyAttachment:
  __JINJA2_CFG_TEMPLATE = """policy-attachments "{{ name }}"
  {% if description is defined %}# {{ description }}{% endif %}
  admin-state {{ mAdminState }}
  enforcement-mode {{ EnforcementMode }}
  {{ "no " if PolicyReferences != 'on' else "" }}policy-references 
  sla-enforcement-mode {{ SLAEnforcementMode }}
exit
"""

  __DEFAULT_PROPS = {
    "PolicyReferences": "on",
    "SLAEnforcementMode": "allow-if-no-sla"
  }

  def __init__(self):
    self.state = dict()

  def to_cfg(self):
    combined_state = PolicyAttachment.__DEFAULT_PROPS.copy()
    combined_state.update(self.state)
    env = Environment(undefined=StrictUndefined)
    t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
    return t.render(combined_state)

def main():
  policy_attachment = PolicyAttachment()
  policy_attachment.state = {
    "name": "test_mpgw",
    "mAdminState": "enabled",
    "EnforcementMode": "enforce"
  }
  print(policy_attachment.to_cfg())

if __name__ == '__main__':
  main()