from datetime import datetime

from common.theme import Theme
from user.user_roles import UserRoles
from user.user_status import UserStatus
from utils.time_utils import TimeUtils

class User:
    def __init__(
        self,
        email_id: str
    ) -> None:
        self.email_id: str = email_id
        self.password: str = ''
        self.confirm_password: str = ''
        self.first_name: str = ''
        self.last_name: str = ''
        self.username: str = ''
        self.mobile_no: str = ''
        # self.date_of_birth: datetime = ''
        self.account_creation_date: int = TimeUtils.get_epoch()
        self.account_status: str = UserStatus.CREATED
        self.theme: str = Theme.DARK
        self.role = UserRoles.USER1
        
    def __str__(self) -> str:
        return  "Email: " + self.email_id + \
                ", First Name: " + self.first_name + \
                ", Last Name: " + self.last_name 
                
    def __repr__(self) -> str:
        return  "Email: " + self.email_id + \
                ", First Name: " + self.first_name + \
                ", Last Name: " + self.last_name 