This is example implementation about jwt in robyn with driver db postgresql

## Usage
create database connection
```
docker-compose up -d db
```
running app service
```
docker-compose up -d app
```

### Register User
- Method: POST
- Endpoint: `/api/v1/user/register`
- Header:
    - Content-Type: `application/json`
    - Accept: `application/json`
- Body :
```json
{
    "id": "int",
    "name": "string",
    "email": "string",
    "password": "string",
}
```

### Login User
- Method: POST
- Endpoint: `/api/v1/user/login`
- Header:
    - Content-Type: `application/json`
    - Accept: `application/json`
- Body :
```json
{
    "email": "string",
    "password": "string",
}
```

### Create Todo
- Method: POST
- Endpoint: `/api/v1/todo/create`
- Header:
    - Content-Type: `application/json`
    - Accept: `application/json`
- Body :
```json
{
    "id": "int",
    "name": "string",
    "desc": "string",
    "time": "time"
}
```

### Update Todo
- Method: PUT
- Endpoint: `/api/v1/todo/update/{id}`
- Header:
    - Content-Type: `application/json`
    - Accept: `application/json`
- Body :
```json
{
    "id": "int",
    "name": "string",
    "desc": "string",
    "time": "time"
}
```

### Get Todo
- Method: GET
- Endpoint: `/api/v1/todo/find`
- Header:
    - Content-Type: `application/json`
    - Accept: `application/json`
- Response :
```json
{
    "status_code": "int",
    "description": "string",
    "data": [
        {
            "id": "int",
            "name": "string",
            "desc": "string",
            "time": "time"
        }
    ],
}
```

### Get Todo by ID
- Method: GET
- Endpoint: `/api/v1/todo/find/{id}`
- Header:
    - Content-Type: `application/json`
    - Accept: `application/json`
- Response :

```json
{
    "status_code": "int",
    "description": "string",
    "data": 
        {
            "id": "int",
            "name": "string",
            "desc": "string",
            "time": "time"
        }
}
```

### Delete Todo by ID
- Method: DELETE
- Endpoint: `/api/v1/todo/delete/{id}`
- Header:
    - Content-Type: `application/json`
    - Accept: `application/json`
- Response :

```json
{
    "status_code": "int",
    "description": "string",
}
```