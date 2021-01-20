# -*- coding: utf-8 -*-
{
    'name': "Mint System Theme",

    'summary': """
        Odoo website theme for Mint System GmbH.
    """,

    'description': """
        Odoo website theme for Mint System GmbH.
    """,
    
    'author': 'Mint System',
    'website': 'https://www.mint-system.ch',
    'website': "https://www.mint-system.ch",
    'license': 'AGPL-3',
    'category': 'Theme',
    'version': '13.0.1.0.0',
    'sequence': 120,

    'depends': ['website_blog','website_theme_install'],

    'data': [
        'views/layout.xml',
        'views/assets.xml',
        'views/snippets.xml',
        'views/snippet_options.xml'
    ],
}