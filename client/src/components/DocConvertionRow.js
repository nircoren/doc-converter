import React from "react";
import FileUpload from "./FileUpload";

export default function DocConvertionRow({ rowIndex,rowData, onUploadDoc }) {
  return (
    <section>
      {rowData.map((docData, index) => 
        <FileUpload key={index} rowIndex={rowIndex} inputIndex={index}/>
      )}
      <button className="btn" onClick={() => "wa"}>
        Button
      </button>
    </section>
  );
}
