import React, {Component} from 'react';

import api from "../Utils";

class Create extends Component {
    constructor(props) {
        super(props);
        this.state = {
            token: null
        }
    }

    componentDidMount() {
        fetch(api.token, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: "ozcan",
                password: "trydjango"
            })
        })
            .then(resp => resp.json())
            .then(data => {
                this.setState({token: data.token});
                console.log(data);
            })
            .catch(error => console.log(error));
    }

    handleFormSubmit = (event) => {
        event.preventDefault();

        let categoryName = event.target.categoryName.value;
        fetch(api.categories + "create/", {
            method: "POST",
            body: JSON.stringify({
                name: categoryName
            }),
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Token " + this.state.token
            }
        })
            .then(resp => resp.json())
            .then(data => console.log(data))
            .catch(error => console.log(error));

    };

    render() {
        return (
            <form action="#" method="POST" onSubmit={this.handleFormSubmit}>
                <label>Name: </label>
                <input type="text" name="categoryName"/>
                <input type="submit"/>
            </form>
        );
    }
}

export default Create;
