user_schema = {
    'username': {
        'type': 'string',
        'unique': True,
        'required': True,
    },
    'password': {
        'type': 'string',
        'required': True,
    },
    'role': {
        'type': 'string',
        'required': True,
        'default': 'user',
    },
    'view_access': {
        'type': 'list',
        'required': True,
        'allowed': ["users", "secret", "wiki"],
        'default': ["users", "wiki"]
    },
    'edit_access': {
        'type': 'list',
        'required': True,
        'allowed': ["users", "secret", "wiki"],
        'default': ["users", "wiki"]
    },
    'is_enabled': {'type': 'boolean', 'default': True},
}
