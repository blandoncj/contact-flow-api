# Contact Flow API

![Python](https://img.shields.io/badge/Python-3.12-%233776AB?logo=python&logoColor=%233776AB)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-%23009688?logo=fastapi&logoColor=%23009688)
![MySQL](https://img.shields.io/badge/MySQL-8.0-%234479A1?logo=mysql&logoColor=%234479A1)
![JWT](https://img.shields.io/badge/JWT-Authentication-%23323330?logo=jsonwebtokens&logoColor=%23323330)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![OAuth2](https://img.shields.io/badge/OAuth2-F4474F)

API for managing contacts, enabling users to authenticate and perform CRUD operations
on their contact list.

## Table of Contents

- [Contact Flow API](#contact-flow-api)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [License](#license)
  - [Author](#author)
  - [Contributing](#contributing)

## Features

- **User Authentication**: Users can register, login and obtain a JWT token to
authenticate themselves.
- **CRUD Operations**: Users can create, read, update and delete contacts.
- **Security**: The API uses JWT for authentication and OAuth2 for authorization.
- **Dockerized**: The API is containerized using Docker.
- **API Documentation**: The API is documented using Swagger UI.

## Prerequisites

- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/)

## Setup

1. Clone the repository:

```bash
git clone https://github.com/blandoncj/ContactFlow-API.git 
```

2. Change directory:

```bash
cd ContactFlow-API
```

3. Create a `.env` file in the root directory and add the following environment variables:

```bash
API_KEY=your_api_key
SECRET_KEY=your_secret_key
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_ROOT_PASSWORD=your_mysql_root_password
MYSQL_HOST=your_mysql_host # docker-compose service hostname (e.g contact_flow)
MYSQL_PORT=your_mysql_port # docker-compose service port (e.g 3306)
MYSQL_DATABASE=your_mysql_database
```

4. Build and run the Docker containers:
  
```bash
docker-compose build
docker-compose up -d
```

> [!NOTE]
> The API will be available at <http://localhost:8000/docs> and the database will be available at <http://localhost:8080> (adminer).

5. Create the database tables:
  
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(50) NOT NULL,
    username VARCHAR(15) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50),
    email VARCHAR(50),
    is_favorite BOOLEAN DEFAULT FALSE,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE phones (
  id INT AUTO_INCREMENT PRIMARY KEY,
  number VARCHAR(20) NOT NULL,
  contact_id INT NOT NULL,
  FOREIGN KEY (contact_id) REFERENCES contacts(id)
)
```

## License

> This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Made with ❤️  by [blandoncj](https://github.com/blandoncj)

## Contributing

Contributions are welcome. Please open a issue or create a pull request to contribute.
