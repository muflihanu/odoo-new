import { rpc } from "@web/core/network/rpc";
import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";


export class RoomBooking extends Interaction {
    static selector = ".booking_form";

       dynamicContent = {

        ".expected_days": {
            "t-on-change": (ev) =>this.expected_days_values(ev),
          },
          ".check_in": {
            "t-on-change": (ev) =>this.check_in_values(ev),
          },

           ".room_type": {
            "t-on-change": (ev)=>this.getting_available_room(ev),
          },
            ".facility": {
            "t-on-change": (ev)=>this.facility_based_roomss(ev),
          },


        "#r_btn_submit": {
            "t-on-click": (ev) =>this._form_values(ev),
          }
      }

          setup() {

      $(".p_ids").chosen();
        this.check_in='';
        this.expected_days=0;
        this.bed_type='';
        this.form_data='';
        this.data='';
        this.mess='';
        this.error='';
        this.expected_error='';
        this.attach_error='';
        this.check_in_flag=false;
        this.days_flag=false;
        this.file_flag=false;
        this.partner_flag=false;
        this.partner='';
        this.count=0;
        this.other_guests_ids=[];
        this.other_guest_error='';
        this.rooms_avl=0;
        this.facility_based_room=0;
    }

    //fetching  room type based rooms
     async getting_available_room(ev){

           this.form_data=new FormData(this.el)
           this.bed_type=this.form_data.get('room type')
       this.room=document.querySelector('#room')
       this.facility=document.querySelector('#facility')
       this.room.innerHTML='';
          this.rooms_avl=  await  rpc('/types_rooms',{room_type:this.bed_type})

       this.rooms_avl.forEach(val => {
       const optionss = new Option(val);
        this.room.options.add(optionss);
});

    }
     //fetching facility and room type based rooms
      async facility_based_roomss(ev){
       this.form_data=new FormData(this.el)

           this.bed_type=this.form_data.get('room type')
           this.facility=this.form_data.get('facility')
       this.room=document.querySelector('#room')

         console.log('facility',this.facility)
       this.room.innerHTML='';
          this.facility_based_room=  await  rpc('/facilityss_rooms',{facility:this.facility,room_type:this.bed_type})
         console.log('available rooms',this.facility_based_room)

       this.facility_based_room.forEach(val => {
       const option = new Option(val);
        this.room.options.add(option);
});

    }
     //check-in date validation
     check_in_values(ev){
    this.form_data=new FormData(this.el)
   this.check_in=this.form_data.get('check_in')
 this.today = new Date().toISOString().slice(0, 10)
   this.error=document.querySelector('#check_in_error');
      if(this.check_in>=this.today){
       this.check_in_flag=true;
     this.error.innerHTML="";

    }else{
        this.error.innerHTML="fill the date field";
     }
 }

 //expected days validation
  expected_days_values(ev){
    this.form_data=new FormData(this.el)
    this.expected_days=this.form_data.get('expected_days')
     this.expected_error= document.querySelector('#expected_error');
      if(this.expected_days<=0){
        this.expected_error.innerHTML="expected  a positive number";
    }else{
     this.expected_error.innerHTML="";
      this.days_flag=true;
     }
 }


 //form submission
 _form_values(ev){
    ev.preventDefault();
     this.form_data=new FormData(this.el)
     console.log(this.form_data)
     this.check_in=this.form_data.get('check_in')
     this.expected_days=this.form_data.get('expected_days')
     this.bed_type=this.form_data.get('room type')
      this.error=document.querySelector('#check_in_error');
      this.expected_error= document.querySelector('#expected_error');
      this.attachment_id= this.form_data.get('attach_id');
      this.attach_error=document.querySelector('#attach_error');
      this.partner=this.form_data.get('partner_id')
      this.part_error=document.querySelector('#partner_error')
      this.count=this.form_data.get('count')
      var values = this.form_data.getAll('p_ids');
      var facility_vals=this.form_data.get('facility');
      console.log('facility_value',facility_vals)
      var room_id=this.form_data.get('room')
      this.other_guest_error=document.querySelector('#other_guest_error')
      console.log(values)

     if(this.partner===''){
      this.part_error.innerHTML="select a customer";
      }else{
         this.part_error.innerHTML="";
         this.partner_flag=true;
       }

     if (this.check_in===''){
      this.error.innerHTML="fill the field";
     }
     else{
     this.error.innerHTML="";
     this.check_in_flag=true;
      }

    if(this.attachment_id['size']==0){
       this.attach_error.innerHTML=" Attach a file";
   }else{
    this.attach_error.innerHTML="";
    this.file_flag=true;
    }

      if(this.expected_days.length==0||this.expected_days==0){
         this.expected_error.innerHTML="expected  a positive number";
     }
     else{
     this.days_flag=true;
      this.expected_error.innerHTML="";
     }



      if (this.count!=0&&values.length!=this.count || this.count==0 &&values.length>0){
       console.log('guesttttt')
       this.other_guest_error.innerHTML="select currect number of guests";
      }else{

       this.other_guest_error.innerHTML="";
        this.data={
      'check_in':this.check_in,
      'expected_days':this.expected_days,
      'bed_type':this.bed_type,
      'partner':this.partner,
      'count':this.count,
            'facilities_ids':facility_vals,
      'room_id':room_id ,
      'other_guest':values,
      }

      }

    if( this.partner_flag==true&&this.check_in_flag==true &&this.days_flag==true &&this.days_flag==true && this.file_flag==true){
     console.log('booking')
     console.log('partner',this.partner)
     console.log('count',this.count)
     console.log('other guest',this.form_data.get('p_ids'))

      if(this.count==0){
       this.data={
      'check_in':this.check_in,
      'expected_days':this.expected_days,
      'bed_type':this.bed_type,
      'partner':this.partner,
      'count':this.count,
       'facilities_ids':facility_vals,
       'room_id':room_id ,
      'other_guest':false,
      }

      }

          const file = this.attachment_id;
           const reader = new FileReader();
        reader.onload = (e) => {
            const base64 = e.target.result.split(",")[1];
            rpc("/hotel_form_rooms", {
                data_value:this.data,
                attachment_value: {
                    name: file.name,
                    data: base64,
                }
            }).then((result) => {
                console.log(result)
                if(result['result']==true){
                     window.location.replace("/room_booking_success_page");
                }else{
                window.location.replace("/hotel_accommodation_booking_template");
                }
            })
        };
        reader.readAsDataURL(file);

}
    }
}
registry.category("public.interactions").add("hotel_management.booking", RoomBooking);
