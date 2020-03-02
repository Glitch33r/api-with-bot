import json
import random as rnd
import requests
import yaml
import string

POST_DATA = [
    {'title': f'Random Title {i}', 'text': f'Random Desc {i}', 'likes': 0} for i in range(100)
]


class AutomatedBot:
    config_data = {}
    users = []

    def __init__(self, config_file, url):
        self.config_file = config_file
        self.api_base_url = url

    def get_config(self):
        """Read data from config file"""
        with open(self.config_file, 'r') as stream:
            self.config_data.update(yaml.load(stream, Loader=yaml.FullLoader))

    def request(self, part_url, payload=None, token=None, method='POST'):
        """Makes HTTP POST request"""
        if token is not None:
            res = requests.request(method, self.api_base_url + part_url, data=payload,
                                   headers={'Authorization': f'Token {token}'})
        else:
            res = requests.post(self.api_base_url + part_url, data=payload)

        return res.status_code, res.content

    def create_post(self):
        """Create random number user posts"""
        result = []
        if 'max_posts_per_user' in self.config_data.keys():
            for user in self.users:
                rand_count = rnd.randint(0, self.config_data['max_posts_per_user'])
                for i in range(rand_count):
                    payload = rnd.choice(POST_DATA)
                    self.request('post/create/', payload, user['Token'])
                    result.append(
                        f'Post title={payload["title"]} text={payload["text"]} user={user["email"]} created')
        else:
            result.append('Sorry, you forget set max number of likes per user.')

        return result

    def like_posts(self):
        """Put random number likes for posts"""
        result = []
        if 'max_likes_per_user' in self.config_data.keys():
            posts_id = self.get_id_of_posts()
            for user in self.users:
                rand_likes = rnd.randint(0, self.config_data['max_likes_per_user'])
                for _ in range(rand_likes):
                    rand_post_id = rnd.choice(posts_id)
                    self.request('post/' + str(rand_post_id) + '/reaction/like/', None, user['Token'], 'PATCH')
                    result.append(
                        f'Post id={rand_post_id} liked by user={user["email"]}')
        else:
            result.append('Sorry, you forget set max number of posts per user.')

    def get_id_of_posts(self):
        """Getting posts Id for further liking"""
        res = requests.get(self.api_base_url + 'post/')
        ids = []
        for post in json.loads(res.content):
            ids.append(post['id'])

        return ids

    def signup(self):
        """Sign up users"""
        result = []
        if 'users' in self.config_data.keys():
            result.append(f'Sign up {self.config_data["users"]} users')
            for i in range(self.config_data['users']):
                st = ''
                for i in range(7):
                    st += rnd.choice(string.ascii_letters + string.digits)

                payload = {
                    'password': f'Q2w3e4r{i}',
                    'email': f'{st}{i}@qwerty.com',
                }
                self.request('user/create/', payload)
                token = self.get_user_token(payload)
                payload.update({'Token': token})
                self.users.append(payload)
                result.append(
                    f'User login={payload["email"]} password={payload["password"]} token={payload["Token"]} registered')
        else:
            result.append('Sorry, you forget set number of users.')

        return result

    def get_user_token(self, user):
        """Login with user for creation post"""
        status, content = self.request('user/token/', user)
        return json.loads(content)['token']
