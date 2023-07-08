import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("DarkBlue6")
label1 = sg.Text("Select file to extract: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key='choose_archive')

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key='choose_folder')

extract_button = sg.Button("Extract")
output_label = sg.Text(key='output', text_color='yellow')

label_col = sg.Column([[label1], [label2]])
input_col = sg.Column([[input1], [input2]])
button_col = sg.Column([[choose_button1], [choose_button2]])

window = sg.Window("Archive Extractor",
                   layout=[[label_col, input_col, button_col],
                           [extract_button, output_label]]
                   )
while True:
    event, values = window.read()
    archivepath = values['choose_archive']
    folder = values['choose_folder']
    extract_archive(archivepath, folder)
    window['output'].update(value="Extraction Completed!")


window.close()
