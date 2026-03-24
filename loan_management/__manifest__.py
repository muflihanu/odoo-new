{
    'name': 'Loan Management',
    'depends':['base','hr'],
    'application':True,
    'instalable':True,

    'data':[
        'security/ir.model.access.csv',
        'views/employee_loan.view.xml',
        'data/ir.sequance.xml',
        'views/loan_management_menu.xml',
        'views/employee_loan_line.xml'
    ]

}