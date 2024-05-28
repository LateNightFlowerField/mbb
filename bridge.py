from sympy.plotting.plot import flat
import tikz
from math import sin, cos, pi, sqrt, atan
from difflib import SequenceMatcher
import argparse
import sympy
from sympy import atan as satan
from sympy import sin as ssin
from sympy import cos as scos
import pathlib


def figdesc(name,pieces,volume,weight,totallength) -> tikz.node:
    return tikz.node(at=(length/2,-0.5),contents=f"Type:\\,{name}\\quad Pieces:\\,{pieces}\\quad Volume:\\,{volume:.2f}\\quad Weight:\\,{weight:.2f}g\\quad Total Length of Segments:\\,{totallength:.2f}cm")

def globalopt(localopts='') -> str|None:
    if args.options == '' and localopts == '':
        return None
    return ",".join([args.options,localopts])


def bailey() -> None:
    seglen = (length-(segments+1)*width)/segments
    ljoint = width*sin(pi/4)
    triside = (seglen/2)-ljoint
    pieces = 3+5*segments
    area = width*(length+lover+rover)+length*width+seglen*length-segments*pow(triside*2,2)
    volume = area*width
    weight = volume * wooddensity + bonus_weight * pieces
    woodlength = 2*length+lover+rover+seglen*(segments+1)+4*segments*(cos(pi/4)*ljoint*2+triside/cos(pi/4)) + bonus_length * pieces
    #Bottom Beam
    pic.draw(tikz.line([(0-lover,0),
                        (length+rover,0),
                        (length+rover,width),
                        (0-lover,width),
                        tikz.cycle()]),opt=globalopt())

    #Beams
    for segnum in range(segments+1):
        offset = segnum*(width+seglen)
        pic.draw(tikz.line([(0+offset,width),
                            (width+offset,width),
                            (width+offset,width+seglen),
                            (0+offset,width+seglen),
                            tikz.cycle()]),opt=globalopt())

    #Squares
    for segnum in range(segments):
        bloffset = width*(segnum+1)+triside+seglen*segnum
        broffset = width*(segnum+1)+seglen-triside+seglen*segnum
        pic.draw(tikz.line([(bloffset,width),
                            (bloffset-triside,width+triside),
                            (bloffset-triside,width+triside+ljoint),
                            (bloffset-triside+ljoint,width+triside+ljoint),
                            (bloffset+ljoint,width+ljoint),
                            (bloffset+ljoint,width),
                            tikz.cycle()]),opt=globalopt())
        pic.draw(tikz.line([(broffset,width),
                            (broffset+triside,width+triside),
                            (broffset+triside,width+triside+ljoint),
                            (broffset+triside-ljoint,width+triside+ljoint),
                            (broffset-ljoint,width+ljoint),
                            (broffset-ljoint,width),
                            tikz.cycle()]),opt=globalopt())
        pic.draw(tikz.line([(bloffset,width+seglen),
                            (bloffset-triside,width+seglen-triside),
                            (bloffset-triside,width+seglen-triside-ljoint),
                            (bloffset-triside+ljoint,width+seglen-triside-ljoint),
                            (bloffset+ljoint,width+seglen-ljoint),
                            (bloffset+ljoint,width+seglen),
                            tikz.cycle()]),opt=globalopt())
        pic.draw(tikz.line([(broffset,width+seglen),
                            (broffset+triside,width+seglen-triside),
                            (broffset+triside,width+seglen-triside-ljoint),
                            (broffset+triside-ljoint,width+seglen-triside-ljoint),
                            (broffset-ljoint,width+seglen-ljoint),
                            (broffset-ljoint,width+seglen),
                            tikz.cycle()]),opt=globalopt())
        
    #Top Beam
    pic.draw(tikz.line([(0,width+seglen),
                        (length,width+seglen),
                        (length,2*width+seglen),
                        (0,2*width+seglen),
                        (0,width+seglen),
                        tikz.cycle()]),opt=globalopt())
    if not args.no_description:
        pic.path(figdesc("Bailey Truss",pieces,volume,weight,woodlength))
    
    if spill:
        print(locals())

def howe() -> None:
    flatjoint = width/cos(pi/4)
    ljoint = width*cos(pi/4)
    triside = (length-2*flatjoint-width*(segments-1)-ljoint*(segments-2))/segments
    seglen = triside + ljoint
    toplen = length-2*(flatjoint+triside-ljoint)
    pieces = 5 + (segments-2)*2
    area = (length+lover+rover)*width+toplen*width+0.5*(toplen+length)*seglen-pow(triside,2)*(segments-1)
    volume = area*width
    weight = volume*wooddensity + bonus_weight*pieces
    woodlength = length+lover+rover+toplen+2*(triside/cos(pi/4)+flatjoint*cos(pi/4)+ljoint/cos(pi/4))+(segments-1)*seglen+(segments-2)*(triside/cos(pi/4)+2*ljoint/cos(pi/4)) + bonus_length*pieces

    #Bottom Beam
    pic.draw(tikz.line([(-lover,0),
                        (length+rover,0),
                        (length+rover,width),
                        (-lover,width),
                        tikz.cycle()]),opt=globalopt())

    #Left End Post
    pic.draw(tikz.line([(0,width),
                        (seglen,width+seglen),
                        (seglen+ljoint,width+seglen),
                        (seglen+ljoint,width+seglen-ljoint),
                        (flatjoint,width),
                        tikz.cycle()]),opt=globalopt())

    #Right End Post
    pic.draw(tikz.line([(length,width),
                        (length-seglen,width+seglen),
                        (length-seglen-ljoint,width+seglen),
                        (length-seglen-ljoint,width+seglen-ljoint),
                        (length-flatjoint,width),
                        tikz.cycle()]),opt=globalopt())

    #Beams
    for segnum in range(segments-1):
        offset = (triside+width+ljoint)*segnum+flatjoint+triside
        pic.draw(tikz.line([(offset,width),
                            (offset,width+seglen),
                            (offset+width,width+seglen),
                            (offset+width,width),
                            tikz.cycle()]),opt=globalopt())
    #Diagonal Beams
    for segnum in range(segments//2-1):
        offset = flatjoint+triside+width+ljoint+segnum*(triside+width+ljoint)
        pic.draw(tikz.line([(offset,width),
                            (offset+triside,width+triside),
                            (offset+triside,width+triside+ljoint),
                            (offset+triside-ljoint,width+triside+ljoint),
                            (offset-ljoint,width+ljoint),
                            (offset-ljoint,width),
                            tikz.cycle()]),opt=globalopt())
        pic.draw(tikz.line([(length-offset,width),
                            (length-offset-triside,width+triside),
                            (length-offset-triside,width+triside+ljoint),
                            (length-offset-triside+ljoint,width+triside+ljoint),
                            (length-offset+ljoint,width+ljoint),
                            (length-offset+ljoint,width),
                            tikz.cycle()]),opt=globalopt())

    #Top Beam
    pic.draw(tikz.line([(flatjoint+triside-ljoint,width+triside+ljoint),
                        (flatjoint+triside-ljoint+toplen,width+triside+ljoint),
                        (flatjoint+triside-ljoint+toplen,width+triside+ljoint+width),
                        (flatjoint+triside-ljoint,width+triside+ljoint+width),
                        tikz.cycle()]),opt=globalopt())
    if do_supports:
        supports((toplen-width)/(segments-2),sup_height,1,segments-2)
    if not args.no_description:
        pic.path(figdesc("Howe Truss",pieces,volume,weight,woodlength))
    if spill:
        print(locals())

def pratt() -> None:
    flatjoint = width/cos(pi/4)
    ljoint = width*cos(pi/4)
    triside = (length-2*flatjoint-width*(segments-1)-ljoint*(segments-2))/segments
    seglen = triside + ljoint
    toplen = length-2*(flatjoint+triside-ljoint)
    adjdist = (segments/2-1)*(triside+ljoint+width)

    pieces = 5 + (segments-2)*2
    area = (length+lover+rover)*width+toplen*width+(0.5*(toplen+length)*seglen-pow(triside,2)*(segments-1))
    volume = area*width
    weight = volume*wooddensity + bonus_weight*pieces
    woodlength = length+lover+rover+toplen+2*(triside/cos(pi/4)+flatjoint*cos(pi/4)+ljoint/cos(pi/4))+(segments-1)*seglen+(segments-2)*(triside/cos(pi/4)+2*ljoint/cos(pi/4)) + bonus_length*pieces
    #Bottom Beam
    pic.draw(tikz.line([(-lover,0),
                        (length+rover,0),
                        (length+rover,width),
                        (-lover,width),
                        tikz.cycle()]),opt=globalopt())

    #Left End Post
    pic.draw(tikz.line([(0,width),
                        (seglen,width+seglen),
                        (seglen+ljoint,width+seglen),
                        (seglen+ljoint,width+seglen-ljoint),
                        (flatjoint,width),
                        tikz.cycle()]),opt=globalopt())

    #Right End Post
    pic.draw(tikz.line([(length,width),
                        (length-seglen,width+seglen),
                        (length-seglen-ljoint,width+seglen),
                        (length-seglen-ljoint,width+seglen-ljoint),
                        (length-flatjoint,width),
                        tikz.cycle()]),opt=globalopt())

    #Beams
    for segnum in range(segments-1):
        offset = (triside+width+ljoint)*segnum+flatjoint+triside
        pic.draw(tikz.line([(offset,width),
                            (offset,width+seglen),
                            (offset+width,width+seglen),
                            (offset+width,width),
                            tikz.cycle()]),opt=globalopt())
    #Diagonal Beams
    for segnum in range(segments//2-1):
        offset = flatjoint+triside+width+ljoint+segnum*(triside+width+ljoint)+adjdist
        pic.draw(tikz.line([(offset,width),
                            (offset+triside,width+triside),
                            (offset+triside,width+triside+ljoint),
                            (offset+triside-ljoint,width+triside+ljoint),
                            (offset-ljoint,width+ljoint),
                            (offset-ljoint,width),
                            tikz.cycle()]),opt=globalopt())
        pic.draw(tikz.line([(length-offset,width),
                            (length-offset-triside,width+triside),
                            (length-offset-triside,width+triside+ljoint),
                            (length-offset-triside+ljoint,width+triside+ljoint),
                            (length-offset+ljoint,width+ljoint),
                            (length-offset+ljoint,width),
                            tikz.cycle()]),opt=globalopt())

    #Top Beam
    pic.draw(tikz.line([(flatjoint+triside-ljoint,width+triside+ljoint),
                        (flatjoint+triside-ljoint+toplen,width+triside+ljoint),
                        (flatjoint+triside-ljoint+toplen,width+triside+ljoint+width),
                        (flatjoint+triside-ljoint,width+triside+ljoint+width),
                        tikz.cycle()]),opt=globalopt())
    if do_supports:
        supports((toplen-width)/(segments-2),sup_height,1,segments-2)
    if not args.no_description:
        pic.path(figdesc("Pratt Truss",pieces,volume,weight,woodlength))
    if spill:
        print(locals())

def warren() -> None:
    ljoint = width/(sin(pi/3)+sin(pi/6))
    triside = (length-2*width/cos(pi/6)-(segments-1)*2*ljoint)/segments
    flatjoint = width/cos(pi/6)
    toplen = (segments-1)*(2*ljoint+triside)+2*ljoint
    triheight = triside*sin(pi/3)
    trilen = triside*cos(pi/3)
    pieces = 2+segments*2
    area = (length+lover+rover)*width+toplen*width+(0.5*(toplen+length)*(triheight+ljoint)-(sqrt(3)/4)*pow(triside,2)*(segments*2-1))
    volume = area*width
    weight = volume*wooddensity + bonus_weight*pieces
    woodlength = lover+rover+length+toplen+2*segments*(triside+ljoint*(cos(pi/6)+sin(pi/6))) + bonus_length*pieces

    #Bottom Beam
    pic.draw(tikz.line([(0-lover,0),
                        (length+rover,0),
                        (length+rover,width),
                        (0-lover,width),
                        tikz.cycle()]),opt=globalopt())

    #Right Post
    pic.draw(tikz.line([(flatjoint,width),
                        (flatjoint+trilen,width+triheight),
                        (flatjoint+trilen,width+triheight+ljoint),
                        (flatjoint+trilen-ljoint,width+triheight+ljoint),
                        (0,width),
                        tikz.cycle()]),opt=globalopt())
    pic.draw(tikz.line([(length-flatjoint,width),
                        (length-flatjoint-trilen,width+triheight),
                        (length-flatjoint-trilen,width+triheight+ljoint),
                        (length-flatjoint-trilen+ljoint,width+triheight+ljoint),
                        (length,width),
                        tikz.cycle()]),opt=globalopt())

    #Posts
    for segmentnum in range(1,segments):
        loffset = triside*segmentnum+2*ljoint*(segmentnum-1)+flatjoint
        roffset = loffset+2*ljoint
        pic.draw(tikz.line([(loffset,width),
                            (loffset-trilen,width+triheight),
                            (loffset-trilen,width+triheight+ljoint),
                            (loffset-trilen+ljoint,width+triheight+ljoint),
                            (loffset+ljoint,width+ljoint),
                            (loffset+ljoint,width),
                            tikz.cycle()]),opt=globalopt())
        pic.draw(tikz.line([(roffset,width),
                            (roffset+trilen,width+triheight),
                            (roffset+trilen,width+triheight+ljoint),
                            (roffset+trilen-ljoint,width+triheight+ljoint),
                            (roffset-ljoint,width+ljoint),
                            (roffset-ljoint,width),
                            tikz.cycle()]),opt=globalopt())
        
    #Top
    pic.draw(tikz.line([(trilen+flatjoint-ljoint,ljoint+width+triheight),
                        (trilen+toplen+flatjoint-ljoint,ljoint+width+triheight),
                        (trilen+toplen+flatjoint-ljoint,ljoint+2*width+triheight),
                        (trilen+flatjoint-ljoint,ljoint+2*width+triheight),
                        (trilen+flatjoint-ljoint,ljoint+width+triheight)
                        ,tikz.cycle()]),opt=globalopt())
    if do_supports:
        supports((toplen-width)/(segments-1),sup_height,1,segments-1)
    if not args.no_description:
        pic.path(figdesc("Warren Truss",pieces,volume,weight,woodlength))
    if spill:
        print(locals())

def k() -> None:
    bigt = atan(ratio)
    flatjoint = width/sin(bigt)
    bljoint = width/(sin(bigt)+cos(bigt))
    x = sympy.symbols('x')
    seglen = (length-width*(segments-1))/segments
    height = ratio*seglen
    meq = sympy.Eq((ssin(satan((height-x)/(seglen-x)))+scos(satan((height-x)/(seglen-x))))*x,width)
    suls = sympy.solveset(meq,x,domain=sympy.S.Reals)
    ljoint = min(suls)
    pieces = 4+segments-1+(segments-2)*2
    area = (length+lover+rover)*width+(length-2*seglen+bljoint*2)*width+0.5*(length+length-2*seglen+2*bljoint)*height-(seglen-ljoint)*(height-2*ljoint)*(segments-2)-(seglen-flatjoint)*(height-bljoint)
    volume = area * width
    weight = volume * wooddensity + bonus_weight*pieces
    botang = atan((height/2-ljoint)/(seglen-ljoint))
    bigbotang = atan((height-bljoint)/(seglen-flatjoint))
    bigsegend = bljoint/sin(bigbotang)+cos(bigbotang)*bljoint
    segend = (sin(botang)+cos(botang))*ljoint
    trihyp = sqrt(pow(height/2-ljoint,2)+pow(seglen-ljoint,2))
    bigtrihyp = sqrt(pow(height-bljoint,2)+pow(seglen-flatjoint,2))
    woodlength = length+lover+rover+length-2*seglen+2*bljoint+(segments-2)*2*(trihyp+segend)+height*(segments-1)+2*(bigtrihyp+bigsegend) + bonus_length*pieces

    #Bottom Beam
    pic.draw(tikz.line([(-lover,0),
                        (length+rover,0),
                        (length+rover,width),
                        (-lover,width),
                        tikz.cycle()]),opt=globalopt())
    
    #End Posts
    pic.draw(tikz.line([(0,width),
                        (flatjoint,width),
                        (seglen,width+height-bljoint),
                        (seglen,width+height),
                        (seglen-bljoint,width+height),
                        tikz.cycle()]),opt=globalopt())
    pic.draw(tikz.line([(length,width),
                        (length-flatjoint,width),
                        (length-seglen,width+height-bljoint),
                        (length-seglen,width+height),
                        (length-seglen+bljoint,width+height),
                        tikz.cycle()]),opt=globalopt())
   
    #Beams
    for segnum in range(segments-1):
        offset = seglen+(width+seglen)*segnum
        pic.draw(tikz.line([(offset,width),
                            (offset,width+height),
                            (offset+width,width+height),
                            (offset+width,width),
                            tikz.cycle()]),opt=globalopt())

    #Left Ks
    for segnum in range(segments-2-(segments-2)//2):
        offset = width+seglen+(width+seglen)*segnum
        pic.draw(tikz.line([(offset,width+height/2),
                            (offset+ljoint,width+height/2),
                            (offset+seglen,width+height/2-ljoint+height/2),
                            (offset+seglen,width+height/2+height/2),
                            (offset+seglen-ljoint,width+height/2+height/2),
                            (offset,width+ljoint+height/2),
                            tikz.cycle()]),opt=globalopt())
        pic.draw(tikz.line([(offset,width+height/2),
                            (offset,width+height/2-ljoint),
                            (offset+seglen-ljoint,width),
                            (offset+seglen,width),
                            (offset+seglen,width+ljoint),
                            (offset+ljoint,width+height/2),
                            tikz.cycle()]),opt=globalopt())

    #Right Ks
    for segnum in range(segments-2-(segments-2)//2):
        offset = -(width+seglen+(width+seglen)*segnum)+length
        pic.draw(tikz.line([(offset,width+height/2),
                            (offset-ljoint,width+height/2),
                            (offset-seglen,width+height-ljoint),
                            (offset-seglen,width+height),
                            (offset-seglen+ljoint,width+height),
                            (offset,width+ljoint+height/2),
                            tikz.cycle()]),opt=globalopt())
        pic.draw(tikz.line([(offset,width+height/2),
                            (offset,width+height/2-ljoint),
                            (offset-seglen+ljoint,width),
                            (offset-seglen,width),
                            (offset-seglen,width+ljoint),
                            (offset-ljoint,width+height/2),
                            tikz.cycle()]),opt=globalopt())

    #Top Beam
    pic.draw(tikz.line([(seglen-bljoint,width+height),
                        (length-seglen+bljoint,width+height),
                        (length-seglen+bljoint,2*width+height),
                        (seglen-bljoint,2*width+height),
                        tikz.cycle()]),opt=globalopt())
    toplen = length-2*seglen+2*bljoint
    if do_supports:
        supports((toplen-width)/(segments-2),sup_height,1,segments-2)
    if not args.no_description:
        pic.path(figdesc("K Truss",pieces,volume,weight,woodlength))
    if spill:
        print(locals())

def baltimore() -> None:
    flatjoint = width/cos(pi/4)
    ljoint = width*cos(pi/4)
    triside = (length-2*flatjoint-width*(segments-1)-ljoint*(segments-2))/segments
    seglen = triside + ljoint
    toplen = length-2*(flatjoint+triside-ljoint)
    adjdist = (segments/2-1)*(triside+ljoint+width)

    pieces = 5 + (segments-2)*2+2*segments
    area = (length+lover+rover)*width+toplen*width+(0.5*(toplen+length)*seglen-(segments-2)*pow(triside,2)*0.5-segments*pow(triside-ljoint,2)/4-segments*pow((triside-ljoint-width)/2,2))
    volume = area*width
    weight = volume*wooddensity + bonus_weight*pieces
    woodlength = length+lover+rover+toplen+2*(triside/cos(pi/4)+flatjoint*cos(pi/4)+ljoint/cos(pi/4))+(segments-1)*seglen+(segments-2)*(triside/cos(pi/4)+2*ljoint/cos(pi/4))+ljoint*sin(pi/4)*segments*2+segments*(seglen/2-ljoint-ljoint*cos(pi/4))+segments*((triside/2-width/2-ljoint/2)/cos(pi/4)) + bonus_length*pieces
    #Bottom Beam
    pic.draw(tikz.line([(-lover,0),
                        (length+rover,0),
                        (length+rover,width),
                        (-lover,width),
                        tikz.cycle()]),opt=globalopt())

    #Left End Post
    pic.draw(tikz.line([(0,width),
                        (seglen,width+seglen),
                        (seglen+ljoint,width+seglen),
                        (seglen+ljoint,width+seglen-ljoint),
                        (flatjoint,width),
                        tikz.cycle()]),opt=globalopt())
    #Left Post Small diagonal
    pic.draw(tikz.line([(flatjoint+triside,width),
                        (flatjoint+triside,width+ljoint),
                        (flatjoint+triside-seglen/2+ljoint,width+seglen/2),
                        (flatjoint+triside-seglen/2,width+seglen/2-ljoint),
                        (flatjoint+triside-ljoint,width),
                        tikz.cycle()]),opt=globalopt())
    #Left post beam
    pic.draw(tikz.line([(flatjoint+triside-seglen/2-width/2,width),
                        (flatjoint+triside-seglen/2-width/2,width+seglen/2-ljoint-ljoint*cos(pi/4)),
                        (flatjoint+triside-seglen/2,width+seglen/2-ljoint),
                        (flatjoint+triside-seglen/2+width/2,width+seglen/2-ljoint-ljoint*cos(pi/4)),
                        (flatjoint+triside-seglen/2+width/2,width),
                        tikz.cycle()]),opt=globalopt())

    #Right End Post
    pic.draw(tikz.line([(length,width),
                        (length-seglen,width+seglen),
                        (length-seglen-ljoint,width+seglen),
                        (length-seglen-ljoint,width+seglen-ljoint),
                        (length-flatjoint,width),
                        tikz.cycle()]),opt=globalopt())
    #Right Post Small diagonal
    pic.draw(tikz.line([(length-flatjoint-triside,width),
                        (length-flatjoint-triside,width+ljoint),
                        (length-flatjoint-triside+seglen/2-ljoint,width+seglen/2),
                        (length-flatjoint-triside+seglen/2,width+seglen/2-ljoint),
                        (length-flatjoint-triside+ljoint,width),
                        tikz.cycle()]),opt=globalopt())
    #Right post beam
    pic.draw(tikz.line([(length-flatjoint-triside+seglen/2+width/2,width),
                        (length-flatjoint-triside+seglen/2+width/2,width+seglen/2-ljoint-ljoint*cos(pi/4)),
                        (length-flatjoint-triside+seglen/2,width+seglen/2-ljoint),
                        (length-flatjoint-triside+seglen/2-width/2,width+seglen/2-ljoint-ljoint*cos(pi/4)),
                        (length-flatjoint-triside+seglen/2-width/2,width),
                        tikz.cycle()]),opt=globalopt())
    #Beams
    for segnum in range(segments-1):
        offset = (triside+width+ljoint)*segnum+flatjoint+triside
        pic.draw(tikz.line([(offset,width),
                            (offset,width+seglen),
                            (offset+width,width+seglen),
                            (offset+width,width),
                            tikz.cycle()]),opt=globalopt())
    #Diagonal Beams
    for segnum in range(segments//2-1):
        offset = flatjoint+triside+width+ljoint+segnum*(triside+width+ljoint)+adjdist
        pic.draw(tikz.line([(offset,width),
                            (offset+triside,width+triside),
                            (offset+triside,width+triside+ljoint),
                            (offset+triside-ljoint,width+triside+ljoint),
                            (offset-ljoint,width+ljoint),
                            (offset-ljoint,width),
                            tikz.cycle()]),opt=globalopt())
        pic.draw(tikz.line([(length-offset,width),
                            (length-offset-triside,width+triside),
                            (length-offset-triside,width+triside+ljoint),
                            (length-offset-triside+ljoint,width+triside+ljoint),
                            (length-offset+ljoint,width+ljoint),
                            (length-offset+ljoint,width),
                            tikz.cycle()]),opt=globalopt())
    #double diagonals
    for segnum in range(segments//2-1):
        offset = flatjoint+triside+width+segnum*(seglen+width)
        pic.draw(tikz.line([(offset,width),
                            (offset,width+ljoint),
                            (offset+seglen/2-ljoint,width+seglen/2),
                            (offset+seglen/2,width+seglen/2-ljoint),
                            (offset+ljoint,width),
                            tikz.cycle()]),opt=globalopt())
        pic.draw(tikz.line([(length-offset,width),
                            (length-offset,width+ljoint),
                            (length-offset-seglen/2+ljoint,width+seglen/2),
                            (length-offset-seglen/2,width+seglen/2-ljoint),
                            (length-offset-ljoint,width),
                            tikz.cycle()]),opt=globalopt())
    #Small Beams
    for segnum in range(segments-2):
        offset = flatjoint+triside+width+seglen/2-width/2+segnum*(seglen+width)
        pic.draw(tikz.line([(offset,width),
                            (offset,width+seglen/2-ljoint-ljoint*cos(pi/4)),
                            (offset+width/2,width+seglen/2-ljoint),
                            (offset+width,width+seglen/2-ljoint-ljoint*cos(pi/4)),
                            (offset+width,width),
                            tikz.cycle()]),opt=globalopt())
    #Top Beam
    pic.draw(tikz.line([(flatjoint+triside-ljoint,width+triside+ljoint),
                        (flatjoint+triside-ljoint+toplen,width+triside+ljoint),
                        (flatjoint+triside-ljoint+toplen,width+triside+ljoint+width),
                        (flatjoint+triside-ljoint,width+triside+ljoint+width),
                        tikz.cycle()]),opt=globalopt())
    if not args.no_description:
        pic.path(figdesc("Baltimore",pieces,volume,weight,woodlength))
    if spill:
        print(locals())
    if do_supports:
        supports((toplen-width)/(segments-2),sup_height,1,segments-2)

def supports(spacing, height, direction, number):
    for segnum in range(number+1):
        offset = segnum*spacing
        suppic.draw(tikz.line([(offset,0),(offset,height),(offset+width,height),(offset+width,0),tikz.cycle()]),opt=globalopt())
    x = sympy.symbols('x')
    meq = sympy.Eq((ssin(satan((height-x)/(spacing-x-width)))+scos(satan((height-x)/(spacing-x-width))))*x,width)
    suls = sympy.solveset(meq,x,domain=sympy.S.Reals)
    ljoint = min(suls)
    for segnum in range(number):
        offset = segnum*spacing+width
        if direction == 1:
            suppic.draw(tikz.line([(offset,0),(offset,ljoint),(offset+spacing-width-ljoint,height),(offset+spacing-width,height),(offset+spacing-width,height-ljoint),(offset+ljoint,0),tikz.cycle()]),opt=globalopt())
        if direction == -1:
            suppic.draw(tikz.line([(offset+spacing-width,0),(offset+spacing-width-ljoint,0),(offset,height-ljoint),(offset,height),(offset+ljoint,height),(offset+spacing-width,ljoint),tikz.cycle()]),opt=globalopt())
    if spill:
        print(locals())



if __name__ == "__main__":
    bridge_types = ['howe','warren','pratt','bailey','k','baltimore']
    bridge_map = {'howe':howe, 'warren':warren, 'pratt':pratt, 'bailey':bailey,'k':k, 'baltimore':baltimore}

    parser = argparse.ArgumentParser(prog='mmb',description='Create scale diagrams for bridges.')
    parser.add_argument('-t','--bridge',type=str,default=None, help='type of bridge')
    parser.add_argument('-w','--width',default=0.238,type=float, help='width of material in cm')
    parser.add_argument('-l','--length',default=24,type=float, help='length of bridge in cm')
    parser.add_argument('-s','--segments',default=6,choices=range(1,16),type=int, help='number of bridge segments')
    parser.add_argument('-o','--overhang',default=[1.0],type=float,nargs='+', help='overhang on both ends in cm') 
    parser.add_argument('-r','--ratio',default=4/3,type=float, help='ratio of segment length to height')
    parser.add_argument('-O','--options',default='',type=str, help='tikz draw options')
    parser.add_argument('-i','--write-image',default='', type=str, help='file to write to')
    parser.add_argument('-d','--density',default=0.15,type=float,help='density of material, used for calculating weight')
    parser.add_argument('--no-description',action='store_true', help='disable stats below diagram')
    parser.add_argument('-S','--weight-per-piece',type=float, default=0.0, help='adds a configureble amount of weight per piece')
    parser.add_argument('-L','--length-per-piece',type=float, default=0.0, help='adds a configureble amount of needed material per piece')
    parser.add_argument('--supports',action='store_true',help='draw support structure')
    parser.add_argument('-v','--height',default=6.0,type=float,help='height of structure, currently only works for supports')
    parser.add_argument('-x','--direction',default=1,type=int,choices=[-1,1],help='which way the support connect')
    parser.add_argument('-D','--debug',default=0,help='makes functions print their locals, useful for getting extra stats')
    parser.add_argument('--write-tikz',action='store_true',help='writes to a file instead of a printing')
    parser.add_argument('-f','--filename',help='filename to write to')

    args = parser.parse_args()
    
    if args.bridge is None and not args.supports:
        raise parser.error(f"please specify a bridge type or \'--supports\'")
    #elif args.bridge is not None and args.supports:
    #    raise parser.error(f"drawing bridge and supports is currently not supported. Please choose one.")

    width = args.width
    length = args.length
    segments = args.segments
    if len(args.overhang) > 1:
        lover, rover = args.overhang
    elif len(args.overhang) == 1:
        lover = args.overhang[0]
        rover = args.overhang[0]
    ratio = args.ratio
    wooddensity = args.density
    bonus_weight = args.weight_per_piece
    bonus_length = args.length_per_piece
    spill = args.debug
    filename = pathlib.PurePath(args.filename)
    do_supports = args.supports
    sup_height = args.height
    if args.write_tikz and not args.filename:
        raise parser.error('filename is reuired with --write-tikz')
    pic = tikz.Picture()
    suppic = tikz.Picture()
    if args.bridge:
        if args.bridge.lower() in ['howe','pratt','k','baltimore'] and args.segments not in range(2,16,2):
            print("Warning! Segment number is odd.")

        if bridge_map.get(args.bridge.lower()) == None:
            matcher = lambda word: SequenceMatcher(None,args.bridge.lower(),word).ratio()
            withweights = {item: matcher(item) for item in bridge_types}
            alt = sorted(withweights.items(),key=lambda t: t[1])[-1]
            if alt[1] > 0.6:
                raise parser.error(f"invalid bridge type: {args.bridge}, did you mean {alt[0]}? valid types are {bridge_types}")
            else:
                raise parser.error(f"invalid bridge type: {args.bridge}, valid types are {bridge_types}")
        bridge_map[args.bridge.lower()]()
    if args.supports and not args.bridge:
        supports((length-width)/(segments),args.height,args.direction,segments)

    if not args.write_image:
        if args.write_tikz:
            with open(filename,"w") as file:
                file.write(pic.code())
            if args.supports:
                with open(f"{filename.parents[0]}/supports_{filename.parts[-1]}", "w") as file:
                    file.write(suppic.code())
        else:
            if args.bridge:
                print(pic.code())
            if args.supports:
                print(suppic.code())
    else:
        pic.write_image(args.write_image)
