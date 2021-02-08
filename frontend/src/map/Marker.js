import React from 'react';
import './Marker.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCoffee } from '@fortawesome/free-solid-svg-icons'

const Marker = (props: any) => {
    const { color, name, id } = props;
    return (
      <div className="marker"
        style={{ backgroundColor: color, cursor: 'pointer'}}
        title={name}
      />

    );
  };

  export default Marker;



  // <div className="marker">
  //   <FontAwesomeIcon icon={['fab', 'apple']} style={{ backgroundColor: color, cursor: 'pointer'}}/>
  // </div>
