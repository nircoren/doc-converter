import React from 'react'
import DocConvertionRow from './DocConvertionRow'
import { useSelector, useDispatch } from 'react-redux';
import { addDocConvertionRow } from '../features/doc/docSlice';

function DocConvertionPanel() {
  const docConvertionRows = useSelector(state => state.doc.docConvertionRows);
  const dispatch = useDispatch();
  const handleAddRow = () => {
    const newRow = [
      { fileName: 'hahira', fileType: 'microsoft_word' },
      { fileName: 'wawa', fileType: 'microsoft_word' },
    ];
    dispatch(addDocConvertionRow({ row: newRow }));
  };

  const handleDocUploaded = () => {

  }

  return (
  <>
   {docConvertionRows.map((rowData,index) =>
       <DocConvertionRow key={index} rowIndex={index} rowData={rowData.docs} onUploadDoc={handleDocUploaded}/>
    )} 
      <button className="btn" onClick={handleAddRow}>Add row</button>

  </>
   
  )
}

export default DocConvertionPanel