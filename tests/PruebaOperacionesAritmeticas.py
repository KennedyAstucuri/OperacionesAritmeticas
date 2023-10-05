import unittest
import math

from src.OperacionesAritmeticas import OperacionesAritmeticas


class PruebaOperacionesAritmeticas(unittest.TestCase):
    def setUp(self)
        self.operacion = OperacionesAritmeticas()
    def test_suma_dosNumeros_respuestaSuma(self):
        def tearDown(self):
            self.operacion = OperacionesAritmeticas()
        #  Arrange
        sumando1 = 13.67
        sumando2 = 15.20
        resultadoEsperado = 28.87

        # Do
        resultadoActual = self.operacion.suma(sumando1,sumando2)

        # Assert
        diferencia=math.fabs(resultadoEsperado - resultadoActual)
        self.assertLessEqual(diferencia, 0.01)

    def test_MCD_dosNumerosNaturales_respuestaMCD(self):
        #  Arrange
        numero1 = 12
        numero2 = 48
        resultadoEsperado = 12

        # Do
        resultadoActual = self.operacion.MCD(numero1, numero2)

        # Assert
        self.assertEqual(resultadoActual, resultadoEsperado)