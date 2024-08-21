import math
import unittest
class operaciones():
    def divi(a,b):
        x=((a[0]*b[0])+(a[1]*b[1]))/((b[0]**2)+(b[1]**2))
        y=((b[0]*a[1])-(b[1]*a[0]))/((b[0]**2)+(b[1]**2))
        return x,y

    def suma(a,b):
        x=a[0]+b[0]
        y=a[1]+b[1]
        return x,y

    def multi(a,b):
        x=((a[0]*b[0])-(a[1]*b[1]))
        y=((a[0]*b[1])+(a[1]*b[0]))
        return x,y

    def resta(a,b):
        x=a[0]-b[0]
        y=a[1]-b[1] 
        return x,y

    def modulo(a):
        x=math.sqrt((a[0]**2)+a[1]**2)
        return x

    def conjugado(a):
        x=a[0]
        y=a[1]*-1
        return x,y

    def polar(a):
        x=math.sqrt((a[0]**2)+a[1]**2)
        y=math.atan(a[1]/a[0])
        return x,y

    def cartesiano(a):
        x=a[0]*math.cos(a[1])
        y=a[0]*math.sin(a[1])
        return x,y
    
    def fase(a):
        x=math.atan2(a[1],a[0])
        return x

class pruebas(unittest.TestCase):
    def test_divi(self):
        resp = operaciones.divi((1, 2), (3, 4))
        self.assertAlmostEqual(resp[0], 0.44, places=2)
        self.assertAlmostEqual(resp[1], 0.08, places=2)
        
        resp2 = operaciones.divi((-2, 1), (1, 2))
        self.assertAlmostEqual(resp2[0], 0, places=2)
        self.assertAlmostEqual(resp2[1], 1, places=2)

    def test_suma(self):
        resp = operaciones.suma((1, 2), (3, 4))
        self.assertEqual(resp, (4, 6))
        
        resp2 = operaciones.suma((3, -1), (1, 4))
        self.assertEqual(resp2, (4, 3))

    def test_multi(self):
        resp = operaciones.multi((1, 2), (3, 4))
        self.assertEqual(resp, (-5, 10))
        
        resp2 = operaciones.multi((3, -2), (1, 2))
        self.assertEqual(resp2, (7, 4))

    def test_resta(self):
        resp = operaciones.resta((1, 2), (3, 4))
        self.assertEqual(resp, (-2, -2))
       
        resp2 = operaciones.resta((3, -1), (1, 4))
        self.assertEqual(resp2, (2, -5))

    def test_modulo(self):
        resp = operaciones.modulo((3, 4))
        self.assertAlmostEqual(resp, 5.0, places=2)
        
        resp2 = operaciones.modulo((0, 3))
        self.assertAlmostEqual(resp2, 3.0, places=2)

    def test_conjugado(self):
        resp = operaciones.conjugado((3, 4))
        self.assertEqual(resp, (3, -4))
        
        resp2 = operaciones.conjugado((4, -7))
        self.assertEqual(resp2, (4, 7))

    def test_polar(self):
        resp = operaciones.polar((3, 4))
        self.assertAlmostEqual(resp[0], 5.0, places=2)
        self.assertAlmostEqual(resp[1], 0.93, places=2) 
        
        resp2 = operaciones.polar((1, 1))
        self.assertAlmostEqual(resp2[0], math.sqrt(2), places=2)
        self.assertAlmostEqual(resp2[1], math.pi/4, places=2) 

    def test_cartesiano(self):
        resp = operaciones.cartesiano((5, 0.93))
        self.assertAlmostEqual(round(resp[0]), 3, places=2)
        self.assertAlmostEqual(round(resp[1]), 4, places=2)
        
        resp2 = operaciones.cartesiano((math.sqrt(2), math.pi/4))
        self.assertAlmostEqual(round(resp2[0]), 1, places=2)
        self.assertAlmostEqual(round(resp2[1]), 1, places=2)
    
    def test_fase(self):
        resp=operaciones.fase((3,4))
        self.assertAlmostEqual(resp, 0.93, places=2)
        
        resp2=operaciones.fase((1,1))
        self.assertAlmostEqual(resp2, math.pi/4, places=2)
if __name__ == "__main__":
    unittest.main()