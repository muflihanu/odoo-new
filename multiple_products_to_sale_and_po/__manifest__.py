{
    'name': 'Multiple Products To Sale And PO',
     'version': '1.2',
     'summary': 'add multiple products To Sale And purchase',
    'depends':['base','purchase','sale'],
    'application':True,
    'instalable':True,

    'data':[
        'views/purchase_order_view.xml',
        'views/sale_order_view.xml',
    ],

'assets': {
   'web.assets_backend': [
       'multiple_products_to_sale_and_po/static/src/js/product_details.js',
       'multiple_products_to_sale_and_po/static/src/xml/product_details.xml',
       'multiple_products_to_sale_and_po/static/src/js/purchase_product_details.js',
       'multiple_products_to_sale_and_po/static/src/xml/purchase_product_details.xml',
   ],
},
}