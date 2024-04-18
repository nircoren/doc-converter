

arr =  {
    'convertion_1' : [ 
    {
        
        'sources' : [
            {
            'file_props':{
                'file_type':'pdf_doc-tables',
                'file_name': 'rishum_pinkas',
                'url': r'C:\Users\nirco\Desktop\pythonProj1\docs\rishum_pinkas.pdf'
            },
             'text_mappings':[ 
                 {
                    'extraction': { # 515.00
                         'indexes': {
                            'table_index': 1,
                            'row': 1,
                            'column': 4,
                        },
                    },
                    'insertion':{
                        'insert_type': 'table',
                        'indexes':{
                            'table_index': 4,
                            'row': 3,
                            'column': 3,
                        },
                    }
                },
                 {
                    'extraction': { # בשלמות
                         'indexes': {
                            'table_index': 3,
                            'row': 3,
                            'column': 0,
                        },
                    },
                    'insertion':{
                        'insert_type': 'table',
                        'indexes':{
                            'table_index': 4,
                            'row': 3,
                            'column': 4,
                        },
                    }
                },
             ]
        },       
        {
            'file_props':{
                'file_type':'pdf_doc',
                'file_name': 'rishum_pinkas',
                'url': r'C:\Users\nirco\Desktop\pythonProj1\docs\rishum_pinkas.pdf'
            },
            'text_mappings':[
                {
                    'extraction': {
                        'text_before' : 'גוש',
                    },
                    'insertion':{
                        'insert_type': 'table',
                        'indexes':{
                            'table_index': 4,
                            'row': 3,
                            'column': 0,
                        },
                    }
                },
                {
                    'extraction': {
                        'text_before' : 'חלקה',
                    },
                    'insertion':{
                        'insert_type': 'table',
                        'indexes':{
                            'table_index': 4,
                            'row': 3,
                            'column': 2,
                        },
                    }
                },
            ]
        } ,
        {
            'file_props':{
                'file_type':'pdf_doc',
                'file_name': 'hahira',
                'url': r'C:\Users\nirco\Desktop\pythonProj1\docs\hahira_test.pdf'
            },
            'text_mappings':[
                {
                    'extraction': {
                        'check': True
                        # tells how many words to take after the text_before
                    },
                    'insertion':{
                        'insert_type': 'checkbox',
                        'index' : 0,
                        'paragraph_includes' : 'רישום זכות חכירה ראשית',
                    }
                },
            
                {
                    'extraction': {
                        'text_before': 'מספר תיק ישן',
                        # tells how many words to take after the text_before
                        'skip_count': 0,
                        'page': 0
                    },
                    'insertion':{
                        'insert_type': 'table',
                        'style': {
                            'bold': True,
                        },
                        'indexes':{
                            'table_index': 0,
                            'row': 1,
                            'column': 1,
                            'page': 0
                        }
                    }
                },
                {
                    'extraction': { # הלפרסון ליאור 
                        'text_before': 'לבין',
                        'text_after': 'מספר',
                    },
                    'insertion':
                    [
                        {
                            'insert_type': 'table',
                            'indexes':{
                                'table_index': 1,
                                'row': 2,
                                'column': 0,
                            }
                        },
                        {
                            'insert_type': 'table',
                            'indexes':{
                                'table_index': 5,
                                'row': 2,
                                'column':-2,
                            }
                        }
                     ]
                },
                {
                    'extraction': {
                        'text_before': 'הנהלת המחכירה תקופת החכירה',
                        'text_after': 'שנים',
                        # tells how many words to take after the text_before
                    },
                    'insertion':{
                        'insert_type': 'paragraph',
                        'text_before': ' לתקופה בת',
                        'text_after':'שנים',
                        'style': {
                            'underline': True,
                        },
                    }
                },
                {
                    'extraction': {
                        'text_before': 'ועד –',
                        'text_after': 'תקופת',
                        # tells how many words to take after the text_before
                        'skip_count': 0,
                    },
                    'insertion':{
                        'insert_type': 'paragraph',
                        'text_before': 'המסתיימת ב-',
                        'text_after':'שנים',
                        'style': {
                            'underline': True,
                        },
                    }
                },
                {
                    'extraction': {
                        'text_before': 'ולראיה באו הצדדים על החתום החוכר שם'  ,
                        'regex' : r'ולראיה באו הצדדים על החתום החוכר שם\s+.+?\s+(\b\w+\b\s\b\w+\b)(?=\s\d)',
                    },
                    'insertion':{
                        'insert_type': 'table',
                        'indexes':{
                            'table_index': 1,
                            'row': 2,
                            'column': 1,
                            'page': 0
                        }
                    }
                },
                {
                    'extraction': {
                        'regex' : r'ולראיה באו הצדדים על החתום החוכר שם\s+.+?\s+\b\w+\b\s\b\w+\b\s+(\d+)',
                    },
                    'insertion':{
                        'insert_type': 'table',
                        'indexes':{
                            'table_index': 1,
                            'row': 2,
                            'column': 2,
                            'page': 0
                        }
                    }
                },
                {
                    'extraction': { # החלק בנכס
                        'regex' : r'החלק בנכס (\S+)',
                    },
                    'insertion':[
                        {
                            'insert_type': 'table',
                            'indexes':{
                                'table_index': 1,
                                'row': 4,
                                'column': 3,
                                'page': 0
                            }
                        },
                        {
                            'insert_type': 'table',
                            'indexes':{
                                'table_index': 1,
                                'row': 2,
                                'column': 4,
                                'page': 0
                            }
                        }
                    ]
                    
                },
                {
                    'extraction': { # גבעת יואב
                        'regex' : r'המקום(.*?)השטח',
                    },
                    'insertion':{
                        'insert_type': 'table',
                        'style': {
                            'underline': True,
                        },
                        'indexes':{
                            'table_index': 4,
                            'row': 0,
                            'column': 1,
                            'page': 0
                        },
                        'text_before': 'המקרקעין הישוב:',
                    
                    }
                },
            ]
        },      
        ],
        'target_file' : {
            'file_props':{
                'file_type':'microsoft_word',
                'url': r'C:\Users\nir-c\Desktop\home_projects\fastapi-python-react-doc-converter\test-docs\target-file.docx'
            },   
            'font_style':{
                'name':'David',
                'size': 10,            
                },
        },
    },
]
}


#  img to text: 
# arr =  [ 
#     {
#         'sources' : [     
#         {
#             'file_props':{
#                 'file_type':'pdf_doc',
#                 'url': r'C:\Users\nirco\Desktop\pythonProj1\docs\hahira_test.pdf'
#             },
#             'text_mappings':[
#                 {
#                     'extraction': { # הלפרסון ליאור 
#                         'text_before': 'לבין',
#                         'text_after': 'מספר',
#                     },
#                     'insertion':
#                     [
#                         {
#                             'insert_type': 'table',
#                             'indexes':{
#                                 'table_index': 1,
#                                 'row': 2,
#                                 'column': 0,
#                             }
#                         },
#                         {
#                             'insert_type': 'table',
#                             'indexes':{
#                                 'table_index': 5,
#                                 'row': 2,
#                                 'column':-2,
#                             }
#                         }
#                      ]
#                 },
#             ]
#         }       
#         ],
#         'target_file' : {
#             'file_props':{
#                 'file_type':'microsoft_word',
#                 'url': r'C:\Users\nirco\Desktop\pythonProj1\test\target-file.docx'
#             },   
#             'font_style':{
#                 'name':'David',
#                 'size': 10,            
#             },
#         },
#     },
     

# ]


        #     {
        #     'file_props':{
        #         'file_type':'png',
        #         'url': r'C:\Users\nirco\Desktop\pythonProj1\docs\page_1.png'
        #     },
        #     'text_mappings':[
        #         {
        #            'extraction': {
        #                'props':   {
        #                 'extraction_type':'rectangle',
        #                 'lang_type': 'heb',
        #                 # 'text_before': 'היא:',
        #                 # 'text_after': 'מצד אחד'
        #             },
        #             'rect_coords': {
        #                 'x': 1296,
        #                 'y': 1238,
        #                 'w': 317,
        #                 'h': 120
        #             },
        #            },
        #             'insertion':{
        #                 'props':{
        #                     'insert_type': 'paragraph',
        #                     'text_before': 'לשכת רישום המקרקעין ב',
        #                     # 'text_after':'סכום לתשלום',
        #                 },
        #                 'style': {
        #                     'underline': True,
        #                 },
        #             }
        #         }, 
        #         {
        #             # todo: change to: pull {...} ,insertion :{...}
        #            'extraction': {
        #                'props':   {
        #                 'extraction_type':'rectangle',
        #                 'lang_type': 'heb',
        #                 'text_before': ':',
        #                 'text_after': 'מס'
        #             },
        #             'rect_coords': {
        #                 'x': 184,
        #                 'y': 230,
        #                 'w': 522,
        #                 'h': 246
        #             },
        #            },
        #             'insertion':{
        #                 'props':{
        #                     'insert_type': 'table',
        #                     'text_before': '',
        #                     'text_after':'סכום לתשלום',
        #                 },
        #                 'style': {
        #                     'bold': True,
        #                 },
        #                 'indexes':{
        #                     'table_index': 0,
        #                     'row': 1,
        #                     'column': 1,
        #                     'page': 0
        #                 }
        #             }
        #         },      
        #          {
        #             # todo: change to: pull {...} ,insertion :{...}
        #            'extraction': {
        #                'props':   {
        #                 'extraction_type':'rectangle',
        #                 'lang_type': 'heb',
        #                 'text_before': 'היא:',
        #                 'text_after': 'מצד אחד'
        #             },
        #             'rect_coords': {
        #                 'x': 85,
        #                 'y': 888,
        #                 'w': 1543,
        #                 'h': 365
        #             },
        #            },
        #             'insertion':{
        #                 'props':{
        #                     'insert_type': 'paragraph',
        #                     'text_before': 'לשכת רישום המקרקעין ב',
        #                     # 'text_after':'סכום לתשלום',
        #                 },
        #                 'style': {
        #                     'underline': True,
        #                 },
        #             }
        #         },      
                     
        #     ],
        #  },
        #   {
        #     'file_props':{
        #         'file_type':'png',
        #         'url': r'C:\Users\nirco\Desktop\pythonProj1\docs\page_3.png'
        #     },
        #     'text_mappings':[
        #         {
        #             # todo: change to: pull {...} ,insertion :{...}
        #            'extraction': {
        #                'props':   {
        #                 'extraction_type':'rectangle',
        #                 'lang_type': 'heb',
        #                 'text_before': 'ייתקופת החכירהיי: ',
        #                 'text_after': 'ש'
        #             },
        #             'rect_coords': {
        #                 'x': 1143,
        #                 'y': 498,
        #                 'w': 404,
        #                 'h': 191
        #             },
        #            },
        #             'insertion':{
        #                 'props':{
        #                     'insert_type': 'paragraph',
        #                     'text_before': ' לתקופה בת',
        #                     'text_before_additions':' ',
        #                     'insert_text_after_additions':' ',
        #                     # 'text_after':'ש', 
        #                     # 'replace': 'line',
        #                 },
        #                 'style': {
        #                     'underline': True,
        #                 }
        #             }
        #         },
        #         {
        #             # todo: change to: pull {...} ,insertion :{...}
        #            'extraction': {
        #                'props':   {
        #                 'extraction_type':'rectangle',
        #                 'lang_type': 'heb',
        #                 'text_before': 'ועד- ',
        #                 'text_after': ' '
        #             },
        #             'rect_coords': {
        #                 'x': 285,
        #                 'y': 390,
        #                 'w': 828,
        #                 'h': 330
        #             },
        #            },
        #             'insertion':{
        #                 'props':{
        #                     'insert_type': 'paragraph',
        #                     'text_before': 'מסתיימת ב',
        #                  'style': {
        #                     'underline': True,
        #                 },
        #                     'text_before_additions':'-',
        #                     # 'text_after':'המסתיימת ב',
        #                 },
                        
        #             }
        #         },
                
        #     ],
        #  },