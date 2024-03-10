import React from 'react';
import './Nav.css';
function Nav() {
    return (
        <div>
            <ul className="navbar">
                <div>
                    <a href="/" className="logo"> 
                        <div className="item-logo"></div>
                        <h3>SHIRTSTORE</h3>
                    </a>
                </div>
                <div className="NameText">
                    <h2>SHIRTSTORE BY MATH LAEMBANG.COM</h2>
                </div>
                <div>
                <a href="/Login" className='nav-item'>
                    <button className="btnLogin-popup">Login</button>
                </a>

                </div>
            </ul>
        </div>
    );
}
// vrjlvnj
export default Nav;
