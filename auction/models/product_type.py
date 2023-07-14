rom odoo import fields,models

class estate_property_tag(models.Model):
	_name = "auction.type"
	_description = "auction type"
	_log_access = False
	_order = "name"

	name = fields.Char("Product Type", required=True)
	color = fields.Integer("Color")