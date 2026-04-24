{
    'name': 'POS Module',
    'version': '1.0',
    'depends':['base','product','point_of_sale'],
    'application':True,
    'instalable':True,

    'data':[
        'security/ir.model.access.csv',
        'views/product_template_view.xml',


    ],

    'assets': {
        'point_of_sale._assets_pos': [
            'pos_module/static/src/xml/pos_product_brand.xml',
        ],
    }
}