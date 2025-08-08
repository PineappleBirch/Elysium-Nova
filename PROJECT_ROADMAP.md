# Portfolio Project Plan: Elysium Nova

Here is a structured list of end-to-end projects designed to build a powerful and diverse portfolio. The projects are centered around Python and SQL and are organized by category and difficulty tier.

---

## 1. The MLOps Forge (Machine Learning Engineering)
*Focus: Deploying, scaling, and maintaining ML models in production environments.*

### Tier 1
1.  **Project: Iris Core**
    * **Description:** Train a simple classifier on the Iris dataset and build a robust API using FastAPI to serve predictions. This is the foundational project for the series.
    * **Skills:** Python, Pandas, Scikit-learn, FastAPI/Flask.
2.  **Dockerized ML Service:**
    * **Project:** Take the "Project: Iris Core" API and containerize it using **Docker**. Write a `Dockerfile` to create a self-contained image that can be run anywhere.
    * **Skills:** Docker, understanding of ports, environments, and dependencies.

### Tier 2
1.  **Sentiment Analysis Web App:**
    * **Project:** Use a pre-trained sentiment analysis model from **Hugging Face Transformers**. Build a **Streamlit** or **FastAPI** web application where a user can type in a sentence and see the sentiment returned. Deploy it using Docker.
    * **Skills:** Hugging Face, Streamlit, FastAPI, Docker.
2.  **Automated Model Training Pipeline:**
    * **Project:** Create a Python script that automatically downloads a dataset, processes it, trains a model, and saves the model artifact and performance metrics.
    * **Skills:** Python scripting, file I/O, Scikit-learn, job scheduling.

### Tier 3
1.  **RAG-based Document Q&A:**
    * **Project:** Build a Retrieval-Augmented Generation (RAG) system. The app will "read" your documents, and a user can ask questions that an LLM answers based on the retrieved context.
    * **Skills:** LLMs, Vector Databases (ChromaDB, FAISS), LangChain/LlamaIndex, embedding models, FastAPI.
2.  **MLOps with CI/CD:**
    * **Project:** Use **DVC** (Data Version Control) to version your data and models. Create a **GitHub Actions** workflow that automatically re-trains, validates, and deploys your model as a Docker container.
    * **Skills:** Git, DVC, GitHub Actions (CI/CD), Docker Hub/GitHub Container Registry.

### Tier 4
1.  **Fine-tune and Deploy a Smaller LLM:**
    * **Project:** Fine-tune a smaller open-source LLM (e.g., FLAN-T5) on a specific dataset. Build a robust API for this model and deploy it on a cloud service.
    * **Skills:** PyTorch/TensorFlow, Hugging Face, cloud deployment (GCP/AWS), model optimization.
2.  **Real-time Prediction Service with Monitoring:**
    * **Project:** Build an ML service that makes predictions in real-time. Use **Prefect** or **Airflow** for scheduled re-training and **Prometheus/Grafana** to monitor for data drift.
    * **Skills:** Prefect/Airflow, Prometheus, Grafana, advanced API development, model drift.

---

## 2. Data Processing and Data Engineering
*Focus: Building reliable pipelines to move, transform, and store data.*

### Tier 1
1.  **API to SQL ETL Script:**
    * **Project:** Write a Python script that extracts data from a public REST API, transforms it using **Pandas**, and loads it into a local **SQLite** database.
    * **Skills:** Python, `requests` library, Pandas, SQL (`CREATE TABLE`, `INSERT`).
2.  **CSV Batch Processing:**
    * **Project:** Create a script that watches a folder for incoming CSVs, processes and cleans the data, and appends it to a master table in a **PostgreSQL** or **DuckDB** database.
    * **Skills:** Python, Pandas, file system operations, SQL, DuckDB/PostgreSQL.

### Tier 2
1.  **Scheduled Cloud ETL Pipeline:**
    * **Project:** Take the "API to SQL" project and schedule it to run daily using **Prefect** or **Airflow**. Load the data into a cloud data warehouse like **Google BigQuery** or **Snowflake**.
    * **Skills:** Prefect/Airflow, cloud authentication, BigQuery/Snowflake client libraries.
2.  **Web Scraper Pipeline:**
    * **Project:** Build a web scraper using **Beautiful Soup** or **Scrapy** to collect data from a website. Store the scraped data in a structured format (JSON or a database) and Dockerize it.
    * **Skills:** Web scraping, HTML basics, Beautiful Soup/Scrapy, Docker.

### Tier 3
1.  **Data Modeling with dbt:**
    * **Project:** Ingest raw data into a data warehouse. Use **dbt (data build tool)** to transform this raw data into clean, well-documented "marts" using only SQL.
    * **Skills:** dbt, advanced SQL, data modeling, Jinja templating.
2.  **Real-time Data Streaming:**
    * **Project:** Use **Kafka** to simulate a stream of events. Write a Python consumer that reads from the stream, performs a simple aggregation, and writes the result to a database.
    * **Skills:** Kafka/PubSub, data serialization (JSON, Avro), real-time processing concepts.

### Tier 4
1.  **Build a Data Lakehouse:**
    * **Project:** Ingest raw data into cloud storage (S3/GCS). Use **Apache Iceberg** or **Delta Lake** with **Spark** or **DuckDB** to manage and query the data, creating a full "lakehouse" architecture.
    * **Skills:** Spark/DuckDB, Apache Iceberg/Delta Lake, Parquet, cloud storage, Terraform.
2.  **Batch & Stream "Lambda" Architecture:**
    * **Project:** Design a system with both a batch layer (e.g., nightly Spark job) and a speed layer (e.g., real-time streaming job) to provide a complete and up-to-date data view.
    * **Skills:** Spark (Batch and Structured Streaming), Kafka, advanced data architecture design.

---

## 3. Manual and Automated Testing (QA)
*Focus: Ensuring software quality through manual checks and automated frameworks.*

### Tier 1
1.  **Manual Test Case Suite:**
    * **Project:** Choose a simple public website. Write a detailed manual test plan and test cases in a structured format (spreadsheet/Markdown).
    * **Skills:** Test case design, bug reporting, requirements analysis.
2.  **First UI Automation Script:**
    * **Project:** Write your first automated test using **Selenium** or **Playwright** with Python to perform a simple user flow and assert a result.
    * **Skills:** Python, Selenium/Playwright, locators (ID, XPath, CSS).

### Tier 2
1.  **UI Test Suite with Page Object Model (POM):**
    * **Project:** Automate a full test suite using the **Page Object Model (POM)** pattern for maintainability. Use a test runner like **pytest**.
    * **Skills:** Pytest, Page Object Model, test organization.
2.  **Automated API Testing:**
    * **Project:** Write a suite of automated tests for a public REST API using Python's `requests` library and `pytest`.
    * **Skills:** API testing concepts (GET, POST, etc.), `requests`, `pytest`, JSON schema validation.

### Tier 3
1.  **CI-Integrated Test Automation:**
    * **Project:** Integrate your UI and API test suites into a **GitHub Actions** CI/CD pipeline that runs on every push and publishes reports.
    * **Skills:** GitHub Actions, test reports (`pytest-html`), environment variables.
2.  **Basic Performance Testing:**
    * **Project:** Use **Locust** to write a simple performance test script in Python. Simulate concurrent users and measure response times.
    * **Skills:** Locust, performance testing concepts (users, RPS).

### Tier 4
1.  **Build a Hybrid Test Automation Framework:**
    * **Project:** Design a scalable test automation framework from scratch using `pytest` that supports both UI and API tests, parallel execution, and different environments.
    * **Skills:** Advanced `pytest`, framework design, Allure reports, configuration management.
2.  **Visual Regression Testing:**
    * **Project:** Implement an automated visual testing solution that takes screenshots and compares them against baselines to detect UI changes.
    * **Skills:** Playwright/Selenium, image comparison algorithms, test workflow design.

---

## 4. Data Analysis and Data Science
*Focus: Extracting insights, telling stories with data, and building predictive models.*

### Tier 1
1.  **Exploratory Data Analysis (EDA):**
    * **Project:** Pick a dataset from Kaggle. Use a **Jupyter Notebook** to conduct a full EDA with **Pandas**, **Matplotlib**, and **Seaborn**, documenting your findings.
    * **Skills:** Pandas, Matplotlib, Seaborn, data storytelling, Jupyter.
2.  **SQL-based Analysis:**
    * **Project:** Load a dataset into a **PostgreSQL** or **SQLite** database. Answer business questions using only **SQL** (window functions, CTEs, etc.).
    * **Skills:** Advanced SQL, data modeling.

### Tier 2
1.  **Interactive Data Dashboard:**
    * **Project:** Build an interactive dashboard with **Streamlit** or **Plotly Dash**. Allow users to filter data and update charts in real-time.
    * **Skills:** Streamlit/Dash, Plotly Express, UI/UX design for data.
2.  **Simple Predictive Model:**
    * **Project:** Build a classification or regression model using **Scikit-learn**. Focus on the full workflow: cleaning, feature engineering, training, and evaluation.
    * **Skills:** Scikit-learn, feature engineering, model evaluation.

### Tier 3
1.  **A/B Test Analysis:**
    * **Project:** Analyze the results of a fictional A/B test using statistical methods (e.g., t-tests) and summarize the results for a non-technical audience.
    * **Skills:** Statistics for data science, hypothesis testing, clear communication.
2.  **Customer Segmentation (Clustering):**
    * **Project:** Use **K-Means clustering** to segment customers. Analyze and describe the resulting clusters to create user personas.
    * **Skills:** Unsupervised learning, K-Means, dimensionality reduction (PCA), data interpretation.

### Tier 4
1.  **Time Series Forecasting:**
    * **Project:** Using a time-series dataset, build a forecasting model with **Prophet** or **ARIMA**. Evaluate your model's forecasts against a holdout set.
    * **Skills:** Time series analysis, Prophet/Statsmodels, forecast evaluation.
2.  **End-to-End Analysis & Recommendation Engine:**
    * **Project:** Perform a deep analysis and build a simple recommendation engine (e.g., for movies). Wrap it in a Streamlit app.
    * **Skills:** Recommendation systems, matrix factorization/cosine similarity, deploying a data application.

---

## 5. Image Processing and Computer Vision
*Focus: Manipulating and extracting information from images and video.*

### Tier 1
1.  **Image Manipulation Tool:**
    * **Project:** Create a simple tool using **OpenCV** or **Pillow** to perform basic image operations: resize, grayscale, blur, etc.
    * **Skills:** OpenCV/Pillow, basic image processing theory, NumPy.
2.  **QR Code / Barcode Reader:**
    * **Project:** Build an application that can detect and decode QR codes or barcodes from an image or live webcam feed.
    * **Skills:** OpenCV, real-time video capture.

### Tier 2
1.  **Object Detection with a Pre-trained Model:**
    * **Project:** Use a pre-trained **YOLO** model to perform real-time object detection on a video stream, drawing bounding boxes and labels.
    * **Skills:** Using pre-trained models, YOLO, OpenCV video processing.
2.  **Document Scanner:**
    * **Project:** Create an app that takes a photo of a document, applies a perspective transform to get a flat "scanned" view, and cleans the image.
    * **Skills:** OpenCV, contour detection, image transformations, thresholding.

### Tier 3
1.  **Custom Image Classifier (Transfer Learning):**
    * **Project:** Collect a custom dataset and use **transfer learning** with a network like MobileNetV2 in **TensorFlow/PyTorch** to train a custom image classifier.
    * **Skills:** TensorFlow/PyTorch, transfer learning, data augmentation, model evaluation.
2.  **Face Recognition and Liveness Check:**
    * **Project:** Build a system that can recognize faces from a known set of people and add a "liveness check" (e.g., detect eye blinks) to prevent spoofing.
    * **Skills:** Face detection, face recognition, liveness detection techniques.

### Tier 4
1.  **Image Segmentation:**
    * **Project:** Implement a semantic segmentation model (like **U-Net**) to classify each pixel in an image (e.g., identify roads in satellite imagery).
    * **Skills:** U-Net architecture, PyTorch/TensorFlow, image segmentation metrics (IoU).
2.  **Generative AI with Style Transfer:**
    * **Project:** Implement Neural Style Transfer. The app should take a "content" image and a "style" image and merge them.
    * **Skills:** Deep learning, CNN feature extraction, loss functions, Generative AI concepts.

---

## OPTIONAL: Combined Projects
*Focus: Integrating skills from multiple domains into a single, complex project.*

1.  **Real-time Anomaly Detection Dashboard (DE + DS + MLE):**
    * **Project:** Build a **Data Engineering** pipeline (Kafka) to stream sensor data. Use an **ML** model to detect anomalies in real-time. Feed results to a live **Data Science** dashboard (Streamlit/Dash).
2.  **Automated Visual Bug Reporting System (CV + QA + DE):**
    * **Project:** Create a **QA** script that takes screenshots. Use **Computer Vision** to detect visual bugs against baselines. If a bug is found, use a **Data Engineering** pipeline to log a detailed report in a database or issue tracker.
