from locust import TaskSet, task, HttpLocust


class ConverterTasks(TaskSet):

    @task(1)
    def process_instances(l):
        payload = {
            "id": "a2d68ca4-fc00-11e9-ae49-0242ac110002",
            "url": "http://localhost:8080/flowable-task/process-api/runtime/process-instances/a2d68ca4-fc00-11e9-ae49-0242ac110002",
            "name": "null",
            "businessKey": "jadmjr",
            "suspended": "false",
            "ended": "false",
            "processDefinitionId": "CadastroGE:1:91c7721f-fbff-11e9-ae49-0242ac110002",
            "processDefinitionUrl": "http://localhost:8080/flowable-task/process-api/repository/process-definitions/CadastroGE:1:91c7721f-fbff-11e9-ae49-0242ac110002",
            "processDefinitionName": "Cadastro GE",
            "processDefinitionDescription": "null",
            "activityId": "null",
            "startUserId": "admin",
            "startTime": "2019-10-31T17:05:27.368Z",
            "variables": [],
            "callbackId": "null",
            "callbackType": "null",
            "tenantId": "",
            "completed": "false"
        }
        l.client.post(
            "/flowable-task/process-api/runtime/process-instances", json=payload)

class ApiUser(HttpLocust):
    task_set = ConverterTasks
    min_wait = 1000
    max_wait = 3000
