from odoo import fields,models

class productCategroy(models.Model):
	_name = "product.category"
	_description = "list of product under category"
	_log_access = False
	_sql_constraints=[('unique_types','UNIQUE(name)','Category name must be unique')]

	name = fields.Char("Category")
	product_id = fields.One2many("auction.product", 'categogy_ids', string='Products')
