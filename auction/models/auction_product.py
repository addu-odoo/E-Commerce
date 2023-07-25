from odoo import fields,models,api
from odoo.exceptions import UserError

class auction_product(models.Model):
	_name = "auction.product"
	_description = "Product details"
	_log_access = False
	_order = "id desc"
	_inherit = "mail.thread","mail.activity.mixin"

	name = fields.Char("Name", tracking=True)
	description = fields.Text("Description")
	start_price = fields.Float("Start Price", required=True)
	current_price = fields.Float("Current Bid Price", required=True, compute="_compute_price")
	selling_price = fields.Float("Selling Price")
	active = fields.Boolean("Active", default=True)
	salesperson = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
	bidder = fields.Many2one('res.partner', string='Bidder name', compute="_compute_buyer", store=True)
	image = fields.Image(string="Image")
	bid_ids = fields.One2many("auction.bid", "product_id", string="Bid list")
	state = fields.Selection(selection=[('sold','Sold'), ('unsold','Unsold')], default='unsold')
	is_sold = fields.Boolean(string='Sold')
	type_ids = fields.Many2many("auction.product.type", string="Product Type")
	categogy_ids = fields.Many2one("product.category", string="Product Categogy")

	_sql_constraints = [
		('check_start_price', 'CHECK(start_price >= 0)', 'The Start Price must be strictyly positive')
		]



	def write(self, vals):
		if 'is_sold' in vals:
			if vals.get('is_sold'):
				vals['state'] = 'sold'
			else:
				vals['state'] = 'unsold'
		return super().write(vals)

	@api.depends("bid_ids")
	def _compute_price(self):
		for record in self:
			if record.bid_ids:
				record.current_price = max(record.bid_ids.mapped('price'))
			else:
				record.current_price = 0

	@api.depends('bid_ids')
	def _compute_buyer(self):
		for record in self:
			if record.bid_ids:
				highest_bid = max(record.bid_ids, key=lambda bid: bid.price)
				record.bidder = highest_bid.partner_id
			else:
				record.bidder = False

	def on_sold(self):
		self.state = 'sold'
		self.is_sold = True
		self.selling_price = self.current_price

	@api.ondelete(at_uninstall=False)
	def ondelete_property(self):
		if self.state == 'unsold':
			raise UserError("Only sold properties can be deleted")