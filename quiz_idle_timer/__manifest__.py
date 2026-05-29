{
    'name': 'Quiz Idle Timer',
    'application':True,
    'installable':True,
    'depends':['base', 'web'],
    'data':{
        'security/ir.model.access.csv',
        'views/quiz_question_view.xml',
        'views/quiz_question_template.xml',
        'views/res_config_settings.xml',
        'views/quiz_over_page.xml',
        'views/quiz_idle_timer_menus.xml',

    },


'assets': {
   'web.assets_backend': [
       'quiz_idle_timer/static/src/js/quiz.js',
       'quiz_idle_timer/static/src/xml/quiz_template.xml',
       'quiz_idle_timer/static/src/js/answer_options.js',


   ],
},

}