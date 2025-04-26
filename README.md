# Forma API

A Django REST framework API with versioning support.

## API Versioning

This project implements URL-based versioning for the API. The API is accessible at:

- `/api/v1/` - Version 1 of the API
- `/api/v2/` - Version 2 of the API

### Version Differences

- **Version 1**: Basic API that includes only essential fields (id, name, description)
- **Version 2**: Enhanced API that includes all fields, including timestamps (created_at, updated_at)

## Project Structure

The project follows a structured approach to versioning:

```
forma/
  api/
    __init__.py
    urls.py           # Main API URLs that include versioned URLs
    v1/
      __init__.py
      serializers.py  # V1 serializers
      urls.py         # V1 URL patterns
      views.py        # V1 views
    v2/
      __init__.py
      serializers.py  # V2 serializers
      urls.py         # V2 URL patterns
      views.py        # V2 views
```

## Setup and Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```
   python manage.py migrate
   ```
4. Run the development server:
   ```
   python manage.py runserver
   ```

## API Documentation

API documentation is available at `/docs/` when the server is running.

## Testing the API

You can test the API using the provided test script:

```
python test_api.py
```

Make sure the Django server is running before executing the test script.

## Adding New Versions

To add a new API version:

1. Create a new directory in `forma/api/` (e.g., `v3/`)
2. Create the necessary files (serializers.py, views.py, urls.py)
3. Update `forma/api/urls.py` to include the new version