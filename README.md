Here is the complete and modern technology stack we used to build your Fake Account Detection platform:

**🧠 Artificial Intelligence & Data Science**

Python: The core programming language powering the machine learning and backend.
Pandas: Used for reading, processing, and cleaning the train.csv and test.csv datasets.
Scikit-Learn: The premier machine learning library used for:
StandardScaler: To mathematically normalize extreme data values (like millions of followers vs a binary profile picture).
Random Forest Classifier: A highly advanced, tree-based ensemble algorithm that replaced the basic KNN model to push our accuracy to 91.67%.
Pickle: Used to serialize and export the trained AI model (knn_model_fixed.pkl) so it can be served instantly without retraining every time.

**⚙️ Backend & API**

FastAPI: A lightning-fast, modern web framework for Python. We used it to build the /predict endpoint that bridges the AI model and the website.
Uvicorn: An ASGI web server that runs the FastAPI application asynchronously, making it capable of handling multiple requests seamlessly.
Jinja2: Used behind the scenes by FastAPI to safely render the HTML templates.

**🎨 Frontend & User Interface**

HTML5: Structured the dynamic form and prediction result containers (index.html).
Vanilla CSS3: We built a custom, premium Glassmorphism design from scratch (style.css), featuring:
Vibrant animated background gradients (the floating blobs).
Frosted glass effects (backdrop-filter) for the main container and LinkedIn button.
Interactive micro-animations (hover effects, loading spinners, and result popups).
Vanilla JavaScript (ES6): We used raw JS (script.js) with the modern Fetch API to capture the user's form inputs, send them to the backend asynchronously, and dynamically update the webpage with the AI's prediction—all without requiring a page reload!
