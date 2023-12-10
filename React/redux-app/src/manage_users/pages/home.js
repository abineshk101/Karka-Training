import { useState,useEffect } from "react"
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { useSelector,useDispatch } from "react-redux";
import { updatedata } from "../redux/counterSlice";
import UserList from "../common component/userlist";

export default function HomePage(){
    axios({
        method:"GET",
        url:"https://agaram.academy/api/action.php?request=getAllMembers",
      }).then(function(response){
        console.log(response)
      })

    return(<>
    <h1>Welcome to Homepage</h1>
        <UserList isDeleteVisible={true} />
        </>
    )}
            