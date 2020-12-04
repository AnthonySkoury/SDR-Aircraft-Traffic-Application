import logo from './logo.svg';
import './App.css';
import NavBar from './navbar/Navbar';
import MapContainer from './map/Map.js';
import AircraftData from './aircraft_data/AircraftData.js';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';

function App() {
  return (
    <div className="App">
    <Container fluid style={{ padding: '0' }}>
      <NavBar/>
      <Row fluid md={12} style={{ flexWrap: 'inherit', marginRight: '0' }}>
        <Col fluid xs={12} md={8}>
          <MapContainer/>
        </Col>
        <Col xs={6} md={4}>
          <AircraftData/>
        </Col>
      </Row>
      </Container>
    </div>
  );
}

export default App;
