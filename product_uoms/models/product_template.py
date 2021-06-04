# -*- coding: utf-8 -*-

from odoo import models, fields, api


class product_uoms(models.Model):
    _inherit = 'product.template'

    product_uoms = fields.Many2many('uom.uom','product_template_uom_uom_rel','product_template_id','uom_uom_id')
    uom_category_id = fields.Many2one(related="uom_id.category_id")