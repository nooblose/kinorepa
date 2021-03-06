translations = {
    "introduction": (
        "Привет, {} 👋\n"
        "Я помогу тебе выбрать крутой фильм на вечер! Вот список доступных команд:\n\n"
        "  - */reg* - зарегистрироваться в системе\n"
        "  - */find* <_название_> - найти фильм\n"
        "  - */liked* - получить фильмы, которые вам понравились\n"
        "  - */to_watch* - получить фильмы, которые вы хотели посмотреть позже\n"
        "  - */set_filters* - добавить фильтры для поиска фильма\n"
    ),
    "nothing_found": "К сожалению, по твоему запросу не удалось ничего найти 😥",
    "already_registered": "Ты уже зарегистрирован и можешь пользоваться ботом",
    "successfully_registered": "Регистрация прошла успешно!",
}


def get(translation):
    return translations[translation]


def get_with_args(translation, *args):
    return translations[translation].format(*args)
