import { useState,useEffect } from "react"
import {Button} from "react-bootstrap"
function User(){
    let [Time,setTime]=useState(0)
    let [startStop,setTimer]=useState(true)
    useEffect(()=>{
        if(startStop){
            setTime(Time+1)
        }
        
    },[startStop,Time])
    return(<>
        <span><b>{Time}</b></span><br></br>
        <Button type="button" onClick={()=>setTimer(!startStop)}>{startStop?"STOP":"START"}</Button>{"          "}
        <Button type="button" onClick={async()=>{await setTimer(false);setTime(0)}}>RESET</Button>
        </>
)}


export default User