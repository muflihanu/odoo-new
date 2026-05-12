import { rpc } from "@web/core/network/rpc";
import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";

export class EmployeeMail extends Interaction {
    static selector = '.details_div';

    dynamicContent = {

        ".mail_btn": {
            't-on-click': (ev) => this.submit_request(ev),
        }

    }

    setup() {
     this.sequence_number='';
     this.employee_name='';
     this.from_date='';
     this.to_date='';
    }
    //request for mail passing the values to the backend
     submit_request(ev) {
         ev.preventDefault();
         const employee_name = this.el.children[0].children[1].innerHTML
         this.employee_name = employee_name.split(': ')[1]
         const sequence_number = this.el.children[0].children[0].innerHTML
         this.sequence_number = sequence_number.split(': ')[1]
         const from_date = this.el.childNodes[3].children[0].innerHTML
         this.from_date = from_date.split(': ')[1]
         const to_date = this.el.childNodes[3].children[1].innerHTML
         this.to_date = to_date.split(': ')[1]

         rpc("/employee_mail/information", {
             sequence: this.sequence_number,
             emp: this.employee_name,
             from_d: this.from_date,
             to: this.to_date
         })

     }

}
registry.category("public.interactions").add("payslips_in_my_account.employeemail",EmployeeMail);