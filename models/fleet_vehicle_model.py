from odoo import api, models, fields

class FleetVehicleModel(models.Model):
    _inherit = 'fleet.vehicle.model'  

color = fields.Char()
