from odoo import fields , models

class FleetStatusPhysical(models.Model):
    _name = 'fleet.status.physical'
    _description = 'Fleet Status Physical'

    kd_sts = fields.Char(string="KD STS", size=4)
    name = fields.Char(string="Physical Status", size=30)

    _sql_constraints = [
        ('unique_kd_sts', 'unique(kd_sts)', 'Status Code must be unique!')
    ]

