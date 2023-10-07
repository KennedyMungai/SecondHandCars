import { ILoginUser } from "@/utils/auth_utils";
import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import axios from "axios";

const initialState: ILoginUser = {
  username: "",
  password: "",
  is_loaded: false,
};

export const loginUser = createAsyncThunk("authenticate/login", async () => {
  const response = await axios.get("/api/login");
  return response.data;
});

const loginSlice = createSlice({
  name: "loginUser",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(loginUser.pending, (state) => {
        state.is_loaded = false;
      })
      .addCase(loginUser.fulfilled, (state, action) => {
        state.is_loaded = true;
        state.username = action.payload.email;
        state.password = action.payload.password;
      })
      .addCase(loginUser.rejected, (state) => {
        state.is_loaded = false;
        state.username = "";
        state.password = "";
      });
  },
});

// export const {loginUser} = loginSlice.actions

export default loginSlice.reducer;
