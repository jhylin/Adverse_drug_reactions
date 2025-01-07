#### **Adverse drug reactions** (ADRs)

This work can be read in conjunction with the previous "[cytochrome P450 and small drug molecules](https://jhylin.github.io/Data_in_life_blog/posts/20_Cyp3a4_2d6_inh/1_CYP450_drugs.html)" post as it is a continuation of this project.

ADRs data collection for CYP3A4 substrates has been completed for the current post. Potentially, more data can be collected on other different CYP substrates in the future.

##### **Drafts of documents**:

0_Ideas.qmd - the very early brainstorming of ideas for this project with some background information

1_ADR_data.qmd - all notes on ADRs and also a list of reference sources for the ADRs data

2_ADR_regressor.ipynb (.qmd version with same file name) - a notebook about building a simple deep neural network (DNN) model to predict therapeutic drug classes for CYP3A4 substrates (which are also drugs)

##### **Other files**:

A few different Python scripts are used in the 2_ADR_regressor.ipynb notebook:
- cyp_drugs.py - for obtaining SMILES of each drug from ChEMBL
- words_tensors.py - for converting ADRs into PyTorch tensors
- Tensors_for_adrs_interactive.py - showing step-by-step outputs how the words_tensors.py is constructed (to be used in VS Code where each line of code can be run like a Jupyter cell)

A few different .tsv/.csv files of CYP3A4 substrates data or their SMILES:
- All_cyp3a4_smiles.tsv - a tsv file containing SMILES of all the CYP3A4 substrates
- strong_cyp3a4_smiles.tsv - a tsv file containing SMILES for strong CYP3A4 substrates only
- All_CYP3A4_substrates - a csv file containing all CYP3A4 substrates (drug names), drug classes along with their ADRs and reference sources
- CYP3A4_mod_substrates - a csv file containing only moderate CYP3A4 substrates, drug classes along with their ADRs and reference sources
- CYP3A4_strong_substrates - a csv file containing only strong CYP3A4 substrates, drug classes along with their ADRs and reference sources