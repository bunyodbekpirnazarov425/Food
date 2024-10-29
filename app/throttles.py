from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class FoodTypeAnonRateThrottle(AnonRateThrottle):
    scope = 'food_type_anon_list'

class FoodTypeUserRateThrottle(UserRateThrottle):
    scope = 'food_type_user_list'

class FoodAnonRateThrottle(AnonRateThrottle):
    scope = 'food_anon_detail'

class FoodUserRateThrottle(UserRateThrottle):
    scope = 'food_user_detail'

class CommentAnonRateThrottle(AnonRateThrottle):
    scope = 'comment_anon_list'

class CommentUserRateThrottle(UserRateThrottle):
    scope = 'comment_user_list'