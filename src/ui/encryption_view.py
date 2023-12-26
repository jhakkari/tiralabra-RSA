from tkinter import ttk, constants, messagebox, Text
from services.rsa_cipher_service import CipherService, MessageLongerThanModulusError


class EncryptionView:

    def __init__(self, tab_selector):
        self._tab_selector = tab_selector
        self._frame = None
        self._public_key_textbox = None
        self._message_to_encrypt_textbox = None
        self._encrypted_message_textbox = None
        self._cipher_service = CipherService()

        self._initialize()

    def _clear_textbox_contents(self):
        self._encrypted_message_textbox.delete("1.0", "end")

    def _set_textbox_contents(self, content):
        self._encrypted_message_textbox.insert("end-1c", f"{content}")

    def _handle_encrypt_message(self):
        self._clear_textbox_contents()

        public_key = self._public_key_textbox.get("1.0", "end").split(", ")
        message = self._message_to_encrypt_textbox.get("1.0", "end-1c")

        try:
            public_exp = int(public_key[0])
            modulus = int(public_key[1])
        
        except:
            self._show_error_message("Input error", "Check given public key")
        else:
            try:
                encrypted_message = self._cipher_service.encrypt(public_exp, modulus, message)
                self._encrypted_message_textbox.insert("end-1c", f"{encrypted_message}")
            except MessageLongerThanModulusError as error:
                self._show_error_message("Encryption error", error)

    def _show_error_message(self, error_type, message):
        messagebox.showerror(error_type, message)

    def _initialize_labels(self):
        public_key_label = ttk.Label(master=self._frame, text="Public key:")
        message_plain_label = ttk.Label(master=self._frame, text="Message:")
        message_encrypted_label = ttk.Label(master=self._frame, text="Encrypted message:")

        public_key_label.grid(row=0, columnspan=2, sticky="ew", padx=5, pady=5)
        message_plain_label.grid(row=2, columnspan=2, sticky="ew", padx=5, pady=5)
        message_encrypted_label.grid(row=4,columnspan=2, sticky="ew", padx=5, pady=5)

    def _initialize_textboxes(self):
        self._public_key_textbox = Text(master=self._frame)
        self._message_to_encrypt_textbox = Text(master=self._frame)
        self._encrypted_message_textbox = Text(master=self._frame)

        self._public_key_textbox.grid(row=1, columnspan=2, sticky="nsew", padx=5, pady=5)
        self._message_to_encrypt_textbox.grid(row=3, columnspan=2, sticky="nsew", padx=5, pady=5)
        self._encrypted_message_textbox.grid(row=5, columnspan=2, sticky="nsew", padx=5, pady=5)

    def _initialize_button(self):
        encrypt_message_button = ttk.Button(self._frame, text="Encrypt", command=self._handle_encrypt_message)
        encrypt_message_button.grid(columnspan=2, sticky="ew", padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._tab_selector)
        self._tab_selector.add(self._frame, text="Encrypt")

        self._initialize_labels()
        self._initialize_textboxes()
        self._initialize_button()

        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_rowconfigure([1, 3, 5], weight=1)
