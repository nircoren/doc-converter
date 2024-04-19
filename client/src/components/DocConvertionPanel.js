import React from 'react'
import DocConvertionRow from './DocConvertionRow'
import { useSelector, useDispatch } from 'react-redux';
import { addDocConversionRow } from './features/doc/docSlice';

function DocConvertionPanel() {
  const docConvertionRows = useSelector(state => state.doc.docConvertionRows);
  const dispatch = useDispatch();
  const handleAddRow = () => {
    const newFiles = [
      { fileName: 'hahira', fileType: 'microsoft_word' },
      { fileName: 'wawa', fileType: 'microsoft_word' },
    ];
    dispatch(addDocConversionRow({ files: newFiles }));
  };
  return (
  <>
   {docConvertionRows.map(row => {
      return <DocConvertionRow onAddRow={handleAddRow}/>
    })} 
  </>
   
  )
}

export default DocConvertionPanel