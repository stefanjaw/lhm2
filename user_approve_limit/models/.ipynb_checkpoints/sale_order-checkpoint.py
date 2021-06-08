# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    approve_limit_user = fields.Float(compute="record_info")
    approve_limit_diff = fields.Float(compute="check_approve_limit")
    approval_request = fields.Many2one('approval.request', "Approval Request")
    
    def record_info(self):
        _logger.info("===DEB18 User ID: %s", self.env.user.approve_limit_sales )
        _logger.info("===DEB19 User ID: %s", self.env.user.name )
        
        self.approve_limit_user = self.env.user.approve_limit_sales
        return self
    
    @api.onchange('amount_total')
    def check_approve_limit(self):
        _logger.info("=====DEB26 Check Approve" )
        approve_limit_user = self.env.user.approve_limit_sales
        amount_total = self.amount_total
        
        diff = approve_limit_user - amount_total
        _logger.info("=====DEB30 DIFF: %s", diff )
        self.approve_limit_diff = diff
        
        return
    
    def request_approval(self):
        model_id= self.get_current_model()
        _logger.info("=====DEB39: MODEL ID NAME %s", model_id.name )
        
        approval_category_id = self.env['approval.category'].search([ ('name','=', model_id.name ) ])
        if not approval_category_id:
            approval_category_id = self.add_category_approval('model_id_name')
        
        owner_id = self.env.user.id
        request_title = "Approval for " + self.name
        amount = self.amount_total

        approval_request_obj = self.env['approval.request']
        result = approval_request_obj.create({
            'request_owner_id': owner_id,
            'name': request_title,
            'category_id': approval_category_id.id,
            'reference': model_id.name + ": " +self.name,
            'amount': amount,
        })
        _logger.info("=====DEB55: RESULT %s", result )
        
        if result:
            update_approver_ids = result._onchange_category_id()
            confirmation1 = result.action_confirm()
            '''
            result.write({
                'request_status' : 'pending',
            })
            '''
            _logger.info("====DEB65 REQUEST STATUS: %s", result.request_status)
            #result44 = result._compute_request_status()
            #_logger.info("====DEB64 Result 44: %s", result44)
        '''
        return  #SE DEBE QUITAR!!!
        _logger.info("========DEB65 ")
        approvers11 = result.mapped('approver_ids').filtered(lambda approver: approver.status == 'new')
        _logger.info("=====DEB67: RESULT %s", approvers11 )
        result22 = approvers11._create_activity()
        _logger.info("=====DEB69: RESULT %s", result22 )
        
        _logger.info("=====DEB142: Approver IDS %s", result.approver_ids )
        '''
        
        body = "<a href='#' data-oe-model='{}' data-oe-id='{}'> Document Requesting Approval {}: {}</a>".format('sale.order', self.id, model_id.name , self.name)
        
        chatter_data = {
            'author_id': self.env.user.id,
            'res_id': result.id,
            'model': 'approval.request',
            'body': body,
        }
        _logger.info("====DEB80 Chatter DATA: %s\n", chatter_data)
        chatter = self.env['mail.message']
        result33 = chatter.sudo().create( chatter_data )
        _logger.info("=====DEB80 RESULT: %s", result33)
        
        self.write({
            'approval_request' : result.id,
        })
        
        return
    
    def get_current_model(self):
        ir_model_txt = self.sudo().env.context.get('params').get('model')
        ir_model = self.env[ 'ir.model' ].search([ ('model','=', ir_model_txt) ])
        return ir_model
    
    def add_category_approval(self, model_id_name):
        approval_category_model = self.env['approval.category']
        
        result = approval_category_model.sudo().create({
            'name': model_id_name,
            'approval_minimum': 1,
            'user_ids': [( 4, 2 )],   #[(4,self.partner_id.id)]}   [( 6, 0, [2] )]
        })
        
        return result
        
    def log_to_chatter(self,body, model_id_name):
        _logger.info("====DEB95 SELF ID: %s", self.id)
        
        chatter = self.env['mail.message']
        chatter.create({
                        'res_id': self.id,
                        'model': model_id_name,
                        'body': body,
                       })
