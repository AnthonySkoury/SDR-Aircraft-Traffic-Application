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
  }

  componentDidUpdate() {
    console.log('markers',this.props.markers)
    console.log(this.props.markers[0].lon)
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
                />
            );
          })}
        </GoogleMapReact>
      </div>
      // always set container height explicitly
      // <div style={{ height: '92vh', width: '100%' }}>
      //     <GoogleMapReact
      //       bootstrapURLKeys={{ key: 'AIzaSyDeWQdLlMHZPAdXkUp1Gv72orwkEu6mKOY' }}
      //       defaultCenter={this.state.center}
      //       defaultZoom={this.state.zoom}
      //     >
      //       <AnyReactComponent
      //         lat={33.955413}
      //         lng={-117.337844}
      //         text="My Marker"
      //       />
      //     </GoogleMapReact>
      //   </div>
    );
  }
}

export default MapContainer


// <div style={{ height: '100vh !important', width: '100%'}}>
//   <Container>
//     <Map
//       google={this.props.google}
//       zoom={8}
//       style={mapStyles}
//       initialCenter={{ lat: 33.68, lng: -117.82}}
//     />
//   </Container>
// </div>
