
import random
import math
import networkx as nx

class Encaminamiento:

    #---ANILLO-------------------------------

    def distanciaAnillo(self,node1,node2,main):
        """Returns the euclidean distance between two nodes"""
        n1 = self.getCoordinatesAnillo(node1,main)
        n2 = self.getCoordinatesAnillo(node2,main)
        d = math.sqrt(math.pow(n2[0]-n1[0],2)+math.pow(n2[1]-n1[1],2))
        return d

    def getCoordinatesAnillo(self,nodeId,main):
        #transformación de coordenadas polares a rectangulares:
        angulo=math.radians((360/main.nodes)*nodeId)#la función math.radians() convierte los grados sexagesimales en radianes
        x = 10*math.cos(angulo)#se asume que el anillo tiene radio 10
        y = 10*math.sin(angulo)#se asume que el anillo tiene radio 10
        coord = [x,y]
        #print("soy",nodeId,"mis coordenadas son",coord)
        return coord

    #---MALLA----------------------------------

    def distancia(self,node1,node2,main):
        n1 = self.getCoordinates(node1,main)
        n2 = self.getCoordinates(node2,main)
        d = math.sqrt(math.pow(n2[0]-n1[0],2)+math.pow(n2[1]-n1[1],2))
        return d

    def getCoordinates(self,nodeId,main):
        x = (nodeId-1)%main.rows
        y = (nodeId-1)//main.columns
        coord = [x,y]
        return coord

    #---COMPASS ROUTING--------------------------

    def angulo(self,destino,origen,nodo,main):
        #print("or",origen,"des",destino,"vecino",nodo)
        if main.grafo==1:#si trabajo en una malla:
            p0 = self.getCoordinates(origen,main)
            p1 = self.getCoordinates(destino,main)
            p2 = self.getCoordinates(nodo,main)
        elif main.grafo==3:#si trabajo en un anillo:
            p0 = self.getCoordinatesAnillo(origen,main)
            p1 = self.getCoordinatesAnillo(destino,main)
            p2 = self.getCoordinatesAnillo(nodo,main)
        #print("origen",p0)
        #print("destino",p1)
        #print("vecino",p2)
        u1 = p1[0]-p0[0]
        #print("u1",u1)
        u2 = p1[1]-p0[1]
        #print("u2",u2)
        v1 = p2[0]-p0[0]
        #print("v1",v1)
        v2 = p2[1]-p0[1]
        #print("v2",v2)
        #calculo del angulo entre vectores mediante producto punto
        div = (u1*v1+u2*v2)/((math.sqrt((math.pow(u1,2) + math.pow(u2,2))))*(math.sqrt((math.pow(v1,2) + math.pow(v2,2)))))
        try:
            angC=math.degrees(math.acos(div))
        except ValueError as error:
            if div>1.0:
                #print("mas grande",div)
                div=1.0
            elif div < -1.0:
                #print("mas pequeño",div)
                div=-1.0
            angC=math.degrees(math.acos(div))
        #print("angC",angC)
        return angC

    def Compass_Routing(self,identificador,vecinos,destino,main):
        w = random.choice(vecinos)
        ang = 360
        #print("origen",identificador,"destino",destino,"vecinos",vecinos)
        if destino in vecinos:
            w = destino
        else:
            for vecino in vecinos:     
                ang2 = self.angulo(destino,identificador,vecino,main) 
                if ang2 <= ang:
                    w = vecino
                    ang = ang2
        #print("angulo seleccionado",ang)
        #print("vecino seleccionado",w)
        return w 

    #---SHORTEST PATH (DIJKSTRA)----------------

    def shortestPath(self,grafo,fuente,destino):
        ruta = nx.shortest_path(grafo, source=fuente, target=destino, weight=None, method='dijkstra')
        return ruta

    #---RANDOM WALK-----------------------------

    def Random_Walk(self,identificador,vecinos):
        w=random.choice(vecinos)
        return w

    #---EXTRAS----------------------------------

    def generaDestino(self,identificador,main,vecinos):
        """genera un nodo destino de manera aleatoria (que no esté en mis vecinos)"""
        d = False
        while(d == False):
            dest=-1
            if main.grafo==3:#si es un anillo con el que estoy trabajando:
                dest = random.randint(1,main.nodes)
            elif main.grafo==1:#si es una malla con la que estoy trabajando:
                dest = random.randint(1,main.rows*main.columns)
            if dest != identificador and dest not in vecinos:
                d = True
        return dest