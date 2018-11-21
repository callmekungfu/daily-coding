import * as React from 'react';

export interface IHelloProps {
    label: string;
    count: number;
    onIncrement: () => any;
}

export const Hello: React.SFC<IHelloProps> = (props) => {
    const { label, count, onIncrement } = props;
    const handleIncrement = () => { onIncrement(); };
    return (
        <div>
            <span>{label}: {count}</span>
            <button type="button" onClick={handleIncrement}>
                {`Increment`}
            </button>
        </div>
    );
};
