from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SupplierPriceSync(models.Model):
    _name = 'supplier.price.sync'
    _description = 'Supplier Price Sync'
    _order = 'create_date desc'

    supplier_id = fields.Many2one('res.partner', string='Supplier', required=True,
        domain=[('supplier_rank', '>', 0)])
    product_id = fields.Many2one('product.template', string='Product')
    product_code = fields.Char('Product Code')
    new_price = fields.Float('New Price', default=0.0)
    new_stock = fields.Float('New Stock Quantity')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('validated', 'Validated'),
        ('applied', 'Applied')
    ], default='draft')

    @api.constrains('new_price')
    def _check_price(self):
        for record in self:
            if record.new_price < 0:
                raise ValidationError(_("Price must not be negative"))

    def action_validate(self):
        self.state = 'validated'

    def action_apply(self):
        for record in self:
            if record.product_id:
                old_price = record.product_id.list_price
                record.product_id.write({
                    'list_price': record.new_price,
                    'qty_available': record.new_stock,
                })
                self.env['price.update.history'].create({
                    'product_id': record.product_id.id,
                    'old_price': old_price,
                    'new_price': record.new_price,
                    'supplier_id': record.supplier_id.id,
                })
                record.state = 'applied'
