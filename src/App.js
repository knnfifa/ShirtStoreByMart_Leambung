import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Nav from "./component/Nav";
import Homepage from "./component/Homepage/Home";
import LoginPage from "./component/Loginpage/Login";
import ManUpage from "./component/ManUpage/Man_U"


function App() {
  return (
    <div>
      <Nav />

      <BrowserRouter>
        <Switch>
            <Route exact path='/'>
                  <Homepage />
            </Route>
          
            <Route path='/login'>
                  <LoginPage />
            </Route>

            <Route exact path='/Man_United'>
                  <ManUpage />
            </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
}
// vjeohv
export default App;
