import React from 'react';


class Timer extends React.Component {

    constructor ( props ) {
        super( props );

        // Magic variable state. This is the only 
        // place where this.state can be defined
        this.state = { 
            date: new Date(),
            posts: [],
            comments: []
        };
    }

    // Magic method that executes after rendering
    // the component
    componentDidMount () {
        this.timerId = setInterval( () => this.tick(), 1000 );
    }

    // Magic method that's executed during tear down
    // of this component
    componentWillUnmount () {
        clearInterval( this.timerId );
    }

    tick () {
        // Helper method `setState` - This built-in
        // method updates the this.state magic variable
        this.setState( {
            date: new Date()
        } );
    }

    render () {
        return <div> { this.state.date.toLocaleTimeString() } </div>;
    }


}

export default Timer;
