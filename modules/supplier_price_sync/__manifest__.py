{
    'name': 'Supplier Price Sync',
    'version': '1.0',
    'category': 'Inventory',
    'sequence': 100,
    'summary': 'Synchronize supplier prices and stock information',
    'description': """
        Module for centralized supplier price and stock synchronization.
        Allows manual input of supplier information and propagates changes across Odoo.
    """,
    'author': 'YourCompany',
    'depends': ['base', 'product', 'purchase', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/supplier_sync_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
