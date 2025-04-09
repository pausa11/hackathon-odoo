{
    'name': 'Billing QuindiColors',
    'version': '1.0',
    'depends': ['base', 'inventory_quindicolors'],
    'data': [
        "security/ir.model.access.csv",
        "views/billing_views.xml",
        "views/billing_menus.xml",
    ],
    'installable': True,
    'application': True,
}
