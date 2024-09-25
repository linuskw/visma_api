from app.models.document import document_schema

secret_document_resource_schema = document_schema.copy()
secret_document_resource_schema.update({
    'parent': {
        'type': 'objectid',
        'nullable': True,
        'data_relation': {
            'resource': 'secret_documents',
            'embeddable': True
        },
    },
})

secret_document_resource = {
    'item_title': 'Secret-Document',
    'schema': document_schema,
}
