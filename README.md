# Heart Disease ML Project

This repository contains a machine learning project for predicting heart disease risk using clinical data. The study includes data preprocessing, exploratory data analysis (EDA), feature engineering, and model building.

---

## 📄 Full LaTeX Report

Below is the LaTeX source for the thesis-style report:

```latex
\documentclass[12pt,a4paper]{article}

\usepackage[margin=1in]{geometry}
\usepackage{setspace}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{hyperref}
\usepackage{caption}

\onehalfspacing

\title{\textbf{Predicting Heart Disease Risk Using Machine Learning}\\
\large An Applied Study on Clinical Decision Support}

\author{
KONTAXIS IOANNIS\\
\small Applied Machine Learning in Healthcare
}

\date{2026}

\begin{document}

\maketitle
\thispagestyle{empty}
\newpage

\begin{abstract}
Heart disease remains one of the leading causes of mortality worldwide, highlighting the need for effective tools that support early detection and clinical decision-making. This study investigates the application of machine learning techniques to predict the presence of heart disease using structured clinical data. Using a publicly available heart disease dataset, multiple classification models were developed and evaluated, including Logistic Regression as a baseline and tree-based models for comparison. Special attention was given to clinically relevant evaluation metrics, prioritizing sensitivity to reduce the risk of missed diagnoses. Furthermore, model explainability techniques were applied to assess the contribution of individual clinical features to predictions. The results demonstrate that machine learning models can provide meaningful support for heart disease risk screening, while also emphasizing the importance of interpretability, ethical considerations, and data limitations in medical applications.
\end{abstract}

\newpage

\section{Introduction}
Cardiovascular diseases represent a significant global health burden and are a leading cause of morbidity and mortality. Early identification of individuals at high risk of heart disease is critical for timely intervention and improved patient outcomes. Traditional risk assessment tools rely on a limited set of clinical rules or statistical models, which may fail to capture complex interactions between multiple patient characteristics.

Recent advances in machine learning have enabled the development of predictive models capable of analyzing large volumes of clinical data and identifying patterns that may not be apparent through conventional methods. However, the adoption of machine learning in healthcare requires careful consideration of model interpretability, reliability, and ethical implications. In clinical environments, transparency and trust are as important as predictive performance.

The objective of this study is to develop and evaluate interpretable machine learning models for predicting heart disease risk based on routinely collected clinical measurements. The focus is placed on building a reproducible and explainable pipeline that aligns with real-world clinical decision-support scenarios.

% Additional sections like Background, Dataset, Methodology, EDA, Results, Discussion, and Conclusion would follow here.

\end{document}