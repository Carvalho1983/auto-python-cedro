from locust import TaskSet, task, HttpLocust

id = ""
task_id = ""


class ConverterTasks(TaskSet):

    @task(1)
    def process_instances(self):

        global id

        payload = {
            "id": "a433fb2c-fc1a-11e9-99c3-0242ac110003",
            "url": "http://localhost:8080/flowable-task/process-api/runtime/process-instances/a433fb2c-fc1a-11e9-99c3-0242ac110003",
            "name": "null",
            "businessKey": "null",
            "suspended": "false",
            "ended": "false",
            "processDefinitionId": "CadastroGE:3:ae8a09b8-fc17-11e9-99c3-0242ac110003",
            "processDefinitionUrl": "http://localhost:8080/flowable-task/process-api/repository/process-definitions/CadastroGE:3:ae8a09b8-fc17-11e9-99c3-0242ac110003",
            "processDefinitionName": "Cadastro GE",
            "processDefinitionDescription": "null",
            "activityId": "null",
            "startUserId": "admin",
            "startTime": "2019-10-31T20:11:36.573Z",
            "variables": [],
            "callbackId": "null",
            "callbackType": "null",
            "tenantId": "",
            "completed": "false"
        }
        response = self.client.post(
            "/flowable-task/process-api/runtime/process-instances", json=payload)

        json_response_dict = response.json()
        id = json_response_dict['id']

    @task(2)
    def tarefas(self):

        global task_id

        payload = {"processInstanceId": id}
        response = self.client.post(
            "/flowable-task/process-api/query/tasks", json=payload)

        json_response_dict = response.json()
        task_id = json_response_dict['data'][0]["id"]

    @task(3)
    def informar_cpf(self):

        global task_id

        endpoint = "/flowable-task/process-api/runtime/tasks/"+task_id

        payload = {"action": "complete", "variables": [
            {"name": "cpf", "value": "09426181652"}]}
        response = self.client.post(endpoint, json=payload)

        task_id = ""
        endpoint = ""

    

        
class ApiUser(HttpLocust):
    task_set = ConverterTasks
    min_wait = 1000
    max_wait = 3000
