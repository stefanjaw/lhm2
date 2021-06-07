# -*- coding: utf-8 -*-

from odoo import models, fields, api


class user_approve_limit(models.Model):
    _inherit = 'res.users'

    approve_limit_sales = fields.Float("User Approve Limit333",
                                          #currency_field='currency_id',
                                          #currency_field=60,
                                          help="Approve Limit for sales or invoices")
    