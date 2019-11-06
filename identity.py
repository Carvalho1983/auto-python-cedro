from locust import TaskSet, task, HttpLocust


class ConverterTasks(TaskSet):

    @task(1)
    def login(l):
        payload = {"user_name": "##", "password": "Toor@2018"}
        l.client.post("/auth/users/login", json=payload)

class ApiUser(HttpLocust):
    task_set = ConverterTasks
    min_wait = 1000
    max_wait = 5000
