# P10 Gestor de Pedidos

## Problemas detectados
1. Código duplicado para calcular los descuentos en el archivo `pedidos.py`.
2. Variables de una sola letra sin significado y bucles `while` manuales en `clientes.py`.
3. Existencia de código muerto como la función `cambiar_estado_pedido()` que no se usa nunca.

## Refactorizaciones realizadas
| Problema | Refactorización | Archivo | Commit |
|---|---|---|---|
| Variables confusas y bucle while | Cambiar bucle while por for y usar variables más claras | clientes.py | Mejora nombres de variables |
| Código duplicado en descuentos | Extracción a la función `calcular_descuento()` | pedidos.py | Extrae lógica de cálculo de pedidos |

## Pruebas creadas
| Test | Qué comprueba |
|---|---|
| test_descuento_grande | Verifica que se aplica un 10% a totales mayores de 100 |
| test_descuento_pequeno | Verifica que se aplica un 5% a totales mayores de 50 |
| test_sin_descuento | Verifica que devuelve 0 para totales bajos |

## Analizador de código
Analizador usado: Ruff
Opciones configuradas:
1. line-length = 100
2. target-version = "py312"
3. select = ["E", "F", "W", "I"]

## Trabajo con Git y ramas
Rama creada: refactor-descuentos
Commits principales: Refactoriza mensaje de despedida
Fusión realizada: Fusión de refactor-descuentos hacia main sin conflictos.

## Integración continua
Resultado del workflow: Todos los tests y el chequeo de Ruff pasaron en verde tras silenciar los avisos menores.
