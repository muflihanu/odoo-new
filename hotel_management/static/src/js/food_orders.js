import { rpc } from "@web/core/network/rpc";
import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";


export class FoodOrder extends Interaction {
    static selector='.food_order_form';
    // async willStart() {
    //     const result = await rpc('/food_orders', {});
    //     console.log('result', result)
    // }

        dynamicContent = {

        ".category_ids": {
            "t-on-change": (ev) =>this.food_items(ev),
          },

        "#btn_submit": {
            "t-on-click": (ev) =>this._form_values(ev),
          }
      }

       setup() {
           // $(".").chosen();
           this.food_items_values='';
       }


    food_items(ev){
            this.form_data=new FormData(this.el)
          const category_values=this.form_data.getAll('category_ids')
          const items_values=this.form_data.getAll('items_ids')

          console.log('category',category_values)
        console.log('food',items_values)
        items_values.innerHTML=category_values


    }

}
registry.category("public.interactions").add("hotel_management.foodorder",FoodOrder);