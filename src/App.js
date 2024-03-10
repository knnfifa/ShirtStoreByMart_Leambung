import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Nav from "./component/Nav";
import Homepage from "./component/Homepage/Home";
import LoginPage from "./component/Loginpage/Login";
import ManUpage from "./component/ManUpage/Man_U";
import Mancipage from "./component/Mancipage/Manci";
import Liverpoolpage from "./component/Liverpoolpage/Liver";
import Arsenalpage from "./component/Arsenalpage/Arsenal";


function App() {
  return (
    <BrowserRouter>
      <div>
        <Nav />

        <Switch>
          <Route exact path="/">
            <Homepage />
          </Route>

          <Route path="/login">
            <LoginPage />
          </Route>

          <Route exact path="/ManUpage">
            <ManUpage />
          </Route>

          <Route exact path="/Mancipage">
            <Mancipage />
          </Route>

          <Route exact path="/Liverpoolpage">
            <Liverpoolpage />
          </Route>

          <Route exact path="/Arsenalpage">
            <Arsenalpage />
          </Route>

        </Switch>
      </div>
    </BrowserRouter>
  );
}

export default App;
