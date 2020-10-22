from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print('greet')
        print("test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text
        return

    def pressed_clear(self):
        print('Clear')
        for instance in self.root.output_label.children:
            instance.state = 'normal'
        self.status_text = ""
        return


BoxLayoutDemo().run()
