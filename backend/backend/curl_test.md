### Obtain a toke
```
curl -X POST -d "username=<USERNAME>&password=<PASSWORD>" http://127.0.0.1:8000/user/get-token/
```

### Create a category
```
curl -X POST -H "Authorization: Token <TOKEN>" -H "Content-Type: application/json" -d '{"name":"hello"}' http://127.0.0.1:8000/category/create/
```

### Get a category
```
curl -X GET -H "Authorization: Token <TOKEN>" -H "Content-Type: application/json" http://127.0.0.1:8000/category/1/
```

### Update a category
```
curl -X PUT -H "Authorization: Token <TOKEN>" -H "Content-Type: application/json" -d '{"name":"Updated"}' http://127.0.0.1:8000/category/1/update/
```

### Delete a category
```
curl -X DELETE -H "Authorization: Token <TOKEN>" -H "Content-Type: application/json" http://127.0.0.1:8000/category/1/delete/
```


### Note
Careful: Url should ends with /
Save your token to localStorage