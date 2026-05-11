"""
Calculadora de Derivadas - Aplicación Móvil
Versión compilable para Android
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np

try:
    from derivatives_calculator import DerivativesCalculator
except ImportError:
    # Fallback si no encuentra el módulo
    class DerivativesCalculator:
        def __init__(self, var='x'):
            import sympy as sp
            self.var = sp.symbols(var)
        
        def symbolic_derivative(self, expr_str, order=1):
            import sympy as sp
            try:
                expr = sp.sympify(expr_str)
                derivative = sp.diff(expr, self.var, order)
                return str(derivative)
            except:
                return "Error"
        
        def simplify_derivative(self, expr_str, order=1):
            import sympy as sp
            try:
                expr = sp.sympify(expr_str)
                derivative = sp.diff(expr, self.var, order)
                simplified = sp.simplify(derivative)
                return str(simplified)
            except:
                return "Error"

# Configurar tamaño de ventana para móvil
Window.size = (480, 800)


class CalculadoraDerivadas(App):
    """Aplicación principal"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.calculator = DerivativesCalculator('x')
        self.title = "Calculadora de Derivadas"
    
    def build(self):
        """Construir interfaz"""
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Título
        title = Label(
            text='📐 Calculadora de Derivadas',
            size_hint_y=0.08,
            font_size='20sp',
            bold=True,
            color=(0.2, 0.6, 1, 1)
        )
        main_layout.add_widget(title)
        
        # Entrada
        input_label = Label(text='Expresión:', size_hint_y=0.06, font_size='14sp')
        main_layout.add_widget(input_label)
        
        self.expr_input = TextInput(
            multiline=False,
            font_size='14sp',
            size_hint_y=0.08,
            background_color=(0.9, 0.9, 0.95, 1)
        )
        main_layout.add_widget(self.expr_input)
        
        # Botones
        buttons_layout = GridLayout(cols=2, size_hint_y=0.16, spacing=5)
        
        btn_first = Button(
            text='1ª Derivada',
            background_color=(0.2, 0.6, 1, 1)
        )
        btn_first.bind(on_press=self.calc_first)
        buttons_layout.add_widget(btn_first)
        
        btn_second = Button(
            text='2ª Derivada',
            background_color=(0.2, 0.8, 0.6, 1)
        )
        btn_second.bind(on_press=self.calc_second)
        buttons_layout.add_widget(btn_second)
        
        btn_simplify = Button(
            text='Simplificar',
            background_color=(1, 0.7, 0.2, 1)
        )
        btn_simplify.bind(on_press=self.simplify)
        buttons_layout.add_widget(btn_simplify)
        
        btn_clear = Button(
            text='Limpiar',
            background_color=(0.8, 0.2, 0.2, 1)
        )
        btn_clear.bind(on_press=self.clear_all)
        buttons_layout.add_widget(btn_clear)
        
        main_layout.add_widget(buttons_layout)
        
        # Resultados
        results_label = Label(text='Resultados:', size_hint_y=0.06, font_size='14sp', bold=True)
        main_layout.add_widget(results_label)
        
        scroll = ScrollView(size_hint_y=0.56)
        self.results_text = Label(
            text='Los resultados aparecerán aquí',
            size_hint_y=None,
            font_size='12sp',
            text_size=(400, None),
            markup=True
        )
        self.results_text.bind(texture_size=self.results_text.setter('size'))
        scroll.add_widget(self.results_text)
        main_layout.add_widget(scroll)
        
        return main_layout
    
    def calc_first(self, instance):
        """Primera derivada"""
        expr = self.expr_input.text.strip()
        if not expr:
            self.results_text.text = '[color=ff0000]Ingrese una expresión[/color]'
            return
        
        try:
            result = self.calculator.symbolic_derivative(expr, order=1)
            simplified = self.calculator.simplify_derivative(expr, order=1)
            
            self.results_text.text = (
                f'[b]Expresión:[/b] {expr}\n\n'
                f'[b]Derivada:[/b]\n{result}\n\n'
                f'[b]Simplificada:[/b]\n{simplified}'
            )
        except Exception as e:
            self.results_text.text = f'[color=ff0000]Error: {str(e)}[/color]'
    
    def calc_second(self, instance):
        """Segunda derivada"""
        expr = self.expr_input.text.strip()
        if not expr:
            self.results_text.text = '[color=ff0000]Ingrese una expresión[/color]'
            return
        
        try:
            result = self.calculator.symbolic_derivative(expr, order=2)
            simplified = self.calculator.simplify_derivative(expr, order=2)
            
            self.results_text.text = (
                f'[b]Expresión:[/b] {expr}\n\n'
                f'[b]2ª Derivada:[/b]\n{result}\n\n'
                f'[b]Simplificada:[/b]\n{simplified}'
            )
        except Exception as e:
            self.results_text.text = f'[color=ff0000]Error: {str(e)}[/color]'
    
    def simplify(self, instance):
        """Simplificar"""
        expr = self.expr_input.text.strip()
        if not expr:
            self.results_text.text = '[color=ff0000]Ingrese una expresión[/color]'
            return
        
        try:
            result = self.calculator.simplify_derivative(expr, order=1)
            self.results_text.text = (
                f'[b]Expresión:[/b] {expr}\n\n'
                f'[b]Derivada Simplificada:[/b]\n{result}'
            )
        except Exception as e:
            self.results_text.text = f'[color=ff0000]Error: {str(e)}[/color]'
    
    def clear_all(self, instance):
        """Limpiar"""
        self.expr_input.text = ''
        self.results_text.text = 'Los resultados aparecerán aquí'


if __name__ == '__main__':
    CalculadoraDerivadas().run()
