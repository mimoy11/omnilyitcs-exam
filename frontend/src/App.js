import React from 'react';
import Report from './Report';

class App extends React.Component {

    constructor ( props ) {
        super( props );

        this.state = { 
            reportId: null,
            downloadLink: null,
            isLoading: false,
            reportComponent: null
        };
    }

    onSubmit = ( name, e ) => {
        e.preventDefault();
        let options = {
            method: 'POST',
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json'
            }
        };

        this.setState({
            isLoading: true,
            reportId: null,
            downloadLink: null,
            reportComponent: null
        });

        fetch('/api/generate', options)
            .then( res => res.json())
            .then( 
                ( result ) => {
                    let response = result.data;
                    this.setState({
                        isLoading: false,
                        reportId: response.id,
                        downloadLink: response.download_link,
                        reportComponent: <Report reportId={ response.id }/> 
                    });
                },
                ( error ) => {
                    console.log( error );
                }
            );
    }
 
    render () {
        return (
        <div>
            <header>{ this.props.name }</header>
            <div>
                <button onClick={ ( e ) => this.onSubmit( this.props.name, e ) }>
                    Generate
                </button>
            </div>

            { this.state.isLoading && (
                <span>Loading...</span>
            ) }

            { this.state.downloadLink && (
                <div>
                    Link: <a href={ this.state.downloadLink }>
                        { this.state.downloadLink }
                    </a>
                </div>
            )}

            { this.state.reportComponent }
        </div>
    );
  }  
}

export default App;
