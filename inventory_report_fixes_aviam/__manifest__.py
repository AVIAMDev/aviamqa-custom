# -*- coding: utf-8 -*-
{
    'name': "inventory_report",

    'summary': """
        1- This Module creates a version of the Sial Report 
        """,

    'description': """
        This module implements report for inventory.
    """,

    'author': "Aviam LTD",
    'website': "http://aviamltd.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '14.0.1.1.0',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/wizard_inventary_report.xml',
        'views/stock_quant.xml',
        'report/inventory_report_view.xml',
    ],
    'qweb':[
        'static/src/xml/menu_header.xml',
    ],

}
