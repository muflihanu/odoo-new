import { renderToElement } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";


import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";

export class HotelRoomBooking extends Interaction {
    static selector = ".booking_form";

       dynamicContent = {
        "#btn_submit": {
            "t-on-click": (ev) =>this._form_values(ev),
          }
      }

    setup() {
        this.check_in='';
        this.expected_days=0;
        this.bed_type='';
        this.form_data='';
        this.data='';
        this.mess='';
    }

  _form_values(ev){
    console.log('working', this)
    ev.preventDefault();
     this.form_data=new FormData(this.el)
       console.log(this.form_data)
     this.check_in=this.form_data.get('check_in')
     this.expected_days=this.form_data.get('expected_days')
     this.bed_type=this.form_data.get('room type')
      this.mess= this.form_data.get('check_in_error')

     if (this.check_in===''){

       document.querySelector('#check_in_error').TextContext="fill the date field!!";

//        alert('expected  a positive number!!')
         console.log('wwwwwwwwwwwwwwwwwwww', document.querySelector('#check_in_error'))
     }
     else if(this.expected_days.length==0||this.expected_days==0){
       alert('expected  a positive number!!')
     }
     else{
       this.data={
      'check_in':this.check_in,
      'expected_days':this.expected_days,
      'bed_type':this.bed_type,
      }
      rpc(
            "/hotel_form",{'data':this.data}
        );
        window.location.replace("/room_booking_success_page");
}
     }

}
registry.category("public.interactions").add("hotel_management.hotel_booking", HotelRoomBooking);





//publicWidget.registry.HotelRoomBooking = publicWidget.Widget.extend({
//    selector: ".booking_form",
//
//     events:{
//     "click  #btn_submit":'_form_values',
//
//     },
//     _form_values: async function(ev){
//     ev.preventDefault();
//     const form_data=new FormData(this.el)
//     console.log(form_data)
//
//     const check_in=form_data.get('check_in')
//     const expected_days=form_data.get('expected_days')
//     const bed_type=form_data.get('room type')
//
//     if (check_in===''){
//     alert('fill the date field')
//     }
//     else if(expected_days===''|| expected_days==0){
//       alert('expected  a positive number!!')
//     }else{
//      const  data={
//      'check_in':check_in,
//      'expected_days':expected_days,
//      'bed_type':bed_type,
//      }
//      console.log(data)
//      const pass= await rpc(
//            "/hotel_form",{'data':data}
//        );
//     }
//
//     }

//    });

