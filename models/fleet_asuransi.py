from odoo import models, fields, api
from datetime import date


class FleetAsuransi(models.Model):
    _name = 'fleet.asuransi'
    _description = 'Fleet Vehicle Insurance'

    # asuransi_id = fields.Many2one('res.users','Asuransi', required=True)
    
    insurance_id = fields.Many2one('asuransi')
    fleet_id = fields.Many2one('fleet.vehicle')
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    status = fields.Selection(
        [('upcoming', 'Upcoming'), ('active', 'Active'), ('expired', 'Expired')],
        string='Status',
        compute='_compute_status',
        store=True
    )


    @api.depends('start_date', 'end_date')
    def _compute_status(self):
        today = date.today()
        for record in self:
            if record.start_date and record.end_date:
                if today < record.start_date:
                    record.status = 'upcoming'
                elif record.start_date <= today <= record.end_date:
                    record.status = 'active'
                else:
                    record.status = 'expired'
