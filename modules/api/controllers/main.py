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
