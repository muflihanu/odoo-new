import { rpc } from "@web/core/network/rpc";
import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";
import { renderToFragment } from "@web/core/utils/render";


export class FoodOrder extends Interaction {
    static selector='.food_order_form';

        dynamicContent = {

        ".category_ids": {
            "t-on-change": (ev) =>this.food_items(ev),
          },

        ".order_btn": {
            "t-on-click": (ev) =>this._order_creating(ev),
          }
      }


     async food_items(ev){
            this.form_data=new FormData(this.el)
          const category_values=this.form_data.getAll('category_ids')
           this.result = await rpc('/food_items', {category_values:category_values});
          const element=document.getElementById('food_orders_div');
         this.result.food_vals.forEach(function(text) {

             element.insertAdjacentHTML("beforeend",`<div class="card  m-5" style="width: 10rem; align-items:center; height:250px;">
                  
                                    <img class="card-img-top text-center" src="data:image/png;base64,${text.img}" alt="'food Image'" style="padding: 0px; margin: 0px; height: 100px; width:180px;"/>
                                   <h4 class="food_name mt-3">${text.food_name}</h4>
                                    <div>
                                  <input  name="qty" class="mb-4 qty" type="number" placeholder="qty" style="width:100px;"/>  
                                  </div>
                                  <button class="btn btn-primary order_btn mb-5">Done</buttom>
                                  <br/>
                                   </div><br/>
                                   
  
`)});
        }
    _order_creating(ev){
             ev.preventDefault();
        const food_name=ev.target.previousElementSibling.previousElementSibling.innerHTML
         const  value=ev.target.previousElementSibling.firstElementChild.valueAsNumber
           const order_div=document.getElementById('order_table');
           order_div.insertAdjacentHTML("beforeend",`
                                      <tr>
                                <td>${food_name}</td>
                                <td>${value}</td>
                                 </tr>`)


    }
}
registry.category("public.interactions").add("hotel_management.foodorder",FoodOrder);