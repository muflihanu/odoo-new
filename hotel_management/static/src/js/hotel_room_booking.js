import { renderToElement } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";




publicWidget.registry.HotelRoomBooking = publicWidget.Widget.extend({
    selector: ".booking_form",

     events:{
     "click  #btn_submit":'_form_values',

     },
     start: function () {
        console.log("dgh")
//        this._super.apply(this,arguments);

     },
     _form_values: function(ev){
     ev.preventDefault();
     const form_data =this.$el;
     console.log(form_data)

     }


    });

