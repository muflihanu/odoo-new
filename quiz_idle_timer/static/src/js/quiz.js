/** @odoo-module **/
import { registry } from "@web/core/registry";
import {Component, useState} from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
const actionRegistry = registry.category("actions");
class QuizDashboard extends Component {


     setup() {
        super.setup();
        this.orm = useService('orm');
        this.action=useService('action');
        this.FetchProductData();
        this.state=useState({
            data:[],
        })


    }

   //fetching all the products
   async FetchProductData(){
        // var result=await  this.orm.call("quiz.question","start_quiz",[],{})
       // this.state.data=result
       // console.log('ttt',this.state.data)


    }



}
QuizDashboard.template = "quiz_idle_timer.QuizDashboard";
actionRegistry.add("quiz_dashboard_tag", QuizDashboard);
