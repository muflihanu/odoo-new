
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
        var order_line_ids=[]
         var  check_values=document.querySelectorAll('.check')
           for (var i = 0; i < check_values.length; i++) {
                  console.log('work')
                     check_values[i].checked=true;
                     order_line_ids.push(check_values[i].dataset.lineId)
                     console.log('checked',order_line_ids)
                }
           rpc('/select/all',{order_line_ids:order_line_ids})
           document.querySelector("a[name='website_sale_main_button']")?.classList.remove('disabled');

        }


}
registry.category('public.interactions').add('select_items_from_cart.SelectAll', SelectAll);