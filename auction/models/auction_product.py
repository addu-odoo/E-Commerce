from odoo import fields,models,api

class auction_product(models.Model):
	_name = "auction.product"
	_description = "Product details"
	_log_access = False

	name = fields.Char("Name")
	description = fields.Text("Description")
	start_price = fields.Float("Start Price", required=True)
	current_price = fields.Float("Current Bid Price", required=True, compute="_compute_price")
	selling_price = fields.Float("Selling Price")
	active = fields.Boolean("Active", default=False)
	salesperson = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
	buyer = fields.Many2one('res.partner', string='Buyer')
	image = fields.Image(string="Image")
	bid_ids = fields.One2many("auction.bid", "product_id", string="Bid list")
	state = fields.Selection(selection=[('sold','Sold'), ('unsold','Unsold')], default='unsold')
	is_sold = fields.Boolean(string='Sold')

	@api.depends("bid_ids")
	def _compute_price(self):
		for record in self:
			if record.bid_ids:
				record.current_price = max(record.bid_ids.mapped('price'))
			else:
				record.current_price = 0

	def on_sold(self):
		self.is_sold = True
		self.selling_price = self.current_price
