# Predicting Heart Disease Risk Using Machine Learning

## Abstract
Heart disease remains one of the leading causes of mortality worldwide, highlighting the need for effective tools that support early detection and clinical decision-making. This study investigates the application of machine learning techniques to predict the presence of heart disease using structured clinical data. Using a publicly available heart disease dataset, multiple classification models were developed and evaluated, including Logistic Regression as a baseline and tree-based models for comparison. Special attention was given to clinically relevant evaluation metrics, prioritizing sensitivity to reduce the risk of missed diagnoses. Furthermore, model explainability techniques were applied to assess the contribution of individual clinical features to predictions. The results demonstrate that machine learning models can provide meaningful support for heart disease risk screening, while also emphasizing the importance of interpretability, ethical considerations, and data limitations in medical applications.

---

## 1. Introduction
Cardiovascular diseases represent a significant global health burden and are a leading cause of morbidity and mortality. Early identification of individuals at high risk of heart disease is critical for timely intervention and improved patient outcomes. Traditional risk assessment tools rely on a limited set of clinical rules or statistical models, which may fail to capture complex interactions between multiple patient characteristics.

Recent advances in machine learning have enabled the development of predictive models capable of analyzing large volumes of clinical data and identifying patterns that may not be apparent through conventional methods. However, the adoption of machine learning in healthcare requires careful consideration of model interpretability, reliability, and ethical implications. In clinical environments, transparency and trust are as important as predictive performance.

The objective of this study is to develop and evaluate interpretable machine learning models for predicting heart disease risk based on routinely collected clinical measurements. The focus is placed on building a reproducible and explainable pipeline that aligns with real-world clinical decision-support scenarios.

---

## 2. Background and Related Work
Risk prediction for heart disease has traditionally been addressed using statistical approaches such as logistic regression-based risk scores, including well-known tools like the Framingham Risk Score. While these models are widely used in clinical practice, they often assume linear relationships between predictors and outcomes and may not fully capture non-linear patterns present in patient data.

In recent years, machine learning methods such as decision trees, random forests, and gradient boosting models have been explored for cardiovascular risk prediction. These approaches have demonstrated improved predictive performance in several studies; however, their lack of interpretability has raised concerns regarding clinical trust and deployment. As a result, there is growing interest in explainable machine learning techniques that balance performance with transparency.

This study builds upon existing research by combining classical and modern machine learning approaches while explicitly addressing interpretability and clinical relevance.

---

## 3. Dataset Description
The dataset used in this study consists of structured clinical records collected for the purpose of heart disease diagnosis. Each record corresponds to an individual patient and includes demographic information, clinical measurements, and diagnostic test results.

### 3.1 Features
The dataset includes the following variables:

- **Age:** Patient age in years  
- **Sex:** Biological sex of the patient  
- **Chest Pain Type:** Categorical variable describing chest pain characteristics  
- **Resting Blood Pressure:** Measured in mm Hg  
- **Serum Cholesterol:** Measured in mg/dl  
- **Fasting Blood Sugar:** Indicator of fasting blood sugar > 120 mg/dl  
- **Resting Electrocardiographic Results:** Categorical ECG outcomes  
- **Maximum Heart Rate Achieved:** Numeric measurement during exercise  
- **Exercise-Induced Angina:** Binary indicator  
- **Oldpeak:** ST depression induced by exercise relative to rest  
- **Slope of the Peak Exercise ST Segment:** Ordinal categorical variable  
- **Number of Major Vessels:** Count of major vessels colored by fluoroscopy  
- **Thalassemia Status (Thal):** Categorical variable indicating heart condition  

The **target variable** indicates the presence or absence of heart disease.

---

## 4. Exploratory Data Analysis (EDA)
Exploratory data analysis was conducted to understand the distribution of patient characteristics and identify potential patterns related to heart disease. Descriptive statistics and visualizations were used to examine age distributions, disease prevalence, and correlations among numerical variables.

Initial analysis revealed notable differences in age, maximum heart rate, and chest pain type distributions between patients with and without heart disease. Correlation analysis indicated moderate relationships between several cardiovascular indicators, motivating the use of multivariate machine learning models.

---

## 5. Methodology

### 5.1 Data Preprocessing
Medical datasets often contain heterogeneous feature types, including **continuous, binary, nominal categorical, and ordinal categorical variables**. Proper preprocessing is essential to ensure that machine learning models interpret these features correctly and do not infer misleading relationships.

- **Continuous variables** (age, blood pressure, cholesterol, max heart rate, ST depression) were imputed using the **median** and standardized using **StandardScaler** to ensure comparable scales.  
- **Binary variables** (sex, fasting blood sugar, exercise-induced angina) were retained in their original numeric form.  
- **Nominal categorical variables** (chest pain type, resting ECG results, thalassemia status) were **one-hot encoded** to prevent the model from assuming artificial ordinal relationships.  
- **Ordinal variables** (slope of ST segment, number of vessels) were preserved in numeric form to maintain their inherent ordering.

A preprocessing pipeline was implemented using scikit-learn’s **Pipeline** and **ColumnTransformer** to ensure reproducibility and prevent data leakage. All preprocessing steps were fitted exclusively on the training data and subsequently applied to the test set.

---

## 6. Future Sections
The following sections will cover:

- Model selection  
- Evaluation strategy  
- Explainability  
- Results  
- Discussion  
- Conclusions