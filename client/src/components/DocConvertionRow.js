import React from 'react'
import FileUpload from './FileUpload'

export default function DocConvertionRow() {
  return (
    <section>
      <FileUpload/>
      <FileUpload/>
      <button className="btn">Button</button>
    </section>
  )
}
