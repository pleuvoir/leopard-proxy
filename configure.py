# -*- coding:utf-8 -*-


import json


class Configure:

    def __init__(self):
        self.log = {}
        self.rabbitmq = {}
        self.accounts = []
        self.markets = {}
        self.proxy = None

    def loads(self, config_file=None) -> None:
        configures = {}
        if config_file:
            try:
                with open(config_file) as f:
                    data = f.read()
                    configures = json.loads(data)
            except Exception as e:
                print(e)
                exit(0)
            if not configures:
                print("config json file error!")
                exit(0)
        self._update(configures)

    def _update(self, update_fields) -> None:
        self.log = update_fields.get("LOG", {})
        self.rabbitmq = update_fields.get("RABBITMQ", None)
        self.accounts = update_fields.get("ACCOUNTS", [])
        self.markets = update_fields.get("MARKETS", [])
        self.heartbeat = update_fields.get("HEARTBEAT", {})
        self.proxy = update_fields.get("PROXY", None)

        for k, v in update_fields.items():
            setattr(self, k, v)


config = Configure()
