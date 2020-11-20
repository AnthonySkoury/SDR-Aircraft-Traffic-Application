import React, { Component } from 'react';

import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import FormControl from 'react-bootstrap/FormControl'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Container from 'react-bootstrap/Container'

class NavBar extends React.Component {
  render() {
    return (
      <>
      <Navbar bg="dark" variant="dark">
        <Navbar.Brand href="#ats">Air Traffic System</Navbar.Brand>
        <Nav className="mr-auto">
          <Nav.Link href="#home">Feature 1</Nav.Link>
          <Nav.Link href="#features">Feature 2</Nav.Link>
          <Nav.Link href="#pricing">Feature 3</Nav.Link>
        </Nav>
        <Form inline>
          <FormControl type="text" placeholder="Search" className="mr-sm-2" />
          <Button variant="outline-info">Search</Button>
        </Form>
      </Navbar>
      </>
    );
  }
}

export default NavBar
