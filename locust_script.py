from locust import TaskSet, task, HttpLocust


class ConverterTasks(TaskSet):
    @task(1)
    def api1(self):
        self.client.get('/posts')
    
    @task(2)
    def api2(self):
        self.client.get('/todos/1')

class ApiUser(HttpLocust):
    task_set = ConverterTasks
    min_wait = 1000
    max_wait = 3000
