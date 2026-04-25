import { ProductCard } from "@point_of_sale/app/components/product_card/product_card";
import { patch } from "@web/core/utils/patch";

import { Component, useState } from "@odoo/owl";
// console.log('hello')

//
// export class Brand extends Component {
//     static template = "pos_module.ProductCard";
//
//     setup() {
//  if(this.props.product.brand_id){
//       this.state = useState({ value: this.props.product.brand_id.raw.name });
//  }
//
//     }
//
//
// }




//
// patch(ProductCard.prototype, {
//     setup(){
//
//         if(this.props.product.brand_id){
//              // console.log('this',this.props.product.brand_id.raw.name)
//             this.val=this.props.product.brand_id.raw.name
//             // console.log(this.val)
//         }
//
//     }
//
// });