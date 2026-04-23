/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/services/pos_store";
console.log('heeelo')
patch(PosStore.prototype, {
    async  processServerData() {
          await super.processServerData();
          console.log('model',this.models)
      }

});












