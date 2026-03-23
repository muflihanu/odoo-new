{
    'name': 'Quick Task',
    'application':True,
    'installable':True,
    'depends':['base','sale','product','purchase','account'],
    'data':{
        'security/ir.model.access.csv',
        'views/quick_task_menu.xml',
        'views/sale_order_views.xml',
        'views/product_template_views.xml',
        'views/res_partners_view.xml',
        'views/purchase_order_view.xml',
        'views/account_move_view.xml',

    }

}