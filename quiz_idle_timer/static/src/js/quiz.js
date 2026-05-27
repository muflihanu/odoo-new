/** @odoo-module **/
import { registry } from "@web/core/registry";
import {Component, useState} from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
const actionRegistry = registry.category("actions");
import { rpc } from "@web/core/network/rpc";
class QuizDashboard extends Component {


     setup() {
        super.setup();
        this.orm = useService('orm');
        this.action=useService('action');
        this.timer=10
        this.seconds=0
       this.interval=setInterval(()=>this.timercheck(),1000)
        this.FetchData();
        this.state=useState({
            questions:{},
            index:0
        })

         window.onkeyup =()=>this.detect();
		window.onclick =()=>this.detect();
        window.onmouseup =()=>this.detect();
        window.onmouseover=()=>this.detect();


    }


    detect(){
         console.log('hello')
        this.seconds=0
    }
   //fetching all
   async FetchData(){

        var result=await rpc('/quiz_values/',{})
         this.state.questions=result.question_answer
    }

   timercheck(){
         this.seconds+=1
       console.log('time',this.seconds)

       if(this.seconds==this.timer){
           window.ontouchstart
           if(this.state.index!=this.state.questions.length-1) {
               this.state.index++
               this.timer += 10
           }else{
               clearInterval(this.interval)
           }
       }

   }
   get  CurrentQuestion(){

      return this.state.questions[this.state.index]
    }

    NextQuestion(){
         if(this.state.index!=this.state.questions.length-1){
             this.state.index++
             console.log('seonds',this.seconds)
             this.seconds=0
         }

    }


    PrevQuetion(){
         if(this.state.index>0){
             this.state.index--
             console.log('seonds',this.seconds)

         }

    }

    CheckingAnswer(ev){
             console.log('ticked!!1',ev.target.checked)
        }




}
QuizDashboard.template = "quiz_idle_timer.QuizDashboard";
actionRegistry.add("quiz_dashboard_tag", QuizDashboard);
