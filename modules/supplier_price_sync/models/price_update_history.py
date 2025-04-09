from odoo import models, fields

class PriceUpdateHistory(models.Model):
    _name = 'price.update.history'
    _description = 'Price Update History'
    _order = 'update_date desc'

    product_id = fields.Many2one('product.template', string='Product', required=True)
    supplier_id = fields.Many2one('res.partner', string='Supplier', required=True)
    old_price = fields.Float('Old Price')
    new_price = fields.Float('New Price')
    update_date = fields.Datetime('Update Date', default=fields.Datetime.now)
    user_id = fields.Many2one('res.users', string='Updated By', default=lambda self: self.env.user)
