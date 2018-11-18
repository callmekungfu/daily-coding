"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const _ = require("lodash");
require("./styles/style.css");
function component() {
    var element = document.createElement('div');
    // Lodash, now imported by this script
    element.innerHTML = _.join(['Hello', 'Yong', 'Lin', 'Wang'], ' ');
    +element.classList.add('hello');
    return element;
}
document.body.appendChild(component());
//# sourceMappingURL=index.js.map