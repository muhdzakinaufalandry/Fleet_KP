from odoo import fields , models

class FleetStatusUnit(models.Model):
    _name = 'fleet.status.unit'
    _description = 'Fleet Status Unit'

    kd_stss = fields.Char(string="KD STS", size=4)
    name = fields.Char(string="Unit Status", size=30)

    _sql_constraints = [
        ('unique_kd_stss', 'unique(kd_stss)', 'Status Code must be unique!')
    ]

