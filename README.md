# IJQ
## Usage
Type:
```bash
python setup.py install
curl -iX GET "https://petstore.swagger.io/v2/pet/1" -H  "accept: application/json" | ijq
```
to get:
```text
HTTP/2 200 
date: Thu, 11 Mar 2021 12:49:12 GMT
content-type: application/json
access-control-allow-origin: *
access-control-allow-methods: GET, POST, DELETE, PUT
access-control-allow-headers: Content-Type, api_key, Authorization
server: Jetty(9.2.9.v20150224)
{
    "category": {
        "id": 1,
        "name": "String"
    },
    "id": 1,
    "name": "String",
    "photoUrls": [
        "string"
    ],
    "status": "available",
    "tags": [
        {
            "id": 10,
            "name": "String"
        }
    ]
}

```
instead of:
```text
HTTP/2 200 
date: Thu, 11 Mar 2021 12:52:16 GMT
content-type: application/json
access-control-allow-origin: *
access-control-allow-methods: GET, POST, DELETE, PUT
access-control-allow-headers: Content-Type, api_key, Authorization
server: Jetty(9.2.9.v20150224)

{"id":1,"category":{"id":0},"name":"Tica","photoUrls":[],"tags":[],"status":"available"}
```