import './App.css';
import React from "react";
import UserList from "./components/Users";
import axios from 'axios'

const api_url = 'http://127.0.0.1:8000/api'

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        };
    }

    componentDidMount() {
        // this.setState(
        //     this.state = {
        //         'users': users
        //     }
        // )
        axios
            .get(`${api_url}/users`)
            .then(response => {
                const users = response.data;
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))


    }


    render() {
        return (
            <UserList users={this.state.users}/>
        )
    }
}


export default App;
