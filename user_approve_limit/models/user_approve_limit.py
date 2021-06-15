# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class user_approve_limit(models.Model):
    _name = 'user_approve_limit_main.user_approve_limit_main'
    _description = 'user_approve_limit.user_approve_limit'
    
    _logger.info("===12 IMPORTED in Models!!!!")

    '''    
    def _compute_limit_user(self):
        _logger.info("compute_limit_user")
        self.approve_limit_user = self.env.user.approve_limit_sales
        return self

    '''
    
    def get_user_limit(self):
        return self.env.user.approve_limit_sales
    
    def get_user_limit_diff(self):
        _logger.info("=====DEB26 Check Approve" )

        approve_limit_user = self.env.user.approve_limit_sales
        amount_total = self.amount_total
        
        diff = approve_limit_user - amount_total
        _logger.info("=====DEB32 DIFF: %s", diff )
        
        return diff

    def get_current_model(self):
        ir_model_txt = self.env.context.get('params').get('model')
        ir_model = self.env[ 'ir.model' ].search([ ('model','=', ir_model_txt) ])
        return ir_model
    
    
    def request_approval(self):
        approval_category = self.env.context.get('approval_category')
       
        model_name = self.env.context.get('model_name')
        
        approval_category_id = self.env['approval.category'].search([ ('name','=', approval_category ) ])
        
        if not approval_category_id:
            add_category_approval = self.env['user_approve_limit_main.user_approve_limit_main'].add_category_approval
            approval_category_id = add_category_approval(approval_category)

        owner_id = self.env.user
        request_title = approval_category + " Id: " + str( self.id )
        amount = self.amount_total

        approval_request_obj = self.env['approval.request']

        result = approval_request_obj.create({
            'request_owner_id': owner_id.id,
            'name': request_title,
            'category_id': approval_category_id.id,
            'reference': approval_category + " Id: " + str(self.id),
            'amount': amount,
        })
        if result:
            update_approver_ids = result._onchange_category_id()
            confirmation1 = result.action_confirm()
        
        body = "<a href='#' data-oe-model='{}' data-oe-id='{}'> Document Requesting Approval {} Id: {}</a>".format(model_name, self.id, approval_category , self.id)
        
        chatter_data = {
            'author_id': self.env.user.id,
            'res_id': result.id,
            'model': 'approval.request',
            'body': body,
        }
        chatter = self.env['mail.message']
        result33 = chatter.sudo().create( chatter_data )
        
        self.write({
            'approval_request' : result.id,
        })
        
        return

    def add_category_approval(self, approval_category):
        _logger.info("Add Category Approval")
        approval_category_model = self.env['approval.category']
        
        result = approval_category_model.sudo().create({
            'name': approval_category,
            'approval_minimum': 1,
            'user_ids': [( 4, 2 )],   #[(4,self.partner_id.id)]}   [( 6, 0, [2] )]
        })
        
        return result