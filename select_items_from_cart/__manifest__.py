{
    'name': 'Select Items from Cart',
    'category': 'Website',
    'version': '1.0',
    'depends': ['base', 'website','sale'],
    'installable': True,
    'application': True,
    'data': {

        'views/shop_cart_lines.xml',
        'views/shop_summary.xml',
    },


'assets': {
        # 'web.assets_backend': ['hotel_management/static/src/js/action_manager.js'],
        'web.assets_frontend': [
           'select_items_from_cart/static/src/js/web_cart.js',
            'select_items_from_cart/static/src/js/select_all.js',



        ],

    },
}