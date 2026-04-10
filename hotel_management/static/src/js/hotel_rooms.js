
import { renderToElement } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";
publicWidget.registry.HotelMnanagementRooms = publicWidget.Widget.extend({
   selector : '.room_section',
   async willStart() {
       const result = await rpc('/hotel_management_room', {});
       console.log('result',result)
       if(result){
           this.$target.empty().html(renderToElement('room_snippet.room_data', {result: result}))
       }
   },
});