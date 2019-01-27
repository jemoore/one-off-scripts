# writes entries in .opml file to an org file
# replace the .opml file name below

import xml.etree.ElementTree as ET
tree = ET.parse('YOUR-FILE-HERE.opml')
root = tree.getroot()

def parseOPML():

    catalog = {}
    # { category: [feed entry list] } where feed entry list = {title: "X', xmlUrl: "Y", htmlUrl: "Z"}

    for item in root.findall('./body'):
        for category in item:
            feedlist = []
            for feed in category:
                entry = {}
                entry['title'] = feed.attrib['title']
                entry['xmlUrl'] = feed.attrib['xmlUrl']
                entry['htmlUrl'] = feed.attrib['htmlUrl']
                feedlist.append(entry)
            catalog[category.attrib['title']] = feedlist

    return catalog

def writeOrgFile(catalog):
    filename = './elfeed.org'
    with open(filename, 'w') as f:
        for category in catalog:
            f.write('* ' + category + '\n')
            for i in range(0, len(catalog[category])):
                f.write('** [[' + catalog[category][i]['xmlUrl'] + '][' + catalog[category][i]['title'] + ']]\n')
                f.write('*** [[' + catalog[category][i]['htmlUrl'] + ']]\n')

def main():
    feeds = parseOPML()
    writeOrgFile(feeds)

    for k in feeds:
        print(k)
        for i in range(0, len(feeds[k])):
            print('\t -- ' + feeds[k][i]['title'])

if __name__ == "__main__":
    main()
