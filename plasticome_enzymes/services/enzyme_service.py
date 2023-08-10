from plasticome_enzymes.models.enzyme_model import FungiEnzyme


def save_enzyme(enzyme: str, ec_number: str):
    """
    Save an enzyme in the database.

    Parameters:
        enzyme (str): The name of the enzyme to be saved.
        ec_number (str): The associated EC number of the enzyme.

    Returns:
        None
    """
    try:
        saved_enzyme = FungiEnzyme.create(enzyme=enzyme, ec_number=ec_number)
        return saved_enzyme.__data__, None
    except Exception as error:
        return None, error


def search_enzyme_by_ec_number(ec_number: str):
    """
    Search an enzyme in the database.

    Parameters:
        ec_number (str): The EC number of the enzyme.

    Returns:
        enzyme_name: The name of the enzyme searched
    """
    try:
        enzyme = (
            FungiEnzyme.select()
            .where(FungiEnzyme.ec_number == ec_number)
            .get()
        )
        return enzyme.__data__, None
    except Exception as error:
        return None, error