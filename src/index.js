"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const _ = require("lodash");
function greeter(person) {
    return "Hello, " + person;
}
let user = _.join(['Yong', 'Lin', 'Wang'], ' ');
document.body.innerHTML = greeter(user);
//# sourceMappingURL=index.js.map