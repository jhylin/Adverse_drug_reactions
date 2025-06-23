import chembl_downloader
from textwrap import dedent
from typing import Optional

def chembl_targets(*target: str,): #file_name: Optional[str] = None):

    """
    Obtain approved drugs' ChEMBL IDs, generic drug/small molecule names, max phases and canonical SMILES,
    protein target CHEMBL IDs
    via using drug names only with an option to save dataframe as tsv files

    :param target: Enter protein target CHEMBL ID e.g. CHEMBL1234 to search in ChEMBL database
    :param file_name: Enter file name if needed in order to save dataframe as a .tsv file in working directory
    :return: A dataframe of small molecules/drugs derived from ChEMBL database 
    along with their ChEMBL IDs, max phases and canonical SMILES
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

    # default query uses the latest ChEMBL version (using version 34 in the meantime)
    df = chembl_downloader.query(sql, version="34")

    return df

    ## TODO: may try incorporating previous pathlib code below to save data or using the simple version below
    # if file_name == None:
    #     return df
    # else:
    #     # save df as .tsv files if a file name is added
    #     df.to_csv(f"{file_name}.tsv", sep='\t', index=False)
    #     return df
    
