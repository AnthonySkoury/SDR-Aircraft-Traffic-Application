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
      placeholder: "Loading",
      dict: {},
      shown: null,
      shownData: []
    };
    this.showAircraft = this.showAircraft.bind(this)
  }

  // showAircraft = (icao) => {
  //   this.setState({
  //     shown: icao
  //   });
  //   console.log("showing", icao)
  // }

  showAircraft(icao) {
    console.log("showing", icao)
    this.setState({
      shown: icao
    },
      () => {
        this.updateShown(this.state.icao)
      }
    );

  }

  // this.setState({
  //     preview: {
  //       img,
  //       scale: this.state.scale,
  //     }
  //   }, () => {
  //     this.props.croppedImage(this.state.preview.img);
  //   })


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
        let end = date.toISOString()
        let temp = date
        temp.setSeconds(temp.getSeconds()-20)
        let start = temp.toISOString()
        console.log('start',start)
        console.log('end', end)
        console.log("http://127.0.0.1:8000/api/aircraftdata/")
        // start = '2020-12-09T20:15:25Z'
        // end = '2020-12-09T20:15:25Z'
        console.log("http://127.0.0.1:8000/api/aircraftdata/?start-time=" + start + "&end-time=" + end)
        // const res = await fetch("http://192.168.0.105:8000/api/aircraftdata/?start-time=" + start + "&end-time="+end)
        // console.log('string is',"http://192.168.0.105:8000/api/aircraftdata/?start-time=" + start + "&end-time="+end)
        const res = await fetch("http://127.0.0.1:8000/api/aircraftdata/?start-time=" + start + "&end-time=" + end)
        // const res = await fetch("http://192.168.0.105:8000/api/aircraftdata/")
        // const res = await fetch("http://192.168.0.105:8000/api/aircraftdata")
        // console.log(res)
        // const res = await fetch("http://192.168.0.1:8000/api/aircraftdata/")
        let data = await res.json();
        // const filteredData = this.state.result.filter(data => new Date(data.timestamp) >= new Date("09/30/2019") && new Date(data.timestamp) <= new Date("10/07/2019"))
        // const filteredData =  data.filter(d => new Date().toISOString() <= d.start-time)
        let data2 = data.filter(d => d.datarecord_set.length > 0)
        let datadict = data.filter(d => d.datarecord_set.length > 0)
        console.log('adding',data)
        console.log('DATA2', data2)
        // console.log('example',data[0].datarecord_set[0].timestamp)
        console.log('time', new Date())
        let newdata = data2
        // console.log('testing',data2[0].datarecord_set[0].latitude)
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

        // console.log(this.sate.shown)
        // if(this.state.shown !== null) {
        //   console.log('updating',this.state.shown)
        //   const aircraft = await fetch("http://127.0.0.1:8000/api/aircraftdata/?icao=" + this.state.shown)
        //   let aircraftData = await aircraft.json();
        //   console.log(aircraftData)
        // }

        this.setState({
          data: newdata,
          mapdata: mapdata,
          markers: marker,
          d: datadict,
          // shown: null
        })
      }, 6000);
    } catch(e) {
      console.log('error', e);
    }
  }

  componentWillUnmount() {
    clearInterval(this.myInterval)
  }

  async updateShown() {
    if(this.state.shown !== null) {
      console.log('updating',this.state.shown)
      const aircraft = await fetch("http://127.0.0.1:8000/api/aircraftdata/?icao=" + this.state.shown)
      // console.log(aircraft)
      let aircraftData = await aircraft.json();
      console.log('aircraft data',aircraftData)

      let aircraftData2 = aircraftData.filter(d => d.datarecord_set.length > 0)
      console.log('aircraft data2',aircraftData2)

      console.log('want',aircraftData2[0].datarecord_set[0])
      this.setState({
        shownData: aircraftData2[0].datarecord_set[0]
      })
      // await setTimeout(()=>{}, 2000);
    }
  }

  render() {
    return (
      <div className="App">
      <Container fluid style={{ padding: '0' }}>
        <NavBar/>
        <Row fluid md={12} style={{ flexWrap: 'inherit', marginRight: '0' }}>
          <Col fluid xs={12} md={8}>
            <MapContainer
              data={this.state.data}
              mapdata={this.state.mapdata}
              markers={this.state.markers}
              showAircraft={this.showAircraft}/>
          </Col>
          <Col xs={6} md={4}>
            <AircraftData
              data={this.state.data}
              mapdata={this.state.mapdata}
              markers={this.state.markers}
              // showAircraft={showAircraft = {(e) => this.showAircraft(e)}
              showAircraft = {(e) => this.showAircraft(e)}
              shown = {this.state.shown}
              shownData = {this.state.shownData}
            />
          </Col>
        </Row>
        </Container>
      </div>
    );
  }
}

export default App;
