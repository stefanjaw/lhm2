# -*- coding: utf-8 -*-
{
    'name': "User Approve Limit",

    'summary': """
        This module define a field in the user settings,
        to enable an amount to approve in the sales orders or invoices""",

    'description': """
        This module define a field in the user settings,
        to enable an amount to approve in the sales orders or invoices
    """,

    'author': "Avalantec",
    'website': "http://www.avalantec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
