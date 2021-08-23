import json


class Generic:
    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj


data = '{"product": "name", "read_logs": {"log_type": "failure", "log_url": "123"}}'

x = json.loads(data, object_hook=Generic.from_dict)
print(x.product, x.read_logs.log_type, x.read_logs.log_url)
