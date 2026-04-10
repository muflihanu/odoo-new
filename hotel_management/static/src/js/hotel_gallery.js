
import { renderToElement } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";
console.log('uuuuuuuuuuuuuuuuuuuuuuuu')
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
	   var chunks = _chunk(result,2)
		chunks[0].is_active = true
	   console.log('chunks',chunks)
		element.html(renderToElement('hotel_management.gallery_snippet_carousel', {
				chunks
			}))
   },

	// start: function () {
	//
	// }
});
publicWidget.registry.hotel_management = HotelGallery;
	return HotelGallery;