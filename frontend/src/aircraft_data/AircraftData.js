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
    // this.state = {
    //   data: [],
    //   mapdata: [],
    //   markers: [],
    //   loaded: false,
    //   placeholder: "Loading"
    // };
  }

<<<<<<< HEAD
  // async componentDidMount() {
  //   console.log('starting')
  //   console.log('time', new Date().toISOString()	)
  //   let date = new Date()
  //   // date.setMilliseconds(0);
  //   let start = date.toISOString()
  //   let temp = date
  //   temp.setSeconds(temp.getSeconds()-1)
  //   let end = temp.toISOString()
  //   // console.log('string is',"http://192.168.0.105:8000/api/aircraftdata/?start-time=" + start + "&end-time="+end)
  //   try {
  //     this.myInterval = setInterval(async () => {
  //       let date = new Date()
  //       // date.setMilliseconds(0);
  //       let start = date.toISOString()
  //       let temp = date
  //       temp.setSeconds(temp.getSeconds()-1)
  //       let end = temp.toISOString()
  //       console.log('start',start)
  //       console.log('end', end)
  //       console.log("http://127.0.0.1:8000/api/aircraftdata/?start-time=" + start + "&end-time=" + end)
  //       start = '2020-12-09T20:15:25Z'
  //       end = '2020-12-09T20:15:25Z'
  //       console.log("http://127.0.0.1:8000/api/aircraftdata/?start-time=" + start + "&end-time=" + end)
  //       // const res = await fetch("http://192.168.0.105:8000/api/aircraftdata/?start-time=" + start + "&end-time="+end)
  //       // console.log('string is',"http://192.168.0.105:8000/api/aircraftdata/?start-time=" + start + "&end-time="+end)
  //       const res = await fetch("http://127.0.0.1:8000/api/aircraftdata/?start-time=" + start + "&end-time=" + end)
  //       // const res = await fetch("http://192.168.0.105:8000/api/aircraftdata/")
  //       console.log('res')
  //       // const res = await fetch("http://192.168.0.1:8000/api/aircraftdata/")
  //       let data = await res.json();
  //       // const filteredData = this.state.result.filter(data => new Date(data.timestamp) >= new Date("09/30/2019") && new Date(data.timestamp) <= new Date("10/07/2019"))
  //       // const filteredData =  data.filter(d => new Date().toISOString() <= d.start-time)
  //       let data2 = data.filter(d => d.datarecord_set.length > 0)
  //       console.log('adding',data)
  //       console.log('DATA2', data2)
  //       // console.log('example',data[0].datarecord_set[0].timestamp)
  //       console.log('time', new Date())
  //       let newdata = data2
  //       console.log('testing',data2[0].datarecord_set[0].latitude)
  //       // let mapdata = data2.filter(d => d.datarecord_set[0].altitude > 0)
  //       let mapdata = data2.filter(function(result) {
  //         return result.datarecord_set[0].latitude > 0
  //       })
  //       let markerslat = mapdata.map(d => (d.datarecord_set[0].latitude))
  //       let markerslon = mapdata.map(d => (d.datarecord_set[0].longitude))
  //       let markersicao = mapdata.map(d => (d.icao))
  //       // let markers = mapdata.map(({ datarecord_set[0], datarecord_set[0] }) => ({ a, b }))
  //       console.log('filtered mapdata',mapdata)
  //       console.log('markerslat', markerslat)
  //       console.log('markerslon', markerslon)
  //       let marker = []
  //       for(var i=0;i<markerslat.length;i++) {
  //         marker.push({icao: markersicao[i], lat: markerslat[i], lon: markerslon[i]})
  //       }
  //       console.log('marker', marker)
  //       // console.log('markers', markers)
  //       // if(data.length > 6) {
  //       //   newdata = data.slice(-6)
  //       // } else {
  //       //   newdata = data
  //       // }
  //       // console.log('new data is',newdata)
  //       console.log('mapdata',mapdata)
  //       this.setState({
  //         data: newdata,
  //         mapdata: mapdata,
  //         markers: marker
  //       })
  //     }, 10000);
  //   } catch(e) {
  //     console.log('error', e);
  //   }
  // }
  //
  // componentWillUnmount() {
  //   clearInterval(this.myInterval)
  // }
=======
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
        
        const res = await fetch("http://127.0.0.1:8000/api/aircraftdata/")
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
>>>>>>> 2b34f7b361fea391905f3e3581381c7cbcdd957b

  render() {
    return (
      <Container fluid style={{ overflowY: 'auto', height: '41.5em', padding: '0', margin: '0', }}>
        <div>Aircraft Data</div>
        <br/>
          <div >
            {this.props.data && this.props.data.map(d => {
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
