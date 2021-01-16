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
    console.log('starting')
    console.log('time', new Date().toISOString()	)
    let date = new Date()
    // date.setMilliseconds(0);
    let start = date.toISOString()
    let temp = date
    temp.setSeconds(temp.getSeconds()-1)
    let end = temp.toISOString()
    // console.log('string is',"http://192.168.0.105:8000/api/aircraftdata/?start-time=" + start + "&end-time="+end)
    try {
      this.myInterval = setInterval(async () => {
        let date = new Date()
        // date.setMilliseconds(0);
        let start = date.toISOString()
        let temp = date
        temp.setSeconds(temp.getSeconds()-1)
        let end = temp.toISOString()
        // const res = await fetch("http://192.168.0.105:8000/api/aircraftdata/?start-time=" + start + "&end-time="+end)
        // console.log('string is',"http://192.168.0.105:8000/api/aircraftdata/?start-time=" + start + "&end-time="+end)
        // const res = await fetch("http://192.168.0.105:8000/api/aircraftdata/?start-time=2020-12-04T21:10:09Z&end-time=2020-12-04T21:11:49Z")
        // const res = await fetch("http://192.168.0.105:8000/api/aircraftdata/")
        
        const res = await fetch("http://192.168.0.1:8000/api/aircraftdata/")
        let data = await res.json();
        // const filteredData = this.state.result.filter(data => new Date(data.timestamp) >= new Date("09/30/2019") && new Date(data.timestamp) <= new Date("10/07/2019"))
        // const filteredData =  data.filter(d => new Date().toISOString() <= d.start-time)
        console.log('adding',data)
        // console.log('example',data[0].datarecord_set[0].timestamp)
        console.log('time', new Date())
        let newdata
        if(data.length > 6) {
          newdata = data.slice(-6)
        } else {
          newdata = data
        }
        console.log('new data is',newdata)
        this.setState({
          data: newdata
        })
      }, 2000);
    } catch(e) {
      console.log('error', e);
    }
  }

  componentWillUnmount() {
    clearInterval(this.myInterval)
  }

  render() {
    return (
      <Container fluid style={{ overflowY: 'auto', height: '41.5em', padding: '0', margin: '0', }}>
        <div>Aircraft Data</div>
        <br/>
          <div >
            {this.state.data && this.state.data.map(d => {
              return (
                  <div key={d.icao}>
                    <Row fluid>
                      <Col>
                        <div>ICAO: {d.icao}</div>
                        <div>Altitude: {d.datarecord_set[0].altitude}</div>
                        <div>Track: {d.datarecord_set[0].track}</div>
                      </Col>
                      <Col>
                        <div>Aircraft Type: {d.aircraft}</div>
                        <div>Ground Speed: {d.datarecord_set[0].ground_speed}</div>
                        <div>Latitude: {d.datarecord_set[0].latitude}</div>
                        <div>Longitude: {d.datarecord_set[0].longitude}</div>
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
