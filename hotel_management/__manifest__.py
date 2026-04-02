{
    'name':'Hotel Management',
    'category': 'Website',
    'depends':['base','mail','account','base_automation','lunch','website'],
    'installable':True,
    'application':True,
    'data':{
        'security/ir.model.access.csv',
        'views/hotel_accommodation_views.xml',
        'views/hotel_managment_menu.xml',
        'views/hotel_rooms_views.xml',
        'views/hotel_food_items_views.xml',
        'views/hotel_food_category_views.xml',
        'views/hotel_facility_views.xml',
        'views/order_food_views.xml',
        'views/hotel_guests_views.xml',
        'views/snippets/hotel_accommodation_webpage_template.xml',
        'views/snippets/hotel_management_snippest_template.xml',
        'views/snippets/hotel_booking_snipet.xml'
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




    },
    'demo':[
        'demo/data_demo.xml',

    ],

    'assets':{
'web.assets_backend':['hotel_management/static/src/js/action_manager.js' ],
 'we.assets_frontend':['static/src/js/hotel_room_booking.js' ],


    },
}
