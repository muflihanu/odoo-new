
import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/services/pos_store";
import { _t } from "@web/core/l10n/translation";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(PosStore.prototype,{

     async setup(){
         super.setup(...arguments);
         this.price_limit=0;


    },

    async pay(){
          this.orderinfo=this.getOrder();
         this.orderlines= this.orderinfo.getOrderlines();
        if(this.orderlines){
            this.orderlines.forEach((item) => {
                if (item.isDiscountLine == false) {
                    this.price_limit += item.priceInclNoDiscount - item.priceIncl
                }
                else {
                this.price_limit += Math.abs(item.priceInclNoDiscount)

            }
             });
                }
            if(this.config.discount_limit<this.price_limit){
                this.discount_amount=this.price_limit.toFixed(2)
                 this.env.services.dialog.add(AlertDialog, {
                    title: _t("Warning"),
                    body: _t(`Maximum discount limit = ${this.config.discount_limit}   Your discount amount = ${this.discount_amount}`)
            });
                this.price_limit=0;

            }else{
                 return await super.pay();
            }


    }


})