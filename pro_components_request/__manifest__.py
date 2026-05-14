# -*- coding: utf-8 -*-

{
    'name': 'Pro Components Request',
    'version': '1.0',
    'depends':['base','product','stock','purchase'],
    'application':True,
    'instalable':True,

    'data':[
        'security/pro_components_request_groups.xml',
        'security/ir.model.access.csv',
        'views/pro_components_request_menu.xml',
        'data/sequence_data.xml',
        'views/employee_request_view.xml',
        'views/all_product_line.xml',
        'views/purchase_order_views.xml',
        'views/stock_picking_views.xml',


    ],

}