# Diccionario de datos

## Fuente y alcance

El dataset corresponde a **Bank Marketing** de UCI Machine Learning Repository, basado en campañas de telemarketing telefónico de una institución bancaria portuguesa.

- Fuente: https://archive.ics.uci.edu/dataset/222/bank%2Bmarketing
- Instancias: 45,211
- Objetivo original: predecir si el cliente contrata un depósito a plazo.
- Licencia: CC BY 4.0.
- Cita: Moro, S., Rita, P., & Cortez, P. (2014). *Bank Marketing* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5K306

## Mapeo de columnas locales

| Columna local | Nombre original | Descripción |
| --- | --- | --- |
| `Age` | `age` | Edad del cliente. |
| `Type of job` | `job` | Tipo de ocupación. |
| `Marital status` | `marital` | Estado civil. |
| `Education level` | `education` | Nivel educativo. |
| `credit in default` | `default` | Si tiene crédito en mora. |
| `Average yearly balance` | `balance` | Balance anual promedio, en euros. |
| `housing loan` | `housing` | Si tiene préstamo hipotecario. |
| `personal loan` | `loan` | Si tiene préstamo personal. |
| `Contact communication type` | `contact` | Canal de contacto: celular, teléfono o desconocido. |
| `Last contact day of the month` | `day` | Día del mes del último contacto. |
| `V11` | `month` | Mes del último contacto. |
| `V12` | `duration` | Duración de la última llamada, en segundos. |
| `V13` | `campaign` | Número de contactos realizados durante la campaña actual, incluido el último. |
| `V14` | `pdays` | Días desde el contacto de una campaña previa; `-1` indica que no hubo contacto previo. |
| `V15` | `previous` | Número de contactos realizados antes de la campaña actual. |
| `V16` | `poutcome` | Resultado de la campaña previa: `unknown`, `other`, `failure` o `success`. |
| `Class` | `y` | Variable objetivo: suscripción a un depósito a plazo. En este proyecto, `1 = no` y `2 = sí`. |

## Restricción para análisis predictivo
`V12` (`duration`) solo se conoce al terminar la llamada. Por tanto, no debe utilizarse para priorizar clientes o predecir la conversión antes del contacto.

Para una priorización inicial también se excluirá `V13` (`campaign`), ya que contiene el número de contactos de la campaña en curso y puede introducir información no disponible al momento de decidir el primer contacto.

## Limitaciones

El análisis es descriptivo y se basa en un dataset histórico. Las asociaciones observadas no prueban causalidad ni deben utilizarse como decisión operativa sin validación adicional.