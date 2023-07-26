# IJQ
## Overview
From [stackoverflow](https://stackoverflow.com/questions/27238411/display-curl-output-in-readable-json-format-in-unix-shell-script) you can find that tools like jq or json_pp will beatify output
```bash
curl https://petstore.swagger.io/v2/pet/1 | jq
```
but if we add `-i` (Include the HTTP response headers) option in curl command then command failed
```bash
$ curl https://petstore.swagger.io/v2/pet/1 -i | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   138    0   138    0     0    100      0 --:--:--  0:00:01 --:--:--   100
parse error: Invalid numeric literal at line 1, column 7
```
How to prevent failure?
Use ijq!

## Install
```bash
git clone git@github.com:1frag/ijq.git
cd ijq
pip install -e .
```

## Usage
```bash
curl -i https://petstore.swagger.io/v2/pet/1 | ijq
```
Output:
```text
HTTP/2 200 
date: Wed, 26 Jul 2023 16:35:50 GMT
content-type: application/json
access-control-allow-origin: *
access-control-allow-methods: GET, POST, DELETE, PUT
access-control-allow-headers: Content-Type, api_key, Authorization
server: Jetty(9.2.9.v20150224)
{
    "category": {
        "id": 1,
        "name": "string"
    },
    "id": 1,
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "status": "available",
    "tags": [
        {
            "id": 1,
            "name": "string"
        }
    ]
}
```
