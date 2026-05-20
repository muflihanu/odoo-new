
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
     async  get_selected_product(ev) {
            console.log('selected', ev)

        }
}
registry.category('public.interactions').add('select_items_from_cart.WebCart', WebCart);