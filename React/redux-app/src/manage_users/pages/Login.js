import { useState } from "react"
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useSelector,useDispatch } from "react-redux"
import { givedata } from "../redux/counterSlice";
import { showtable } from "../redux/counterSlice";

const LoginPage=()=>{
    const navigate = useNavigate();
    let user=useSelector((state)=>state.userdata.logindata)
    let getId=useSelector((state)=>state.userdata.navigateID)
    let dispatch=useDispatch();
    let [alldata,setalldata]=useState({
        email:"pavi@gmail.com",
        password:"123",
    })
    const checklogin=()=>{   
     if(localStorage.getItem("guest_user")){
        localStorage.removeItem("guest_user")
        navigate(`/userdata/${getId}`)
     }else{
          axios({
            method:"Post",
            url:`https://agaram.academy/api/action.php?request=candidate_login&email=${alldata.email}&password=${alldata.password}`,
          }).then(function(response){
            if(response.data.status=='success'){
                localStorage.setItem("After_login",true)
                dispatch(givedata(alldata))
                navigate("/home")
            }else{
                alert("incorrect data")
            }
          })
        }
    }
    
    return(<>
        <h2>Login Page</h2>
        <h4>Email</h4>
        <input type="text"  onKeyUp={(e)=>setalldata({...alldata,email:e.target.value})}></input>
        <h4>Password</h4>
        <input type="text"  onKeyUp={(e)=>setalldata({...alldata,password:e.target.value})}></input>
        <br></br>
        <button type="button" onClick={checklogin}>done</button>
        {/* <button type="button" onClick={ axios.get("http://agaram.academy/api/action.php?request=getAllMembers").then(function(response){
                console.log(response.data.data)
            })}>show</button> */}
        </>
       
    )
}
export default LoginPage;