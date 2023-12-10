import { useState } from "react"
import { useNavigate } from "react-router-dom";
import axios from "axios"

export default function RegisterPage(){
    let navigate=useNavigate()
    let [newdata,setnewdata]=useState({
        username:"",
        email:"",
        password:""
    })
    function postData(){
    axios({
        method:"POST",
        url:"https://agaram.academy/api/action.php",
        Data:{request:"create_candidate",
                newdata}
      }).then(function(response){
        console.log(response)
        navigate("/")
      })}
      return(<>
        <h1>Register Page</h1>
        <h3><b>Username</b></h3>
        <input type="text" onKeyUp={(e)=>setnewdata({...newdata,username:e.target.value})}></input>
        <h3><b>Email</b></h3>
        <input type="text" onKeyUp={(e)=>setnewdata({...newdata,email:e.target.value})}></input>
        <h3><b>Password</b></h3>
        <input type="text" onKeyUp={(e)=>setnewdata({...newdata,password:e.target.value})}></input><br/>
        <button onClick={postData}>Register</button>
        </>
      )
}