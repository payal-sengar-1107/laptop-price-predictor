# Laptop Price Predictor 💻📊

This is an end-to-end Machine Learning project that predicts the price of a laptop based on its configuration and specifications (such as Brand, Type, RAM, CPU, GPU, OS, Weight, etc.).

## 🚀 Live Demo
You can test the interactive web application live here: [Live Streamlit App](https://streamlit.app)

## 🛠️ Tech Stack & Libraries Used
- **Language:** Python
- **Frontend & Deployment:** Streamlit, Streamlit Community Cloud
- **Data Analysis & Machine Learning:** Pandas, NumPy, Scikit-Learn
- **Algorithms Evaluated:** Linear Regression, Ridge, Lasso, Decision Tree, Random Forest Regressor

## 📈 Key Process & Learnings (CampusX Project Workflow)
- **Data Cleaning:** Processed the raw dataset by removing units (like 'GB' from RAM and 'kg' from Weight) and converting them into numerical types.
- **Feature Engineering:** Extracted valuable insights from the `ScreenResolution` column to create new binary features like `Touchscreen` and `Ips`. Split the `Memory` column into dedicated `HDD` and `SSD` features.
- **Pipeline Implementation:** Utilized `ColumnTransformer` and Scikit-Learn `Pipeline` to orchestrate one-hot encoding for categorical variables and scaling, ensuring clean code without data leakage.
- **Model Selection:** Reached optimum performance using the Random Forest Regressor, which was then exported using `pickle` for deployment.
