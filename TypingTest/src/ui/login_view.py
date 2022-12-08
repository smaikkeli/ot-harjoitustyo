from tkinter import ttk, constants, StringVar

from services.user_service import user_service
from services.user_service import UserNotFoundError, IncorrectPasswordError

class LoginView:
    def __init__(self, root, handle_menu_view, handle_create_user_view):

        self._root = root
        self._handle_menu_view = handle_menu_view
        self._handle_create_user_view = handle_create_user_view

        self._frame = None
        self._username_form = None
        self._password_form = None

        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self): 

        self._root.geometry("270x120")
        self._frame = ttk.Frame(master = self._root)

        self._initialize_error_variable()
        self._initialize_username_and_password_label()   
        self._initialize_username_and_password_form()
        self._initialize_login_and_create_user_button()

    def _initialize_error_variable(self):

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(master=self._frame,
                                textvariable = self._error_variable,
                                font = ('consolas', 10, 'bold'),
                                foreground = 'red')
        
        self._error_label.grid(row = 0, column = 1, padx=5, pady=1)

    def _initialize_username_and_password_label(self):

        username_label = ttk.Label(master=self._frame,
                                text = "Username",
                                font=('consolas', 10, "bold"))
        password_label = ttk.Label(master=self._frame,
                                text = "Password",
                                font=('consolas', 10, "bold"))

        username_label.grid(column = 0, row = 1, padx= 5, pady = 5)
        password_label.grid(column = 0, row = 2, padx = 5, pady = 5)

    def _initialize_username_and_password_form(self):

        self._username_form = ttk.Entry(master = self._frame)
        self._password_form = ttk.Entry(master = self._frame, show = "*")

        self._username_form.grid(column = 1, row = 1, padx = 5, pady = 5)
        self._password_form.grid(column = 1, row = 2, padx = 5, pady = 5)

    def _initialize_login_and_create_user_button(self):

        login_button = ttk.Button(master = self._frame,
                                text = "Login", 
                                command = self._handle_login)

        create_user_button = ttk.Button(master = self._frame,
                                    text = "Create user",
                                    command = self._handle_create_user_view)

        login_button.grid(column = 0, row = 3, padx = 5, pady = 3)
        create_user_button.grid(column = 1, row = 3, padx = 5, pady = 3)

    def _handle_login(self):

        username = self._username_form.get()
        password = self._password_form.get()

        try:
            user_service.login(username, password)
            self._handle_menu_view()
        except UserNotFoundError:
            self._error_variable.set("User not found")
            self._error_label.grid(row = 0, column = 1, columnspan = 2, padx=5, pady = 1)
        except IncorrectPasswordError:
            self._error_variable.set("Incorrect password")
            self._error_label.grid(row = 0, column = 1, columnspan = 2, padx=5, pady = 1)