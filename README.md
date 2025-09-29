Applied AI Engineer Assignment: AI-Powered Market Intelligence

This repository hosts a project demonstrating the capability to transform raw, fragmented app store data into actionable market intelligence using a pipeline that integrates data science, feature engineering, and a Large Language Model (LLM).

The goal of this assignment was to simulate a market intelligence analyst by automatically identifying trends, key performance indicators, and strategic recommendations for mobile app businesses.

Project Deliverables

The repository includes two primary Jupyter Notebooks that document the entire process and findings:

Applied AI Engineer Assignment.ipynb	The main technical notebook. It contains the complete code for data cleaning, data merging (Google Play + Apple App Store data), LLM integration, and the generation of structured business insights.
Executive Report.ipynb	A high-level, business-focused report summarizing the project's Executive Summary, Data Overview, Key Insights, and Recommendations derived from the analysis, suitable for non-technical stakeholders.

Technical Flow

The market intelligence pipeline implemented in the project follows these stages:

Data Ingestion & Cleaning: Load raw app data. Handle missing values, drop duplicates, and normalize data types (e.g., converting install counts and prices).

Data Merging: Combine datasets from different app stores (implied: Google Play and Apple App Store) into a unified dataframe for comprehensive analysis.

Feature Engineering: Create new, valuable features like combined_rating or platform_indicator to enrich the analysis scope.

LLM Integration (Market Intelligence Agent): Use the cleaned, processed dataset as context for a Large Language Model (like OpenAI) and prompt it to act as a Market Analyst.

Structured Insight Generation: The LLM generates actionable business insights and provides a quantifiable confidence score for each recommendation, ensuring results are reliable and directly applicable.
