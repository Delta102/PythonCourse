## PRUEBAS UNITARIAS

import unittest
import cambiaTexto

class cambiaTextoTesting(unittest.TestCase):
    def testMayusculas01(self):
        palabra = "Hello World"
        resultado = cambiaTexto.todoMayusculas(palabra)
        self.assertEqual(resultado, "HELLO WORLD")

    def testMayusculas02(self):
        palabra = "Hello World"
        resultado = cambiaTexto.todoMayusculas(palabra)
        self.assertNotEqual(resultado, "hello world")

    def testprimeraMayus01(self):
        palabra = "hello World"
        resultado = cambiaTexto.primeraLetraMayuscula(palabra)
        self.assertEqual(resultado, "Hello World")

if __name__ == '__main__':  ## 
    unittest.main()