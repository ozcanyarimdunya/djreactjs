import React, {Component} from 'react';
import List from "./category/List";
import Create from "./category/Create";

import './App.css'

class App extends Component {
    render() {
        return (
            <div>
                <Create/>
                <List/>
            </div>
        );
    }
}

export default App;
