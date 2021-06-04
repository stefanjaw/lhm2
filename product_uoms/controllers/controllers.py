# -*- coding: utf-8 -*-
# from odoo import http


# class ProductUoms(http.Controller):
#     @http.route('/product_uoms/product_uoms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_uoms/product_uoms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_uoms.listing', {
#             'root': '/product_uoms/product_uoms',
#             'objects': http.request.env['product_uoms.product_uoms'].search([]),
#         })

#     @http.route('/product_uoms/product_uoms/objects/<model("product_uoms.product_uoms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_uoms.object', {
#             'object': obj
#         })
