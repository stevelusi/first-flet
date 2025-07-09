import flet as ft


def main(page: ft.Page):
    page.title("welcome to flet initial")
    
    enter= ft.TextField()
    
    
    
    def greet(e):
        if not enter.value:
            enter.error_text= "pls type your name"
        else:
            page.clean()
            ft.Text(f"hello {input.value}!!!")
    
    
    
    
    
    button= ft.ElevatedButton("click me", on_click= greet)
    
    page.add(
        enter,
        button
    )
    
ft.app(main)
    
    