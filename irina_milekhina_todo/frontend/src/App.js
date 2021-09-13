import './App.css';
import React from "react";
import axios from 'axios'
import UserList from "./components/Users";
import Header from "./components/Header";
import Footer from "./components/Footer";
import ProjectList from "./components/Projects";
import TodoList from "./components/Todos";
import {BrowserRouter, Route, Switch} from "react-router-dom";
import ProjectDetailItem from "./components/ProjectDetail";


const api_url = 'http://127.0.0.1:8000/api'
const apiServices = ['users', 'projects', 'todos']

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': []
        };
    }

    componentDidMount() {
        axios
            .get(`${api_url}/${apiServices[0]}/`)
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users,
                    }
                );
            })
            .catch(error => console.log(error));

        axios
            .get(`${api_url}/${apiServices[1]}/`)
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects,
                    }
                );
            })
            .catch(error => console.log(error));

        axios
            .get(`${api_url}/${apiServices[2]}/`)
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos,
                    }
                );
            })
            .catch(error => console.log(error));
    }


    render() {
        return (
            <div className={'App'}>
                <BrowserRouter>
                    <Header/>
                    <div className="container">
                        <Switch>
                            <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                            <Route exact path='/projects/'
                                   component={() => <ProjectList projects={this.state.projects}/>}/>
                            <Route exact path='/todos/' component={() => <TodoList todos={this.state.todos}/>}/>
                            <Route exact path='/projects/:id'>
                                <ProjectDetailItem projects={this.state.projects}/>
                            </Route>
                        </Switch>
                    </div>
                </BrowserRouter>
                <Footer/>
            </div>
        )
    }
}

export default App;
