{
    'name': 'Payslip in My Account',
    'category': 'Website',
    'depends': ['base', 'website','hr','sale','mail'],
    'installable': True,
    'application': True,
    'data': {
        'security/paslip_in_my_account_groups.xml',
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/payslips_in_my_account_menu.xml',
        'views/user_payslip_portal_template.xml',
        'views/payslip_template.xml',
        'views/hr_employee.xml',
        'views/custom_payslip.xml',
        'views/custom_payslip_line.xml',
        'views/salary_structure.xml',
        'views/payslip_details_template.xml',
        'report/ir_action_report.xml',
        'report/payslip_report_template.xml',
        'views/employee_mails.xml',
        'data/payslip_mail_template.xml',

    },


    'assets': {
        # 'web.assets_backend': ['hotel_management/static/src/js/action_manager.js'],
        'web.assets_frontend': [
           'payslips_in_my_account/static/src/js/employee_mail.js',
        ],
    },
}
