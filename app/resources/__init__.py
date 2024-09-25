from .secret_documents import secret_document_resource
from .users import user_resource
from .wiki_documents import wiki_document_resource

DOMAIN = {
    'users': user_resource,
    'secret': secret_document_resource,
    'wiki': wiki_document_resource
}
