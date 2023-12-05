import { useState } from "react"
import { Link } from "react-router-dom"

const Loginpage=(props)=>{
    let [alldata,setalldata]=useState({
        email:"abinesh@gmail.com",
        password:12345,
    })
    const checklogin=()=>{   
            if(alldata.email==response.data.email && alldata.password==response.data.password){
              props.setIslogged({status:true,email:alldata.email})
              navigate('/home')       
            }
    }
    
    return(<>
        <h2>Login Page</h2>
        <h4>Email</h4>
        <input type="text" onKeyUp={(e)=>setalldata({...alldata,email:e.target.value})}></input>
        {/* {JSON.stringify(alldata.email)} */}
        <h4>Password</h4>
        <input type="text" onKeyUp={(e)=>setalldata({...alldata,password:e.target.value})}></input>
        {/* {JSON.stringify(alldata.password)} */}
        <br></br>
        <button type="button" onClick={checklogin}>done</button>
        
        <nav>
          <ul>
            <li>
              <Link to={`/form`}>form</Link>
            </li>
            <li>
              <Link to={`/todo`}>todo</Link>
            </li>
          </ul>
        </nav>
        </>
       
    )
}
export default Loginpage