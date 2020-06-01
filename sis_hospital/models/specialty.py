# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Specialty(models.Model):
     _name = 'sis_hospital.specialty'
     _description = 'Hospital Specialty'

     name = fields.Char(string="Specialty", required=True)


