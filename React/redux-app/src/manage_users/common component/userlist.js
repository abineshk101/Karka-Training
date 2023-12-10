import { useEffect } from "react"
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import Table from 'react-bootstrap/Table';
import { useSelector,useDispatch } from "react-redux";
import { updatedata,setId } from "../redux/counterSlice";

export default function UserList(props){
    let navigate=useNavigate()
    let dispatch=useDispatch()
    let getdata=useSelector((state)=>state.userdata.alldata)

    useEffect(()=>{
        Checklogin();
    },[])    

    function Checklogin(){
        // if(localStorage.getItem("After_login")){
        //     axios.get("http://agaram.academy/api/action.php?request=getAllMembers").then(function(response){
        //         dispatch(updatedata(response.data.data))
        //     })
        // }
        axios.get("http://agaram.academy/api/action.php?request=getAllMembers").then(function(response){
                    dispatch(updatedata(response.data.data))
                })
    }
    function del(id){
        axios.get(`https://agaram.academy/api/action.php?request=removeMember&id=${id}`);
        Checklogin()
    }

    function sendId(id){
        dispatch(setId(id))
localStorage.setItem("guest_user",true)
navigate("/")
    }
    

    return(<>
        <Table striped bordered hover variant="dark">
            <thead>
                <tr>
                <th>id</th>
                <th>name</th>
                <th>email</th>
                <th>aadhar</th>
                <th>address</th>
                <th>View</th>
                {localStorage.getItem("After_login")?<th>{props.isDeleteVisible==true?<td>delete</td>:null}</th>:null}
                </tr>
            </thead>
            <tbody>
                {getdata.map((data)=>{
                    return(
                        <tr>
                            <td>{data.id}</td>
                            <td>{data.name}</td>
                            <td>{data.email}</td>
                            <td>{data.aadhar}</td>
                            <td>{data.address}</td>
                            <td>{localStorage.getItem("After_login")?<Link  to={`/userdata/${data.id}`}>view</Link>:<Link onClick={()=>sendId(data.id)} >view</Link>}</td>
                           {localStorage.getItem("After_login")?<td>{props.isDeleteVisible==true?<button onClick={()=>del(data.id)}>delete</button>:null}</td>:null}
                        </tr>
                    )
                })}
            </tbody>
        </Table>
        {localStorage.getItem("After_login") ?<button type="button" onClick={()=>{localStorage.removeItem("After_login");navigate("/")}}>logout</button>:null}
        </>
    )}
            