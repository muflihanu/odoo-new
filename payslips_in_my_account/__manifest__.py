{
    'name': 'Payslip in My Account',
    'category': 'Website',
    'depends': ['base', 'website','hr'],
    'installable': True,
    'application': True,
    'data': {
        'security/ir.model.access.csv',
        'views/payslips_in_my_account_menu.xml',
        'views/user_portal_template.xml',
        'views/payslip_template.xml',
        'views/hr_employee.xml',
        'views/custom_payslip.xml',

    },


    # 'assets': {
    #     'web.assets_backend': ['hotel_management/static/src/js/action_manager.js'],
    #     'web.assets_frontend': [
    #         'https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.2/jquery.min.js',
    #         'hotel_management/static/src/js/lib/chosen.jquery.min.js',
    #         'hotel_management/static/src/js/lib/chosen.min.css',
    #         'hotel_management/static/src/js/hotel_room_booking.js',
    #         'hotel_management/static/src/js/room_booking_through_rooms.js',
    #         'hotel_management/static/src/xml/hotel_management_room_content.xml',
    #         'hotel_management/static/src/js/hotel_rooms.js',
    #          'hotel_management/static/src/js/hotel_gallery.js',
    #         'hotel_management/static/src/xml/hotel_management_gallery_content.xml',
    #         'hotel_management/static/src/js/lib/jquery.multiselect.js',
    #         'hotel_management/static/src/js/lib/jquary.multiselect.css',
    #         'hotel_management/static/src/js/food_orders.js',
    #
    #
    #     ],

    # },
}
