# iCRUD

## Project Overview
This project is a **lightweight ORM and dynamic CRUD API** built using **Flask** and **MySQL**.  
It automates CRUD operations for any model dynamically, without manually writing routes for each table.  
Designed for flexibility, reusability, and simplicity in API development.

## Project Structure

```
├── src/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── database.py          # Database configuration
│   ├── core/
│   │   ├── __init__.py
│   │   ├── SQLBuilder.py        # Core ORM query builder
│   │   ├── Model.py             # Base Model class
│   │   └── decorators.py        # Dynamic model loading decorator
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── crudy.py             # CRUD controller functions
│   ├── models/
│   │   ├── __init__.py
│   │   ├── Url.py               # URL model example
│   │   └── User.py              # User model example
│   └── tests/
│       ├── __init__.py
│       └── test_model.py        # Unit tests
├── requirements.txt
└── README.md
```

## Installation

### Prerequisites

- Python 3.7+
- MySQL 5.7+
- pip

### Requirements

Create a `requirements.txt` file with the following dependencies:

```
Flask==3.0.0
mysql-connector-python==8.2.0
inflect==7.0.0
Hashids
```

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/icrud.git
cd icrud
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure database connection in `src/config/database.py`:
```python
host = "127.0.0.1"
port = 3306
user = "root"
password = "your_password"
database = "your_database"
```

4. Create your database:
```sql
CREATE DATABASE bitly;

-- Create urls table
CREATE TABLE urls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(300) NOT NULL,
    short_url VARCHAR(50) NOT NULL,
    clicks INT DEFAULT 0,
    status ENUM('Active', 'Inactive') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_name VARCHAR(150) NOT NULL,
    quantity INT DEFAULT 0,
    price DECIMAL(10,2) DEFAULT 0.00,
    status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

5. Run the Flask application:
```bash
flask --app src.index run --debug
```

The application will start on `http://127.0.0.1:5000`

## Usage

### Defining a Model

Create a new model by extending the `Model` class. Here's the example from the project:

**Url Model** (`src/models/Url.py`):
```python
from src.core.Model import Model

class Url(Model):
    table_name = "urls"
    slug_column = "status"
    
    columns = {
        "id": {
            "key": "id",
            "type": "int",
            "primary": True
        },
        "url": {
            "key": "url",
            "type": "varchar",
            "length": 300
        },
        "short_url": {
            "key": "short_url",
            "type": "varchar",
            "length": 50
        },
        "count": {
            "key": "clicks",  # Maps to 'clicks' column in database
            "type": "int",
        },
        "status": {
            "key": "status",
            "type": "enum",
            "options": ["Active", "Inactive"]
        },
    }
```

**User Model** (`src/models/User.py`):
```python
from src.core.Model import Model

class User(Model):
    table_name = "users"
    
    columns = {
        "id": {
            "key": "id",
            "type": "int",
            "primary": True
        },
        "user_id": {
            "key": "user_id",
            "type": "int"
        },
        "product_name": {
            "key": "product_name",
            "type": "varchar",
            "length": 150
        },
        "quantity": {
            "key": "quantity",
            "type": "int"
        },
        "price": {
            "key": "price",
            "type": "decimal(10,2)"
        },
        "status": {
            "key": "status",
            "type": "enum",
            "options": ["Pending", "Completed", "Cancelled"]
        },
        "created_at": {
            "key": "created_at",
            "type": "datetime"
        },
        "modified_at": {
            "key": "modified_at",
            "type": "datetime"
        }
    }
```

### CRUD Operations

#### Create
```python
from src.models.Url import Url

# Create a new record
url_id = Url.create(
    url="https://example.com",
    short_url="ex123",
    count=0,
    status="Active"
)
print(f"Created URL with ID: {url_id}")
```

#### Read All
```python
# Get all records
urls = Url.all()

# With pagination
urls = Url.all(page=1, limit=10)

# With filtering (OData-style)
urls = Url.all(filter="count eq 10 and status eq Active")
```

#### Find by ID
```python
# Find single record by slug_column value
url = Url.find("Active")  # Using slug_column defined in model
```

#### Filtering Operators

The framework supports OData-style filtering:

| Operator | SQL Equivalent | Example | Description |
|----------|----------------|---------|-------------|
| `eq` | `=` | `status eq Active` | Equal to |
| `ne` | `!=` | `status ne Inactive` | Not equal to |
| `gt` | `>` | `price gt 100` | Greater than |
| `lt` | `<` | `price lt 1000` | Less than |
| `ge` | `>=` | `quantity ge 10` | Greater than or equal to |
| `le` | `<=` | `quantity le 50` | Less than or equal to |

Combine with logical operators:
```python
# AND condition
filter = "price gt 100 and status eq Active"

# OR condition
filter = "category eq Electronics or category eq Books"
```

### Query Parameters Reference

| Parameter | Type | Default | Description | Example |
|-----------|------|---------|-------------|---------|
| `page` | integer | 1 | Page number for pagination | `page=2` |
| `limit` | integer | 20 | Number of records per page | `limit=10` |
| `filter` | string | '' | OData-style filter expression | `filter=status eq Active` |

**How Pagination Works:**

| Page | Limit | SQL Generated | Records Returned |
|------|-------|---------------|------------------|
| 1 | 10 | `LIMIT 10 OFFSET 0` | Records 1-10 |
| 2 | 10 | `LIMIT 10 OFFSET 10` | Records 11-20 |
| 3 | 10 | `LIMIT 10 OFFSET 20` | Records 21-30 |
| 1 | 20 | `LIMIT 20 OFFSET 0` | Records 1-20 |
| 5 | 5 | `LIMIT 5 OFFSET 20` | Records 21-25 |

**Formula**: `OFFSET = (page - 1) × limit`

**Example API Calls:**

```bash
# Get first 10 records
GET /api/urls?page=1&limit=10

# Get records 11-20
GET /api/urls?page=2&limit=10

# Get active URLs with pagination
GET /api/urls?page=1&limit=10&filter=status eq Active

# Get URLs with more than 100 clicks
GET /api/urls?filter=count gt 100

# Complex filter with pagination
GET /api/urls?page=1&limit=5&filter=count gt 50 and status eq Active
```

### Flask Routes with Dynamic Model Loading

Use the `@model_from_path` decorator for automatic model resolution:

```python
from flask import Flask
from src.core.decorators import model_from_path
from src.controllers.crudy import create_item, fetch_list, fetch_detail

app = Flask(__name__)

@app.route('/api/<table_name>', methods=['POST'])
@model_from_path
def create(Model):
    return create_item(Model)

@app.route('/api/<table_name>', methods=['GET'])
@model_from_path
def list_items(Model):
    return fetch_list(Model)

@app.route('/api/<table_name>/<id>', methods=['GET'])
@model_from_path
def detail(Model, id):
    return fetch_detail(Model, id)

if __name__ == '__main__':
    app.run(debug=True)
```

**How it works:**
- The decorator converts `table_name` from plural to singular using the `inflect` library
- Converts snake_case to PascalCase (e.g., `urls` → `Url`)
- Dynamically imports the model from `src.models.{ModelName}`
- Passes the model class to your controller function

### API Examples

**Create a URL:**
```bash
curl -X POST http://localhost:5000/api/urls \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "short_url": "ex123"}'
```

**Get all URLs with pagination:**
```bash
curl "http://localhost:5000/api/urls?page=1&limit=10"
```

**Filter URLs:**
```bash
curl "http://localhost:5000/api/urls?filter=status eq Active and count gt 100"
```

**Get single URL:**
```bash
curl http://localhost:5000/api/urls/1
```

## Lifecycle Hooks

Override these methods in your model for custom behavior:

```python
class Url(Model):
    def beforeInsert(self):
        print("About to insert URL")
    
    def afterInsert(self):
        print("URL inserted successfully")
    
    def beforeUpdate(self):
        print("About to update URL")
    
    def afterUpdate(self):
        print("URL updated successfully")
    
    def beforeDelete(self):
        print("About to delete URL")
    
    def afterDelete(self):
        print("URL deleted successfully")
```

> **Note**: Lifecycle hooks framework is implemented but update and delete operations are still in development.

## Configuration

### Timestamps

Models automatically include `created_at` and `modified_at` timestamps. Disable by setting:

```python
class Product(Model):
    time_stamps = False
```

### Custom Column Mapping

Map model attributes to different database column names:

```python
columns = {
    "count": {           # Model attribute name
        "key": "clicks",  # Actual database column name
        "type": "int"
    }
}
```

This is used in the Url model where the `count` attribute maps to the `clicks` column in the database.



