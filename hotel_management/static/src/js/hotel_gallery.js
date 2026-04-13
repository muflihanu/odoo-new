
import { renderToFragment } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { Interaction } from "@web/public/interaction";
import { rpc } from "@web/core/network/rpc";
import { registry } from "@web/core/registry";
console.log('uuuuuuuuuuuuuuuuuuuuuuuu')

// export class HotelGallery extends Interaction {
//
// 	static selector = '.hotel_gallery_snippet';
//
// 	setup() {
// 		this.element = '';
// 		this.chunks = '';
// 	}
//



export function _chunk(array, size) {
	const chunk_data = [];
	for (let i = 0; i < array.length; i += size) {
		chunk_data.push(array.slice(i, i + size));
	}
	return chunk_data;
}
var HotelGallery = publicWidget.Widget.extend({
   selector : '.hotel_gallery_snippet',
   async willStart() {
	    const result = await rpc('/gallery',{});
	   console.log('result',result)

	   const element = this.$el.find("#courosel")
	   var chunks = _chunk(result,5)
		chunks[0].is_active = true
	   console.log('chunks',chunks)
	   const d = new Date();
       let ms = d.getMilliseconds();
		element.html(renderToFragment('hotel_management.gallery_snippet_carousel', {chunks, unique:ms}))
   },
});
publicWidget.registry.hotel_management = HotelGallery;
	return HotelGallery;