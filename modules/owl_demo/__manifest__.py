{
    'name': 'OWL Demo',
    'version': '1.0',
    'category': 'Tools',
    'depends': ['base', 'web'],
    'assets': {
        'web.assets_backend': [
            'owl_demo/static/src/js/owl_demo.js',
            'owl_demo/static/src/js/MyComponent.js',
            'owl_demo/static/src/xml/MyComponent.xml',
        ],
    },
    'data': [
        'views/templates.xml',
        'views/actions.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
