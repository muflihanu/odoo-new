/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component,useState } from "@odoo/owl";
import { useDebounced } from "@web/core/utils/timing";
const actionRegistry = registry.category("actions");
import { useService } from "@web/core/utils/hooks";
class PurchaseProductDetails extends Component {

    setup() {
        super.setup();
        this.orm = useService('orm');
        this.action=useService('action');
        this.FetchProductData();
        this.state=useState({
            data:[],
        })
      this.plus=0
        this.products =new Object();
      this.purchase_id=this.props.action.params.order_id

    }

    //fetching all the products
   async FetchProductData(){
        var result=await  this.orm.call("purchase.order.line","get_products",[],{})
       this.state.data=result.product_values


    }
       //increasing the product quantity
      increaseQuantity(el) {
        this.plus=Number(el.target.parentElement.nextSibling.innerHTML)
        this.plus=this.plus+1
          el.target.parentElement.nextSibling.innerHTML=this.plus
    }
    //decreasing the product quantity
    decreaseQuantity(ev){
         this.plus=Number(ev.target.parentElement.previousElementSibling.innerHTML)
         if(this.plus<=0){
             ev.target.parentElement.previousElementSibling.innerHTML='0'
         }else{
             this.plus=this.plus-1
        ev.target.parentElement.previousElementSibling.innerHTML=this.plus


         }

    }
     //adding the selected products
     async AddSelectedProducts(ev, productId,price) {
         console.log('price',price)
         const qty=ev.target.parentElement.parentElement.childNodes[1].childNodes[0].childNodes[1].innerHTML
         if(qty>0){
                 if(Object.keys(this.products).length!=0){

                      for (const [key, value] of Object.entries(this.products)) {
                       if(key == productId){

                            delete this.products[key];
                            this.products[productId]=[qty,price];
                       }else{
                            this.products[productId]=[qty,price];
                            ev.target.parentElement.parentElement.parentElement.parentElement.childNodes[0].checked=true

                       }
                      }

                 }else{
                      this.products[productId]=[qty,price];
                      ev.target.parentElement.parentElement.parentElement.parentElement.childNodes[0].checked=true

                 }

         }

        }

        //creating the record with selected products
        async  CreateRecord(ev){

            if(Object.keys(this.products).length>0){
            for (const [key, value] of Object.entries(this.products)) {
                         await this.orm.create('purchase.order.line',[{order_id:this.purchase_id,
                                  name: "product",
                                  product_id:key,
                                  product_qty:value[0],
                             price_unit:value[1]
                             ,}])}
                }

             if (this.env.config.breadcrumbs.length > 1) {
                 await this.action.restore();
        }else{
                 await this.action.doAction({
                type: "ir.actions.act_window",
                res_model: 'purchase.order',
                views: [[false, "form"]],
                view_mode: "form",
                res_id: this.purchase_id,
            });
             }
             
         }


}

PurchaseProductDetails.template = "multiple_products_to_sale_and_po.PurchaseProductDetals";
  actionRegistry.add("purchase_product_details_tag",PurchaseProductDetails);
