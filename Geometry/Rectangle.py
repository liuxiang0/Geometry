'''a very user friendly Rectangle.

Provides an implementation of a rectangle designed to be easy to use:
 - built on a very friendly Point class
 - provides a wealth of accessors that are read-write
 - 


'''

import random
import math

from .Point import Point

class Rectangle(object):

    def randomSizeAndLocation(cls,radius,widthLimits,heightLimits,origin=None):
        '''
        :param: radius       - float
        :param: widthLimits  - iterable of floats with length >= 2
        :param: heightLimits - iterable of floats with length >= 2
        :param: origin       - optional Point subclass
        :return: Rectangle
        '''

        r = cls(widthLimits,heightLimits,origin)

        r.origin = Point.randomLocation(radius,origin)

    @classmethod
    def randomSize(cls,widthLimits,heightLimits,origin=None):
        '''
        :param: widthLimits  - iterable of integers with length >= 2
        :param: heightLimits - iterable of integers with length >= 2
        :param: origin       - optional Point subclass
        :return: Rectangle
        '''

        r = cls(0,0,origin)

        r.w = random.randint(widthLimits[0],widthLimits[1])
        r.h = random.randint(heightLimits[0],heightLimits[1])
            
        return r
    
    @classmethod
    def randomLocation(cls,radius,width,height,origin=None):
        '''
        :param: radius - float
        :param: width  - float
        :param: height - float
        :param: origin - optional Point subclass
        :return: Rectangle

        '''
        
        rOrigin = Point.randomLocation(radius,origin)
        
        return cls(width,height,rOrigin)


    def __init__(self,width,height,origin=None):
        '''
        :param: width  - float X distance from origin.x
        :param: height - float Y distance from origin.y
        :param: origin - Point subclass
        :return: Rectangle
        
        Returns a Rectangle object in the XY plane defined by
        origin, length and width.  All other properties are derived.

        Note: Origin may have a non-zero Z coordinate to facilitate
              Z-ordering.
        '''
        
        try:
            self.origin = iter(origin)
        except TypeError:
            pass
        
        self.width  = width
        self.height = height

    @property
    def origin(self):
        '''
        Point describing the origin of the rectangle. Defaults to (0,0,0).
        '''
        try:
            return self._origin
        except AttributeError:
            pass
        self._origin = Point()
        return self._origin

    @origin.setter
    def origin(self,newOrigin):
        self.origin.xyz = newOrigin

    @property
    def O(self):
        '''
        Shorthand for origin, Point.
        '''
        return self.origin

    @O.setter
    def O(self,newO):
        self.origin = newO

    @property
    def width(self):
        '''
        Width of the rectangle, float.
        '''
        try:
            return self._width
        except AttributeError:
            pass
        self._width = 0
        return self._width

    @width.setter
    def width(self,newWidth):
        self._width = float(newWidth)

    @property
    def height(self):
        '''
        Height of the rectangle, float.
        '''
        try:
            return self._height
        except AttributeError:
            pass
        self._height = 0
        return self._height

    @height.setter
    def height(self,newHeight):
        self._height = float(newHeight)
            
    @property
    def w(self):
        '''
        Shorthand for width, float.
        '''
        return self.width
    
    @w.setter
    def w(self,newWidth):
        self.width = newWidth

    @property
    def h(self):
        '''
        Shorthand for height, float.
        '''
        return self.height
    
    @h.setter
    def h(self,newHeight):
        self.height = newHeight

    @property
    def x(self):
        '''
        Shorthand for origin.x, float.
        '''
        return self.origin.x

    @x.setter
    def x(self,newX):
        self.origin.x = newX
    
    @property
    def y(self):
        '''
        Shorthand for origin.y, float.
        '''
        return self.origin.y

    @y.setter
    def y(self,newY):
        self.origin.y = newY

    @property
    def z(self):
        '''
        Shorthand for origin.z, float.
        '''
        return self.origin.z

    @z.setter
    def z(self,newZ):
        self.origin.z = newZ

    @property
    def xy(self):
        '''
        Shorthand for origin.xy, iterable of floats.
        '''
        return self.origin.xy

    @xy.setter
    def xy(self,newXY):
        self.origin.xy = newXY

    @property
    def xz(self):
        '''
        Shorthand for origin.xz, iterable of floats
        '''
        return self.origin.xz
    
    @xz.setter
    def xz(self,newXZ):
        self.origin.xz = newXZ
        
    @property
    def yz(self):
        '''
        Shorthand for origin.yz, iterable of floats.
        '''
        return self.origin.yz
    
    @yz.setter
    def yz(self,newYZ):
        self.origin.yz = newYZ
    
    @property
    def xyz(self):
        '''
        Shorthand for origin.xyz, iterable of floats.
        '''
        return self.origin.xyz
    
    @xyz.setter
    def xyz(self,newXYZ):
        self.origin.xyz = newXYZ

    @property
    def minX(self):
        '''
        Minimum X coordinate boundry, float.
        '''
        return self.origin.x
    
    @property
    def midX(self):
        '''
        Middle X coordinate, float.
        '''
        return self.origin.x + (self.width/2)

    @property
    def maxX(self):
        '''
        Maximum X coordinate boundry, float.
        '''
        return self.origin.x + self.width

    @property
    def minY(self):
        '''
        Minimum Y coordinate, float.
        '''
        return self.origin.y
    
    @property
    def midY(self):
        '''
        Middle Y coordinate, float.
        '''
        return self.origin.y + (self.height/2)

    @property
    def maxY(self):
        '''
        Maximum Y coordinate, float.
        '''
        return self.origin.y + self.height

    @property
    def A(self):
        '''
        Point whose coordinates are (minX,minY,origin.z)
        '''
        return Point(self.origin)

    @A.setter
    def A(self,newA):
        self.origin = newA

    @property
    def B(self):
        '''
        Point whose coordinates are (maxX,minY,origin.z)
        '''
        return Point(self.maxX,self.minY,self.origin.z)

    @B.setter
    def B(self,newB):
        self.origin = newB
        self.origin.x -= self.width

    @property
    def C(self):
        '''
        Point whose coordinates are (maxX,maxY,origin.z)
        '''
        return Point(self.maxX,self.maxY,self.origin.z)

    @C.setter
    def C(self,newC):
        self.origin = newC
        self.origin.x -= self.width
        self.origin.y -= self.height

    @property
    def D(self):
        '''
        Point whose coordinates are (minX,maxY,origin.Z)
        '''
        return Point(self.minX,self.maxY,self.origin.z)

    @D.setter
    def D(self,newD):
        self.origin = newD
        self.origin.y -= self.height

    @property
    def center(self):
        '''
        Point whose coordinates are (midX,midY,origin.z)
        '''
        return Point(self.midX,self.midY,self.origin.z)
    
    @center.setter
    def center(self,newCenter):
        self.origin = newCenter
        self.origin.x -= (self.width/2)
        self.origin.y -= (self.height/2)
    
    @property
    def midAB(self):
        '''
        Point inbetween A and B.
        '''
        return self.A.midpoint(B)
    
    @midAB.setter
    def midAB(self,newMidAB):
        self.origin = newMidAB
        self.origin.x -= (self.width/2)

    @property
    def midBC(self):
        '''
        Point inbetween B and C.
        '''
        return self.B.midpoint(C)
    
    @midBC.setter
    def midBC(self,newMidBC):
        self.origin = newMidBC
        self.origin.x -= self.width
        self.origin.y -= (self.height/2)

    @property
    def midCD(self):
        '''
        Point inbetween C and D.
        '''
        return self.C.midpoint(D)
    
    @midCD.setter
    def midCD(self,newMidCD):
        self.origin = newMidCD
        self.origin.x -= (self.width/2)
        self.origin.y -= self.height

    @property
    def midAD(self):
        '''
        Point inbetween A and D.
        '''
        return self.A.midpoint(D)
    
    @midAD.setter
    def midAD(self,newMidAD):
        self.origin = newMidAD
        self.origin.y -= (self.height/2)

    @property
    def perimeter(self):
        '''
        Returns the permeter of the rectangle, float.
        '''
        return (self.width*2) + (self.height*2)        

    @property
    def area(self):
        '''
        Returns the area of the rectangle, float.
        '''
        return self.width * self.height

    @property
    def isSquare(self):
        '''
        Returns true of self.width equals self.height.
        '''
        return self.width == self.height

    @property
    def isCCW(self):
        '''
        Returns True of the points A, B, C form a counter clockwise angle.
        '''
        return self.A.isCCW(self.B,self.C)

    @property
    def ccw(self):
        '''
        Returns A.ccw(B,C), float.

        >0 : counter clockwise and the area of the parallelpiped 
         0 : collinear, not genearlly possible in a well-formed rectangle
        <0 : clockwise and also the area of the parallelpipled
        '''
        return self.A.ccw(self.B,self.C)
    
    def __str__(self):
        return repr(self)

    def __repr__(self):
        fmt = '<%s(width=%.2f,height=%.2f,origin=%s)>'
        return fmt % (self.__class__.__name__,self.w,self.h,self.origin)

    def __eq__(self,other):
        '''
        x == y iff:
          x.origin == y.origin
          x.width  == y.width
          x.height == y.height
        '''
        oeq = self.origin == other.origin
        weq = self.w == other.w
        heq = self.h == other.h
        return oeq and weq and heq

    def __contains__(self,other):
        '''
        x in y iff:
          (y.A in x) or (y.B in x) or (y.C in x) or (y.D in x)
        '''
        # does ccw/cw of self or other matter here?
        
        if self.containsPoint(other.A):
            return True
        if self.containsPoint(other.B):
            return True
        if self.containsPoint(other.C):
            return True
        if self.containsPoint(other.D):
            return True
        return False

    def scale(self,dx=1.0,dy=1.0):
        '''
        :param: dx - optional float
        :param: dy - optional float
        '''
        self.width *= dx
        self.height *= dy

    def inset(self,other,percentage):
        '''
        :param: other       - Rectangle subclass
        :param: percentagle - float
        '''
        pass
    
    def union(self,other):
        '''
        :param: other - Rectangle subclass
        '''
        # returns a rectangle composed of the bounds of self and other
        pass

    def intersect(self,other):
        '''
        :param: other - Rectangle subclass
        '''
        # returns an iterable of rectangles that compose the intersection
        # a limit of 0 to 4 rects?
        pass

    def containsPoint(self,point,Zorder=False):
        '''
        :param: point  - Point subclass
        :param: Zorder - optional Boolean
        '''
        if not point.isBetweenX(self.A,self.B):
            return False
        if not point.isBetweenY(self.A,self.D):
            return False

        if Zorder:
            return point.z == self.origin.z
        
        return True

    def zorder(self,other):
        '''
        :param: other - Rectangle subclass
        :return: float
        
        >0:  self <  other
         0:  self eq other
        <0:  self > other
        '''
        
        return other.origin.z - self.origin.z

    def flipX(self):
        '''
        '''
        self.width *= -1

    def flipY(self):
        '''
        '''
        self.height *= -1