from .services.tesseractService import get_cropped_img_str, print_heb
from .services.msWordService import insert_text_to_table,create_new_doc,save_doc,insert_text_to_paragraph,replace_text,check_box
from .services import docService
# change this to get dict from another place
from .dictionary import arr
from PIL import Image

def convert_files_to_doc(request_data):
    for action in arr[request_data['action_name']]:
        doc = create_new_doc(action['target_file']['file_props']['url'])
        for source in action['sources']:
            file = request_data['files'][source['file_props']['file_name']]
            texts_to_insert = get_source_texts(source,file)
            insert_texts_to_target(doc,texts_to_insert, action['target_file'])
    doc_id = save_doc(doc,action['target_file']['font_style'])
    return doc_id

def insert_texts_to_target(doc,texts_to_insert, target):
        if(target['file_props']['file_type'] == 'microsoft_word'):
              for text_to_insert in texts_to_insert:
                    if not isinstance(text_to_insert['insertion'], list):
                        text_to_insert['insertion'] = [text_to_insert['insertion']]
                    for insertion in text_to_insert['insertion']:
                        if insertion['insert_type'] == 'table':
                            insert_text_to_table(doc,insertion,text_to_insert['text'])
                        elif insertion['insert_type'] == 'paragraph':
                            insert_text_to_paragraph(doc,insertion,text_to_insert['text'])
                        elif insertion['insert_type'] == 'checkbox':
                            check_box(doc,insertion)
                   


    
def get_source_texts(source,file):
    if(source['file_props']['file_type'] == 'png'):
        texts_to_insert = []
        # here the img needs to be defined
        for text_to_insert in source['text_mappings']:
            if text_to_insert['extraction']['props']['extraction_type'] == 'rectangle':
                reqt_coords = text_to_insert['extraction']['rect_coords']
                result_text = get_cropped_img_str(source['file_props']['url'],reqt_coords['x'],reqt_coords['y'],reqt_coords['w'],reqt_coords['h'])
                if(text_to_insert['extraction']['props']['text_before'] != '' or text_to_insert['extraction']['props']['text_after'] != ''):  
                    result_text = extract_text_between_strings(result_text,text_to_insert['extraction']['props']['text_before'],text_to_insert['extraction']['props']['text_after'])
                elif text_to_insert['extraction']['props']['replace']:
                    result_text = replace_text(result_text,text_to_insert['extraction']['props']['replace'])
                texts_to_insert.append({'insertion':text_to_insert['insertion'],'text':result_text})

    elif(source['file_props']['file_type'] == 'pdf_doc'):
        pdf_text_list = docService.get_all_text_from_pdf(file)
        texts_to_insert = docService.find_words_between(pdf_text_list,source['text_mappings'])

    elif(source['file_props']['file_type'] == 'pdf_doc-tables'):
        texts_to_insert =  docService.get_insertion_text(file, source['text_mappings'])
    return texts_to_insert


def extract_text_between_strings(input_string, start_string, end_string):
    start_index = input_string.find(start_string)
    if start_string == '':
        start_index = 0
    if start_index == -1:
        return None  # Start string not found
    
    start_index += len(start_string)
    end_index = input_string.find(end_string, start_index)

    if end_index == -1:
        end_index = len(input_string) # End string not found

    result_text = input_string[start_index:end_index]
    return result_text.strip()
