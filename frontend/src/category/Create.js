import React, {Component} from 'react';

import api from "../Utils";

class Create extends Component {
    constructor(props) {
        super(props);
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
                "Content-Type": "application/json"
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
