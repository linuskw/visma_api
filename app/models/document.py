document_schema = {
    'headline': {
        'type': 'string',
        'required': True,
    },
    'content': {
        'type': 'string',
        'required': True,
    },
    'author': {
        'type': 'string',
        'required': True,
    },
    'parent': {
        'type': 'objectid',
        'nullable': True,
        'data_relation': {
            'resource': 'secret_documents',
            'embeddable': True
        },
    },
    'is_enabled': {'type': 'boolean', 'default': True},
}