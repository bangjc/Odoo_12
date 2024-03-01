# -*- coding: utf-8 -*-

{
    'name': 'Nama Module',
    'version': '12.0.0.0.0',
    'category': 'Productivity',
    'summary': 'Descripsi tentang modul',
    'author': 'ITDS (Nama Author)',
    'company': 'Mitra Asa Pratama',
    'website': 'https://www.mitraasa.co.id',
    'depends': [
        'crm',
        'sale',
        'msi_timesheet'
    ],
    'images': ['static/description/icon.jpg'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_itds.xml',
    ],
    'installable': True,
    'application' : True,
    'auto_install': False,
}