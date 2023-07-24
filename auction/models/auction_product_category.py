from odoo import fields,models,api

class productCategroy(models.Model):
	_name = "product.category"
	_description = "list of product under category"
	_log_access = False
	_order = "name"
	_sql_constraints=[('unique_types','UNIQUE(name)','Category name must be unique')]

	name = fields.Char("Category")
	product_id = fields.One2many("auction.product", 'categogy_ids', string='Products')
	bid_ids = fields.One2many("auction.bid","product_category_ids")
	bid_count = fields.Integer(compute="_compute_bid")
	sequence=fields.Integer("Sequence",default=1)

	@api.depends('bid_ids')
	def _compute_bid(self):
		for record in self:
			record.bid_count = len(record.bid_ids)