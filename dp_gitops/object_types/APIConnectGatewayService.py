from jinja2 import Environment, StrictUndefined


class APIConnectGatewayService:
    __JINJA2_CFG_TEMPLATE = """apic-gw-service
  admin-state {{ mAdminState }}
  local-address {{ LocalAddress }}
  local-port {{ LocalPort }}
  ssl-client {{ SSLClient.value }}
  ssl-server {{ SSLServer.value }}
  api-gw-address {{ APIGatewayAddress }}
  api-gw-port {{ APIGatewayPort }}
  gateway-peering {{ GatewayPeering.value }}
  gateway-peering-manager {{ GatewayPeeringManager.value }}
  {{ "no " if V5CompatibilityMode != 'on' else "" }}v5-compatibility-mode 
  slm-mode {{ V5CSlmMode }}
  no database-mode 
  no log-strip-non-ascii 
exit
"""

    __DEFAULT_PROPS = {
        "name": "default",
        "V5CompatibilityMode": "off",
        "V5CSlmMode": "autounicast",
        "IPUnicast": ""
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
        "mAdminState": "enabled",
        "LocalAddress": "eth0_ipv4_1",
        "LocalPort": 8543,
        "SSLClient": {
            "value": "appsdomain",
            "href": "/mgmt/config/default/SSLClientProfile/appsdomain"
        },
        "SSLServer": {
            "value": "appsdomain",
            "href": "/mgmt/config/default/SSLServerProfile/appsdomain"
        },
        "APIGatewayAddress": "eth0_ipv4_1",
        "APIGatewayPort": 8443,
        "GatewayPeering": {
            "value": "appsdomain"
        },
        "GatewayPeeringManager": {
            "value": "default"
        }
    }
    print(api_connect_gateway_service.to_cfg())


if __name__ == '__main__':
    main()
