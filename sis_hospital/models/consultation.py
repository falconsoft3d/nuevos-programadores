# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Consultation(models.Model):
     _name = 'sis_hospital.consultation'
     _description = 'Hospital Consultation'

     name = fields.Char(string="Name", required=True)
     partner_id = fields.Many2one('res.partner', "Patient", required=True)
     specialty_id = fields.Many2one('sis_hospital.specialty', "Specialty", required=True)


