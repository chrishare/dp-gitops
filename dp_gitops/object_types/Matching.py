from jinja2 import Environment, StrictUndefined


class Matching:
    __JINJA2_CFG_TEMPLATE = """matching "{{ name }}"
  {% if MatchRules is mapping -%}
    {% if MatchRules.Type == 'url' %}urlmatch "{{ MatchRules.Url }}"{% endif -%}
    {% if MatchRules.Type == 'errorcode' %}errorcode "{{ MatchRules.ErrorCode }}"{% endif -%}
    {% if MatchRules.Type == 'fullyqualifiedurl' %}fullurlmatch "{{ MatchRules.Url }}"{% endif -%}
    {% if MatchRules.Type == 'host' %}hostmatch "{{ MatchRules.Url }}"{% endif -%}
    {% if MatchRules.Type == 'method' %}methodmatch "{{ MatchRules.Url }}"{% endif -%}
    {% if MatchRules.Type == 'http' %}httpmatch "{{ MatchRules.HttpTag }}" "{{ MatchRules.HttpValue }}"{% endif -%}
    {% if MatchRules.Type == 'xpath' %}xpathmatch "{{ MatchRules.XPATHExpression }}"{% endif -%}
    xpath
  {% else %}{% for item in MatchRules -%}
    {% if item.Type == 'url' %}urlmatch "{{ item.Url }}"{% endif -%}
    {% if item.Type == 'errorcode' %}errorcode "{{ item.ErrorCode }}"{% endif -%}
    {% if item.Type == 'fullyqualifiedurl' %}fullurlmatch "{{ item.Url }}"{% endif -%}
    {% if item.Type == 'host' %}hostmatch "{{ item.Url }}"{% endif -%}
    {% if item.Type == 'method' %}methodmatch "{{ item.Url }}"{% endif -%}
    {% if item.Type == 'http' %}httpmatch "{{ item.HttpTag }}" "{{ item.HttpValue }}"{% endif -%}
    {% if item.Type == 'xpath' %}xpathmatch "{{ item.XPATHExpression }}"{% endif -%}
  {% if not loop.last %}
  {% endif %}{% endfor %}{% endif %}
  {{ "no " if MatchWithPCRE != 'on' else "" }}match-with-pcre 
  {{ "no " if CombineWithOr != 'on' else "" }}combine-with-or 
exit
"""

    __DEFAULT_PROPS = {
        "MatchWithPCRE": "off",
        "CombineWithOr": "off"
    }

    def __init__(self):
        self.state = dict()

    def to_cfg(self):
        combined_state = Matching.__DEFAULT_PROPS.copy()
        combined_state.update(self.state)
        env = Environment(undefined=StrictUndefined)
        t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
        return t.render(combined_state)


def main():
    matching = Matching()
    matching.state = {
        "name": "test_match",
        "mAdminState": "enabled",
        "MatchRules": [
            {
                "Type": "url",
                "HttpTag": "",
                "HttpValue": "",
                "Url": "adsasd",
                "ErrorCode": "",
                "XPATHExpression": "",
                "Method": "default",
                "CustomMethod": ""
            },
            {
                "Type": "http",
                "HttpTag": "header_name",
                "HttpValue": "header_value",
                "Url": "",
                "ErrorCode": "",
                "XPATHExpression": "",
                "Method": "default",
                "CustomMethod": ""
            },
            {
                "Type": "errorcode",
                "HttpTag": "",
                "HttpValue": "",
                "Url": "",
                "ErrorCode": "0x04b30005",
                "XPATHExpression": "",
                "Method": "default",
                "CustomMethod": ""
            },
            {
                "Type": "xpath",
                "HttpTag": "",
                "HttpValue": "",
                "Url": "",
                "ErrorCode": "",
                "XPATHExpression": "//*:meh",
                "Method": "default",
                "CustomMethod": ""
            },
            {
                "Type": "fullyqualifiedurl",
                "HttpTag": "",
                "HttpValue": "",
                "Url": "fullish",
                "ErrorCode": "",
                "XPATHExpression": "",
                "Method": "default",
                "CustomMethod": ""
            },
            {
                "Type": "host",
                "HttpTag": "",
                "HttpValue": "",
                "Url": "asd",
                "ErrorCode": "",
                "XPATHExpression": "",
                "Method": "default",
                "CustomMethod": ""
            },
            {
                "Type": "method",
                "HttpTag": "",
                "HttpValue": "",
                "Url": "",
                "ErrorCode": "",
                "XPATHExpression": "",
                "Method": "DELETE",
                "CustomMethod": ""
            }
        ]
    }
    print(matching.to_cfg())


if __name__ == '__main__':
    main()
