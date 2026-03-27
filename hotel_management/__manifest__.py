{
    'name':'Hotel Management',
    'depends':['base','mail','account','base_automation','lunch'],
    'installable':True,
    'application':True,
    'data':{
        'views/hotel_accommodation_views.xml',
        'views/hotel_managment_menu.xml',
        'views/hotel_rooms_views.xml',
        'views/hotel_food_items_views.xml',
        'views/hotel_food_category_views.xml',
        'views/hotel_facility_views.xml',
        'views/order_food_views.xml',
        'views/hotel_guests_views.xml',
        'data/sequence_data.xml',
        'data/hotel_accommodation_email_templates.xml',
        'data/hotel_accommodation_automatic_email_data.xml',
        'data/hotel_management_automated_action_data.xml',
        'data/hotel_management_archive_automation_data.xml',
        'security/ir.model.access.csv',
        'report/hotel_management_report_template.xml',
        'report/ir.actions.report.xml',
        'security/hotel_management_groups.xml',
        'security/hotel_management_security.xml',
        'wizard/hotel_management_report_wizard.xml',
        'static/src/js/action_manager.js',



    },
    'demo':[
        'demo/data_demo.xml',

    ]
}
