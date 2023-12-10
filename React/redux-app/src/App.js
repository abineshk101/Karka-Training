import * as React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import LoginPage from './manage_users/pages/Login';
import RegisterPage from './manage_users/pages/Register';
import HomePage from './manage_users/pages/home';
import { Provider } from 'react-redux';
import store from './manage_users/redux/store';
import Userdetail from "./manage_users/pages/userdata";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

const router = createBrowserRouter([
  {
    path:"/",
    element:<LoginPage/>
  },
  {
    path:"/register",
    element:<RegisterPage/>
  },
  {
    path:"/home",
    element:<HomePage/>
  },
  {
    path:"/userdata/:userID",
    element:<Userdetail/>,
  }
]);
function App() {
  return (
    <Provider store={store}>
    <RouterProvider router={router} />
    </Provider>
  );
}

export default App;
