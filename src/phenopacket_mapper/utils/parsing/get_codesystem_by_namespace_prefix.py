from typing import List, Optional

from phenopacket_mapper.data_standards import CodeSystem


def get_codesystem_by_namespace_prefix(namespace_prefix_str: str, resources: List[CodeSystem]) -> Optional[CodeSystem]:
    """
    Returns the CodeSystem object that matches the namespace prefix string. If no match is found, returns None.

    :param namespace_prefix_str: The namespace prefix string to match
    :param resources: The list of CodeSystem objects to search through
    :return: The CodeSystem object that matches the namespace prefix string, or None if no match is found
    """
    if resources:
        for res in resources:
            potential_matches = [res.namespace_prefix.lower(), res.name.lower(), *(s.lower() for s in res.synonyms)]
            if namespace_prefix_str.lower() in potential_matches:
                return res
