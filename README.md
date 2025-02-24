### **Adverse drug reactions** (ADRs)

This work can be read in conjunction with the previous "[cytochrome P450 and small drug molecules](https://jhylin.github.io/Data_in_life_blog/posts/20_Cyp3a4_2d6_inh/1_CYP450_drugs.html)" post as it is a continuation of this project.

ADRs data collection for CYP3A4 substrates has been completed for the current post. Potentially, more data can be collected on other different CYP substrates in the future - for February 2025, ADRs for CYP2D6 substrate are being collected.

#### **Documents**:

0_Ideas.qmd (draft version) - the very early brainstorming of ideas for this project with some background information

1_ADR_data.qmd - all [notes](https://jhylin.github.io/Data_in_life_blog/posts/22_Simple_dnn_adrs/1_ADR_data.html) on ADRs and also a list of reference sources for the ADRs data

2_ADR_regressor.ipynb (.qmd version with same file name) - a notebook ([post link](https://jhylin.github.io/Data_in_life_blog/posts/22_Simple_dnn_adrs/2_ADR_regressor.html)) about building a simple deep neural network (DNN) model to predict therapeutic drug classes for CYP3A4 substrates (which are also drugs)

3_ADR_reg_early_stop.ipynb - a notebook that incorporates early stopping code to minimise model overfitting, with notes annotated in a [note post](https://jhylin.github.io/Data_in_life_blog/posts/22_Simple_dnn_adrs/4_Prevent_overfit_note.html)

4_Prevent_overfit_note.qmd - the [note post](https://jhylin.github.io/Data_in_life_blog/posts/22_Simple_dnn_adrs/4_Prevent_overfit_note.html) that shows 3 different probable strategies that can be used to minimise model overfitting when using PyTorch (may be extended to other machine learning algorithms as well)

#### **Other files:**

A few different Python scripts are used in the 2_ADR_regressor.ipynb notebook:
- cyp_drugs.py - for obtaining SMILES of each drug from ChEMBL
- words_tensors.py - for converting ADRs into PyTorch tensors
- Tensors_for_adrs_interactive.py - showing step-by-step outputs how the words_tensors.py is constructed (to be used in VS Code where each line of code can be run like a Jupyter cell)

A few different .tsv/.csv files of CYP3A4 substrates data or their SMILES:
- All_CYP3A4_substrates - contains all CYP3A4 substrates (drug names), drug classes along with their ADRs and reference sources
- CYP3A4_mod_substrates.csv - contains only moderate CYP3A4 substrates, drug classes along with their ADRs and reference sources
- CYP3A4_strong_substrates.csv - contains only strong CYP3A4 substrates, drug classes along with their ADRs and reference sources
- All_cyp3a4_smiles.tsv - contains SMILES of all the CYP3A4 substrates
- strong_cyp3a4_smiles.tsv - contains SMILES for strong CYP3A4 substrates only

*Please note that all of the CYP3A4 and 2D6 substrates curated in the datasets are based on "[The Flockhart Cytochrome P450 Drug-Drug Interaction Table](https://drug-interactions.medicine.iu.edu/MainTable.aspx)" which is continuously being updated over time (at least twice yearly as quoted from source), so the files stored here may not reflect the most up-to-date version - refer to the table directly if needing latest information*

#### **Dedication**

*This work is dedicated to all the scientists and front-line medical and pharmacy staff who have been working with therapeutic drugs throughout their lives trying to minimise ADRs and heal people as much as possible.*