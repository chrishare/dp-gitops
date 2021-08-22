from jinja2 import Environment, StrictUndefined


class LogLabel:
    __JINJA2_CFG_TEMPLATE = """logging category "{{ name }}"
  {% if description is defined %}# {{ description }}{% endif %}
  admin-state {{ mAdminState }}
exit
"""

    __DEFAULT_PROPS = {
    }

    def __init__(self):
        self.state = dict()

    def to_cfg(self):
        combined_state = LogLabel.__DEFAULT_PROPS.copy()
        combined_state.update(self.state)
        env = Environment(undefined=StrictUndefined)
        t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
        return t.render(combined_state)


def main():
    log_label = LogLabel()
    log_label.state = {
        "name": "test_policy",
        "mAdminState": "enabled"
    }
    print(log_label.to_cfg())


if __name__ == '__main__':
    main()
