# -*- coding: utf-8 -*-
# from odoo import http


# class FleetExtended(http.Controller):
#     @http.route('/fleet_extended/fleet_extended', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fleet_extended/fleet_extended/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fleet_extended.listing', {
#             'root': '/fleet_extended/fleet_extended',
#             'objects': http.request.env['fleet_extended.fleet_extended'].search([]),
#         })

#     @http.route('/fleet_extended/fleet_extended/objects/<model("fleet_extended.fleet_extended"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fleet_extended.object', {
#             'object': obj
#         })

