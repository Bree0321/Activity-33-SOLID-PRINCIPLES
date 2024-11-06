class AccountManager:
    def create_account(self):
        pass

    def update_profile(self):
        pass

    def delete_account(self):
        pass

class RecommendationService:
    def get_recommendations(self):
        pass

class User(AccountManager, RecommendationService):
    pass

class Guest(AccountManager):
    pass