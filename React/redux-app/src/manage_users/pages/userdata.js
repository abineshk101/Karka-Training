import { resolvePath, useParams } from "react-router"
import { useEffect } from "react"
import axios from "axios"
import { useDispatch } from "react-redux"
import { showtable } from "../redux/counterSlice"
import { useSelector } from "react-redux"
import UserList from "../common component/userlist"

export default function Userdetail(){
    let singleuser=useSelector((state)=>state.userdata.singleuser)
    let dispatch=useDispatch()
    let {userID}=useParams()
  
    useEffect(()=>{
        axios.get(`https://agaram.academy/api/action.php?request=getMemberDetail&id=${userID}`).then(function(response){
            dispatch(showtable(response.data.data))
        })
    },[])
    return(<>
        <h1>Username  <b>{singleuser.name}</b></h1>
        {/* <table>
            <thead>
                <tr>
                    <th>id</th>
                    <th>name</th>
                    <th>email</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{singleuser.id}</td>
                    <td>{singleuser.name}</td>
                    <td>{singleuser.email}</td>
                    <td>{singleuser.aadhar}</td>
                </tr>
            </tbody>
        </table> */}
        <UserList/>
        </>
    )
}