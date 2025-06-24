import chembl_downloader
from chembl_downloader import latest
import pandas as pd
from textwrap import dedent
from typing import Optional
from pathlib import Path

def chembl_targets(*target: str, file_name: Optional[str] = None):

    """
    Obtain assay ChEMBL IDs, protein target type (fixed at single target - see SQL in script), tax IDs, 
    protein target CHEMBL IDs, canonical SMILES, approved drugs/small molecule ChEMBL IDs, 
    generic drug/small molecule names, max phases, assay standard types, pchembl values
    via using protein target ChEMBL IDs with an option to save data as .tsv files and load as a dataframe

    :param target: Enter protein target CHEMBL ID e.g. CHEMBL1234 to search in ChEMBL database
    :param file_name: Enter file name if needed in order to save dataframe as a .tsv file in working directory 
    (currently set at ~/.data/adr directory)
    :return: A dataframe containing various protein target and drug data from ChEMBL as explained above
    """

    # dedent to remove leading whitespaces from every line
    # https://docs.python.org/3/library/textwrap.html#textwrap.dedent

    sql = dedent(
        f"""\
        SELECT
            ASSAYS.chembl_id              AS assay_chembl_id,
            TARGET_DICTIONARY.target_type,
            TARGET_DICTIONARY.tax_id,
            TARGET_DICTIONARY.chembl_id,
            COMPOUND_STRUCTURES.canonical_smiles,
            MOLECULE_DICTIONARY.chembl_id AS molecule_chembl_id,
            MOLECULE_DICTIONARY.pref_name,
            MOLECULE_DICTIONARY.max_phase,
            ACTIVITIES.standard_type,
            ACTIVITIES.pchembl_value
        FROM TARGET_DICTIONARY
            JOIN ASSAYS ON TARGET_DICTIONARY.tid == ASSAYS.tid
            JOIN ACTIVITIES ON ASSAYS.assay_id == ACTIVITIES.assay_id
            JOIN MOLECULE_DICTIONARY ON MOLECULE_DICTIONARY.molregno == ACTIVITIES.molregno
            JOIN COMPOUND_STRUCTURES ON MOLECULE_DICTIONARY.molregno == COMPOUND_STRUCTURES.molregno
        WHERE TARGET_DICTIONARY.chembl_id = '{target}'
            AND ACTIVITIES.pchembl_value IS NOT NULL
            AND TARGET_DICTIONARY.target_type = 'SINGLE PROTEIN'
        """
    ).strip().replace('\'(', ' ').strip().replace(",)'", ' ')

    # Pick any directory, but make sure it's relative to your home directory
    directory = Path.home().joinpath(".data", "adr")
    # Create the directory if it doesn't exist
    directory.mkdir(exist_ok=True, parents=True)
    # Use latest ChEMBL version
    latest_version = latest()
    # Create a file path that corresponds to the previously cached ChEMBL data 
    path = directory.joinpath(f"{file_name}_{latest_version}.tsv")

    if path.is_file():
        # If the .tsv file already exists, load it
        df = pd.read_csv(path, sep=',')
    elif file_name == None:
        # If no file name provided, load df from query directly
        df = chembl_downloader.query(sql)
    else:
        # If the .tsv file doesn't already exist, make the query then cache it
        df = chembl_downloader.query(sql)
        df.to_csv(path, sep=",", index=False)
        
    return df