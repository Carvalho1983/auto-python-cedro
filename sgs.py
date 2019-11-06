from locust import TaskSet, task, HttpLocust


class ConverterTasks(TaskSet):

    @task(1)
    def login(l):
        payload = {"user_name": "##", "password": "Toor@2018"}
        l.client.post("/auth/users/login", json=payload)

    @task(2)
    def api2(self):
        self.client.get('/categorias/2')

class ApiUser(HttpLocust):
    task_set = ConverterTasks
    min_wait = 1000
    max_wait = 3000
