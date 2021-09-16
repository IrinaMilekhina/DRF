import React from 'react';

class LoginForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {'login': '', 'password': ''}
    }

    handleChange(event) {
        this.setState(
            {[event.target.name]: event.target.value}
        );
    }

    handleSubmit(event) {
        this.props.getToken(this.state.login, this.state.password)
        event.preventDefault()
    }

    render() {
        return (
            <div className="form_container">
                <form className="form_login" onSubmit={(event) => this.handleSubmit(event)}>
                    <p>Введите логин и пароль:</p>
                    <input type="text" name="login" id="input_login" className="form_input" placeholder="Username"
                           value={this.state.login}
                           onChange={(event) => this.handleChange(event)}/>
                    <input type="password" name="password" id="input_password" className="form_input"
                           placeholder="Password"
                           value={this.state.password}
                           onChange={(event) => this.handleChange(event)}/>
                    <input type="submit" value="Войти" className="form_button"/>
                </form>
            </div>
        )
    }
}

export default LoginForm