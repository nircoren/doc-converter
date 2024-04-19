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
      state.docConvertionRows.push(createDocConvertionRow(0, action.payload.row));
      console.log(state.docConvertionRows)
    },
    setDocContent(state,action) {
      console.log('action',action)
      const {rowIndex, inputIndex, doc} = action.payload
      state.docConvertionRows[rowIndex].docs[inputIndex].content = doc
      console.log('doc', state.docConvertionRows[rowIndex].docs[inputIndex].content)
    }
  }
});

export const { addDocConvertionRow, setDocContent } = docSlice.actions;

export default docSlice.reducer;
