
import React from "react";
import './Liver.css';
import LogoManU from './Pict/Liverpool.png'; 

class Liver extends React.Component {
    render() {
        return (
            <div className="Liver-info">
                <center>
                    <div className="Logo-Liver-info">
                        <img src={LogoManU} alt="โลโก้ Liverpool" className="Logo-Liver" />
                    </div>
                </center>
                <center><h1 style={{ color: 'white' }}>Liverpool FC</h1></center>
                <center><h2 style={{ color: 'white' }}>4 Product</h2></center>
            </div>
        );
    }
}

export default Liver;
