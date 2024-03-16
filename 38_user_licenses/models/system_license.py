# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError
import http.client
import json

class SystemLicense(models.Model):
    _description = "System License"
    _name = 'system.license'
    _inherit = ['mail.activity.mixin', 'mail.thread']

    name = fields.Char('Code', default="New", copy=False)
    user_id = fields.Many2one('res.users', string='User', required=True, default=lambda self: self.env.user)
    create_date = fields.Datetime('Create Date', default=fields.Datetime.now)

    id_database = fields.Char('ID Database', required=True)
    license_code = fields.Char('License Code', required=True)

    type = fields.Selection([
                            ('0',  '0 %'),
                            ('50',  '50 %'),
                            ('100', '100 %')
                            ], string='type', required=True)

    number_of_uses = fields.Integer('Number of Uses')
    number_of_uses_original = fields.Integer('Number Original')

    product_id = fields.Many2one('product.product', string='Product', required=True)
    expiration_date = fields.Date('Expiration Date', required=True)

    user_use_id = fields.Many2one('res.users', string='User', required=True, default=lambda self: self.env.user)


    @api.model
    def create(self, vals):
        if vals.get('name', "New") == "New":
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'system.license') or "New"
        return super(SystemLicense, self).create(vals)


    def load_license(self):
        print("load_license")

        for i in range(0, 2):
            conn = http.client.HTTPSConnection("api.namefake.com")
            payload = ''
            headers = {}
            conn.request("GET", "/", payload, headers)
            res = conn.getresponse()
            data = res.read()

            # Necesito tenerlo en un json
            json_data = json.loads(data.decode("utf-8"))
            print(json_data)


            user_use_id_id = self.env['res.users'].search([('name', '=', json_data['name'])], limit=1)

            if not user_use_id_id:
                user_use_id_id = self.env['res.users'].create({
                    'name': json_data['name'],
                    'login': json_data['email_d'] + '@demo.es' if json_data['email_d'] else json_data['name'].replace(' ', '.').lower() + '@demo.es',
                    'password': '1234'
                })


            system_license_id = self.env['system.license'].create({
                'id_database': json_data['name'],
                'license_code': json_data['uuid'],
                'type': '100',
                'number_of_uses': 0,
                'number_of_uses_original': json_data['bonus'],
                'product_id': 1,
                'expiration_date': '2025-12-31',
                'user_use_id': user_use_id_id.id
            })



    def load_licence(self):
        url = "https://www.marlonfalcon.com/api/password/20"
        print("load_licence")

        conn = http.client.HTTPSConnection("www.marlonfalcon.com")
        payload = ''
        headers = {}
        conn.request("GET", "/api/password/20", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

        license_code = data.decode("utf-8")
        self.license_code = license_code.replace('{"password":"', '').replace('"}', '')
        self.number_of_uses += 1

        return True