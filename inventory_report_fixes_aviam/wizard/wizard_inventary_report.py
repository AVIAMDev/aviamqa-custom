# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import UserError

class WizardInventaryReport(models.TransientModel):
    _name = "inventary.report.wizard"
    _description = "generate report of inventory"

    category_ids = fields.Many2one("product.category", string = "Product Category", help="Choose category product")

    def action_report_wizard(self):
        """ Action Report Specific Category """
        if not self.category_ids:
            raise UserError(_("Select Category"))
        stock_quant = self.env['stock.quant'].search([],limit=1)
        datas={
            'wizard_category_ids':self.category_ids.id or None,
            'category_all': False
        }
        report = self.env.ref('inventory_report_fixes_aviam.xml_action_report_inventory').report_action(stock_quant[0],data=datas)
        report.update({'close_on_report_download': True})
        return report

    def action_report_wizard_all(self):
        """ Action Report All Category """
        stock_quant = self.env['stock.quant'].search([],limit=1)
        datas={
            'category_all': True
        }
        report = self.env.ref('inventory_report_fixes_aviam.xml_action_report_inventory').report_action(stock_quant[0],data=datas)
        report.update({'close_on_report_download': True})
        return report