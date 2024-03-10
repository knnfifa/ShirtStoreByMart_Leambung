
import React from "react";
import './Arsenal.css';
import LogoManU from './Pictu/Arsenal.png'; 

class Arsenal extends React.Component {
    render() {
        return (
            <div className="ManU-info">
                <center>
                    <div className="Logo-Arsenal-info">
                        <img src={LogoManU} alt="โลโก้ Arsenal" className="Logo-Arsenal" />
                    </div>
                </center>
                <center><h1 style={{ color: 'white' }}>Arsenal FC</h1></center>
                <center><h2 style={{ color: 'white' }}>4 Product</h2></center>
            </div>
        );
    }
}

export default Arsenal;
