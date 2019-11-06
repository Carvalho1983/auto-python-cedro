from locust import TaskSet, task, HttpLocust

class ConverterTasks(TaskSet):

    @task(1)
    def api_categorias(self):
        self.client.get('http://10.1.9.163:8080/categorias/1')

class ApiUser(HttpLocust):
    task_set = ConverterTasks
    min_wait = 1000
    max_wait = 3000
