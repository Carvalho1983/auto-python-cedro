print("hello world")

id = ""
task_id = ""

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
response = client.post(
    "/flowable-task/process-api/runtime/process-instances", json=payload)

json_response_dict = response.json()
id = json_response_dict['id']

print("ID: %s" % (id))
