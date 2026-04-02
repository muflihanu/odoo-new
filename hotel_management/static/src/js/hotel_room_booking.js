import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";

class  RoomBookingInteraction extends Interaction{

      static selector="booking_form"

      setup(){
      this.inputCheckIn='';
      }

      ".check_in":{
       "t-on-input": (ev) => {
                this.inputCheckIn = ev.target.value;

      }
      console.log( this.inputCheckIn,'muflih')
}