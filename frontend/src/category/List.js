import React, {Component} from 'react';
import ListItem from "./ListItem";
import api from "../Utils";

class List extends Component {
    constructor(props) {
        super(props);
        this.state = {
            categories: []
        }
    }

    componentWillMount() {
        fetch(api.categories, {})
            .then(resp => resp.json())
            .then(data => {
                this.setState({categories: data.results})
            })
            .catch(error => console.log(error));
    }

    render() {
        return (
            <ul>
                {
                    this.state.categories.map((item, index) => <ListItem key={index} text={item.name}/>)
                }
            </ul>
        );
    }
}

export default List;
