from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

from .user import User
from .activityplan import ActivityPlan
from .mealplan import MealPlan