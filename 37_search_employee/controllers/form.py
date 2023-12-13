import jinja2
from odoo import http
from odoo.http import request
from odoo.exceptions import UserError
from odoo import models, fields, _
import werkzeug
import werkzeug.utils

import logging
_logger = logging.getLogger(__name__)

loader = jinja2.PackageLoader('odoo.addons.37_search_employee', 'views')
env = jinja2.Environment(loader=loader, autoescape=True)

class SearchEmployee(http.Controller):

    @http.route('/public/employee', methods=['GET'],  cors='*', auth='public')
    def get_home(self, **kwargs):
        my_current_url = request.session.get('my_current_url')
        user = kwargs.get('user_id')
        company = http.request.env['res.company'].sudo().search([], limit=1)
        return env.get_template('home.html').render({
                'csrf_token': http.request.csrf_token(),
                'user': user,
            })