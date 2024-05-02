import pandas as pd
import xml.etree.cElementTree as ET

tree = ET.parse(r"arquivos.xml")
root = tree.getroot()

def getvalueofnode(node):
    """ return node text or None """
    return node.text if node is not None else None


def main():
    """ main """
    parsed_xml = tree
    dfcols = ['account', 'total']
    df_xml = pd.DataFrame(columns=dfcols)


for node in parsed_xml.getroot():
    account = node.attrib.get('Type="String"')
    

    df_xml = df_xml.append(
        pd.Series([account, getvalueofnode(total)], index=dfcols),
        ignore_index=True)

print(df_xml)


main()