import React from 'react';
import './Home.css'; // เชื่อมต่อไฟล์ CSS
import Footer from '../Footer';
class Homepage extends React.Component {
    render() {
        return (
            <>
                <div className="banner-info">
                    <div className="item"></div>
                    <div className="item"></div>
                    <div className="item"></div>
                    <div className="item"></div>
                    <div className="item"></div>
                </div>

                <Footer />
                 {/* ikrgpr */}
            </>
        );
    }
}

export default Homepage;