import importlib


def import_models():
    modules = [
        "domains.auth.models.user",
        "domains.auth.models.user_setting",
        "domains.questions.models.achievement",
        "domains.questions.models.category",
        "domains.questions.models.question",
        "domains.questions.models.progress",
        "domains.notifications.models.notification",
        "domains.questions.models.attempt",
        "domains.questions.models.user_achievement",
        "domains.questions.models.streak",
        "domains.leaderboards.models.leaderboard",
        "domains.leaderboards.models.leaderboard_history",
        "domains.social.models.social_connection",
        "domains.purchases.models.in_app_purchase",
        "domains.purchases.models.virtual_currency",
        "domains.feedback.models.feedback",
        "domains.questions.models.answer",
    ]

    for module in modules:
        importlib.import_module(module)
