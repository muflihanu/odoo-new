{
    'name': 'Quiz Idle Timer',
    'application':True,
    'installable':True,
    'depends':['base'],
    'data':{
        'security/ir.model.access.csv',
        'views/quiz_idle_timer_menus.xml',
        'views/quiz_question_view.xml',
        'views/quiz_question_template.xml',
    },


'assets': {
   'web.assets_backend': [
       'quiz_idle_timer/static/src/js/quiz.js',
       'quiz_idle_timer/static/src/xml/quiz_template.xml',


   ],
},

}