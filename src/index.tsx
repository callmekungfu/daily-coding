import * as React from 'react';
import * as ReactDOM from 'react-dom';

import {
    Hello,
} from './components/hello';

import { Link } from './components/Link';

import './styles/style.css';

class Main extends React.Component<{}, {count: number}> {
    state = {
        count: 0,
    };
    render() {
        return (
            <div>
                <Hello
                    label="TypeScript"
                    count={this.state.count}
                    onIncrement={() => {
                        this.setState({count: this.state.count + 1});
                    }}
                />
                <Link page="https://yonglinwang.ca">My Website</Link>
            </div>
        );
    }
}

ReactDOM.render(
    <Main />,
    document.getElementById('example'),
);
