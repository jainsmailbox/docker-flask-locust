from locust import HttpLocust, TaskSet, between

def index(1):
    l.client.get("/")

class UserBehaviour(TaskSet):
    tasks = {index: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(5.0, 9.0)
    

