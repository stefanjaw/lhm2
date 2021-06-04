# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class product_uoms(models.Model):
    _inherit = 'product.template'

    product_uoms = fields.Many2many('uom.uom','product_template_uom_uom_rel',
                                    'product_template_id','uom_uom_id',)
    
    uom_category_id = fields.Many2one(related="uom_id.category_id")

    uoms_empty = fields.Char(compute="_define_uoms")

    @api.onchange('uom_id')
    def _update_product_uoms(self):
        category_uoms = self.env['uom.uom'].search([ ('category_id','=', self.uom_id.category_id.id) ])
        self.write({
            'product_uoms': category_uoms
        })
        return

    def _define_uoms(self):
        _logger.info("Checking Empty UOMs")
        
        records_to_update = self.env['product.template'].search([ ('product_uoms','=', False) ])
        if len( records_to_update ) == 0:
            self.uoms_empty = "No Empty Uoms Detected"
            _logger.info("Checking Empty UOMs Ended")
            return self
               
        for record in records_to_update:
            category_uoms = self.env['uom.uom'].search([ ('category_id','=', record.uom_id.category_id.id) ])

            if len(record.product_uoms) == 0:
                record.write({
                'product_uoms': category_uoms
            })
               
            self.uoms_empty = "Updated"
        _logger.info("Checking Empty UOMs Ended")
        return self
