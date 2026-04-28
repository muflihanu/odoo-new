import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/services/pos_store";
import { _t } from "@web/core/l10n/translation";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import {PurchaseLimitPopup} from "./purchase_limit_popup.js";


patch(PosStore.prototype, {


     async pay(){
         this.orderinfo=this.getOrder();

          this.partner=this.orderinfo.getPartner();
         this.order_total_amount=this.orderinfo.prices.taxDetails.total_amount
         if(!this.partner) {

              this.env.services.dialog.add(AlertDialog, {
                    title: _t("Warning"),
                    body: _t("Select a Customer")
            });
             return false
         }
         else if(this.partner.activate_purchase_limit==true && this.order_total_amount>this.partner.purchase_limit){

              this.env.services.dialog.add(PurchaseLimitPopup,   {
                title: _t("Warning"),
                body: _t(`your purchase limit = ${this.partner.purchase_limit}`),
            });
             return false
         }else{
             console.log('limit')

         }

          return await super.pay();
      },



});