# api_pokemones/controllers/main.py
from odoo import http
from odoo.http import request

class ReactPokemon(http.Controller):

    @http.route('/pokemon', auth='user', type='http', website=True)
    def index(self, **kw):
        return request.render('api_pokemones.react_view_template', {})
