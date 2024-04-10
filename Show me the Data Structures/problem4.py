class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = set() # Since each user is unique changed to set for more efficent lookup

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user): # For this problem  I changed self.users from list to set since each user is unique
        self.users.add(user) # O(1)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users(): # O(1)
        return True
    for i in group.groups:
        if is_user_in_group(user, i):
            return True
    return False


