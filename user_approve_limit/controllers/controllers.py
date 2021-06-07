# -*- coding: utf-8 -*-
# from odoo import http


# class UserApproveLimit(http.Controller):
#     @http.route('/user_approve_limit/user_approve_limit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/user_approve_limit/user_approve_limit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('user_approve_limit.listing', {
#             'root': '/user_approve_limit/user_approve_limit',
#             'objects': http.request.env['user_approve_limit.user_approve_limit'].search([]),
#         })

#     @http.route('/user_approve_limit/user_approve_limit/objects/<model("user_approve_limit.user_approve_limit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('user_approve_limit.object', {
#             'object': obj
#         })
