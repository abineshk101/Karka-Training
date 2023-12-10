import {createSlice} from '@reduxjs/toolkit'

export const Counterslice=createSlice({
    name:"userdata",
    initialState:{
        logindata:"",
        alldata:[],
        singleuser:{},
        navigateID:""
    },
    reducers:{
        givedata:(state,actions)=>{state.logindata=actions.payload},
        updatedata:(state,actions)=>{state.alldata=actions.payload},
        showtable:(state,actions)=>{state.singleuser=actions.payload},
        logout:(state)=>{state.logindata=""},
        setId:(state,actions)=>{state.navigateID=actions.payload}
    }
})

export const {givedata,logout,updatedata,showtable,setId}=Counterslice.actions
export default Counterslice.reducer