from jinja2 import Environment, StrictUndefined


class GatewayPeering:
    __JINJA2_CFG_TEMPLATE = """gateway-peering "{{ name }}"
  local-address {{ LocalAddress }}
  local-port {{ LocalPort }}
  primary-count {{ PrimaryCount }}
  monitor-port {{ MonitorPort }}
  {{ "no " if ClusterAutoConfig != 'on' else "" }}cluster-auto-config 
  {{ "no " if ClusterAutoConfig != 'on' else "" }}enable-peer-group 
  priority {{ Priority }}
  {{ "no " if EnableSSL != 'on' else "" }}enable-ssl 
  persistence {{ PersistenceLocation }}
  local-directory {{ LocalDirectory }}
  log-level internal
  max-memory {{ MaxMemory }}
exit
"""

    __DEFAULT_PROPS = {
        "PrimaryCount": 1,
        "ClusterAutoConfig": "on",
        "EnablePeerGroup": "off",
        "Priority": 100,
        "EnableSSL": "off",
        "MaxMemory": 0
    }

    def __init__(self):
        self.state = dict()

    def to_cfg(self):
        combined_state = GatewayPeering.__DEFAULT_PROPS.copy()
        combined_state.update(self.state)
        env = Environment(undefined=StrictUndefined)
        t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
        return t.render(combined_state)


def main():
    gateway_peering = GatewayPeering()
    gateway_peering.state = {
        "name": "appsdomain",
        "mAdminState": "enabled",
        "LocalAddress": "eth0_ipv4_1",
        "LocalPort": 8546,
        "MonitorPort": 8547,
        "PersistenceLocation": "memory",
        "LocalDirectory": "local:///"
    }
    print(gateway_peering.to_cfg())


if __name__ == '__main__':
    main()
