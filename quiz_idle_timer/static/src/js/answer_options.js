/** @odoo-module **/
import { registry } from "@web/core/registry";
import {Component, useState,onWillUnmount,onWillDestroy} from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
const actionRegistry = registry.category("actions");
export class AnswerOptions extends Component {

    static template="quiz_idle_timer.Answer";

    setup() {
        super.setup();

    }


   static props = {
       answer: Object,
       checkingAnswer:Function,

   };







}

