import { rpc } from "@web/core/network/rpc";
import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";
import { renderToFragment } from "@web/core/utils/render";


export class FoodOrder extends Interaction {
    static selector='.food_order_form';

        dynamicContent = {

        // ".category_ids": {
        //     "t-on-change": (ev) =>this.food_items(ev),
        //   },

        ".order_btn": {
            "t-on-click": (ev) =>this._order_creating(ev),
          },
        "#btn_submit":{
            't-on-click':(ev)=>this.submit_orders(ev),
        }

      }

    setup(){
            $(".category_ids").chosen().change((ev) => this.food_items(ev));
       this.food_names=[];
       this.food_qty=[];
       this.food_price=[];
       this.category_error='';
       this.qty_error_p='';
    }
     async food_items(ev){
            this.form_data=new FormData(this.el)
          const category_values=this.form_data.getAll('category_ids')

          console.log(123123, category_values)
           this.result = await rpc('/food_items', {category_values:category_values});
          const element=document.getElementById('food_orders_div');
          element.innerHTML='';
         this.result.food_vals.forEach(function(text) {


             element.insertAdjacentHTML("beforeend",`<div class="card  m-5" style="width: 10rem; align-items:center; height:280px;">
                  
                                    <img class="card-img-top text-center" src="data:image/png;base64,${text.img}" alt="'food Image'" style="padding: 0px; margin: 0px; height: 100px; width:180px;"/>
                                   <h4 class="food_name mt-3">${text.food_name}</h4>
                                    <h5 class="food_price mt-1 mb-2 text-center">${text.food_price}</h5>
                                    <div>
                                  <input  name="qty" class="mb-2 qty" type="number" placeholder="Quantity" style="width:100px;"/>  
                                  </div>
                                  <button class="btn btn-primary order_btn mb-5">Done</buttom>
                                  <br/>
                                   </div><br/>
                                   
  
`)});
        }
    _order_creating(ev){
             ev.preventDefault();
             this.qty_error_p=document.querySelector('#qty_error');
              const order_div=document.getElementById('order_table');
        const food_name=ev.target.previousElementSibling.parentElement.children[1].innerHTML
       const  food_p=ev.target.previousElementSibling.parentElement.children[2].innerHTML
        console.log('food_name',food_name)
         const  value=ev.target.previousElementSibling.firstElementChild.valueAsNumber
        console.log(ev.target.previousElementSibling.firstElementChild.valueAsNumber)
        console.log('value qty',value)
        if(isNaN(value)==true){
            this.qty_error_p.innerHTML='please enter quantity';
        }else{
             this.qty_error_p.innerHTML='';
              this.food_qty.push(value)
             this.food_price.push(food_p)
             this.food_names.push(food_name)
            order_div.insertAdjacentHTML("beforeend",`
                                      <tr>
                                <td style="border:1px solid; padding:5px;">${food_name}</td>
                                <td  style="border:1px solid; padding:5px;">${value}</td>
                                 </tr>`)
        }




    }

     async submit_orders(ev){
            ev.preventDefault();
             this.form_data=new FormData(this.el)
            this.accommodation=this.form_data.get('accommodation_id')
            this.category_error=document.querySelector('.category_error');
            const category_values=this.form_data.getAll('category_ids')
             console.log(category_values)
            if(category_values.length==0){
                this.category_error.innerHTML='please select  a category';
            }else{
                this.category_error.innerHTML='';
            }

         console.log(this.accommodation)
         console.log(this.food_names)
        console.log(this.food_qty)
         console.log(this.food_price)
         await  rpc ('/create_order',{accommodation_id:this.accommodation,food_names:this.food_names,food_qty:this.food_qty,food_price:this.food_price})


    }


}
registry.category("public.interactions").add("hotel_management.foodorder",FoodOrder);