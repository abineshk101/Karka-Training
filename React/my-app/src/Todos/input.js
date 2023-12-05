import { useState } from "react"
import Button from 'react-bootstrap/Button';

const Call=(props)=>{
    let [array_item,new_item]=useState([])

return (
    <>
    <input type='text' onKeyUp={(a)=>new_item(a.target.value)}></input>
    <Button as="a" variant='danger' onClick={()=>props.vari_fun([...props.vari,array_item])}>Add</Button>
    </>
    )
}

export default Call