from typing import List, Union, Any

from rarelink_phenopacket_mapper.data_standards import CodeSystem, Date

synonyms = {
    str: ["str", "string"],
    int: ["int", "integer"],
    float: ["float", "double"],
    bool: ["boolean", "bool"],
    Date: ["date", "dd/mm/yyyy", "mm/yyyy", "yyyy", "dd-mm-yyyy", "mm-yyyy"]
}


def parse_string_type_representation(type_str: str, resources: List[CodeSystem]) -> List[Union[Any, CodeSystem, type]]:
    """Parses a string representing of one or multiple data types or code systems to a list of `type` in Python

    The purpose of this method is to parse entries in a Data Model tabular file for `DataField.data_type`. In the
    tabular file, the user can list typical primitive data types such as string, int, etc., or date as a data type.
    Further is it possible to list the name space prefix (e.g., "SCT" for SNOMED CT) of a specific resource (given its
    inclusion in the list passed as the `resources` parameter) to indicate that codes or terms from that resource are
    permittable.

    E.g.
    >>> parse_string_type_representation("integer, str, Boolean")
    [int, str, bool]

    :param type_str:
    :param resources:
    :return:
    """
    if not type_str or not type_str.strip():  # checks for all sorts of empty strings, with however many white spaces
        return [Any]

    single_type_strings = type_str.split(',')
    types = []
    for single in single_type_strings:
        types.append(_parse_single_string_type_repr(type_str=single, resources=resources))

    if not types:
        return [Any]

    return types


def _parse_single_string_type_repr(type_str: str, resources: List[CodeSystem]) -> Union[Any, CodeSystem, type]:
    """Parses a string representing a data type to the `type` in Python

    E.g.:
    >>> _parse_single_string_type_repr('date', [])
    Date

    :param type_str:
    :param resources:
    :return:
    """
    if " " in type_str:
        type_str = type_str.replace(" ", "")

    if resources:
        for res in resources:
            print()
            if type_str.lower() in [res.namespace_prefix.lower(), res.name.lower(), *(s.lower() for s in res.synonyms)]:
                return res

    for type_ in synonyms.keys():
        for syn in synonyms[type_]:
            if syn.lower() == type_str.lower():
                return type_

    # if nothing has matched
    raise ValueError(f"No matching data types or resources could be found for '{type_str}'")
