import * as _ from 'lodash';

function greeter(person: string) {
    return "Hello, " + person;
}

let user = _.join(['Yong','Lin','Wang'], ' ');

document.body.innerHTML = greeter(user)