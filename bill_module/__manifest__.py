{
    'name':'Bill Module',
    'depends':['base','account','purchase','sale'],
    'installable':True,
    'application':True,
    'data':{
        'security/ir.model.access.csv',
        'views/account_move_views.xml',
        'views/account_move_menu.xml',
        'views/sale_order_views.xml'

    }
}