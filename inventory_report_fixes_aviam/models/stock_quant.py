 #-*- coding: utf-8 -*-
from odoo import models

class StockQuant(models.Model):
    _inherit = "stock.quant"

    def get_category_master(self):
        """ Get Category Master """
        return self.env['product.category'].search([('parent_id','=',False)],order="parent_path asc")

    def get_group_category(self,categ_master_id):
        """ Get Group Category """
        return self.env['product.category'].search([('parent_path','like','%d/' % categ_master_id)],order="parent_path asc")        

    def get_sum_value(self,categ_master_id):
        """ Get SUM Value Product"""
        categ_ids = self.get_group_category(categ_master_id)
        res = 0
        for categ in categ_ids:
            product_ids = self.get_products(categ.id)
            for product in product_ids:
                res += product.quantity * product.product_id.list_price
        return res

    def get_products(self,categ_id):
        """ Get Products """
        return self.search([('product_id.categ_id.id','=',int(categ_id))])

    def reversed_dict(self,values):
        """ Reverse Dictionary Keys """
        return reversed(list(values.keys()))