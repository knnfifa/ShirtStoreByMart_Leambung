
import React from "react";
import './Manci.css';
import LogoManci from './Pic/Mancity.png'; 

class Manci extends React.Component {
    render() {
        return (
            <div className="Manci-info">
                <center>
                    <div className="Logo-Manci-info">
                        <img src={LogoManci} alt="โลโก้ Manchester city" className="Logo-Manci" />
                    </div>
                </center>
                <center><h1 style={{ color: 'white' }}>Manchester City FC</h1></center>
                <center><h2 style={{ color: 'white' }}>4 Product</h2></center>
            </div>
        );
    }
}

export default Manci;
