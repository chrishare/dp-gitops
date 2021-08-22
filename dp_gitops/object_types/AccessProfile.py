from jinja2 import Environment, StrictUndefined


class AccessProfile:
    __JINJA2_CFG_TEMPLATE = """access-profile "{{ name }}"
  {% if description is defined %}# {{ description }}{% endif %}
  admin-state {{ mAdminState }}
  {% for item in AccessPolicies %}access-policy {{ item }}
  {% endfor -%}
exit
"""

    __DEFAULT_PROPS = {
    }

    def __init__(self):
        self.state = dict()

    def to_cfg(self):
        combined_state = AccessProfile.__DEFAULT_PROPS.copy()
        combined_state.update(self.state)
        env = Environment(undefined=StrictUndefined)
        t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
        return t.render(combined_state)


def main():
    access_profile = AccessProfile()
    access_profile.state = {
        "name": "test_access_profile",
        "mAdminState": "enabled",
        "AccessPolicies": [
            "*/*/*?Access=r",
            "*/default/*?Access=r+w+a+d+x"
        ]
    }
    print(access_profile.to_cfg())


if __name__ == '__main__':
    main()
