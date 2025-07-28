# 🛠️ Django Order Management System

A modern, responsive Django-based Order Management System with a beautiful UI and full CRUD functionality.

## 📸 Features

- **📋 Order List View**: Display orders in a responsive grid layout
- **➕ Add Orders**: Modal form for creating new orders
- **✏️ Edit Orders**: Inline row editing with Update/Cancel functionality
- **🗑️ Delete Orders**: Bulk delete with confirmation
- **✅ Real-time Validation**: Form validation with visual feedback
- **🎨 Modern UI**: Bootstrap 5 with custom styling
- **📱 Responsive Design**: Works on desktop, tablet, and mobile

## 🏗️ Tech Stack

- **Backend**: Django 5.2.4 (Python)
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **UI Framework**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.0.0

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd "project test"
   ```

2. **Activate the virtual environment**
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies** (if not already installed)
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Load sample data** (optional)
   ```bash
   python manage.py load_sample_data
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser and navigate to**
   ```
   http://127.0.0.1:8000/
   ```

## 📊 Database Schema

### Order Model
- `order_id` (CharField, Primary Key): Unique order identifier
- `customer_name` (CharField): Customer's full name
- `freight` (DecimalField): Shipping cost
- `ship_name` (CharField): Shipping company name
- `ship_country` (CharField): Destination country
- `created_at` (DateTimeField): Order creation timestamp
- `updated_at` (DateTimeField): Last modification timestamp

## 🎯 Usage Guide

### Adding Orders
1. Click the **"Add"** button in the toolbar
2. Fill in the required fields (Order ID, Customer Name, Freight)
3. Optionally fill in Ship Name and Ship Country
4. Click **"Save Order"**

### Editing Orders
1. Select a single order by checking its checkbox
2. Click the **"Edit"** button
3. Modify the values directly in the table row
4. Click **"Update"** to save or **"Cancel"** to discard changes

### Deleting Orders
1. Select one or more orders using checkboxes
2. Click the **"Delete"** button
3. Confirm deletion in the modal dialog

### Bulk Operations
- Use the **"Select All"** checkbox to select all orders
- Perform bulk delete operations on multiple orders

## 🎨 UI Components

### Action Buttons
- **Add**: Opens modal for creating new orders
- **Edit**: Enables inline editing (requires single selection)
- **Delete**: Removes selected orders (requires confirmation)
- **Update**: Saves changes during edit mode
- **Cancel**: Discards changes during edit mode

### Table Features
- **Responsive Design**: Horizontal scrolling on small screens
- **Row Selection**: Checkbox-based selection with visual feedback
- **Hover Effects**: Visual feedback on row hover
- **Sortable Columns**: Click headers to sort (future enhancement)

## 🔧 Customization

### Styling
- Modify `static/css/style.css` for custom styling
- Update Bootstrap classes in templates for different themes

### Functionality
- Extend `static/js/orders.js` for additional JavaScript features
- Modify views in `orders/views.py` for backend logic changes

### Database
- Add new fields to `orders/models.py`
- Run `python manage.py makemigrations` and `python manage.py migrate`

## 📁 Project Structure

```
project test/
├── order_management/          # Django project settings
│   ├── settings.py           # Project configuration
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI configuration
├── orders/                   # Orders app
│   ├── models.py            # Order model definition
│   ├── views.py             # View functions
│   ├── forms.py             # Form definitions
│   ├── urls.py              # App URL routing
│   ├── templates/           # HTML templates
│   │   └── orders/
│   │       └── order_list.html
│   └── management/          # Custom management commands
│       └── commands/
│           └── load_sample_data.py
├── static/                  # Static files
│   ├── css/
│   │   └── style.css       # Custom styles
│   └── js/
│       └── orders.js       # JavaScript functionality
├── manage.py               # Django management script
├── db.sqlite3             # SQLite database
└── README.md              # This file
```

## 🐛 Troubleshooting

### Common Issues

1. **Static files not loading**
   - Ensure `STATICFILES_DIRS` is configured in settings.py
   - Run `python manage.py collectstatic` if needed

2. **Database errors**
   - Delete `db.sqlite3` and run migrations again
   - Check model field definitions

3. **JavaScript not working**
   - Check browser console for errors
   - Ensure Bootstrap and jQuery are loaded

### Development Tips

- Use browser developer tools to debug JavaScript
- Check Django debug toolbar for performance insights
- Monitor Django logs for backend errors

## 🔮 Future Enhancements

- [ ] Advanced filtering and search
- [ ] Export to CSV/Excel
- [ ] Pagination for large datasets
- [ ] User authentication and permissions
- [ ] API endpoints for mobile apps
- [ ] Real-time updates with WebSockets
- [ ] Advanced reporting and analytics

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

**Built with ❤️ using Django and Bootstrap** 