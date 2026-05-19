/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component,useState } from "@odoo/owl";
const actionRegistry = registry.category("actions");
import { useService } from "@web/core/utils/hooks";
import { renderToFragment } from "@web/core/utils/render";
class ProductDetails extends Component {

    setup() {
        super.setup();
        this.orm = useService('orm');
        this._fetch_product_data();
        this.state=useState({
            data:[],
        })
      this.plus=0
        this.products =new Object();
        this.color='';

      this.sale_id=this.props.action.params.sale_order_id
        console.log('id',this.sale_id)

    }

   async _fetch_product_data(){
        var result=await  this.orm.call("sale.order.line","get_products",[],{})
       this.state.data=result.product_values


    }

      increaseQuantity(el) {
        this.plus=Number(el.target.parentElement.nextSibling.innerHTML)
        this.plus=this.plus+1
          el.target.parentElement.nextSibling.innerHTML=this.plus
    }

    decreaseQuantity(ev){
         this.plus=Number(ev.target.parentElement.previousElementSibling.innerHTML)
         if(this.plus<=0){
             ev.target.parentElement.previousElementSibling.innerHTML='0'
         }else{
             this.plus=this.plus-1
        ev.target.parentElement.previousElementSibling.innerHTML=this.plus
         }

    }

     add_selected_products(ev, productId) {

         const qty=ev.target.parentElement.parentElement.childNodes[1].childNodes[0].childNodes[1].innerHTML
         if(qty>0){
                 if(Object.keys(this.products).length!=0){

                      for (const [key, value] of Object.entries(this.products)) {
                       if(key == productId){
                            console.log(`${key} is ${value}`);
                       }else{
                            this.products[productId]=qty;
                     console.log('dd',ev)
                     // this.color.style.backgroundColor = "red";
                       }

            }

                 }else{
                      this.products[productId]=qty;
                     console.log('else')
                 }


         }

        }

        async  create_record(ev){

         console.log('creating',this.sale_id)
            console.log('dict', typeof this.products,Object.keys(this.products).length)
            if(Object.keys(this.products).length>0){

            for (const [key, value] of Object.entries(this.products)) {
                  console.log(`${key} is ${value}`);
                          this.orm.create('sale.order.line',[
                    {order_id:this.sale_id,
                        name: "product",
                        product_id:key,
                        product_uom_qty:value,
                    }
                ])
            }

                }else{
                alert("Select at least one product ")
            }

         }


}

ProductDetails.template = "multiple_products_to_sale_and_po.product_detals";
  actionRegistry.add("product_details_tag",ProductDetails);
