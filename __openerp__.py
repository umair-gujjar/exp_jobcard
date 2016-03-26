# -*- coding: utf-8 -*-
{
    'name': "Expert Jobcard",

    'summary': "Addition of fields and bill management in Mrp and Product",

    'description': "Fields are added in the MRP and Product",

    'author': "Tax Tech",
    'website': "http://www.taxtech.com",


    # any module necessary for this one to work correctly
    'depends': ['base','mrp','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
}
