import uuid
import httpx
from getgauge.python import step, DataStoreFactory

BASE_URL = "http://127.0.0.1:8000"
client = httpx.Client(base_url=BASE_URL)
store = DataStoreFactory.scenario_data_store()


@step("Create a task with title <title> and description <description>")
def create_task(title, description):
    response = client.post(
        "/api/v1/tasks/", json={"title": title, "description": description}
    )
    store.put("response", response)


@step("The response status should be <expected_code>")
def assert_status_code(expected_code):
    response = store.get("response")
    assert response.status_code == int(expected_code)


@step("The response object should have a <key> field equal to <value>")
def assert_json_object_field(key, value):
    response_json = store.get("response").json()
    assert isinstance(response_json, dict)
    assert str(response_json.get(key)) == value


@step("Save the <key> from the response as <alias>")
def store_value_from_response(key, alias):
    response_json = store.get("response").json()
    store.put(alias, response_json.get(key))


@step("Get the task using the saved <alias>")
def get_task_by_stored_uuid(alias):
    task_uuid = store.get(alias)
    response = client.get(f"/api/v1/tasks/{task_uuid}")
    store.put("response", response)


@step("Update the task with the saved <alias>, setting the status to <status>")
def update_task_status(alias, status):
    task_uuid = store.get(alias)
    response = client.put(f"/api/v1/tasks/{task_uuid}", json={"status": status})
    store.put("response", response)


@step("Delete the task with the saved <alias>")
def delete_task_by_stored_uuid(alias):
    task_uuid = store.get(alias)
    response = client.delete(f"/api/v1/tasks/{task_uuid}")
    store.put("response", response)


@step(
    "Getting the task with the saved <alias> again should return status <expected_code>"
)
def re_get_task_and_fail(alias, expected_code):
    task_uuid = store.get(alias)
    response = client.get(f"/api/v1/tasks/{task_uuid}")
    assert response.status_code == int(expected_code)


@step("Requesting a task with a random UUID should return status <expected_code>")
def request_random_uuid(expected_code):
    random_uuid = uuid.uuid4()
    response = client.get(f"/api/v1/tasks/{random_uuid}")
    assert response.status_code == int(expected_code)


@step(
    "Attempting to create a task without a title should return status <expected_code>"
)
def create_task_no_title(expected_code):
    response = client.post("/api/v1/tasks/", json={"description": "some description"})
    assert response.status_code == int(expected_code)


@step("Request the list of all tasks")
def request_list_of_all_tasks():
    response = client.get("/api/v1/tasks/")
    store.put("response", response)
    assert response.status_code == 200


@step("The response should have at least <count> task(s)")
def response_should_have_at_least(count):
    response_json = store.get("response").json()
    assert isinstance(response_json, list)
    assert len(response_json) >= int(count)


@step("Get the first task from the list response")
def get_first_task_from_list():
    response_json = store.get("response").json()
    assert isinstance(response_json, list)
    assert (
        len(response_json) > 0
    ), "Список задач пуст, невозможно получить первый элемент"
    store.put("current_task", response_json[0])


@step("The task should have a <key> field equal to <value>")
def assert_task_field(key, value):
    task = store.get("current_task")
    assert task is not None, "Предыдущий шаг не сохранил текущую задачу"
    assert str(task.get(key)) == value
