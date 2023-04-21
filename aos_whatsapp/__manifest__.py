# See LICENSE file for full copyright and licensing details.

{
    'name': 'Whatsapp Client',
    'version': '16.0.0.1.0',
    'license': 'OPL-1',
    'author': "Alphasoft",
    'sequence': 1,
    'website': 'https://www.alphasoft.co.id/',
    'images':  ['images/main_screenshot.png'],
    'summary': 'This module is used for Whatsapp Client Connection',
    'category': 'Extra Tools',
    'depends': [
        'mail',
        'base_setup',
        'contacts',
    ],
    'external_dependencies': {'python': ['html2text']},
    'data': [
        'security/ir.model.access.csv',
        'data/whatsapp_mail_message_cron.xml',
        'views/res_partner_view.xml',
        'views/mail_message.xml',
        'views/mail_template.xml',
        'views/ir_whatsapp_server.xml',
        'views/menuitem_view.xml',
        'wizard/check_partner_mobile_view.xml',
        'wizard/whatsapp_message_view.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    'price': 0.0,
    'currency': 'EUR',
    'installable': True,
    'application': False,
    'auto_install': False,
}
