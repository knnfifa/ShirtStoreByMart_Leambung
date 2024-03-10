import React from 'react';
import './Login.css';

class LoginPage extends React.Component {
    // สร้างเมธอดสำหรับการเปิดโหมด Login
    login() {
        // ใส่โค้ดที่ต้องการให้เกิดขึ้นเมื่อกดปุ่ม Login
        console.log("Login clicked");

        // ถ้ามีการคลิก Login ให้กรอบ btn ย้อนกลับไปครอบปุ่ม Login
        document.getElementById('btn').style.left = '10px';

        // เลื่อนแบบฟอร์ม login กลับมาแสดง
        document.getElementById('login').style.left = '50px';
        document.getElementById('register').style.left = '600px';
        document.getElementById('register').style.top = '0';
    }

    // สร้างเมธอดสำหรับการเปิดโหมด Register
    register() {
        // ใส่โค้ดที่ต้องการให้เกิดขึ้นเมื่อกดปุ่ม Register
        console.log("Register clicked");

        // เลื่อนกรอบ btn ไปครอบกรอบ register
        document.getElementById('btn').style.left = '215px';

        // เลื่อนแบบฟอร์ม register ขึ้นมา
        document.getElementById('login').style.left = '-500px';
        document.getElementById('register').style.left = '50px';
        document.getElementById('register').style.top = '-150px';
    }

    render() {
        return (
            <div className="form-box">
                <div className="button-box">
                    <div id="btn"></div>
                    {/* เรียกใช้เมธอด login เมื่อคลิกที่ปุ่ม Login */}
                    <button type="button" className="toggle-btn" onClick={this.login}>Login</button>
                    {/* เรียกใช้เมธอด register เมื่อคลิกที่ปุ่ม Register */}
                    <button type="button" className="toggle-btn" onClick={this.register}>Register</button>
                </div>

                <form id="login" className="input-group">
                    <h5 className="text-email" >Email Address</h5>
                    <h5 className="text-password" >Password</h5>
                    <input type="text" className="input-field" placeholder="Email Address" />
                    <input type="password" className="input-field" placeholder="Password" />
                    <button type="submit" className="submit-btn">Login</button>
                </form>

                <form id="register" className="input-group">
                    <h5 className="text-email" >Email Address</h5>
                    <h5 className="text-password" >Password</h5>
                    <input type="text" className="input-field" placeholder="Email Address" />
                    <input type="password" className="input-field" placeholder="Password" />
                    <button type="submit" className="submit-btn">Register</button>
                </form>
            </div>
        );
    }
}
// dvojduhh
export default LoginPage;
