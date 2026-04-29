import { patch } from "@web/core/utils/patch";
import {ControlButtons} from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { NumberPopup } from "@point_of_sale/app/components/popups/number_popup/number_popup";
import { usePos } from "@point_of_sale/app/hooks/pos_hook";
console.log('working')
patch(NumberPopup.prototype,{

    async setup(){
         super.setup(...arguments)
        this.pos=usePos();
    },


    async confirm(){
        console.log('disc btn',this.state.buffer)
        this.order=this.pos.getOrder()
        console.log(this.order.displayPrice)
        this.global_discount=this.order.displayPrice*this.state.buffer/100
        console.log('global dics',this.global_discount)
        // this.pos.price_limit+=this.global_discount
        // console.log('price limit',this.pos.price_limit)
        // this.pos.setDiscountFromUI(this.order.displayPrice,this.global_discount)
        return super.confirm();
    }

})

