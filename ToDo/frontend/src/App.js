import React from 'react';
//import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import axios from 'axios';
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import {BrowserRouter, Route, Routes, Link, Switch} from 'react-router-dom'


const NotFound404 = ({ location }) => {
return (
    <div>
        <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
)
}


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': []
        }
    }


    componentDidMount() {
        axios.get('http://127.0.0.1:8000/users/')
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error));

        axios.get('http://127.0.0.1:8000/projects/')
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error));
    }

    render() {
        return (
            <div className="App">
            <Menu/>
               <BrowserRouter>
                   <nav>
                       <ul>
                           <li><Link to="/">Users</Link></li>
                           <li><Link to="/projects">Projects</Link></li>
                       </ul>
                   </nav>
                   <Routes>
                       <Route exact path='/' element={<UserList users={this.state.users}/>}/>
                       <Route exact path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                   </Routes>
                </BrowserRouter>
               <Footer/>
            </div>
        )
    }
}

export default App;