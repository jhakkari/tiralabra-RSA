from tkinter import ttk, constants, Text
from services.rsa_key_service import KeyService


class KeyGenerationView:

    def __init__(self, tab_selector):
        self._tab_selector = tab_selector
        self._frame = None
        self._public_key_textbox = None
        self._private_key_textbox = None
        self._key_service = KeyService()

        self._initialize()
    
    def _clear_textbox_contents(self):
        self._public_key_textbox.delete("1.0", "end")
        self._private_key_textbox.delete("1.0", "end")

    def _handle_generate_keys(self):
        self._clear_textbox_contents()

        keys = self._key_service.generate_keys()
        self._public_key_textbox.insert("end-1c", f"{keys[0]}, {keys[1]}")
        self._private_key_textbox.insert("end-1c", f"{keys[2]}, {keys[1]}")

    def _initialize_labels(self):
        public_key_label = ttk.Label(master=self._frame, text="Public key:")
        private_key_label = ttk.Label(master=self._frame, text="Private key:")

        public_key_label.grid(row=0, columnspan=2, sticky="ew", padx=5, pady=5)
        private_key_label.grid(row=2, columnspan=2, sticky="ew", padx=5, pady=5)

    def _initialize_textboxes(self):
        self._public_key_textbox = Text(master=self._frame)
        self._private_key_textbox = Text(master=self._frame)

        self._public_key_textbox.grid(row=1, columnspan=2, sticky="nsew", padx=5, pady=5)
        self._private_key_textbox.grid(row=3, columnspan=2, sticky="nsew", padx=5, pady=5)

    def _initialize_button(self):
        generate_keys_button = ttk.Button(self._frame, text="Generate", command=self._handle_generate_keys)
        generate_keys_button.grid(columnspan=2, sticky="ew", padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._tab_selector)
        self._tab_selector.add(self._frame, text="Keys")

        self._initialize_labels()
        self._initialize_textboxes()
        self._initialize_button()

        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_rowconfigure([1, 3], weight=1)
