
### README.txt for Little Lemon Restaurant API

#### Project Title: Little Lemon Restaurant Booking API

#### Overview
This API allows users to book tables at the Little Lemon restaurant. It uses Django REST Framework for building the API endpoints, and integrates with JWT-based authentication to ensure secure access.

#### API Endpoints

1. **Token Authentication**  
   - **POST /api/token/**  
   - **Purpose:** Obtain JWT access and refresh tokens.
   - **Request Body:**
   ```json
   {
     "username": "your_username",
     "password": "your_password"
   }
   ```

2. **Booking API**  
   - **GET /api/bookings/**  
     - **Purpose:** Retrieve a list of all bookings.
     - **Headers:**  
       `Authorization: Bearer <access_token>`
   
   - **POST /api/bookings/**  
     - **Purpose:** Create a new booking.
     - **Request Body:**
     ```json
     {
       "date": "2025-04-30", 
       "time": "19:00", 
       "table": 1, 
       "user": 1
     }
     ```
     - **Headers:**  
       `Authorization: Bearer <access_token>`

3. **Menu Item API**  
   - **GET /api/menu/**  
     - **Purpose:** Retrieve a list of all menu items.
     - **Headers:**  
       `Authorization: Bearer <access_token>`

#### Running the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url.git
   cd your-repo-directory
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

5. Access the API at:
   - `http://127.0.0.1:8000/api/`

#### Testing the API
You can test the API using the Thunder Client in VS Code, Postman, or Insomnia by following these steps:

1. Obtain a JWT token using the **POST /api/token/** endpoint.
2. Use the `access` token in the `Authorization` header to make requests to other endpoints like `/api/bookings/` and `/api/menu/`.

---

### GitHub Repository
[Your GitHub Repository URL]

