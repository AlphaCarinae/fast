## Scope

  The `main.py` is a a python-based graphQL API that will respond to the following query structure. It has been created using on `FastAPI` and `strawberry`.

  ```
  query {
  person {
    email
    name
    address {
      number
      street
      city
      state
    }
  }
}
  ```

### Starting the service

the API can be started by running the following in the bash prompt.

```
uvicorn main:app --reload
```

_Notes:_

- the test file is not finished and needs better implementation.

## Requirements

The required libraries have been included in the `requirements.txt` file.