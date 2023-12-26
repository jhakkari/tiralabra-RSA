from tkinter import ttk
from ui.key_generation_view import KeyGenerationView
from ui.encryption_view import EncryptionView
from ui.decryption_view import DecryptionView

class UI:
    def __init__(self, root):
        self._tab_selector = ttk.Notebook(root)
    
    def start(self):
        self._initialize_tabs()

    def _initialize_tabs(self):
        self._tab_selector.pack(expand=1, fill='both')
        
        KeyGenerationView(self._tab_selector)
        EncryptionView(self._tab_selector)
        DecryptionView(self._tab_selector)
