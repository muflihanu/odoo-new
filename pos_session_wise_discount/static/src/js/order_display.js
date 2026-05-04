import { patch } from "@web/core/utils/patch";
import { OrderDisplay } from "@point_of_sale/app/components/order_display/order_display";
import { PosOrderAccounting } from "@point_of_sale/app/models/accounting/pos_order_accounting";
import { PosOrder } from "@point_of_sale/app/models/pos_order";
import { formatCurrency } from "@web/core/currency";


patch(PosOrderAccounting.prototype, {
   async setup(){
       this.disc=0;
       return super.setup();

   },

    discount_validation(){
       let disc=0;
        this.lines.forEach((item) => {
                if (item.isDiscountLine == false) {
                    disc += item.displayPriceNoDiscount-item.displayPrice
                    console.log('item',disc)
                }
                else {
                disc += Math.abs(item.priceInclNoDiscount)
                    console.log('g',item)
            }
             });
       return disc;
    },





    get discount_total(){

        return formatCurrency(this.discount_validation(), this.currency.id);


    }







})