from tkinter import ttk, constants, Text
from services.rsa_key_service import KeyService

class KeyGenerationView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._public_key_textbox = None
        self._private_key_textbox = None
        self._key_service = KeyService()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _handle_generate_keys(self):
        keys = self._key_service.generate()
        self._public_key_textbox.insert("end-1c", f"{keys[0]}")
        self._private_key_textbox.insert("end-1c", f"{keys[1]}")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        public_key_label = ttk.Label(master=self._frame, text="Public key:")
        private_key_label = ttk.Label(master=self._frame, text="Private key:")

        self._public_key_textbox = Text(master=self._frame)
        self._private_key_textbox = Text(master=self._frame)

        generate_keys_button = ttk.Button(self._frame, text="Generate", command=self._handle_generate_keys)

        public_key_label.grid(columnspan=2, sticky="ew", padx=5, pady=5)
        self._public_key_textbox.grid(columnspan=2, sticky="ew", padx=5, pady=5)
        private_key_label.grid(columnspan=2, sticky="ewns", padx=5, pady=5)
        self._private_key_textbox.grid(columnspan=2, sticky="ew", padx=5, pady=5)
        generate_keys_button.grid(columnspan=2, sticky="ewns", padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1)