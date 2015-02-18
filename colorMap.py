# Grab an svg and create a random color map.
# county.svg file source  : http://commons.wikimedia.org/wiki/File:Usa_counties_large.svg
#
# 2014.21.02
# AMS


from randomhexcolor import randomhexcolor
from BeautifulSoup import BeautifulSoup

xml = open('county.svg').read()
doc = BeautifulSoup(xml, selfClosingTags = ['defs','sodipodi:namedview'])

paths = doc.findAll('path')

styleprefix = '"font-size:12px;fill:'
stylesuffix = ';fill-rule:nonzero;stroke:#000000;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel"'
for path in paths:
	if path['id'] not in ['State_Lines', 'separator']:
		path['style'] = styleprefix + randomhexcolor(0.5) + stylesuffix
        
        f = open('coloredmap.svg', 'w')
print >> f, doc.prettify()
f.close()
