#ecoding=utf-8
# author:herui
# time:2020/7/10 17:56
# function:

def test_xpath():
    import xml.etree.ElementTree as ET
    # tree = ET.parse('xml_data.xml')
    root = ET.fromstring('<?xml version="1.0"?><node a="1"></node>')
    print((root.findall(".//node")))

def test_lxml_xpath():
    from lxml import etree
    # html = etree.Element("xml_data.xml")
    text='''<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>'''
    # html = etree.HTML(text)
    # print(len(html.xpath("//neighbor")))
    xml = etree.XML(text)
    print(len(xml.xpath("//neighbor")))

