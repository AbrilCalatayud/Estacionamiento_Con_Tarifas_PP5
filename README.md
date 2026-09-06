# Tarea de Paradigmas de Programación 5: Estacionamiento con tarifas

## Consigna: [Link](https://paradigmas-v-fie.github.io/reuniones-2026/ejercicios/reuniones/clase-3.html)

## Tarjetas CRC
| Clase | Responsabilidades | Colaboradores |
|---|---|---|
| Estadia | calcular total, validar que la patente no sea vacía, validar que las horas sean positivas, aceptar o rechazar un modificador, aplicar modificadores en orden, entregar una copia de sus modificadores | ModificadorTarifa (pongo solo la clase padre, porque Estadia interactua con todas las clases hijas) |
| EstadiaMensual | aplicar descuento por estadía mensual sobre el total de la estadía | (no pongo ModificadorTarifa, porque ya lo tiene la clase padre) |
| ModificadorTarifa | proveer plantilla base: entregar nuevo valor total con una modificación |  |
| Nocturna | entregar nuevo valor total con $200 pesos más por cada hora  |  |
| FinDeSemana | entregar nuevo valor total con un aumento del 50% |  |

## Evidencia a entregar
### Explicá en 3 líneas qué contrato comparten los modificadores...
aplicar(total, horas) -> float. Todos los modificadores deben recibir un total y una cantidad de horas de estadía en el estacionamiento, devolviendo un nuevo total post-modificación 
### ...y en 2 más por qué EstadiaMensual es una especialización (es-un) y no un modificador más.
Porque los modificadores están relacionados con las *condiciones* en las que se da la estadía, mientras que las estadías están relacionadas con el *tipo de acuerdo* que tiene el vehículo con el lugar. La estadía por defecto se paga completa y el cliente solo paga cuando está adentro, mientras que con el abono mensual se paga un "suscripción" al estacionamiento que luego otorga un beneficio.