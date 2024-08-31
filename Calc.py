import flet as ft

def main(page: ft.Page):
    page.window.width = 353
    page.window.height = 314
    page.window.resizable = False   
    page.title = "Calc App"

    # To store the current expression and result
    expression = ""

    # Display result in this Text control
    result = ft.Text(value="0", size=30)

    # Function to handle button click
    def button_click(e):
        nonlocal expression
        button_value = e.control.text
        
        if button_value == "AC":
            expression = ""
            result.value = "0"
        elif button_value == "=":
            try:
                # Evaluate the expression and update the result
                result.value = str(eval(expression))
                expression = result.value  # Update expression with result for further calculations
            except:
                result.value = "Error"
                expression = ""
        elif button_value == "+/-":
            if expression:
                try:
                    # Negate the current expression
                    expression = str(-eval(expression))
                    result.value = expression
                except:
                    result.value = "Error"
                    expression = ""
        else:
            # Append clicked button to the expression
            if result.value == "0" and button_value.isdigit():
                expression = button_value  # Replace 0 with the first digit
            else:
                expression += button_value
            result.value = expression
        
        # Update the display
        result.update()

    # Class definitions for buttons
    class CalcButton(ft.ElevatedButton):
        def __init__(self, text, expand=1):
            super().__init__()
            self.text = text
            self.expand = expand
            self.on_click = button_click  # Attach the button click handler

    class DigitButton(CalcButton):
        def __init__(self, text, expand=1):
            CalcButton.__init__(self, text, expand)
            self.bgcolor = ft.colors.BLUE_700
            self.color = ft.colors.BLUE_200

    class ActionButton(CalcButton):
        def __init__(self, text):
            CalcButton.__init__(self, text)
            self.bgcolor = ft.colors.BLUE_900
            self.color = ft.colors.BLUE_400

    class ExtraActionButton(CalcButton):
        def __init__(self, text):
            CalcButton.__init__(self, text)
            self.bgcolor = ft.colors.BLUE_900
            self.color = ft.colors.BLUE_500
    
    page.add(
        ft.Container(
            width=350,
            height=300,
            bgcolor=ft.colors.GREY,
            border_radius=ft.border_radius.all(1),
            padding=1,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[result], alignment="end"),
                    ft.Row(
                        controls=[
                            ExtraActionButton(text="AC"),
                            ExtraActionButton(text="+/-"),
                            ExtraActionButton(text="%"),
                            ActionButton(text="/"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="7"),
                            DigitButton(text="8"),
                            DigitButton(text="9"),
                            ActionButton(text="*"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="4"),
                            DigitButton(text="5"),
                            DigitButton(text="6"),
                            ActionButton(text="-"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="1"),
                            DigitButton(text="2"),
                            DigitButton(text="3"),
                            ActionButton(text="+"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="0", expand=2),
                            DigitButton(text="."),
                            ActionButton(text="="),
                        ]
                    ),
                ]
            ),
        )
    )

ft.app(target=main)




