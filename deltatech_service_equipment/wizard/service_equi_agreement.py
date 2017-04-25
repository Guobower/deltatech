# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2015 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com       
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
##############################################################################

from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
import openerp.addons.decimal_precision as dp
from openerp.api import Environment



class service_equi_agreement(models.TransientModel):
    _name = 'service.equi.agreement'
    _description = "Service Equipment Agreement"


    equipment_id = fields.Many2one('service.equipment', string="Equipment", readonly=True)  
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, domain=[('is_company','=',True)])
    agreement_id = fields.Many2one('service.agreement', string='Contract Service', )
    
    @api.model
    def default_get(self, fields):
        defaults = super(service_equi_agreement, self).default_get(fields)
      
        active_id = self.env.context.get('active_id', False)
        if active_id:
            defaults['equipment_id'] =  active_id
            equipment = self.env['service.equipment'].browse(active_id)
            defaults['partner_id'] = equipment.partner_id.id
            agreement = self.env['service.agreement'].search([('partner_id','=',equipment.partner_id.id)],limit=1)
            if agreement:
                defaults['agreement_id'] = agreement.id
        else:
            raise Warning(_('Please select equipment.'))
        return defaults    


    @api.multi
    def do_agreement(self):
        if not self.agreement_id:
            cycle = self.env.ref('deltatech_service.cycle_monthly')
            values = {}
            values['partner_id'] = self.partner_id.id
            values['cycle_id'] = cycle.id
            self.agreement_id = self.env['service.agreement'].create(values)
            
        #self.equipment_id.write({'agreement_id':self.agreement_id.id,
        #                         'partner_id':self.partner_id.id})
        for template in self.equipment_id.type_id.categ_id.template_meter_ids:
            values = {}
            values['agreement_id'] = self.agreement_id.id
            values['equipment_id'] = self.equipment_id.id
            values['currency_id']  = template.currency_id.id
            values['product_id']   = template.product_id.id
             
            for meter in self.equipment_id.meter_ids:
                if meter.meter_categ_id == template.meter_categ_id:
                    values['meter_id']   = meter.id
                    values['uom_id']     = template.meter_categ_id.bill_uom_id.id
                    
            self.env['service.agreement.line'].create(values)
   
        action = { 
            'domain': "[('id','=',%s)]" % self.agreement_id.id,
            'name': _('Service Agreement'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'service.agreement',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'res_id': self.agreement_id.id
        } 
        return action
    
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: 