# TaskManager Django Backend

A lightweight backend service for managing personal tasks. Each task is tied to a user and only visible to that user.

## Features

- Django REST API (token-based authentication)
- GraphQL endpoint (with authentication)
- Each task: title, status, created_at, assigned_to

## Setup

```bash
git clone https://github.com/AnamZ78/taskmanager.git

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

## API Endpoints

- Get Token: `POST /api-token-auth/`
- List/Create Tasks: `GET/POST /tasks/`
- Update/Delete Task: `PUT/DELETE /tasks/<id>/`
- GraphQL: `POST /graphql/`

**All endpoints require:**  
`Authorization: Token <your_token>`

## Postman Collection

See the provided Postman collection for ready-to-use API requests.
{
	"info": {
		"_postman_id": "33b2c369-3a38-4c33-99c6-9f6a4e5ed1de",
		"name": "TaskManager API",
		"description": "REST and GraphQL API for personal task management",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "47708131",
		"_collection_link": "https://anam-z-6343435.postman.co/workspace/2a6d8d94-912b-49ca-8512-9e36665d9101/collection/47708131-33b2c369-3a38-4c33-99c6-9f6a4e5ed1de?action=share&source=collection_link&creator=47708131"
	},
	"item": [
		{
			"name": "Get Auth Token",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"username\": \"{{username}}\",\n  \"password\": \"{{password}}\"\n}"
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api-token-auth/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api-token-auth",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "List Tasks",
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Authorization",
						"value": "Token {{token}}"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/tasks/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"tasks",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Create Task",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Authorization",
						"value": "Token {{token}}"
					},
					{
						"key": "Content-Type",
						"value": "application/json"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"title\": \"My new task\",\n  \"status\": \"pending\"\n}"
				},
				"url": {
					"raw": "http://127.0.0.1:8000/tasks/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"tasks",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Update Task",
			"request": {
				"method": "PUT",
				"header": [
					{
						"key": "Authorization",
						"value": "Token {{token}}"
					},
					{
						"key": "Content-Type",
						"value": "application/json"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"title\": \"Updated title\",\n  \"status\": \"completed\"\n}"
				},
				"url": {
					"raw": "http://127.0.0.1:8000/tasks/{{task_id}}/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"tasks",
						"{{task_id}}",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Delete Task",
			"request": {
				"method": "DELETE",
				"header": [
					{
						"key": "Authorization",
						"value": "Token {{token}}"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/tasks/{{task_id}}/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"tasks",
						"{{task_id}}",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "GraphQL List Tasks",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Authorization",
						"value": "Token {{token}}"
					},
					{
						"key": "Content-Type",
						"value": "application/json"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"query\": \"query { allTasks { id title status createdAt assignedTo { id username } } }\"\n}"
				},
				"url": {
					"raw": "http://127.0.0.1:8000/graphql/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"graphql",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "GraphQL Create Task",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Authorization",
						"value": "Token {{token}}"
					},
					{
						"key": "Content-Type",
						"value": "application/json"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"query\": \"mutation { createTask(title: \\\"GraphQL Task\\\", status: \\\"pending\\\") { task { id title status } } }\"\n}"
				},
				"url": {
					"raw": "http://127.0.0.1:8000/graphql/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"graphql",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "GraphQL Update Task",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Authorization",
						"value": "Token {{token}}"
					},
					{
						"key": "Content-Type",
						"value": "application/json"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"query\": \"mutation { updateTask(id: {{task_id}}, title: \\\"Updated via GraphQL\\\", status: \\\"completed\\\") { task { id title status } } }\"\n}"
				},
				"url": {
					"raw": "http://127.0.0.1:8000/graphql/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"graphql",
						""
					]
				}
			},
			"response": []
		}
	],
	"variable": [
		{
			"key": "username",
			"value": "your_username"
		},
		{
			"key": "password",
			"value": "your_password"
		},
		{
			"key": "token",
			"value": ""
		},
		{
			"key": "task_id",
			"value": "1"
		}
	]
}

