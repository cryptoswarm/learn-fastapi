# What is FastAPI

FastAPI is a modern, high-performance web framework for building APIs with Python based on standard type hints. It has the following key features:

## Fast to run:

It offers very high performance, on par with NodeJS and Go, thanks to Starlette and pydantic.

## Fast to code:

It allows for significant increases in development speed.

## Reduced number of bugs:

It reduces the possibility for human-induced errors.

## Intuitive:

It offers great editor support, with completion everywhere and less time debugging.

## Straightforward:

It’s designed to be uncomplicated to use and learn, so you can spend less time reading documentation.

## Short:

It minimizes code duplication.

## Robust:

It provides production-ready code with automatic interactive documentation.

## Standards-based:

It’s based on the open standards for APIs, OpenAPI and JSON Schema.

The framework is designed to optimize your developer experience so that you can write simple code to build production-ready APIs with best practices by default.

# Run application

## Clone the repo

```git
git clone <repo url>
```

## Create a virtual environement

1. Create

```python
python3.12 -m venv venv
```

2. Activate

```python
source venv/bin/active
```

3. Install dependencies

- Install dependencies from `requirements.txt`

```python
pip install -r requirements
```

- Install the following 2 libraries:

```python
pip install fastapi uvicorn[standard]
```

## Run

```python
uvicorn main:app --reload
```
