from kivy.app import App
from kivy.lang import Builder
M_TO_KM = 1.60934

class MilestoKilometer(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate_m_to_km(self):
        result = self.check_input_error()
        calresult = result * M_TO_KM
        self.root.ids.output_label.text = str(calresult)

    def handle_change_number(self, change):
        changedinput = self.check_input_error() + change
        self.root.ids.input_number.text = str(changedinput)
        self.handle_calculate_m_to_km()

    def check_input_error(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilestoKilometer().run()
