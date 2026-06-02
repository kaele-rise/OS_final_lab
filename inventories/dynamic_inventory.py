#!/usr/bin/env python3
import json

INVENTORY = {
    "staging": {
        "hosts": ["localhost"],
        "vars": {
            "env": "staging",
            "ansible_user": "root",
            "ansible_password": "root",
            "ansible_port": 2222,
            "ansible_ssh_common_args": "-o StrictHostKeyChecking=no",
            "db_host": "localhost",
            "nginx_port": 8080,
            "debug": True,
            "app_name": "myapp",
            "app_port": 5000,
            "db_name": "app_staging",
            "db_user": "staging_user"
        }
    },
    "production": {
        "hosts": ["localhost"],
        "vars": {
            "env": "production",
            "ansible_user": "root",
            "ansible_password": "root",
            "ansible_port": 2223,
            "ansible_ssh_common_args": "-o StrictHostKeyChecking=no",
            "db_host": "localhost",
            "nginx_port": 80,
            "debug": False,
            "app_name": "myapp",
            "app_port": 5000,
            "db_name": "app_prod",
            "db_user": "prod_user"
        }
    },
    "mock": {
        "hosts": ["localhost"],
        "vars": {
            "ansible_user": "root",
            "ansible_password": "root",
            "ansible_port": 2224,
            "ansible_ssh_common_args": "-o StrictHostKeyChecking=no"
        }
    },
    "_meta": {
        "hostvars": {
            "localhost": {}
        }
    }
}

print(json.dumps(INVENTORY, indent=2))
