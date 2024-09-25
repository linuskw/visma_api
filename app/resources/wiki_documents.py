from app.models.document import document_schema

wiki_document_resource_schema = document_schema.copy()
wiki_document_resource_schema.update({
    'parent': {
        'type': 'objectid',
        'nullable': True,
        'data_relation': {
            'resource': 'wiki_documents',
            'embeddable': True
        },
    },
})

wiki_document_resource = {
    'item_title': 'Wiki-Document',
    'schema': document_schema,
}
