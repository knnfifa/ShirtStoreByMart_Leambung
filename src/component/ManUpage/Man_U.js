
import React from "react";
import './Man_U.css';
import LogoManU from './Picture/LogoManU.png'; 

class Man_U extends React.Component {
    render() {
        return (
            <div className="ManU-info">
                <center>
                    <div className="Logo-Man_U-info">
                        <img src={LogoManU} alt="โลโก้ Manchester United" className="Logo-Man_U" />
                    </div>
                </center>
                <center><h1 style={{ color: 'white' }}>Manchester United</h1></center>
                <center><h2 style={{ color: 'white' }}>4 Product</h2></center>
            </div>
        );
    }
}

export default Man_U;
