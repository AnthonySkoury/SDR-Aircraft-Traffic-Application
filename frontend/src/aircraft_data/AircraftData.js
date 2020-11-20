import React, { Component } from 'react';

import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import FormControl from 'react-bootstrap/FormControl'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Container from 'react-bootstrap/Container'

// import data from "./test.js";
class AircraftData extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  async componentDidMount() {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/aircraft/")
      const data = await res.json();
      console.log(data)
      console.log('adding',data)
      this.setState({
        data
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <Container fluid>
        <div>Aircraft Data</div>
        <br/>
          <div>
            {this.state.data.map(d => {
              return (
                  <div key={d.icao}>
                    <Row fluid>
                      <Col>
                        <div>ICAO: {d.icao}</div>
                        <div>Callsign: {d.callsign}</div>
                      </Col>
                      <Col>
                        <div>Aircraft Type: {d.aircraft}</div>
                        <div>Name: {d.name}</div>
                      </Col>
                    </Row>
                    <br/>
                  </div>
              );
            })}
          </div>
          <br/>
      </Container>

    );
  }
}

export default AircraftData;


{/*
<Row>
  <div>
  {
    data.map((data,key) => {
      return (
        <div key={key}>
          <Row fluid>
            <Col>
              <div>Flight: {data.flight}</div>
              <div>Altitude: {data.altitude}</div>
              <div>Speed: {data.speed}</div>
            </Col>
            <Col>
              <div>Latitude: {data.latitude}</div>
              <div>Longitude: {data.longitude}</div>
              <div>Track: {data.track}</div>
            </Col>
          </Row>
        </div>
      )
    })
  }
  </div>
</Row>
<Row>
  <Col>
    <div>Flight: N619GE</div>
    <div>Altitude: 1075</div>
    <div>Speed: 112</div>
  </Col>
  <Col>
  <div>Lat: 33.677</div>
  <div>Lon: -117.938</div>
  <div>Track: 202</div>
  </Col>
</Row>
*/}
