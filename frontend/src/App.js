import logo from './logo.svg';
import './App.css';
import NavBar from './navbar/Navbar';
import MapContainer from './map/Map.js';
import Data from './aircraft_data/Data.js';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';

function App() {
  return (
    <div className="App">
      <NavBar/>
      <MapContainer/>
    </div>
  );
}

export default App;
