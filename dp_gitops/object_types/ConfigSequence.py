from jinja2 import Environment, StrictUndefined


class APIConnectGatewayService:
    __JINJA2_CFG_TEMPLATE = """config-sequence "{{ name }}"
  admin-state {{ mAdminState }}
  {% if Locations is mapping %}
  location
    directory {{ Locations.Directory}}
    access-profile {{ Locations.AccessProfileName.value }}
  exit
  {% else %}
  {% for item in Locations %}
  location
    directory {{ item.Directory}}
    access-profile {{ item.value }}
  exit
  {% if not loop.last %}
  {% endif %}{% endfor %}{% endif %}
  match-pattern {{ MatchPattern }}
  result-name-pattern {{ ResultNamePattern }}
  status-name-pattern {{ StatusNamePattern }}
  {{ "no " if Watch != 'on' else "" }}watch 
  {{ "no " if UseOutputLocation != 'on' else "" }}use-output-location 
  output-location {{ OutputLocation }}
  {{ "no " if DeleteUnused != 'on' else "" }}delete-unused 
  run-sequence-interval {{ RunSequenceInterval }}
  max-log-file-size 1024
  {{ "no " if Capabilities.MarkExternal != 'on' else "" }}mark-objects-external 
  {{ "no " if Capabilities.DeleteConfig != 'on' else "" }}delete-config 
  output-cleanup-interval 0
  serialize-deferred-processing 
  no optimize-for-apic 
  always-run-config 
  {{ "no " if Capabilities.MonitorPersistence != 'on' else "" }}monitor-persistence 
exit
"""

    __DEFAULT_PROPS = {
        "MatchPattern": "(.*).cfg$",
        "ResultNamePattern": "$1.log",
        "StatusNamePattern": "$1.status",
        "Watch": "on",
        "UseOutputLocation": "off",
        "OutputLocation": "logtemp:///",
        "DeleteUnused": "on",
        "RunSequenceInterval": 3000,
        "Capabilities": {
            "APIConnect": "off",
            "MonitorPersistence": "off",
            "ApplyAllObjects": "on",
            "MarkExternal": "on",
            "DeleteConfig": "off"
        }
    }

    def __init__(self):
        self.state = dict()

    def to_cfg(self):
        combined_state = APIConnectGatewayService.__DEFAULT_PROPS.copy()
        combined_state.update(self.state)
        env = Environment(undefined=StrictUndefined)
        t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
        return t.render(combined_state)

def main():
    api_connect_gateway_service = APIConnectGatewayService()
    api_connect_gateway_service.state = {
        "name": "my_apic_gws",
        "mAdminState": "enabled",
        "Locations": {
            "Directory": "local:///",
            "AccessProfileName": {
                "value": "appsdomain"
            }
        }
    }
    print(api_connect_gateway_service.to_cfg())


if __name__ == '__main__':
    main()
