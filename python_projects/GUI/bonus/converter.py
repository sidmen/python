import PySimpleGUI as sg


def convert(feet, inches):
    meters = f"{feet * 0.3048 + inches * 0.0254} m"
    return meters


feet_label = sg.Text("Enter feet:")
inches_label = sg.Text("Enter inches:")

feet_input = sg.Input(key='feet')
inches_input = sg.Input(key='inches')

convert_button = sg.Button("Convert")
exit_button = sg.Button('Exit')

output_label = sg.Text(key='output')

window = sg.Window("Converter",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [convert_button, exit_button, output_label]],
                   font=("Helvetica", 20)
                   )

while True:
    event, values = window.read()
    match event:
        case 'Convert':
            try:
                feet = float(values['feet'])
                inches = float(values['inches'])
                meters = convert(feet, inches)
                window['output'].update(value=meters)
            except ValueError:
                sg.popup("Please provide two numbers", title="Error", font=("Helvetica", 20))

        case 'Exit':
            exit()
        case sg.WIN_CLOSED:
            break

window.close()
