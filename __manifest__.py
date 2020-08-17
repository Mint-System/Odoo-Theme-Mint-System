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
    'version': '0.7.11',
    'sequence': 120,

    'depends': ['website_blog'],

    'data': [
        'views/layout.xml',
        'views/assets.xml',
        'views/snippets.xml',
        'views/snippet_options.xml'
    ],
}