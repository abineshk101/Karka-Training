import { configureStore } from '@reduxjs/toolkit'
import userdataReducer from './counterSlice'

const store=configureStore({
  reducer: {userdata:userdataReducer},
})

export default store;