function createDocConvertionRow(id, files) {
    return {
      id: id,
      docs: files.map(file => ({
        fileName: file.fileName,
        fileType: file.fileType,
        content: file.content || '',  // Default content can be an empty string
      })),
    };
  }
  
  export default createDocConvertionRow;

  
// const DocConvertionRows = [
//     {
//       id: 0,
//       files: [
//         {
//           fileName: 'rishum',
//           fileType: 'microsoft_word',
//           content: '',
//         },
//         {
//           fileName: 'pinkas',
//           fileType: 'microsoft_word',
//           content: '',
//         },
//       ],
//     },
//   ];