import React, {Component} from 'react';

class ListItem extends Component {
    render() {
        return (
            <li>{this.props.text}</li>
        );
    }
}

export default ListItem;
