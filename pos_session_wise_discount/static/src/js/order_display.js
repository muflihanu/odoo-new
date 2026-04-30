import { patch } from "@web/core/utils/patch";
import { OrderDisplay } from "@point_of_sale/app/components/order_display/order_display";
import { usePos } from "@point_of_sale/app/hooks/pos_hook";

patch(OrderDisplay.prototype, {
   async setup(){
       this.pos=usePos();
       this.disc=this.pos.price_limit
       console.log('display',this.pos)
       return super.setup();
   },
    

})