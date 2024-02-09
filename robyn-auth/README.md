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