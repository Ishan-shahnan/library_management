# 📚 Library Management System API

A simple Library Management System API built with Django REST Framework for managing books, authors, members, and borrowing operations.

## 🚀 Features

- **Books Management**: Add, view, update, and delete books
- **Authors Management**: Manage book authors
- **Members Management**: Manage library members
- **Borrowing System**: Borrow and return books
- **JWT Authentication**: User login and registration
- **Role-based Permissions**: Admin and member access control
- **API Documentation**: Interactive Swagger documentation

## 🛠️ Technology Stack

- **Backend**: Django 5.2.5, Django REST Framework
- **Database**: PostgreSQL (Production), SQLite (Development)
- **Authentication**: JWT with Djoser
- **Media Storage**: Cloudinary
- **Static Files**: WhiteNoise
- **Deployment**: Vercel
- **Documentation**: drf-yasg (Swagger)

## 📋 API Endpoints

### Authentication
```
POST /auth/users/        # Register new user
POST /auth/jwt/create/   # Get access & refresh tokens
POST /auth/jwt/refresh/  # Refresh access token
POST /auth/jwt/verify/   # Verify token
```

### Core Resources
```
GET/POST /api/books/             # List/Create books
GET/PUT/DELETE /api/books/{id}/  # Retrieve/Update/Delete book

GET/POST /api/authors/           # List/Create authors
GET/PUT/DELETE /api/authors/{id}/ # Retrieve/Update/Delete author

GET/POST /api/members/           # List/Create members (Admin only)
GET/PUT/DELETE /api/members/{id}/ # Retrieve/Update/Delete member (Admin only)

POST /api/borrow/                # Borrow a book
POST /api/return/                # Return a book
```

### Documentation
```
GET /swagger/                    # Interactive API documentation
```

## 🔐 User Roles

- **Librarian (Admin)**: Full access to all operations
- **Member (User)**: Can view books/authors, borrow/return books

## 🚀 Local Development

### Prerequisites
- Python 3.9+
- pip

### Setup
1. Clone the repository
```bash
git clone <repository-url>
cd library_management
```

2. Create virtual environment
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
# or
source .venv/bin/activate      # Mac/Linux
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Apply migrations
```bash
python manage.py migrate
```

5. Create superuser
```bash
python manage.py createsuperuser
```

6. Run development server
```bash
python manage.py runserver
```

7. Visit the API documentation
```
http://127.0.0.1:8000/swagger/
```

## 🌐 Production Deployment

### Environment Variables Required

```env
# Database
DATABASE_URL=postgresql://username:password@host:port/database

# Cloudinary (for media files)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# Django
SECRET_KEY=your_secret_key
DEBUG=False
```

### Deploy to Vercel

1. Install Vercel CLI
```bash
npm i -g vercel
```

2. Login to Vercel
```bash
vercel login
```

3. Deploy
```bash
vercel --prod
```

4. Set environment variables in Vercel dashboard

## 📝 API Usage Examples

### Authentication
```bash
# Register
curl -X POST http://localhost:8000/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'

# Login
curl -X POST http://localhost:8000/auth/jwt/create/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

### Using the API
```bash
# Get books (with authentication)
curl -X GET http://localhost:8000/api/books/ \
  -H "Authorization: Bearer your_access_token"

# Create a book (admin only)
curl -X POST http://localhost:8000/api/books/ \
  -H "Authorization: Bearer admin_access_token" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Python Programming", 
    "author": 1, 
    "isbn": "1234567890123",
    "category": "Programming",
    "availability_status": true
  }'
```

## 🧪 Testing

Visit the interactive API documentation at `/swagger/` to test all endpoints directly from your browser.

## 📄 License

This project is for educational purposes as part of Django learning curriculum.

## 🤝 Contributing

This is a learning project. Feel free to fork and experiment!

---

**Built with ❤️ using Django REST Framework**
