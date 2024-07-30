# __manifest__.py
{
    'name': 'POS Close Notification',
    'version': '1.0',
    'summary': 'Send notification when POS session closes',
    'description': 'This module sends a notification when a POS session is closed.',
    'author': 'Tu Nombre',
    'depends': ['point_of_sale', 'bus', 'web'],
    'data': [
        'views/assets.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
