{
    'name':'travell_agency',
    'version': '1.0',
    'depends':['base','sale'],
    'installable':True,
    'application':True,
    'data':[
      'security/ir.model.access.csv',
        'views/travel_agency_action.xml',
        'views/travel_agency_view.xml',
        'views/travel_agency_menu.xml',
        'views/travel_agency_form.xml',

    ]
}