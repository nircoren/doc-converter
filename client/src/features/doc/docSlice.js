import { createSlice } from '@reduxjs/toolkit';

export const docSlice = createSlice({
  name: 'doc',
  initialState: {
    value: 0
  },
  reducers: {
    increment: (state) => {
      state.value += 1;
    },
    decrement: (state) => {
      state.value -= 1;
    },
    incrementByAmount: (state, action) => {
      state.value += action.payload;
    }
  }
});

export const { increment, decrement, incrementByAmount } = docSlice.actions;

export default docSlice.reducer;
