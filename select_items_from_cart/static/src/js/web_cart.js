
import { browser } from '@web/core/browser/browser';
import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";
import { rpc } from '@web/core/network/rpc';
import { redirect } from '@web/core/utils/urls';
import wSaleUtils from '@website_sale/js/website_sale_utils';



export class WebCart extends Interaction {
    static selector = '.o_cart_product';
    dynamicContent = {
        '.check': {
            "t-on-change":(ev)=> this.get_selected_product(ev),
        },
    }

    setup(){
    }
     async  get_selected_product(ev) {

            const check=ev.target.checked
         console.log('selected',check )
            const order_id=ev.target.parentElement.children[2].innerHTML
            console.log('selected', ev.target.parentElement.children[2].innerHTML)
         rpc('/selected_orders',{check:check,order_id:order_id})

        }
}
registry.category('public.interactions').add('select_items_from_cart.WebCart', WebCart);