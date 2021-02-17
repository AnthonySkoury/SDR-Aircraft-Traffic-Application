import React from 'react';
import './Marker.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCoffee } from '@fortawesome/free-solid-svg-icons'

class Marker extends React.Component {
  constructor(props) {
    super(props);
    this.state = {

    };
  }

  // handleshowAircraft(e) {
  //   this.props.showAircraft(e.target.value)
  // }

    render() {
      return (
        <div className="marker"
          style={{ backgroundColor: this.props.color, cursor: 'pointer'}}
          title={this.props.name}
          onClick={() => this.props.handleshowAircraft(this.props.name)}
        />

      );
    }
}

export default Marker;

// const Marker = (props: any) => {
//     const { color, name, id } = props;
//     return (
//       <div className="marker"
//         style={{ backgroundColor: color, cursor: 'pointer'}}
//         title={name}
//       />
//
//     );
//   };
//
//   export default Marker;



  // <div className="marker">
  //   <FontAwesomeIcon icon={['fab', 'apple']} style={{ backgroundColor: color, cursor: 'pointer'}}/>
  // </div>
