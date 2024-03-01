from datetime import datetime
from datetime import timedelta
from dateutil import relativedelta
from odoo import models, fields, api
from odoo import api, fields, models, SUPERUSER_ID, _
# from odoo.tools.translate import _
# from odoo.exceptions import UserError, AccessError

# Buku Tamu kebutuhan Marketing untuk pencatatan tamu yang hadir berkunjung di boot pada saat event
class event_visitor(models.Model):
	_name = 'event_visitor'
	_order = 'name asc'
	_inherit = ['mail.thread', 'mail.activity.mixin']
	
	name = fields.Char('Number', default='New', readonly=True)
	event_name = fields.Many2one('nama_event', string='Event Name', required=True)
	event_type = fields.Selection([('1','Pusat'),('2','Cabang')], string='Event Type')
	event_periode = fields.Integer(string='Period', compute='_compute_period')
	event_date_start = fields.Date(string='Event Start Date', default=fields.Date.today())
	event_date_end = fields.Date(string='Event End Date', default=fields.Date.today() + timedelta(days=5))
	event_venue = fields.Char(string='Venue')
	event_tema = fields.Char(string='Event Theme')
	visitor_outlet = fields.Many2one('tbl_msi_cus_universal', string='Outlet Name')
	visitor_pic = fields.Char(string='Visitor Name')
	visitor_role = fields.Char(string='Role')

	@api.depends('event_date_start', 'event_date_end')
	def _compute_period(self):
		for rec in self:
			if rec.event_date_start and rec.event_date_end:
				delta = rec.event_date_end - rec.event_date_start
				rec.event_periode = delta.days + 1
			else:
				rec.event_periode = 0

class nama_event(models.Model):
	_name = 'nama_event'

	name = fields.Char('Event Name')
	active = fields.Boolean('Active', default=True)
