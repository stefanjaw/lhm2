# -*- coding: utf-8 -*-

from odoo import models, fields, api

from .user_approve_limit import user_approve_limit

import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    approve_limit_user = fields.Float("User Approve Limit",compute="_compute_limit_user",)
    approve_limit_diff = fields.Float(compute="check_approve_limit")
    approval_request = fields.Many2one('approval.request', "Approval Request")
    approval_request_status = fields.Selection(related="approval_request.request_status")

    @api.onchange('approve_limit_user')
    def _compute_limit_user(self):
        self.approve_limit_user = user_approve_limit.get_user_limit(self)
        _logger.info("21==INV=====APPROVE LIMIT USER: %s",  self.approve_limit_user )
        return 
    
    @api.onchange('invoice_line_ids')
    def _onchange_update_diff(self):
        _logger.info("26========== ONCHANGE diff")
        self.write({
           'approve_limit_diff': user_approve_limit.get_user_limit_diff(self) 
        })
        return

    
    def check_approve_limit(self):
        #Se ejecuta ON_CREATE SOLAMENTE
        self.approve_limit_diff = user_approve_limit.get_user_limit_diff(self)
        _logger.info("35======INV=== Check Approve %s", self.approve_limit_diff )
        return

    def request_approval(self):
        result = user_approve_limit.request_approval(self)
        return
