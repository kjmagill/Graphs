import random
from queue import Queue
from faker import Faker

fake = Faker()

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print('WARNING: You cannot be friends with yourself')
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print('WARNING: Friendship already exists')
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        # reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # add users
        for i in range(0, num_users):
            self.add_user(fake.name())

        # create frienships
        # generate all possible friendship combinations
        possible_friendships = []

        # avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # shuffle the possible friendships
        random.shuffle(possible_friendships)

        # create friendships for the first X pairs of the list
        # x is determined by the formula: num_users * avg_friendships // 2
        # need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # create a queue to store all unseen vertices and
        # create a dict to store all seen/touched vertices
        unseen = Queue()
        seen = dict()

        # initialize the queue by adding the input user_id
        unseen.enqueue(user_id)
        # store a list in the seen dict containing the input user_id
        seen[user_id] = [user_id]

        # while there are items in the queue...
        while unseen.size() > 0:

            # grab the current vertex (user) from the queue
            current = unseen.dequeue()
            # grab the list of friends from the friendships dict for the current user
            friends = self.friendships[current]

            # for each friend in the list...
            for friend in friends:

                # if the current friend has not been seen yet, add it to the queue
                if friend not in seen:
                    unseen.enqueue(friend)

                    # grab a copy of the list of friends already seen up until now
                    path_to_friend = list(seen[current])

                    # add the current friend to the end of this list and
                    # to the seen dict with this list as its value
                    path_to_friend.append(friend)
                    seen[friend] = path_to_friend 
        
        # return the seen dict
        # each key is a different user and each associated value is a list
        # which includes the paths to that user's friends in the graph
        return seen


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
