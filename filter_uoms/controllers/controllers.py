# -*- coding: utf-8 -*-
# from odoo import http


# class FilterUoms(http.Controller):
#     @http.route('/filter_uoms/filter_uoms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filter_uoms/filter_uoms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('filter_uoms.listing', {
#             'root': '/filter_uoms/filter_uoms',
#             'objects': http.request.env['filter_uoms.filter_uoms'].search([]),
#         })

#     @http.route('/filter_uoms/filter_uoms/objects/<model("filter_uoms.filter_uoms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filter_uoms.object', {
#             'object': obj
#         })
