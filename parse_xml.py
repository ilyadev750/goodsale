from lxml import etree

ROOT = None
CATEGORY_LV_0 = None
CATEGORIES_LV_1 = {}
CATEGORIES_LV_2 = {}
CATEGORIES_LV_3 = {}
CATEGORIES_REMAINING = {}


def parseXML(xmlFile):
    """
    Парсинг XML
    """
    with open(xmlFile, 'rb') as fobj:
        xml = fobj.read()

    parser = etree.XMLParser(recover=True)
    root = etree.fromstring(xml, parser=parser)
    
    for appt in root.getchildren():
        for elem in appt.getchildren():
            if elem.tag == 'categories':
                for e in elem.getchildren():
                    parent_key = e.get('parentId')
                    child_key = e.get('id')
                    if not parent_key:
                        ROOT = child_key
                    elif parent_key == ROOT:
                        CATEGORIES_LV_1[child_key] = e.text
                    elif CATEGORIES_LV_1.get(parent_key):
                        CATEGORIES_LV_2[child_key] = e.text
                    elif CATEGORIES_LV_2.get(parent_key):
                        CATEGORIES_LV_3[child_key] = e.text
                    elif CATEGORIES_LV_3.get(parent_key):
                        CATEGORIES_REMAINING[child_key] = e.text
                    elif CATEGORIES_REMAINING.get(parent_key):
                        CATEGORIES_REMAINING[child_key] = CATEGORIES_REMAINING[parent_key] + '/' + e.text
                        print(CATEGORIES_REMAINING[child_key])

            # elif not elem.text:
            #     text = "None"
            # else:
            #     text = elem.text
            
            # print(elem.tag + " => " + text)
    # print(CATEGORIES_LV_1)
    # print(CATEGORIES_LV_2)
    # print(CATEGORIES_LV_3)
    print(CATEGORIES_REMAINING)


if __name__ == "__main__":
    parseXML("elektronika_products.xml")