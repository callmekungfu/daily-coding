import * as React from 'React';

export interface ILinkProps {
    page: string;
    children: any;
}

interface IState {
    class: string;
}

const STATUS = {
    HOVERED: 'hovered',
    NORMAL: 'normal',
};

export class Link extends React.Component<ILinkProps, IState> {
    readonly state: IState = {
        class: STATUS.NORMAL,
    };

    handleMouseEnter = () => {
        this.setState({
            class: STATUS.HOVERED,
        });
    }
    handleMouseLeave = () => {
        this.setState({
            class: STATUS.NORMAL,
        });
    }
    render() {
        const { handleMouseEnter, handleMouseLeave } = this;
        const { page } = this.props;
        return(
            <a
                className={this.state.class}
                href={page || '#'}
                onMouseEnter={handleMouseEnter}
                onMouseLeave={handleMouseLeave}
            >
                {this.props.children}
            </a>
        );
    }
}
