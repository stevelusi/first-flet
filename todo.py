import flet as ft

def main(page: ft.Page):
    page.title = "TO-DO App"
    page.horizontal_alignment = "right"
    page.theme_mode = "light"
    #page.window_bgcolor = "blue"
    
    # taking in input
    input_text = ft.TextField(hint_text = "this is optional....", width=400)
    
    def button_clicked(e):
        page.add(
            ft.Checkbox(label=input_text.value)
        )
    
    # aligning the inputed text and button in a row
    page.add(
        ft.Row(
            [
                input_text,
                ft.ElevatedButton(text = "Add", color="red", on_click=button_clicked)
            ]
        )
    )
    
    
ft.app(target= main)