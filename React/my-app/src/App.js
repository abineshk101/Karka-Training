import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
// import Todo from './Todos/todo';
// import Form from './Todos/form';
// import Loginpage from './loginpage';
import { useState,useEffect } from 'react';
// import Store from './store';
import { Provider } from 'react-redux';
import ReduxHome from './Reducer/redux_Home';
import ReduxLogin from './Reducer/redux_Login';
import reduxStore from './Reducer/redux_store';

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

function App() {
    let [Islogged,setIslogged]=useState({status:false,email:""})
    const router = createBrowserRouter([
//       {
// path: "/todos",
//         element:<Todo islogged={Islogged} setIslogged={setIslogged}/>,
//       },
      
      // {
      //   path: "/form",
      //   element:<Form />,
      // },
      // {
      //   path: "/",
      //   element:<Loginpage islogged={Islogged} setIslogged={setIslogged} />,
      // }
      { 
        path:"/home",
        element:<ReduxHome />
      },
      {
        path:"/login",
        element:<ReduxLogin />,
      },
    ]);
    
    return (<>
    <Provider store={reduxStore}>
    <RouterProvider router={router} />

    {/* <Locate/> */}
    {/* <Welcome /> */}
      {/* <Todo />
      <Form /> */}
      </Provider>
      </>
    )}

    export default App;
    


