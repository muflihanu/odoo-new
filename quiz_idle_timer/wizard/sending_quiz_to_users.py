from odoo import api, fields, models, tools

class SendingQuizToUsers(models.TransientModel):

    _name = 'wizard.sending.quiz.to.users'


    # users_ids=fields.Many2many('res.users', string='Users')
    user_id = fields.Many2one('res.users', string='User')

    def action_send_mail(self):
        template = self.env.ref('quiz_idle_timer.email_template_for_quiz')
        print('set',self.read())
        # email_values = {'email_from': self.env.user.email}
        template.send_mail(self.id, force_send=True)