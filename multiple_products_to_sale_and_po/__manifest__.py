{
    'name': 'Multiple Products To Sale And PO',
     'version': '1.2',
     'summary': 'add multiple products To Sale And purchase',
    'depends':['base','purchase','sale'],
    'application':True,
    'instalable':True,

    'data':[
        # 'views/res_config_settings_views.xml',
        'views/purchase_order_line_view.xml',
    ]

}