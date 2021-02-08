import logo from './logo.svg';
import './App.css';
import NavBar from './navbar/Navbar';
import MapContainer from './map/Map.js';
import AircraftData from './aircraft_data/AircraftData.js';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import React, { Component } from 'react';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      mapdata: [],
      markers: [],
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
        console.log('start',start)
        console.log('end', end)
        console.log("http://127.0.0.1:8000/api/aircraftdata/?start-time=" + start + "&end-time=" + end)
        // start = '2020-12-09T20:15:25Z'
        // end = '2020-12-09T20:15:25Z'
        console.log("http://127.0.0.1:8000/api/aircraftdata/?start-time=" + start + "&end-time=" + end)
        // const res = await fetch("http://192.168.0.105:8000/api/aircraftdata/?start-time=" + start + "&end-time="+end)
        // console.log('string is',"http://192.168.0.105:8000/api/aircraftdata/?start-time=" + start + "&end-time="+end)
        const res = await fetch("http://127.0.0.1:8000/api/aircraftdata/?start-time=" + start + "&end-time=" + end)
        // const res = await fetch("http://192.168.0.105:8000/api/aircraftdata/")
        console.log('res')
        // const res = await fetch("http://192.168.0.1:8000/api/aircraftdata/")
        let data = await res.json();
        // const filteredData = this.state.result.filter(data => new Date(data.timestamp) >= new Date("09/30/2019") && new Date(data.timestamp) <= new Date("10/07/2019"))
        // const filteredData =  data.filter(d => new Date().toISOString() <= d.start-time)
        let data2 = data.filter(d => d.datarecord_set.length > 0)
        console.log('adding',data)
        console.log('DATA2', data2)
        // console.log('example',data[0].datarecord_set[0].timestamp)
        console.log('time', new Date())
        let newdata = data2
        console.log('testing',data2[0].datarecord_set[0].latitude)
        // let mapdata = data2.filter(d => d.datarecord_set[0].altitude > 0)
        let mapdata = data2.filter(function(result) {
          return result.datarecord_set[0].latitude > 0
        })
        let markerslat = mapdata.map(d => (d.datarecord_set[0].latitude))
        let markerslon = mapdata.map(d => (d.datarecord_set[0].longitude))
        let markersicao = mapdata.map(d => (d.icao))
        console.log('filtered mapdata',mapdata)
        console.log('markerslat', markerslat)
        console.log('markerslon', markerslon)
        let marker = []
        for(var i=0;i<markerslat.length;i++) {
          marker.push({icao: markersicao[i], lat: markerslat[i], lon: markerslon[i]})
        }
        // console.log('marker', marker)

        console.log('mapdata',mapdata)
        this.setState({
          data: newdata,
          mapdata: mapdata,
          markers: marker
        })
      }, 10000);
    } catch(e) {
      console.log('error', e);
    }
  }

  componentWillUnmount() {
    clearInterval(this.myInterval)
  }
  render() {
    return (
      <div className="App">
      <Container fluid style={{ padding: '0' }}>
        <NavBar/>
        <Row fluid md={12} style={{ flexWrap: 'inherit', marginRight: '0' }}>
          <Col fluid xs={12} md={8}>
            <MapContainer data={this.state.data} mapdata={this.state.mapdata} markers={this.state.markers}/>
          </Col>
          <Col xs={6} md={4}>
            <AircraftData data={this.state.data} mapdata={this.state.mapdata} markers={this.state.markers}/>
          </Col>
        </Row>
        </Container>
      </div>
    );
  }
}

export default App;
