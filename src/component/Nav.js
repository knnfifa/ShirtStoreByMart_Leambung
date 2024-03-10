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
             {/* --------------logo -----------*/}
                <div className="NameText">
                    <h2>SHIRTSTORE BY MART LAEMBANG.COM</h2>
                </div>
                {/* --------------shirtstore -----------*/}
                <div>
                  <a href="/Login" className='nav-item'>
                    <button className="btnLogin-popup">Login</button>
                  </a>
                </div>
                 {/* --------------login -----------*/}
      
            </ul>
        </div>
    );
}

export default Nav;
