import React from 'react';


class Report extends React.Component {
    static LABELS = {
        "alphabet": "Alphabetical string",
        "real_numbers": "Real numbers",
        "integers": "Integers",
        "alphanumeric": "Alphanumerics"
    }

    constructor ( props ) {
        super( props );
        this.props = props;

        this.state = {
            reportList: []
        }
    }


    getReport = ( reportId, e ) => {
        e.preventDefault();

        let options = {
                method: 'GET',
                mode: 'cors',
                cache: 'no-cache',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json'
                }
            };


        fetch(`/api/stats/${reportId}`, options)
            .then( res => res.json())
            .then( 
                ( result ) => {
                    let response = result.data;
                    this.setState({
                        ...this.state.reportId,
                        reportList: Object.keys(response).map( (key) => 
                            <li key={ key }>
                                <label>{ Report.LABELS[key] }:</label>
                                &nbsp;{ response[key] }
                            </li>
                        )
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
                { this.props.reportId && (<div>
                    <button onClick={ ( e ) => this.getReport( this.props.reportId, e ) }>Report</button>
                </div>
                )}

                <div>
                    <ul> { this.state.reportList }</ul>
                </div>
            </div>
        );
    }
}


export default Report;
