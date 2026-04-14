from odoo import  fields, models,api,tools

class IrUiMenu(models.Model):
    _inherit = "ir.ui.menu"


    @api.model
    @tools.ormcache('frozenset(self.env.user._get_group_ids())', 'debug')
    def _visible_menu_ids(self, debug=False):
     new=set()
     res=super(IrUiMenu,self)._visible_menu_ids()
     current_user_menus=frozenset(self.env.user.menu_to_hide)
     for ids in current_user_menus:
         new.add(ids.id)

     if current_user_menus:
            return   res-new
     return  res
