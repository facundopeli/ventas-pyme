# Proyecto VentasPyme

## Escenario
Análisis de ventas de una Pyme utilizando un dataset simulado en formato CSV.

## Dataset
Archivo: `datos/ventas.csv`  
Columnas: `sales_date`, `product`, `sales_amount`  
Fuente: dataset de ejemplo provisto en la consigna.

## Script de análisis
Ubicación: `scripts/analisis_ventas.py`  
Indicadores calculados:
- Ventas totales
- Producto más vendido
- Ventas por mes

Genera un gráfico de evolución mensual en `resultados/ventas_por_mes.png`.

## Instrucciones de ejecución
1. Clonar el repo en Google Colab.  
2. Descargar el dataset en `/datos`.  
3. Ejecutar el script:  
   ```bash
   !python scripts/analisis_ventas.py
