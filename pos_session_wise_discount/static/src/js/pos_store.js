
import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/services/pos_store";
import { _t } from "@web/core/l10n/translation";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(PosStore.prototype,{

     async setup(){
         super.setup(...arguments);
         this.price_limit=0;
    },
        async setDiscountFromUI(line,val){
         console.log('ddd',this)
         console.log('line discount',line.prices.no_discount_total_included)
            console.log('val',val)
            console.log('discount amount',line.prices.no_discount_total_included*val/100)
            this.price_dic=line.prices.no_discount_total_included*val/100
            this.price_limit+=this.price_dic
            console.log('orginal product discount price',this.price_limit)

            if(this.config.discount_limit!=0 && this.config.discount_limit<this.price_limit){
                this.price_limit-=this.price_dic
                console.log('discount limit reach',this.price_limit)
                 this.env.services.dialog.add(AlertDialog, {
                    title: _t("Warning"),
                    body: _t(`Maximum discount limit = ${this.config.discount_limit}`)
            });
            }else{
                console.log('stil have discount value')
                return await super.setDiscountFromUI(line,val);
            }



    },


      async applyDiscount(percent, order = this.getOrder()) {
        await super.applyDiscount(...arguments);
        console.log('discount btn')
        // await this.updatePrograms();
    },

    async restrictLineDiscountChange(){
         console.log('discccc')
        return super.restrictLineDiscountChange();
    }

})