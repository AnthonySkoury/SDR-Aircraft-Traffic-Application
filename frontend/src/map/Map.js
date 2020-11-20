import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Container from 'react-bootstrap/Container'

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

  render() {
    return (
      // always set container height explicitly
      <div style={{ height: '92vh', width: '100%' }}>
          <GoogleMapReact
            bootstrapURLKeys={{ key: '' }}
            defaultCenter={this.state.center}
            defaultZoom={this.state.zoom}
          >
          <AnyReactComponent
            lat={59.955413}
            lng={30.337844}
            text="My Marker"
          />
          </GoogleMapReact>
        </div>
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
