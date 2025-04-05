# Flask Project Setup Guide

This README will guide you through setting up and running a Flask web application.

## Getting Started

### Step 1: Clone the Repository (if applicable)

If you're cloning the project from a repository, use the following command:

```
git clone <your-repository-url>
cd <your-repository-folder>
```

### Step 2: Set Up a Virtual Environment

It's recommended to use a virtual environment to keep your dependencies isolated:

1. Create a virtual environment:

```
python3 -m venv venv
```

2. Activate the virtual environment:
   - On Windows:
   ```
   .\venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```
   source venv/bin/activate
   ```

### Step 3: Install Dependencies

Once the virtual environment is activated, install Flask and other dependencies:

```
pip install -r requirements.txt
```

### Step 4: Run the Application

To start the Flask development server, use the following command:

```
python app.py
```

The server will start and be available at http://127.0.0.1:5000/ by default.

## Project Structure

### Step 5: Directory Structure

The project is organized as follows:

```
/flask_project
    /static     # For static files like CSS, JS, and images
    /templates  # For HTML templates
    app.py      # Main Flask application
    requirements.txt  # List of dependencies
```

### Step 6: Create/Modify Templates

Create HTML files in the `templates/` directory for the views you want to render. The default template is `index.html`, which is rendered when you visit the homepage.

### Step 7: Create Static Files

Put any static assets (like CSS, JavaScript, images) in the `static/` directory. These files can be linked directly in your templates.

## Dependencies Management

### requirements.txt

This project uses the `requirements.txt` file to manage dependencies. Below is the content for the `requirements.txt` file:

```
Flask==2.0.1
```

To generate the `requirements.txt` file, follow these steps:

1. After installing the necessary libraries, run:

```
pip freeze > requirements.txt
```

This command will capture all the packages in your virtual environment and store them in the `requirements.txt` file.

To install the dependencies listed in `requirements.txt`:

```
pip install -r requirements.txt
```

## Flask App Details

- **app.py**: This file contains the main logic for the Flask application. It initializes the app, defines the routes, and renders HTML templates.
- **Templates**: The app uses Jinja2 templating to dynamically generate HTML pages. By default, the `index.html` template is rendered on visiting the homepage.
- **Static Files**: Any static assets like images, CSS files, and JavaScript are served from the `static` directory.

## License

This project is licensed under the MIT License – see the LICENSE file for details.
