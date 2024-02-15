import React from 'react';
import { Navbar, Nav, NavDropdown, Form, FormControl, Button, Container } from 'react-bootstrap';
import irecipe_logo from '../assets/irecipe_logo.png';
import styles from '../styles/NavBar.module.css';
import { NavLink } from 'react-router-dom';

const NavBar = () => {
    return (
        <Navbar bg="light" expand="md" fixed='top'>
            <Container>
                <NavLink to="/">
                    <Navbar.Brand><img src={irecipe_logo} alt='logo' height={45} /></Navbar.Brand>
                </NavLink>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="ml-auto">
                    <NavLink exact className={styles.NavLink} activeClassName={styles.Active} to="/"><i className='fas fa-home'></i> Home</NavLink>
                    <NavLink className={styles.NavLink} activeClassName={styles.Active} to="/signin" ><i className='fas fa-sign-in-alt'></i> Sign in</NavLink>
                    <NavLink className={styles.NavLink} activeClassName={styles.Active} to="signup"><i className='fas fa-user-plus'></i> Sign up</NavLink>
                    
                </Nav>
                <Form inline>
                    <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                    <Button variant="outline-success">Search</Button>
                </Form>
            </Navbar.Collapse>
            </Container>
        </Navbar>
    );
};

export default NavBar;