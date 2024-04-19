import React from 'react'
import FileUpload from './FileUpload'

export default function DocConvertionRow({onAddRow}) {

  return (
    <section>
      <FileUpload/>
      <FileUpload/>
      <button className="btn" onClick={() => onAddRow()}>Add row</button>
      <button className="btn" onClick={() => onAddRow()}>Button</button>
    </section>
  )
}
