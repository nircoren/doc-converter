import { createSlice } from '@reduxjs/toolkit';
import createDocConvertionRow from '../../factory'

export const docSlice = createSlice({
  name: 'doc',
  initialState: {
    docConvertionRows: [
      createDocConvertionRow(0, [
        { fileName: 'rishum', fileType: 'microsoft_word' },
        { fileName: 'pinkas', fileType: 'microsoft_word' },
      ])
    ],
  },
  reducers: {
    addDocConvertionRow(state, action) {
      console.log('was')
      state.docConvertionRows.push(createDocConvertionRow(0, action.payload.files));
    }
  }
});

export const { addDocConvertionRow } = docSlice.actions;

export default docSlice.reducer;
