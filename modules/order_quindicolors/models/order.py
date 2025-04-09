from odoo import fields, models

class Order(models.Model):
    _name = "order_quindicolors.order"
    _description = "order of the inventory"

    start_date = fields.Date(automatic=True, read_only=True)
    delivery_date = fields.Date(read_only=True)
    value = fields.Selection([
        ("good", "Good"),
        ("regular", "Regular"),
        ("bad", "Bad")
    ])
    origin_location = fields.Char()
    destination_location = fields.Char()
    state = fields.Selection([
        ("pending","Pending"),
        ("preparing","Preparing"),
        ("on_way", "On way"),
        ("finish","Finish")
    ])

