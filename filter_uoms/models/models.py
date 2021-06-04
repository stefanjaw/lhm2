# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class filter_uoms(models.Model):
#     _name = 'filter_uoms.filter_uoms'
#     _description = 'filter_uoms.filter_uoms'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
