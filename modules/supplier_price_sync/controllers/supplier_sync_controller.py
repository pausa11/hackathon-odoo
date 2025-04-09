from odoo import http
from odoo.http import request

class SupplierSyncController(http.Controller):
    @http.route('/supplier_sync/info', type='json', auth='user')
    def get_sync_info(self):
        return {
            'status': 'success',
            'message': 'Supplier Sync Controller is active'
        }
