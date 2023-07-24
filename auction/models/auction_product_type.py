from odoo import fields, models

class auction_product_type(models.Model):
    _name = "auction.product.type"
    _description = "Auction Type"
    _log_access = False
    _order = "name"

    _sql_constraints=[('unique_types','UNIQUE(name)','types name must be unique')]

    name = fields.Char("Product Type", required=True)
    color = fields.Integer("Color")
