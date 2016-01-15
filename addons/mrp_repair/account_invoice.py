from openerp import models, fields, api, _
from openerp.osv import osv
from bsddb.dbtables import _columns
from datetime import datetime
from dateutil import relativedelta
import time
import datetime as only_datetime


class account_invoice_line(models.Model):
    _inherit = 'account.invoice.line'
       
    rma_id = fields.Many2one('mrp.repair', 'RMA no')
