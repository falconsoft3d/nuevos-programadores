# -*- coding: utf-8 -*-
# from odoo import http


# class SisHospital(http.Controller):
#     @http.route('/sis_hospital/sis_hospital/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sis_hospital/sis_hospital/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sis_hospital.listing', {
#             'root': '/sis_hospital/sis_hospital',
#             'objects': http.request.env['sis_hospital.sis_hospital'].search([]),
#         })

#     @http.route('/sis_hospital/sis_hospital/objects/<model("sis_hospital.sis_hospital"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sis_hospital.object', {
#             'object': obj
#         })
