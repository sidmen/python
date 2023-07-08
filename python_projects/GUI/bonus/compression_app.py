import PySimpleGUI as sg
from zip_creator import make_archive   # from zip_creator.py

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key='choose_files')   # not a generic button (sg.Button), but a button to browse multiple files (filesbrowse) | for single file use filebrowse

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key='choose_folder')  # button to browse folders

compress_button = sg.Button("Compress")
output_label = sg.Text(key='output', text_color='yellow')

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]]
                   )

while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values['choose_files'].split(';')
    folder = values['choose_folder']

    make_archive(filepaths=filepaths, dest_dir=folder)
    window['output'].update(value="Compression Completed!")

window.close()