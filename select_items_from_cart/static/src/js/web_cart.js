
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

    setup(ev){
        document.querySelector("a[name='website_sale_main_button']")?.classList.add('disabled');
        // var total=document.querySelector('[name="o_order_total_untaxed"]')
        //  const amountUntaxed = ev.target.querySelector(
        //     'tr[name="o_order_total_untaxed"] .monetary_field'
        // );
        // console.log('this',amountUntaxed)
    }
     async  get_selected_product(ev) {

            const check=ev.target.checked
         console.log('selected',check )
            const order_id=ev.target.parentElement.children[2].innerHTML
            console.log('selected', ev.target.parentElement.children[2].innerHTML)
         await rpc('/selected_orders',{check:check,order_id:order_id})
        document.querySelector("a[name='website_sale_main_button']")?.classList.remove('disabled');

        }


}
registry.category('public.interactions').add('select_items_from_cart.WebCart', WebCart);