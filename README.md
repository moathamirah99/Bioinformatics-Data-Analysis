# Bioinformatics and Health Data Analysis

## Overview
This repository contains a collection of Python scripts focused on bioinformatics, genomic data processing, and exploratory data analysis (EDA) of global health and cancer datasets. It demonstrates the application of data manipulation, synthetic data generation, and data visualization techniques to biological and medical datasets.

## Projects Included

### 1. Genomic Data Simulator (`dna_mock_data_generator.py`)
- Generates synthetic patient genomic records using NumPy and Pandas.
- Simulates DNA/RNA mutations (SNPs, insertions, deletions).
- Translates wild-type and mutant codons to amino acids.
- Classifies mutation categories (missense, nonsense, silent, frameshift) and assigns phenotypic statuses (e.g., pathogenic vs. benign).

### 2. Global Health & Mortality Analysis (`global_health_analysis.py`)
- Exploratory Data Analysis (EDA) of a Global Health and Disease Burden dataset.
- Uses Matplotlib to visualize cancer mortality rates in relation to various factors like healthcare spending, hospital bed capacity, physician density, and life expectancy.

### 3. METABRIC Breast Cancer RNA Analysis (`metabric_cancer_eda.py`)
- In-depth EDA of the METABRIC breast cancer dataset.
- Analyzes and visualizes clinical features such as PAM50 subtypes, HER2 status, and age distributions.
- Explores overall patient survival across different age groups and clinical subtypes.
- Investigates gene expression correlations (TP53, BRCA1, BRCA2) using heatmaps and boxplots.

### 4. DNA Sequence Analyzer (`dna_sequence_analyzer.py`)
- A command-line interface (CLI) tool for basic DNA sequence manipulation.
- Performs simple sequence alignment to locate mutations and calculate similarity percentages.
- Calculates GC content and generates sequence complements and reverse complements.

## Technologies & Libraries Used
- **Python 3**
- **Pandas:** Data manipulation, cleaning, and aggregation.
- **NumPy:** Numerical operations and synthetic data generation.
- **Matplotlib:** Data visualization (bar charts, scatter plots, boxplots, heatmaps, pie charts).
