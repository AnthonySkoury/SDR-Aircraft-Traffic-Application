import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Container from 'react-bootstrap/Container'

import Marker from './Marker';

const mapStyles = {
  width: '100%',
  height: '100%'
};

const AnyReactComponent = ({ text }) => <div>{text}</div>;


class MapContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      center: {
        lat: 33.68,
        lng: -117.82
      },
      zoom: 11
    };
    this.handleshowAircraft = this.handleshowAircraft.bind(this);
  }

  handleshowAircraft(e) {
    console.log('e is',e)
    this.props.showAircraft(e)
  }

  componentDidUpdate() {
    // console.log('markers',(this.props.markers !== null) && this.props.markers)
    // console.log(this.props.markers !== null && this.props.markers[0].lon)
  }

  render() {
    return (
      <div style={{ height: '94vh', width: '100%' }}>
        <GoogleMapReact
          bootstrapURLKeys={{ key: '' }}
          defaultCenter={this.state.center}
          defaultZoom={this.state.zoom}
        >
          {this.props.markers && this.props.markers.map(d => {
            return (
                <Marker key={d.icao}
                    lat = {d.lat}
                    lng={d.lon}
                    name={d.icao}
                    color = "blue"
                    handleshowAircraft = {(e) => this.handleshowAircraft(e)}
                    onClick={() => this.props.showAircraft('name')}
                    // showAircraft = {this.props.showAircraft}
                />
            );
          })}
        </GoogleMapReact>
      </div>
    );
  }
}

export default MapContainer
