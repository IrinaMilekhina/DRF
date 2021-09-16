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
import LoginForm from "./components/LoginForm";
import Cookies from "universal-cookie/lib";


const api_url = 'http://127.0.0.1:8000/api';
const apiServices = ['users', 'projects', 'todos'];
const apiAuth = 'api-token-auth';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': ''
        };
    }

    getToken(username, password) {
        axios.post(api_url + apiAuth + '/', {username: username, password: password})
            .then(response => {
                this.setToken(response.data['token']);
            })
            .catch(error => alert('Неверный логин или пароль'));
    }

    setToken(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.loadData())
    }

    getTokenFromStorage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.loadData())
    }

    isAuthenticated() {
        return this.state.token !== '';
    }

    logout() {
        this.setToken('')
        window.location.reload()
    }

    loadData() {
        apiServices.forEach((apiService) => {
            axios
                .get(`${api_url}/${apiService}/`)
                .then(response => {
                    const data = response.data.results
                    this.setState(
                        {
                            [apiService]: data
                        }
                    );
                }).catch(error => console.log(error));
        })
    }


    componentDidMount() {
        this.getTokenFromStorage();
        this.loadData();
    }

    render() {
        return (
            <div className={'App'}>
                <BrowserRouter>
                    <Header userIsAuth={this.isAuthenticated.bind(this)} userLogout={this.logout.bind(this)}/>
                    <div className="container">
                        <Switch>
                            <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                            <Route exact path='/projects/'
                                   component={() => <ProjectList projects={this.state.projects}/>}/>
                            <Route exact path='/todos/' component={() => <TodoList todos={this.state.todos}/>}/>
                            <Route exact path='/login/' component={() =>
                                <LoginForm getToken={(username, password) => this.getToken(username, password)}/>}/>
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
