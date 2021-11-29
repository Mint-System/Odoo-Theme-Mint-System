{
    'name': "Mint System Theme",

    'summary': """
        Odoo website theme for Mint System GmbH.
    """,
    
    'author': 'Mint System GmbH, Odoo Community Association (OCA)',
    'website': 'https://www.mint-system.ch',
    'license': 'AGPL-3',
    'category': 'Theme',
    'version': '14.0.2.0.0',
    'sequence': 120,

    'depends': ['website_blog'],

    'data': [
        'views/layout.xml',
        'views/assets.xml',
        'views/snippets.xml',
        'views/snippet_options.xml'
    ],
}