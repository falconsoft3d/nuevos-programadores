##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2018 Marlon Falcon Hernandez
#    (<http://www.marlonfalcon.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'User Licenses',
    'version': '17.0',
    'author': 'Your name',
    'maintainer': 'Your name',
    'website': 'http://www.yourweb.com',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'summary': 'User Licenses by create...',
    'depends': ['base','mail','sale'],
    'data': [
              'data/ir_sequence.xml',
              'data/ir_cron.xml',
              'security/ir.model.access.csv',
              'security/security_groups.xml',
              'views/system_license_views.xml',
              'views/menu_views.xml',

            ],
    'images': ['static/description/banner.jpg'],
}
