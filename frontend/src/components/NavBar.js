import React from 'react';
import { Navbar, Nav, NavDropdown, Form, FormControl, Button, Container } from 'react-bootstrap';
import irecipe_logo from '../assets/irecipe_logo.png';
import styles from '../styles/NavBar.module.css';

const NavBar = () => {
    return (
        <Navbar bg="light" expand="md" fixed='top'>
            <Container>
            <Navbar.Brand><img src={irecipe_logo} alt='logo' height={45} /></Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="ml-auto">
                    <Nav.Link style={{ color: 'rgb(0 0 0)', fontWeight: 'bold' }}><i className='fas fa-home'></i> Home</Nav.Link>
                    <Nav.Link style={{ color: 'rgb(0 0 0)', fontWeight: 'bold' }}><i className='fas fa-sign-in-alt'></i> Sign in</Nav.Link>
                    <Nav.Link style={{ color: 'rgb(0 0 0)', fontWeight: 'bold' }}><i className='fas fa-user-plus'></i> Sign up</Nav.Link>
                    
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