import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/services/pos_store";
import {ask,} from "@point_of_sale/app/utils/make_awaitable_dialog";
import { _t } from "@web/core/l10n/translation";


patch(PosStore.prototype, {


     async pay(){
         this.orderinfo=this.getOrder();
          this.partner=this.orderinfo.getPartner();
          if(this.partner){
               this.partner_purchase_limit=this.partner.purchase_limit;
          }

         this.order_total_amount=this.orderinfo.prices.taxDetails.total_amount
         if(!this.partner) {
               await ask(this.env.services.dialog, {
                title: _t("Warning"),
                body: _t(" Select a Customer"),
            });
             return false
         }
         else if(this.order_total_amount>this.partner_purchase_limit){
              await ask(this.env.services.dialog, {
                title: _t("Warning"),
                body: _t(`your purchase limit = ${this.partner_purchase_limit}`),
            });
             return false
         }else{
             console.log('limit')

         }
          return await super.pay();
      },

    async _confirm(){
         console.log('admin can approve!!')

        return super._confirm();
     }

});