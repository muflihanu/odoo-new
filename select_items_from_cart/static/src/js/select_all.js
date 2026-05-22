
import { browser } from '@web/core/browser/browser';
import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";
import { rpc } from '@web/core/network/rpc';
import { redirect } from '@web/core/utils/urls';
import wSaleUtils from '@website_sale/js/website_sale_utils';



export class SelectAll extends Interaction {
    static selector = '#shop_cart';
    dynamicContent = {
         ".select":{
             't-on-click':(ev)=>this.SelectAll(ev),
         }
    }

    setup(){

    }
      SelectAll(ev) {
         // document.querySelector('.check{{line.id}}').checked=true
         console.log('select all',this)
         rpc('/select/all')

        }


}
registry.category('public.interactions').add('select_items_from_cart.SelectAll', SelectAll);