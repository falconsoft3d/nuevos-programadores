# -*- coding: utf-8 -*-
import jinja2
from odoo import http

loader = jinja2.PackageLoader('odoo-custom-addons.custom_cv', 'views')
env = jinja2.Environment(loader=loader, autoescape=True)


class CustomCv(http.Controller):
    @http.route('/', methods=['GET'], auth='public')
    def index(self, **kw):
         company = http.request.env['res.company'].sudo().search([], limit=1)
         return env.get_template('index.html').render({
             'company': company,
             'company_fhone': company.phone,
             'company_email': company.email,
             'logo': company.logo and 'data:image/png;base64,%s' % company.logo.decode()
         })

    @http.route('/', methods=['POST'], type='json', auth='public')
    def creat_lead(self, name, phone, email, message, **kwargs):
        partner = http.request.env['res.partner'].sudo().search([('email', 'ilike', email.strip())], limit=1)
        if not partner:
            partner = partner.sudo().create({
                'name': name.strip(),
                'phone': phone.strip(),
                'email': email.strip(),
            })
        http.request.env['crm.lead'].sudo().create({
            'name': '%s  <%s>' % (name.strip(), email.strip()),
            'partner_id': partner.id,
            'email_from': email.strip(),
            'description': message.strip(),
            'user_id' : 2,
        })
        return {
            'name': name,
        }
