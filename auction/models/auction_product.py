from odoo import fields,models

class auction_product(models.Model):
	_name = "auction.product"
	_description = "Product details"
	_log_access = False

	name = fields.Char("Name")
	description = fields.Text("Description")
	start_price = fields.Float("Start Price", required=True)
	current_price = fields.Float("Current Price", required=True)
	active = fields.Boolean("Active", default=False)
	salesperson = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
	buyer = fields.Many2one('res.partner', string='Buyer', copy=False)
	image = fields.Image(string="Image")