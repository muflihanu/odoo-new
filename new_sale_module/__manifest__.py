{
    'name': 'sale new',
    'depends':['base','hr','sale'],
    'application':True,
    'instalable':True,

    'data':[
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        # 'data/ir.sequance.xml',
        # 'views/loan_management_menu.xml',
        # 'views/employee_loan_line.xml',
        # 'views/hr_employye_view.xml'
    ]

}