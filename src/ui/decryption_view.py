from tkinter import ttk, constants, messagebox, Text
from services.rsa_cipher_service import CipherService


class DecryptionView:

    def __init__(self, tab_selector):
        self._tab_selector = tab_selector
        self._frame = None
        self._private_key_textbox = None
        self._message_to_decrypt_textbox = None
        self._decrypted_message_textbox = None
        self._cipher_service = CipherService()

        self._initialize()

    def _clear_textbox_contents(self):
        self._decrypted_message_textbox.delete("1.0", "end")

    def _handle_decrypt_message(self):
        self._clear_textbox_contents()

        private_key = self._private_key_textbox.get("1.0", "end").split(", ")

        try:
            encrypted_message = int(self._message_to_decrypt_textbox.get("1.0", "end-1c"))
            private_exp = int(private_key[0])
            modulus = int(private_key[1])
        except:
            self._show_error_message("Invalid input", "Check given private key")
        
        try:
            message = self._cipher_service.decrypt(private_exp, modulus, encrypted_message)
        except:
            self._show_error_message("Decryption error", "Message cannot be decrypted")
        else:
            self._decrypted_message_textbox.insert("end-1c", f"{message}")

    def _show_error_message(self, error_type, message):
        messagebox.showerror(error_type, message)

    def _initialize_labels(self):
        private_key_label = ttk.Label(master=self._frame, text="Private key:")
        message_encrypted_label = ttk.Label(master=self._frame, text="Encrypted message:")
        message_plain_label = ttk.Label(master=self._frame, text="Message:")

        private_key_label.grid(row=0, columnspan=2, sticky="ew", padx=5, pady=5)
        message_encrypted_label.grid(row=2, columnspan=2, sticky="ew", padx=5, pady=5)
        message_plain_label.grid(row=4, columnspan=2, sticky="ew", padx=5, pady=5)

    def _initialize_textboxes(self):
        self._private_key_textbox = Text(master=self._frame)
        self._modulo_textbox = Text(master=self._frame)
        self._message_to_decrypt_textbox = Text(master=self._frame)
        self._decrypted_message_textbox = Text(master=self._frame)

        self._private_key_textbox.grid(row=1, columnspan=2, sticky="nsew", padx=5, pady=5)
        self._message_to_decrypt_textbox.grid(row=3, columnspan=2, sticky="nsew", padx=5, pady=5)
        self._decrypted_message_textbox.grid(row=5, columnspan=2, sticky="nsew", padx=5, pady=5)

    def _initialize_button(self):
        decrypt_button = ttk.Button(self._frame, text="Decrypt", command=self._handle_decrypt_message)
        decrypt_button.grid(columnspan=2, sticky="ew", padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._tab_selector)
        self._tab_selector.add(self._frame, text="Decrypt")

        self._initialize_labels()
        self._initialize_textboxes()
        self._initialize_button()
        
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_rowconfigure([1, 3, 5], weight=1)
