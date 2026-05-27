from odoo import http
from odoo.http import request

class QiuzController(http.Controller):
  """fetching available"""
  @http.route('/start_quiz/',type='http',auth="user",website=True)
  def quiz_starting_page(self,page=1):
        questions=request.env['quiz.question'].sudo().search([])
        total = questions.sudo().search_count([])
        pager = request.website.pager(
            url='/start_quiz',
            total=total,
            page=1,
            step=1,
        )
        offset = pager['offset']
        print('offset',offset)
        # customer_obj =questions[offset: offset + 1]
        return request.render("quiz_idle_timer.quiz_page",{'questions':pager})

  @http.route('/quiz_values/', type='jsonrpc', auth="user")
  def get_quiz_values(self):
      question_answer=[]
      questions=request.env['quiz.question'].sudo().search([])
      for ques in questions:
          question_answer.append({'id': ques.id, 'question': ques.name,'answer':[i.option_name for i in ques.quiz_answer_ids]})
      return {'question_answer':question_answer}



