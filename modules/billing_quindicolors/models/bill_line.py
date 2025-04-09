from odoo import api, fields, models

class BillLine(models.Model):
    _name = 'billing_quindicolors.bill_line'
    _description = 'Bill Line'

    bill_id = fields.Many2one('billing_quindicolors.bill', string='Bill Reference', required=True, ondelete='cascade')
    product_id = fields.Many2one('inventory.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', default=1.0)
    price = fields.Float(string='Price')
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('quantity', 'price')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price
            
    