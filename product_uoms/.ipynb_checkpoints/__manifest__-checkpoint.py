# -*- coding: utf-8 -*-
{
    'name': "Product Available UOMs",

    'summary': """
        This module let the user to enable the possible UOMs
        that will be selectable when generating a sales or Invoice """,

    'description': """
        This module let the user to enable the possible UOMs
        that will be selectable when generating a sales or Invoice 
    """,

    'author': "Avalantec",
    'website': "http://www.avalantec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','uom','sale_management','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product_template.xml',
        'views/sale_order.xml',
        'views/account_move.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
