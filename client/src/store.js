import { configureStore } from '@reduxjs/toolkit';
import docReducer from './features/doc/docSlice';

const store = configureStore({
  reducer: {
    doc: docReducer
  }
});

export default store;
