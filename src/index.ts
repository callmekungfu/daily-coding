import * as _ from 'lodash';
import './styles/style.css';


function component() {
    var element = document.createElement('div');
    // Lodash, now imported by this script
    element.innerHTML = _.join(['Hello', 'Yong', 'Lin', 'Wang'], ' '); +
    element.classList.add('hello');
    return element;
}

document.body.appendChild(component());