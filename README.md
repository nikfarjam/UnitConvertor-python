# UnitConvertor-python
An example of AWS serverless RESTful API by Python

### Install

This project use [Pipenv](https://pypi.org/project/pipenv/) to manage dependencies and environment.
For **production** installation

   ``` pipenv install ``` 

   ``` pipenv shell ```

For **development** and **test**

   ``` pipenv install --dev ```

   ``` pipenv shell ```

### Tests

1. **Integration Test**
   
   ``` >python3 ./test/integration_test.py ```

2. **Unit Tests**
   
   ``` >python3 -m pytest ./test/test_*.py ```

