# 🛒 **Supermarket**

## _Arquitectura Medallon en Azure Databricks_
<div align="left">







Pipeline analítico para transformar, modelar y visualizar datos del Supermarket Dataset (Kaggle https://www.kaggle.com/code/amunsentom/analysis-supermarket-superstore-dataset), usando arquitectura Medallion y prácticas de ingeniería de datos profesional.

</div>

🎯 Descripción

Este proyecto implementa un pipeline completo de ingesta, transformación, modelado dimensional y visualización, partiendo del dataset tipo supermercado de Kaggle (similar al de Instacart).
Se utiliza Databricks, PySpark y Delta Lake para procesar los datos bajo la arquitectura Bronze → Silver → Gold, y se expone la capa analítica hacia Power BI.

✨ Destacados del Proyecto

🥈 Modelo Dimensional (Star Schema) basado en ventas, productos y clientes

🧱 Arquitectura Medallion optimizada para escalabilidad

⚡ PySpark + Delta Lake para ingesta robusta y ACID

🪣 ADLS Gen2 con contenedores raw/bronze/silver/gold

📊 Power BI Dashboard con KPIs ejecutivos

🔄 Proceso modular y versionable

📦 Pipeline listo para extender o orquestar

🏛️ Arquitectura
Flujo General de Datos
📦 Kaggle CSVs (Raw)
        ↓
🥉 Bronze Layer → Datos brutos en Delta
        ↓
🥈 Silver Layer → Limpieza, tipificación y joins
        ↓
🥇 Gold Layer → Modelo dimensional + agregados
        ↓
📊 Power BI → Dashboards y análisis

Detalle por Capa
<table> <tr> <td width="33%" valign="top">
🥉 Bronze Layer

Propósito: Ingesta sin modificación

Datos CSV almacenados en:
abfss://raw@storage/supermarket/

Estructura idéntica al origen

Sin validaciones

Trazabilidad garantizada

Tablas:

aisles_bronze

departments_bronze

products_bronze

orders_bronze

order_products_prior_bronze

order_products_train_bronze

</td> <td width="33%" valign="top">
🥈 Silver Layer

Propósito: Preparación para análisis

Tipificación de columnas

Limpieza de nulos y duplicados

Unificación de order_products

Relaciones básicas producto–pasillo–departamento

Tablas:

aisles_silver

departments_silver

products_silver

orders_silver

order_products_all_silver

</td> <td width="33%" valign="top">
🥇 Gold Layer

Propósito: Analítica lista para BI

Tablas dimensionales:

dim_product

dim_customer

dim_date

dim_time

dim_order (opcional)

Tablas de hechos:

fact_order_item

fact_order (agregado por orden)

Características:

Star schema optimizado

Cálculo de KPIs

Tablas listas para Power BI

</td> </tr> </table>
📁 Estructura del Proyecto
supermarket-analytics/
│
├── 📂 proceso/
│   ├── 🐍 1_ingest_bronze.py
│   ├── 🐍 2_transform_silver.py
│   ├── 🐍 3_model_gold.py
│   └── 📄 ddl_medallion.sql
│
├── 📂 powerbi/
│   ├── dashboard_supermarket.pbix
│   └── tema_supermarket.json
│
└── 📄 README.md

🛠️ Tecnologías
<div align="center">
Tecnología	Uso
Azure Databricks	Procesamiento distribuido con Spark
PySpark	Transformaciones del pipeline
Delta Lake	Tablas ACID + Time Travel
ADLS Gen2	Almacenamiento medallion
Power BI	Visualización del modelo Gold
GitHub	Versionado del proyecto
</div>
⚙️ Requisitos

Azure Databricks Workspace

Cluster activo (incluye Spark 3.5+)

Azure Storage Gen2 con contenedores:
raw, bronze, silver, gold

Token de acceso Databricks

Credenciales de conexión a Power BI

Dataset Kaggle del supermarket

🚀 Instalación y Ejecución
1️⃣ Configurar Conexión a ADLS
spark.conf.set(f"fs.azure.account.auth.type.{storage}.dfs.core.windows.net", "OAuth")


(Se documenta completo dentro de los notebooks)

2️⃣ Ejecutar el DDL

Notebook/Script:

1_ingest_bronze.py


Crea estructuras en Delta Lake.

3️⃣ Ingesta Bronze
dbutils.notebook.run("1_ingest_bronze", 300)

4️⃣ Transformación Silver
dbutils.notebook.run("2_transform_silver", 300)

5️⃣ Modelado Gold
dbutils.notebook.run("3_model_gold", 300)

6️⃣ Conexión Power BI

Usar:

servidor.database.windows.net,1433
database: dbsupermarket


Modo de conexión: Import o DirectQuery.

📊 Modelo Dimensional (Gold)
                    DIM_DATE
                       |
                    (date_key)
                       |
DIM_PRODUCT --- FACT_ORDER_ITEM --- DIM_CUSTOMER
                       |
                    (order_id)
                       |
                    DIM_ORDER
                       |
                    DIM_TIME

🧩 Fact Table — FACT_ORDER_ITEM
Campo	Descripción
order_id	Identificador de orden
customer_id	Cliente
product_id	Producto
add_to_cart_order	Secuencia en carrito
reordered_flag	1 si es recompra
date_key	Día de la compra
time_key	Hora de la compra
🧱 Dimensiones principales
DIM_PRODUCT

product_id

product_name

aisle_name

department_name

DIM_CUSTOMER

user_id

total_orders

avg_days_between_orders

DIM_DATE

date_key

day_of_week

day_name

DIM_TIME

time_key

hour_of_day

📈 Dashboard en Power BI

Incluye:

⭐ KPIs

Total Orders

Items Sold

Reorder Rate

Avg Basket Size

📊 Visualizaciones

Ventas por departamento

Top productos

Archivo recomendado:

powerbi/dashboard_supermarket.pbix



👩‍💻 Autora
<div align="center">
Sandra Rocío Castro Medina

Ingeniera de Datos | Arquitectura en Azure | Databricks | Power BI

