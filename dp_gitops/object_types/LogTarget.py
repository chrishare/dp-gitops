from jinja2 import Environment, StrictUndefined


class LogTarget:
    __JINJA2_CFG_TEMPLATE = """logging target "{{ name }}"
  {% if description is defined %}# {{ description }}{% endif %}
  admin-state {{ mAdminState }}
  type {{ Type }}
  priority {{ Priority }}
  soap-version {{ SoapVersion }}
  format {{ Format }}
  timestamp {{ TimestampFormat }}
  {{ "no " if FixedFormat != 'on' else "" }}fixed-format 
  size {{ Size }}
  local-file "{{ LocalFile }}"
  archive-mode {{ ArchiveMode }}
  upload-method {{ UploadMethod }}
  rotate {{ Rotate }}
  {{ "no " if UseANSIColor != 'on' else "" }}ansi-color 
  facility {{ SyslogFacility }}
  rate-limit {{ RateLimit }}
  connect-timeout {{ ConnectTimeout }}
  idle-timeout {{ IdleTimeout }}
  active-timeout {{ ActiveTimeout }}
  {{ "no " if FeedbackDetection != 'on' else "" }}feedback-detection 
  {{ "no " if IdenticalEventSuppression != 'on' else "" }}event-detection 
  suppression-period {{ IdenticalEventPeriod }}
  ssl-client-type {{ SSLClientConfigType }}
  retry-interval {{ RetryInterval }}
  retry-attempts {{ RetryAttempts }}
  long-retry-interval {{ LongRetryInterval }}
  precision {{ LogPrecision }}
  {% if LogEvents is mapping %}event "{{ LogEvents.Class.value }}" "{{ LogEvents.Priority }}"{% else %}{% for item in LogEvents %}event "{{ item.Class.value }}" "{{ item.Priority }}"{% if not loop.last %}
  {% endif %}{% endfor %}{% endif %}
exit
"""

    __DEFAULT_PROPS = {
        "Priority": "normal",
        "SoapVersion": "soap11",
        "Format": "text",
        "TimestampFormat": "syslog",
        "FixedFormat": "off",
        "ArchiveMode": "rotate",
        "UploadMethod": "ftp",
        "Rotate": 3,
        "UseANSIColor": "off",
        "SyslogFacility": "user",
        "RateLimit": 100,
        "ConnectTimeout": 60,
        "IdleTimeout": 15,
        "ActiveTimeout": 0,
        "FeedbackDetection": "off",
        "IdenticalEventSuppression": "off",
        "IdenticalEventPeriod": 10,
        "SSLClientConfigType": "proxy",
        "RetryInterval": 1,
        "RetryAttempts": 1,
        "LongRetryInterval": 20,
        "LogPrecision": "second",
    }

    def __init__(self):
        self.state = dict()

    def to_cfg(self):
        combined_state = LogTarget.__DEFAULT_PROPS.copy()
        combined_state.update(self.state)
        env = Environment(undefined=StrictUndefined)
        t = env.from_string(self.__JINJA2_CFG_TEMPLATE)
        return t.render(combined_state)


def main():
    log_target = LogTarget()
    log_target.state = {
        "name": "test_policy",
        "mAdminState": "enabled",
        "Type": "file",
        "Size": 500,
        "LocalFile": "logtemp:///temp.log",
        "LogEvents": [{
            "Class": {
                "value": "all"
            },
            "Priority": "error"
        },{
            "Class": {
                "value": "apiconnect"
            },
            "Priority": "error"
        }]
    }
    print(log_target.to_cfg())


if __name__ == '__main__':
    main()
