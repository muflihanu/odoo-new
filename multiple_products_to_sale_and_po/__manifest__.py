{
    'name': 'Multiple Products To Sale And PO',
     'version': '1.2',
     'summary': 'add multiple products To Sale And purchase',
    'depends':['base','purchase','sale'],
    'application':True,
    'instalable':True,

    'data':[
        'security/ir.model.access.csv',
        'views/purchase_order_line_view.xml',
        'views/product_details_view.xml',
        'views/sale_order.xml',
        'wizard/sale_product_wizard.xml',
    ],

'assets': {
   'web.assets_backend': [
       'multiple_products_to_sale_and_po/static/src/js/product_details.js',
       'multiple_products_to_sale_and_po/static/src/xml/product_details.xml',
   ],
},
}