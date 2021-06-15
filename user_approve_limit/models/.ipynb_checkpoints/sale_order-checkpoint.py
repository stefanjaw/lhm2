# -*- coding: utf-8 -*-

from odoo import models, fields, api

from .user_approve_limit import user_approve_limit

import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    approve_limit_user = fields.Float("User Approve Limit",compute="_compute_limit_user",)
    approve_limit_diff = fields.Float(compute="check_approve_limit")
    approval_request = fields.Many2one('approval.request', "Approval Request")
    approval_request_status = fields.Selection(related="approval_request.request_status")

    @api.onchange('approve_limit_user')
    def _compute_limit_user(self):
        _logger.info("20=======APPROVE LIMIT USER: %s",  self.approve_limit_user )
        self.approve_limit_user = user_approve_limit.get_user_limit(self)
        return 
    
    @api.onchange('amount_total')
    def check_approve_limit(self):
        _logger.info("=====DEB30 Check Approve" )
        self.approve_limit_diff = user_approve_limit.get_user_limit_diff(self)
        return

    def request_approval(self):
        result = user_approve_limit.request_approval(self)
        return
