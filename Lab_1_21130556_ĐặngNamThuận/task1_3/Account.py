from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, name, email, country):
        self.__name = name
        self.__email = email
        self.__country = country
        self.__friends = list()
        self.__posts = list()

    @abstractmethod
    def __repr__(self):
        pass

    def get_Country(self):
        return self.__country

    def get_Name(self):
        return self.__name

    def get_Email(self):
        return self.__email

    def get_LastName(self):
        return str(self.get_Name()).split()[-1]

    def get_Posts(self):
        return self.__posts

    def get_Friends(self):
        return self.__friends

    def add_post(self, post):
        self.get_Posts().append(post)

    def add_friend(self, account):
        self.get_Friends().append(account)

    def getMaxLikePostInListFriends(self):
        re = 0
        max_like_post = None
        if self.get_Friends():
            for account in self.get_Friends():
                if account.get_Posts():
                    for post in account.get_Posts():
                        if re < post.get_Likes():
                            re = post.get_Likes()
                            max_like_post = post
        return max_like_post

    def getMaxLikePostByFriend(self):
        max_like_post = self.getMaxLikePostInListFriends()
        for account in self.get_Friends():
            if max_like_post in account.get_Posts():
                break
        return account
