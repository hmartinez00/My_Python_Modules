import xml.etree.ElementTree as ET

from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom

import unicodedata

def remove_accents(value):
    normalized_value = unicodedata.normalize('NFKD', value)
    without_accents = ''.join(c for c in normalized_value if not unicodedata.combining(c))
    return without_accents


def prettify(__elem__):
    """Return a pretty-printed XML string for the Element.
    """
    __rough_string__ = ElementTree.tostring(__elem__, 'utf-8')
    __reparsed__ = minidom.parseString(__rough_string__)
    return __reparsed__.toprettyxml(indent="  ")