# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Hospital(models.Model):
     _name = 'sis_hospital.hospital'
     _description = 'Hospital Module'

     name = fields.Char(string="Name", required=True)
     country = fields.Char(string="Country", required=True)


