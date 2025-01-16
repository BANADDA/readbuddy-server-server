from flask import Blueprint

from src.controllers.document_controller import query_document, upload_document


def init_routes(app):
    routes = Blueprint('routes', __name__)
    
    routes.route('/upload', methods=['POST'])(upload_document)
    routes.route('/query', methods=['POST'])(query_document)
    # routes.route('/document-ids', methods=['GET'])(get_document_ids)
    
    app.register_blueprint(routes)
