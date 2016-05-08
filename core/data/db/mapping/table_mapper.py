import xml.etree.ElementTree as ET
import os

'''
    Parses XML.
    Returns table mappings

'''

dirname = os.path.dirname(__file__)
base_path = dirname + '/xml/'


def get_mappings(source, table):
    path = base_path + source.value + ".xml"

    tree = ET.parse()
    root = tree.getroot()
