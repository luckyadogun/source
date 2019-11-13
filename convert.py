import csv
from itertools import zip_longest

import fitz

from helpers import get_headers, get_csv_fields


def get_docs():
    '''
    NOTE: In the tasks, page 8 and 9 were requested
    to be solved. The PDF libary used sees page 8 as 7
    and page 9 as 8.

    This function parses document for processing 
    and returns the parsed docs
    '''
    pdf_file = fitz.open('n.pdf')
    pg_7 = pdf_file.getPageText(7, output="text")
    pg_8 = pdf_file.getPageText(8, output="text")
    # remove whitespace from text
    doc_1 = pg_7.strip(" ").split("\n")
    doc_2 = pg_8.strip(" ").split("\n")

    return doc_1[1:36], doc_2


def cleaned_doc_1_and_convert(output_name):
    '''
    This function cleans the parsed data for first page 
    and return it for conversion to output format. 
    '''
    doc_1 = get_docs()[0]

    new_list = []
    for d in doc_1:
        new_list.append(d.strip())

    new_list = new_list[0:36]
    left_col = new_list[1::2] #no at odd positions in list
    right_col = new_list[::2] #no at even positions in list
    # delete an unwanted item from list
    __del_item__ = right_col.pop(1)

    with open('{}.csv'.format(output_name), 'w') as f_obj:
        csv_output = csv.writer(f_obj)
        csv_output.writerows(zip_longest(*[left_col, right_col]))

    status = '{} is ready!'.format(output_name)
    return status


def cleaned_doc_2_and_convert(text_name, csv_name):
    '''
    This function cleans the parsed data for second page 
    and return it for conversion to output format. 
    '''
    doc_2 = get_docs()[1]

    get_text = doc_2[83:91]
    headers = get_headers(data=doc_2) # cleans the doc and return table headers
    rows = get_csv_fields(doc_2[17:83], headers) 

    # convert text file
    with open("{}.txt".format(text_name), "w") as text_file:
        for txt in get_text:   
            text_file.write(txt)

    # convert to csv file
    with open("{}.csv".format(csv_name), "w", newline='') as f_obj:
        csv_output = csv.writer(f_obj)
        csv_output.writerow(headers)
        for i in rows:
            csv_output.writerow(i)


def main():
    doc_1_name = input('Enter doc name for 1st page [CSV]: > ')
    doc_2_text = input('Enter doc name for 2nd page [TEXT]: > ')
    doc_2_csv = input('Enter doc name for 2nd page [CSV]: > ')

    cleaned_doc_1_and_convert(doc_1_name)
    cleaned_doc_2_and_convert(doc_2_text, doc_2_csv)




if __name__ == "__main__":
    print("********** Processing ************")
    main()
    print("\nDocument is ready. Check your directory")








        


