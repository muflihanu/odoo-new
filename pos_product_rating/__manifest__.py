
{
   'name': 'Pos Product Rating',
    'version': '1.0',
    'depends':['base','point_of_sale'],
    'application':True,
    'instalable':True,

    'data':[
        'views/product_template_view.xml',


    ],

    'assets': {
        'point_of_sale._assets_pos': [
            'pos_product_rating/static/src/xml/product_rating_productcard.xml',
            'pos_product_rating/static/src/xml/order_line_product_rating.xml',

        ],
    }
}