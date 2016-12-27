# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Theme Shop',
    'summary': ' ',
    'description': '',
    'category': 'Theme',
    'sequence': 900,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'data/theme_bootswatch_data.xml',
        'views/theme_bootswatch_templates.xml',
    ],
    'images': ['static/description/icon.png'],
    'application': False,
}
