from pathlib import Path
from typing import Union, Dict
import xml.etree.ElementTree as ET


def read_xml(path: Union[str, Path]) -> Dict:
    if isinstance(path, str):
        path = Path(path)

    tree = ET.parse(path)
    root = tree.getroot()

    def xml_to_dict(element):  # recursive
        if len(element) == 0:
            return element.text
        return {element.tag: {child.tag: xml_to_dict(child) for child in element}}

    return xml_to_dict(root)