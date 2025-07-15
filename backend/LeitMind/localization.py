translations = {
    "fr": {
        "user_not_found": "Aucun compte ne correspond à cet email.",
        "invalid_password": "Mot de passe incorrect.",
        "account_locked": "Le compte est verrouillé.",
        "default_error": "Une erreur est survenue.",
    },
    "en": {
        "user_not_found": "No account found with that email.",
        "invalid_password": "Incorrect password.",
        "account_locked": "Account is locked.",
        "default_error": "An unexpected error occurred.",
    },
}


def translate(error_code: str, lang: str) -> str:
    print(f"Translating error code '{error_code}' to language '{lang}'")
    print(f"Available translations: {translations.get(lang, translations['en'])}")
    return translations.get(lang, translations["en"]).get(
        error_code, translations["en"]["default_error"]
    )
