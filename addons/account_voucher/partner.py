# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
##############################################################################

from operator import itemgetter
import time

from openerp import SUPERUSER_ID
from openerp.osv import fields, osv
from openerp import api

class res_partner(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'Partner'
    
    def _payment_count(self, cr, uid, ids, field_name, arg, context=None):
        Payment = self.pool['account.voucher']
        return {
            partner_id : Payment.search_count(cr,uid, [('partner_id', '=', partner_id)])
            for partner_id in ids
        }
        
    
    """ Inherits partner and adds Issue information in the partner form """
    
    _columns = {
        'payment_count': fields.function(_payment_count, string='Payments', type='integer'),
        }
