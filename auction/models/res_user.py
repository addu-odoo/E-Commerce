from odoo import models, fields


class Users(models.Model):
    _inherit = "res.users"

    product_ids = fields.One2many("auction.product", "salesperson")