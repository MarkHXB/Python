"""
OOP guide
"""
#every word has to be capitalized
#example: class SystemArchitecture:....
#this is PascalCase
#camelCase is always the first word's first letter is lower cased
#snake_case is alike this one
class User:
    #init = initalize, tehát az alapokat lefektettjük
    #all of the attributes have to be determine here
    #self = maga a class neve, tehát egy példányosításnál maga a class neve: User() és ebből jönnek az attribútomok user.id.....
    def __init__(self,user_id,username):
       self.id = user_id
       self.username = username
       self.followers = 0
       self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

#object
user_1 = User(0,"Karla")
user_2 = User(1,"Max")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
