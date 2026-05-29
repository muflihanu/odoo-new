/** @odoo-module **/
import { registry } from "@web/core/registry";
import {Component, useState,onWillUnmount,onWillDestroy} from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
const actionRegistry = registry.category("actions");
import { rpc } from "@web/core/network/rpc";
class AnswerOptions extends Component {


     setup() {
        super.setup();






    }





















}
// AnswerOptions.template = "quiz_idle_timer.QuizDashboard";
actionRegistry.add("quiz_dashboard_tag", AnswerOptions);
