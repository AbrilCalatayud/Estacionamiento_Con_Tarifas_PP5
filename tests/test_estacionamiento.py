import pytest
from solucion.estacionamiento import Nocturna, FinDeSemana
from solucion.estadia import Estadia, EstadiaMensual, facturar

def test_calculo_total_estadia_sin_modificador():
    estadia = Estadia("AB123CD", 2)

    assert estadia.total(1000) == 2000

def test_calculo_total_estadia_nocturna():
    estadia = Estadia("AB123CD", 2)
    estadia.agregar_modificador(Nocturna())

    assert estadia.total(1000) == 2400

def test_calculo_total_estadia_fin_de_semana():
    estadia = Estadia("AB123CD", 2)
    estadia.agregar_modificador(FinDeSemana())

    assert estadia.total(1000) == 3000

def test_calculo_total_estadia_varios_modificadores():
    estadia = Estadia("AB123CD", 2)
    estadia.agregar_modificador(FinDeSemana())
    estadia.agregar_modificador(Nocturna())

    assert estadia.total(1000) == 3400

def test_patente_invalida():
    with pytest.raises(ValueError):
        Estadia("", 2)

def test_horas_invalidas():
    with pytest.raises(ValueError):
        Estadia("AB123CD", -2)

def test_rechazo_modificador_invalido():
    estadia = Estadia("AB123CD", 2)
    
    with pytest.raises(TypeError):
        estadia.agregar_modificador(EstadiaMensual("AB123CD", 2, 20))

def test_coleccion_modificadores_inmutable_desde_afuera():
    estadia = Estadia("AB123CD", 2)
    estadia.agregar_modificador(FinDeSemana())
    
    assert estadia.total(1000) == 3000

    with pytest.raises(AttributeError):
        estadia.modificadores.append(Nocturna())

    assert estadia.total(1000) == 3000

def test_estadia_mensual_horas_invalidas_falla_igual():
    with pytest.raises(ValueError):
        EstadiaMensual("AB123CD", -2, 20)

def test_estadia_mensual_con_modificador():
    estadia_mensual = EstadiaMensual("AB123CD", 2, 20)
    estadia_mensual.agregar_modificador(FinDeSemana())

    assert estadia_mensual.total(1000) == 2400

def test_facturar_lista_estadias_mezclada_mezclada():
    estadia = Estadia("AB123CD", 2)
    estadia_mensual = EstadiaMensual("AB123CD", 2, 20)
    estadias = [estadia, estadia_mensual]

    assert facturar(estadias, 1000) == 3600