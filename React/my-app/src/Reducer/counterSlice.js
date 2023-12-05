import {createSlice} from '@reduxjs/toolkit'

export const Counterslice=createSlice({
    name:"counter",
    initialState:{
        value:{},
    },
    reducers:{
        changename:(state,actions)=>{state.value=actions.payload},
        logout:(state)=>{state.value={}}
    }
})

export const {changename,logout}=Counterslice.actions
export default Counterslice.reducer