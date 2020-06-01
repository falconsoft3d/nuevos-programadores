# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    client_rut = fields.Char(string="Rut", size=10, help="This is the rut")
    client_age = fields.Char(string="Age", size=3, help="Type our age")
    client_profession = fields.Char(string="Profession", size=50, help="Type your profession")
