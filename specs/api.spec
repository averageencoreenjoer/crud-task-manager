# Task Manager API

## Task Lifecycle
* Create a task with title "Learn Gauge" and description "Write tests"
* The response status should be "201"
* The response object should have a "title" field equal to "Learn Gauge"
* Save the "uuid" from the response as "task_uuid"
* Get the task using the saved "task_uuid"
* The response status should be "200"
* Request the list of all tasks
* The response should have at least "1" task(s)
* Get the first task from the list response
* The task should have a "status" field equal to "создано"
* Update the task with the saved "task_uuid", setting the status to "в работе"
* The response status should be "200"
* The response object should have a "status" field equal to "в работе"
* Delete the task with the saved "task_uuid"
* The response status should be "204"
* Getting the task with the saved "task_uuid" again should return status "404"

## Error Handling
* Requesting a task with a random UUID should return status "404"
* Attempting to create a task without a title should return status "422"