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
                    <h2>SHIRTSTORE BY MATH LAEMBANG.COM</h2>
                </div>
                {/* --------------shirtstore -----------*/}
                <div>
                  <a href="/Login" className='nav-item'>
                    <button className="btnLogin-popup">Login</button>
                  </a>
                </div>
                 {/* --------------login -----------*/}
                <div>
                  <a href="/ManUpage" className='nav-item2'>
                    <button className="btnmanu-popup">ManUpage</button>
                  </a>
                 </div>
                {/* --------------ManU -----------*/}
                <div>
                  <a href="/Mancipage" className='nav-item3'>
                    <button className="btnmanu-popup">Mancipage</button>
                  </a>
                 </div>
                   {/* --------------Manci -----------*/}
                   <div>
                  <a href="/Liverpoolpage" className='nav-item4'>
                    <button className="btnmanu-popup">Liverpage</button>
                  </a>
                 </div>
                   {/* --------------Manci -----------*/}
                   <div>
                  <a href="/Arsenalpage" className='nav-item5'>
                    <button className="btnmanu-popup">Arsenalpage</button>
                  </a>
                 </div>
                   {/* --------------Manci -----------*/}
            </ul>
        </div>
    );
}

export default Nav;
