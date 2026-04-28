{
    'name': 'Pos Session_Wise Discount',
    'version': '1.0',
    'depends':['base','point_of_sale'],
    'application':True,
    'instalable':True,

    'data':[
    #     'security/ir.model.access.csv',
        'views/res_config_settings.xml',
    #
    #
    ],

    'assets': {
        'point_of_sale._assets_pos': [
            'pos_session_wise_discount/static/src/js/pos_store.js',
            # 'pos_purchase_limit/static/src/js/purchase_limit_popup.js',
            # 'pos_purchase_limit/static/src/xml/purchase_limit_dialog.xml',
        ],
    }
}