{
    'name': 'Mandatory Attachment For PO',
    'depends':['base','purchase'],
    'application':True,
    'instalable':True,

    'data':[
        'views/res_config_settings_views.xml',
        'views/purchase_order.xml',
    ]

}