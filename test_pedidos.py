from pedidos import calcular_descuento


def test_descuento_grande():
    assert calcular_descuento(200) == 20.0


def test_descuento_pequeno():
    assert calcular_descuento(60) == 3.0


def test_sin_descuento():
    assert calcular_descuento(20) == 0.0
