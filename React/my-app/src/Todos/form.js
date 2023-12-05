import { useState,useEffect } from "react"
import Call from "./input";
import axios from 'axios';

const Form=()=>{
    let [array_item,new_item]=useState([])
    function add(){
      axios({
        method: 'get',
        url: 'https://jsonplaceholder.typicode.com/posts',
      }).then(function(response){
        console.log(response)
      });
    }
    useEffect(()=>{add()},[])
    return(<>
    <h2>Name List</h2>
      <table className='table table-primary' border={1}>
        <tr>
          <td>No</td>
          <td>Items</td>
        </tr>
        {
          array_item.map((t,i)=>(
            <tr>
              <td>{i+1}</td>
              <td>{t}</td>
            </tr>
          ))
        }
      </table>
      <Call vari={array_item} vari_fun={new_item} />
      {/* <button type="button" onClick={add}>add</button> */}
</>
    )}

    export default Form