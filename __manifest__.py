# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'school',
    'version': '1',
    'category': 'details',
    'author': 'HN0416',
    'company': 'HN',
    'maintainer': 'school',
    'summary': 'school details',
    "description": """To manage school details""",
    "depends": ['base'],
    'data': [
        'views/school_details_view.xml',
        'views/subjects_available_view.xml',
        'views/admission_form_view.xml',
        'views/student_profile_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
