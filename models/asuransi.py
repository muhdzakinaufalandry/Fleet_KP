from odoo import fields, models

class Asuransi(models.Model):
    _name = 'asuransi'
    _description = 'asuransi'

    provider = fields.Many2one('res.users', string='PIC')
    pic_phone = fields.Char(related='provider.phone', string='PIC Number')
    pic = fields.Many2one(related='provider.company_id', string='Provider')
    provider_address = fields.Char(related='pic.street', string='Provider Address')
    provider_phone = fields.Char(related='pic.phone', string='Provider Number')
    fleet_insurance_ids = fields.One2many('fleet.asuransi','insurance_id')
