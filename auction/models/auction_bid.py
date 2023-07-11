from odoo import fields,models,api
from datetime import timedelta
from odoo.tools.float_utils import float_compare
from odoo.exceptions import ValidationError

class auction_bid(models.Model):
	_name = "auction.bid"
	_description = "Detail of Bidders"
	_log_access = False
	_order = "price desc"

	price = fields.Float("Price")
	status = fields.Selection(selection=[("Accepted","Accepted"), ("Refused","Refused")], string="Status", copy=False)
	partner_id = fields.Many2one('res.partner', string='Partner', required=True)
	product_id = fields.Many2one('auction.product', default=lambda self: self._get_default_product_id())
	validity = fields.Integer("Validity(Days)", default=7)
	date_deadline = fields.Date(string="Date Deadline", compute="_compute_date", inverse="_inverse_date")

	@api.model
	def _get_default_product_id(self):
		active_id = self._context.get('active_id')
		if active_id:
			return active_id
		else:
			return False


	@api.depends("validity")
	def _compute_date(self):
		for record in self:
			record.date_deadline = fields.Date.today() + timedelta(days=record.validity)

	def _inverse_date(self):
		for record in self:
			record.validity = (record.date_deadline - fields.Date.today()).days

	def action_confirm(self):
		for record in self:
			record.status = 'Accepted'
			# record.product_id.current_price = record.price
			# record.property_id.buyer = record.partner_id


	def action_Refused(self):
		for record in self:
			record.status = 'Refused'
			# record.property_id.selling_price = 0
			# record.property_id.buyer = None


	@api.constrains('price', 'product_id')
	def validat_bid_price(self):
		for record in self:
			if(float_compare(record.price,record.product_id.current_price,precision_rounding=0.01)<0):
				raise ValidationError(("Your bid price should be greater than the current value of the product"))