from odoo import http
from odoo.http import request

class UserAPI(http.Controller):

    @http.route('/api/users', auth='public', type='json', csrf=False)
    def get_users(self):
        users = request.env['res.users'].sudo().search([], limit=50)
        return [{
            'id': u.id,
            'name': u.name,
            'login': u.login,
            'email': u.email or '',
        } for u in users]
    
    @http.route('/api/products', auth='public', type='json', csrf=False)
    def get_products(self):
        products = request.env['inventory.product'].sudo().search([], limit=50)
        return [{
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'quantity': p.quantity,
            'image': p.image
            # Agrega aquí los campos que realmente tenga tu modelo
        } for p in products]
