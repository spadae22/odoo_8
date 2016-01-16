from openerp import models, fields, api, _
from openerp.osv import osv

class account_invoice_line(models.Model):
    _inherit = 'account.invoice.line'
       
    rma_id = fields.Many2one('mrp.repair', 'RMA no')
