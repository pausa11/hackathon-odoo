/** @odoo-module **/

import { registry } from "@web/core/registry";
import { MyComponent } from "./MyComponent";

// Ahora registramos como un "clientAction"
registry.category("actions").add("my_owl.demo", MyComponent);
