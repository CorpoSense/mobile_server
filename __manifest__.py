# -*- coding: utf-8 -*-
{
    'name': "Mobile Server",

    'summary': "Server module for mobile applications.",

    'description': """
        This module controls which module will be installed on mobile application.
    """,

    'author': "CorpoSense",
    'website': "https://www.corposense.com",
    'license': "MIT",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '11.0.1.0.1',

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
    'installable': True,
}
