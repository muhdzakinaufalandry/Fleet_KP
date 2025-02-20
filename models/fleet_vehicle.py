from odoo import api, models, fields
from odoo.exceptions import ValidationError

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'  

    engine_number = fields.Char(string="Engine Number", help="Minimum 17 Digits", size=17,required=True) 
    engine_capacity = fields.Float(string="Engine Capacity")
    hul_number = fields.Char(string="Hul Number")
    branch_name = fields.Many2one('res.company', 'Branch Name')
    status_unit = fields.Many2one('fleet.status.unit', 'Unit Status')
    status_physical = fields.Many2one('fleet.status.physical', 'Physical Status')
    vehicle_type = fields.Selection(
        related='model_id.vehicle_type', 
        store=True, 
        readonly=False
    )
    fleet_insurance_id = fields.One2many('fleet.asuransi', 'fleet_id')
    type = fields.Char(string="Type")
    OTR = fields.Monetary(string="OTR")
    active = fields.Boolean()
    model_name = fields.Char(related="model_id.name", store=True)
    pic_name = fields.Many2one(related="fleet_insurance_id.insurance_id.provider", store=True)
    pic_number = fields.Char(related="fleet_insurance_id.insurance_id.pic_phone", store=True)
    provider_name = fields.Many2one(related="fleet_insurance_id.insurance_id.pic", store=True)
    date_start = fields.Date(related="fleet_insurance_id.start_date", store=True)
    date_end = fields.Date(related="fleet_insurance_id.end_date", store=True)
    statuss = fields.Selection(related="fleet_insurance_id.status", store=True)


    @api.constrains('engine_number')
    def _check_engine_number_length(self):
        for record in self:
            if record.engine_number and len(record.engine_number) != 17:
                raise ValidationError("Engine Number must consist of 17 characters (letters/numbers).")