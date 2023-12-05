import { useState } from "react"
import { useNavigate } from "react-router-dom";
import Call from "./input";

const Todo=(props)=>{
    let [array_item,new_item]=useState([])
    if(checkuser=="abinesh@gmail.com"){
      alert("Authenticate user")
    }else{
      alert("hacker")
    }
      

    return(<>
      <h2>Product List</h2>
      <table className='table table-primary' border={1}>
        <tr>
          <td>No</td>
          <td>Items</td>
        </tr>{
          array_item.map((t,i)=>(
            <tr>
              <td>{i+1}</td>
              <td>{t}</td>
            </tr>
          ))
        }
      </table>
        <Call vari={array_item} vari_fun={new_item} />
        {props.islogged?`welcome to ${props.islogged.email}`:"failed"}
      </>
    )
  }


  export default Todo;