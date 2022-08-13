class RegLocators:
    """Локаторы страницы регистрации"""

    reg_input_name = '(//input[@name="name"])[1]'  # Поле ввода имени на странице регистрации
    reg_input_email = '(//input[@name="name"])[2]'  # Поле ввода email на странице регистрации
    reg_input_password = '//input[@name="Пароль"]'  # Поле ввода пароля на странице регистрации
    reg_link_login = '//a[@href="/login"]'  # Кнопка "Войти" на странице регистрации
    reg_text_invalid_password = '//p[text()="Некорректный пароль"]'  # Ошибка "Некорректный пароль" на странице регистрации
    reg_button_submit = '//button[text()="Зарегистрироваться"]'  # Кнопка "зарегистрироваться" на странице регистрации


class AuthLocators:
    """Локаторы страницы авторизации"""

    auth_input_email = '//input[@name="name"]'  # Поле ввода email на странице авторизации
    auth_link_forgot_password = '//a[@href="/forgot-password"]'  # ссылка на страницу восстановления пароля на странице авторизации
    auth_button_login = '//button[text()="Войти"]'  # кнопка "Войти" на странице авторизации
    auth_link_register = '//a[@href="/register"]'  # ссылка на страницу регистрации на странице авторизации
    auth_input_password = RegLocators.reg_input_password  # Поле ввода пароля на странице авторизации


class MainLocators:
    """Локаторы с основой страницы"""

    personal_account_button_logout = '//button[text()="Выход"]'  # кнопка "Выход" на странице  личного кабинета
    main_constructor_header = '//p[text()="Конструктор"]'  # Кнопка "Конструктор" на главнгой странице в header
    main_logo_header = '//div[@class="AppHeader_header__logo__2D0X2"]'  # Логотип на главной странице в header
    main_personal_account_header = '//p[text()="Личный Кабинет"]'  # Кнопка "личный кабинет" на главной странице в header
    main_button_login = '//button[text()="Войти в аккаунт"]'  # кнопка "Войти в аккаунт" на главной странице
    main_tab_menu_buns = '//span[text()="Булки"]'  # Вкладка "Булки" в таб меню на главной странице
    main_tab_menu_sauces = '//span[text()="Соусы"]'  # Вкладка "Соусы" в таб меню на главной странице
    main_tab_menu_fillings = '//span[text()="Начинки"]'  # Вкладка "Начинки" в таб меню на главной странице
    main_button_place_an_order = '//button[text()="Оформить заказ"]'  # кнопка "Оформить заказ" на главной странице
    main_title_buns = '//h2[text()="Булки"]'  # заголовок раздела "Булки"
    main_title_sauces = '//h2[text()="Соусы"]'  # заголовок раздела "Соусы"
    main_title_fillings = '//h2[text()="Начинки"]'  # заголовок раздела "Начинки"
    main_last_element_in_the_constructor = "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[last()]/a[last()]"
