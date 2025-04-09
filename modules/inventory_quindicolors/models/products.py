from odoo import fields, models

class Products(models.Model):
    _name = "inventory.product"
    _description = 'Products of the inventory'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ("out_of_stock", "Out of Stock"),
        ("discontinued", "Discontinued"),
        ("active", "Active"),
    ], default="active", string="Status", copy=False)
    price = fields.Float(string="Price", required=True)
    quantity = fields.Integer(string="Quantity", required=True)
    date_created = fields.Datetime(string="Date Created", default=fields.Datetime.now, readonly=True)
    provider_price = fields.Float(string="Provider Price", required=True)
    image = fields.Text(string="Image")
