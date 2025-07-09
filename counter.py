import flet as ft
from time import sleep


def main(page: ft.Page):
    page.title = "counter app"
    page.bgcolor = "yellow"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    
    text = ft.Text(color="black")
    page.add(text)
    
    for i in range(1,11):
        text.value = "Count " + str(i)
        page.update()
        sleep(1) #allows program to sleep for one second
        
    
ft.app(target = main)
    