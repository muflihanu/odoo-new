import { patch } from "@web/core/utils/patch";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { usePos } from "@point_of_sale/app/hooks/pos_hook";

// patch(ConfirmationDialog.prototype,{
//
//      async setup() {
//         super.setup();
//         this.pos = usePos();
//     },
//      async _approve(){
//             this.pos.navigate("PaymentScreen",{orderUuid: this.pos.selectedOrderUuid})
//          this._confirm();
//      }
//
//
//
// });


export class PurchaseLimitPopup extends   ConfirmationDialog{
    static template = "pos_purchase_limit.purchase_limitDialog";

       async setup() {
        super.setup();
        this.pos = usePos();
    }
     async _approve(){
            this.pos.navigate("PaymentScreen",{orderUuid: this.pos.selectedOrderUuid})
         await this._confirm();
     }

}