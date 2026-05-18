/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
const actionRegistry = registry.category("actions");
class ProductDetails extends Component {}
ProductDetails.template = "multiple_products_to_sale_and_po.product_detals";
// Register the component with the action tag
actionRegistry.add("product_details_tag",ProductDetails);