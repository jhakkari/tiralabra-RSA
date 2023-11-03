from ui.key_generation_view import KeyGenerationView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        self._show_key_generation_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def _show_key_generation_view(self):
        self._hide_current_view()
        self._current_view = KeyGenerationView(self._root)
        self._current_view.pack()
