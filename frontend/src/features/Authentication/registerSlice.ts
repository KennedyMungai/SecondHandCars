import { IRegisterUser } from "@/utils/auth_utils";
import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import axios from "axios";

const initialState: IRegisterUser = {
  email: "",
  password: "",
  is_loaded: false,
};

export const createUser = createAsyncThunk(
  "authenticate/register",
  async () => {
    const response = await axios.post(
      "http://localhost:8000/auth/register",
      initialState
    );

    return response.data;
  }
);

const registerSlice = createSlice({
  name: "registerUser",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(createUser.pending, (state) => {
        state.is_loaded = false;
      })
      .addCase(createUser.fulfilled, (state, action) => {
        state.is_loaded = true;
        state.email = action.payload.email;
        state.password = action.payload.password;
      })
      .addCase(createUser.rejected, (state) => {
        state.is_loaded = false;
        state.email = "";
        state.password = "";
      });
  },
});

// export const { createUser } = registerSlice.actions;

export default registerSlice.reducer;
