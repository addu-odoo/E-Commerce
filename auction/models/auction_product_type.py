from odoo import fields, models

class auction_product_type(models.Model):
    _name = "auction.product.type"
    _description = "Auction Type"
    _log_access = False
    _order = "name"

    name = fields.Char("Product Type", required=True)
    color = fields.Integer("Color")
