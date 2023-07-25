from odoo import models 

class auction_product(models.Model):
    _inherit = "auction.product"

    def on_sold(self):
        project = self.env['project.project'].search([('name', '=', 'Sold Properties')], limit=1)

        if not project:
	        self.env['project.project'].create({'name': 'Sold Properties',})
	        
        self.env['project.task'].create({
            'name': self.name,
            'project_id': project.id,
            'user_ids': self.salesperson,
        })
        return super().on_sold()
