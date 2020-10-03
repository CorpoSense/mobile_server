# -*- coding: utf-8 -*-
{
    'name': "Mobile Server",

    'summary': "Server module for mobile applications.",

    'description': """
        This module controls which module will be installed on mobile application.
    """,

    'author': "CorpoSense",
    'website': "http://www.corposense.com",
    'license': "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '11.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/settings.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False
}
