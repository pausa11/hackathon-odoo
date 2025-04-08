/** @odoo-module **/

import { Component, useState } from "@odoo/owl";

export class MyComponent extends Component {
    setup() {
        this.state = useState({ count: 0 });
    }

    increment() {
        this.state.count++;
    }
}

MyComponent.template = "owl_demo.MyComponent";
