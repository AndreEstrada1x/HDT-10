import unittest
from main import leer_archivo, construir_grafo, ruta_mas_corta, ciudad_centro, modificar_grafo

class TestGrafoMethods(unittest.TestCase):
    def setUp(self):
        # Preparar datos para las pruebas
        self.datos = [
            ('ciudad1', 'ciudad2', 1.0, 2.0, 3.0, 4.0),
            ('ciudad2', 'ciudad3', 2.0, 3.0, 4.0, 5.0),
            # Agrega más datos si es necesario
        ]
        self.grafo = construir_grafo(self.datos)

    def test_leer_archivo(self):
        # Verificar si los datos son leídos correctamente del archivo
        self.assertEqual(leer_archivo("logistica.txt"), self.datos)

    def test_ruta_mas_corta(self):
        # Verificar si la ruta más corta es calculada correctamente
        self.assertEqual(ruta_mas_corta(self.grafo, 'ciudad1', 'ciudad3'), 'La ruta más corta entre ciudad1 y ciudad3 es: ciudad1 -> ciudad2 -> ciudad3, tiempo: 3.0 horas.\nCiudades intermedias: ciudad2')

    def test_ciudad_centro(self):
        # Verificar si la ciudad centro es identificada correctamente
        self.assertEqual(ciudad_centro(self.grafo), ['ciudad2'])

    def test_modificar_grafo(self):
        # Verificar si el grafo es modificado correctamente
        modificar_grafo(self.grafo, "b")
        self.assertTrue(self.grafo.has_edge('ciudad1', 'ciudad3'))

if __name__ == '__main__':
    unittest.main()
