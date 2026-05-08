import { rpc } from "@web/core/network/rpc";
import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";

console.log('wwwwww')

export class EmployeeMail extends Interaction {
    static selector = '.details_div';

    dynamicContent = {

        ".mail_btn": {
            't-on-click': (ev) => this.submit_request(ev),
        }

    }

    setup() {
     this.sequence_number='';
    }
    submit_request(ev){
        ev.preventDefault();

        console.log('mailllll',this)
    }




}
registry.category("public.interactions").add("payslips_in_my_account.employeemail",EmployeeMail);