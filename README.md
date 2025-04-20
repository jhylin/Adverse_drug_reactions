### **Adverse drug reactions** (ADRs)

ADRs data for cytochrome P450 (CYP) 3A4, 2D6, 2C19, 2C9, 1A2, 2B6, 2E1 and 2C8 substrates have all been collected for now (since February till April 2025).

This work can be read in conjunction with the previous [cytochrome P450 and small drug molecules](https://jhylin.github.io/Data_in_life_blog/posts/20_Cyp3a4_2d6_inh/1_CYP450_drugs.html) post as it is a continuation of this project, and contains some background information about CYP enzymes at the beginning.

#### **Documents**:

0_Ideas.qmd - the very early brainstorming of ideas for this project with information on reasons behind this work, what have been done and possible future outlooks

1_ADR_data.qmd - [notes](https://jhylin.github.io/Data_in_life_blog/posts/22_Simple_dnn_adrs/1_ADR_data.html) on ADRs and also a list of drug information reference sources used for the ADRs dataset

2_ADR_regressor.ipynb (.qmd version with same file name) - a notebook ([post link](https://jhylin.github.io/Data_in_life_blog/posts/22_Simple_dnn_adrs/2_ADR_regressor.html)) about building a simple deep neural network (DNN) model to predict therapeutic drug classes for CYP3A4 substrates (which are also drugs)

3_ADR_reg_early_stop.ipynb - a notebook that incorporates early stopping code to minimise model overfitting, with notes annotated in a [note post](https://jhylin.github.io/Data_in_life_blog/posts/22_Simple_dnn_adrs/4_Prevent_overfit_note.html)

4_Prevent_overfit_note.qmd - the [note post](https://jhylin.github.io/Data_in_life_blog/posts/22_Simple_dnn_adrs/4_Prevent_overfit_note.html) that shows 3 different probable strategies that can be used to minimise model overfitting when using PyTorch (may be extended to other machine learning algorithms as well)

#### **Other files**:

A few different Python scripts are used in the 2_ADR_regressor.ipynb notebook:
- cyp_drugs.py - for obtaining SMILES of each drug from ChEMBL
- words_tensors.py - for converting ADRs into PyTorch tensors
- Tensors_for_adrs_interactive.py - showing step-by-step outputs how the words_tensors.py is constructed (to be used in VS Code where each line of code can be run like a Jupyter cell)

A few different .tsv/.csv files containing ADRs and/or SMILES data for CYP substrates:

- **cyp_substrates_adrs.csv** - main file for use which contains ADRs for strong and moderate CYP3A4, 2D6, 2C19, 2C9, 1A2, 2B6, 2E1 and 2C8 substrates with their drug names, specific notes regarding ADRs documented (for selected drugs only), evidence of CYP substrate strengths, drug classes, two drug references sources and information checking dates

- **cyp3a4_substrates.csv** - contains ADRs for all CYP3A4 substrates with drug names, ADR notes, evidence of CYP strengths, drug classes, two drug references sources and information checking dates (this is the .csv file used in 2_ADR_regressor.ipynb or .qmd file with same file name)

- **cyp3a4_smiles.tsv** - as an example of SMILES retrieved via cyp_drugs.py script for all CYP3A4 substrates 


Last checked dates for CYP substrate strengths of evidence: 
- CYP3A4 and 2D6 substrates on 24th Feb 2025; 2C19 substrates on 6th Mar 2025; 2C9 substrates on 10th Mar 2025; 1A2 substrates on 25th Mar 2025; 2B6 substrates on 27th Mar 2025; 2E1 and 2C8 substrates on 7th Apr 2025

Please note that all of the CYP substrates curated in the datasets are based on "[The Flockhart Cytochrome P450 Drug-Drug Interaction Table](https://drug-interactions.medicine.iu.edu/MainTable.aspx)" which is continuously being updated over time (at least twice yearly as quoted from source), so the files stored here may not reflect the most up-to-date version - refer to the table directly if needing latest information

#### **Feedback and comments**

The dataset may still contain information that require further refinements, additions or corrections (there may be things I've missed) - feedback and/or comments are welcomed, please submit via issues/pull requests in this GitHub repo. This also applies to the notebooks and scripts listed above as well.

#### **Dedication**

*This work is dedicated to all the scientists and front-line medical and pharmacy staff who have been working with therapeutic drugs throughout their lives trying to minimise ADRs and heal people as much as possible.*