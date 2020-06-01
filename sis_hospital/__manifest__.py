# -*- coding: utf-8 -*-
{
    'name': "sis_hospital",

    'summary': """
        Module to Manage hospitals with Odoo13""",

    'description': """
        With this Module it will be possible to Manage Hospitals by creating hospitals, specialties and consultations  
    """,

    'author': "Ernesto A. Mederos",
    'website': "https://www.linkedin.com/in/ernesto-ahmed-mederos-70a03819a/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Clients',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hospital.xml',
        'views/specialty.xml',
        'views/consultation.xml',
        'views/res_partner.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
