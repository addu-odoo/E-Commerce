from odoo import models
from odoo import Command


class auction_product(models.Model):
    _inherit = "auction.product"

    def on_sold(self):
        self.env['account.move'].create(
            {
                'move_type' : 'out_invoice',
                'partner_id' : self.bidder.id,
                'invoice_line_ids' : [
                    Command.create(
                        {
                            "name" :self.name,
                            "quantity" : 1,
                            "price_unit" : self.current_price,
                        },
                    ),
                    Command.create(
                        {
                            "name" :'Product Tax',
                            "quantity" : 1,
                            "price_unit" : self.current_price * 6/100,
                        },
                    ),
                    Command.create(
                        {
                            "name" : "administrative fees",
                            "quantity" : 1,
                            "price_unit" : 100.00,
                        },
                    )],
            }
        )

        return super().on_sold()