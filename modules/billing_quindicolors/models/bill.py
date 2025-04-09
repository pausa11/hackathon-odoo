from odoo import api, fields, models

class Bill(models.Model):
    _name = 'billing_quindicolors.bill'
    _description = 'Billing for Quindicolors'

    name = fields.Char(string='Bill Number', required=True)
    date_created = fields.Date(string='Creation Date', default=fields.Date.today)
    customer_name = fields.Char(string='Customer Name', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')
    
    # Añadir este campo:
    bill_line_ids = fields.One2many('billing_quindicolors.bill_line', 'bill_id', string='Bill Lines')
    
    # Campo calculado para el total:
    total_amount = fields.Float(string='Total Amount', compute='_compute_total', store=True)

    @api.depends('bill_line_ids.subtotal')
    def _compute_total(self):
        for bill in self:
            bill.total_amount = sum(line.subtotal for line in bill.bill_line_ids)