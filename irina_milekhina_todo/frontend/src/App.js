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
import LoginForm from "./components/Auth";
import Cookies from "universal-cookie/lib";

const default_url = 'http://127.0.0.1:8000/'
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
            'token': '',
            'currentUsername': '',
            'currentUserFullname': ''
        };
    }

    getCurrentUserFullname(username, users) {
        const user = users.find(user => user.username === username)
        return `${user.firstName} ${user.lastName}`
    }

    getToken(username, password) {
        axios.post(default_url + apiAuth + '/', {username: username, password: password})
            .then(response => {
                this.setToken(response.data['token'], username);
            })
            .catch(error => alert('Неверный логин или пароль'));
    }

    setToken(token, username) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token, 'currentUsername': username}, () => this.loadData())
    }

    isAuthenticated() {
        return this.state.token !== '';
    }

    logout() {
        this.setToken('', '')
        this.setState({'currentUserFullname': ''})
        window.location.reload()
    }

    getTokenFromStorage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.loadData())
    }


    loadData() {
        const headers = this.getHeaders()
        let data;
        apiServices.forEach((apiService) => {
            axios
                .get(`${api_url}/${apiService}/`, {headers})
                .then(response => {
                    if (apiService === 'users' && this.state.currentUserFullname === '') {
                        data = {
                            [apiService]: response.data.results,
                            'currentUserFullname':
                                this.getCurrentUserFullname(this.state.currentUsername, response.data.results)
                        }
                    } else {
                        data = {[apiService]: response.data.results}
                    }
                    this.setState(
                        data
                    );
                }).catch(error => {
                console.log(error);
                this.setState(
                    {
                        [apiService]: []
                    }
                );
            });
        })
    }

    getHeaders() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.isAuthenticated()) {
            headers['Authorization'] = 'Token' + this.state.token
        }
        return headers
    }

    componentDidMount() {
        this.getTokenFromStorage();
    }

    render() {
        return (
            <div className={'App'}>
                <BrowserRouter>
                    <Header userIsAuth={this.isAuthenticated.bind(this)} userLogout={this.logout.bind(this)}
                            username={this.state.currentUserFullname}/>
                    <div className="container">
                        <Switch>
                            <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                            <Route exact path='/projects/'
                                   component={() => <ProjectList projects={this.state.projects}/>}/>
                            <Route exact path='/todos/' component={() => <TodoList todos={this.state.todos}/>}/>
                            <Route exact path={'/login/'} component={() => <LoginForm
                                getToken={(username, password) => this.getToken(username, password)}/>}/>
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
