import './App.css';
import React from "react";
import axios from 'axios'
import UserList from "./components/Users";

import Header from "./components/Header";
import Footer from "./components/Footer";


const api_url = 'http://127.0.0.1:8000/api'

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        };
    }

    componentDidMount() {
        axios
            .get(`${api_url}/users/`)
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
            <div>
                <Header/>
                <UserList users={this.state.users}/>
                <Footer/>
            </div>
        )
    }
}

export default App;
