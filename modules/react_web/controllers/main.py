# api_pokemones/controllers/main.py
from odoo import http
from odoo.http import request

class ReactWeb(http.Controller):

    @http.route('/react', auth='user', type='http', website=True)
    def index(self, **kw):
        return request.render('react_web.react_view_template', {})
