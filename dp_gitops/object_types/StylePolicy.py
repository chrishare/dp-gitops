from jinja2 import Environment, StrictUndefined


class StylePolicy:
    __JINJA2_CFG_TEMPLATE = """stylepolicy "{{ name }}"
  {% if description is defined %}# {{ description }}{% endif %}
  admin-state {{ mAdminState }}
  reset
  filter "{{ DefStylesheetForSoap }}"
  xsldefault "{{ DefStylesheetForXsl }}"
  xquerydefault "{{ DefXQueryForJSON }}"
  {% if PolicyMaps is mapping %}match "{{ PolicyMaps.Match.value }}" "{{ PolicyMaps.Rule.value }}"{% else %}{% for item in PolicyMaps %}match "{{ item.Match.value }}" "{{ item.Rule.value }}"{% if not loop.last %}
  {% endif %}{% endfor %}{% endif %}
exit
"""

    __DEFAULT_PROPS = {
        "DefStylesheetForSoap": "store:///filter-reject-all.xsl",
        "DefStylesheetForXsl": "store:///identity.xsl",
        "DefXQueryForJSON": "store:///reject-all-json.xq"
    }

    def __init__(self):
        self.state = dict()

    def to_cfg(self):
        combined_state = StylePolicy.__DEFAULT_PROPS.copy()
        combined_state.update(self.state)
        env = Environment(undefined=StrictUndefined)
        t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
        return t.render(combined_state)


def main():
    style_policy = StylePolicy()
    style_policy.state = {
        "name": "test_policy",
        "mAdminState": "enabled",
        "EnforcementMode": "enforce",
        "PolicyMaps": [{
            "Match": {
                "value": "ANY",
                "href": "/mgmt/config/default/Matching/ANY"
            },
            "Rule": {
                "value": "test_policy_rule_req",
                "href": "/mgmt/config/default/StylePolicyRule/test_policy_rule_req"
            }
        },{
            "Match": {
                "value": "ANY",
                "href": "/mgmt/config/default/Matching/ANY"
            },
            "Rule": {
                "value": "test_policy_rule_req",
                "href": "/mgmt/config/default/StylePolicyRule/test_policy_rule_req"
            }
        }]
    }
    print(style_policy.to_cfg())


if __name__ == '__main__':
    main()
