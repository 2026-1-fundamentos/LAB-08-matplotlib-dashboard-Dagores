# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    
    # Create docs folder if it doesn't exist
    os.makedirs("docs", exist_ok=True)
    
    # Read the data
    df = pd.read_csv("files/input/shipping-data.csv")
    
    # Set up matplotlib to not display plots
    plt.ioff()
    
    # 1. Shipping per Warehouse
    plt.figure(figsize=(10, 6))
    warehouse_counts = df["Warehouse_block"].value_counts().sort_index()
    warehouse_counts.plot(kind="bar", color="steelblue")
    plt.title("Shipping per Warehouse", fontsize=14, fontweight="bold")
    plt.xlabel("Warehouse Block", fontsize=12)
    plt.ylabel("Number of Shipments", fontsize=12)
    plt.xticks(rotation=0)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png", dpi=100, bbox_inches="tight")
    plt.close()
    
    # 2. Mode of Shipment
    plt.figure(figsize=(10, 6))
    mode_counts = df["Mode_of_Shipment"].value_counts()
    mode_counts.plot(kind="bar", color="coral")
    plt.title("Mode of Shipment", fontsize=14, fontweight="bold")
    plt.xlabel("Mode of Shipment", fontsize=12)
    plt.ylabel("Number of Shipments", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png", dpi=100, bbox_inches="tight")
    plt.close()
    
    # 3. Average Customer Rating
    plt.figure(figsize=(10, 6))
    avg_rating = df.groupby("Warehouse_block")["Customer_rating"].mean().sort_index()
    avg_rating.plot(kind="bar", color="mediumseagreen")
    plt.title("Average Customer Rating by Warehouse", fontsize=14, fontweight="bold")
    plt.xlabel("Warehouse Block", fontsize=12)
    plt.ylabel("Average Rating", fontsize=12)
    plt.xticks(rotation=0)
    plt.ylim(0, 5)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png", dpi=100, bbox_inches="tight")
    plt.close()
    
    # 4. Weight Distribution
    plt.figure(figsize=(10, 6))
    plt.hist(df["Weight_in_gms"], bins=30, color="orchid", edgecolor="black", alpha=0.7)
    plt.title("Weight Distribution", fontsize=14, fontweight="bold")
    plt.xlabel("Weight (gms)", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("docs/weight_distribution.png", dpi=100, bbox_inches="tight")
    plt.close()
    
    # Create HTML dashboard
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shipping Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }
        .dashboard {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }
        .chart-container {
            background-color: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .chart-container img {
            width: 100%;
            height: auto;
            border-radius: 4px;
        }
        @media (max-width: 768px) {
            .dashboard {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Shipping Dashboard</h1>
        <div class="dashboard">
            <div class="chart-container">
                <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse">
            </div>
            <div class="chart-container">
                <img src="mode_of_shipment.png" alt="Mode of Shipment">
            </div>
            <div class="chart-container">
                <img src="average_customer_rating.png" alt="Average Customer Rating">
            </div>
            <div class="chart-container">
                <img src="weight_distribution.png" alt="Weight Distribution">
            </div>
        </div>
    </div>
</body>
</html>
"""
    
    # Save the HTML file
    with open("docs/index.html", "w") as f:
        f.write(html_content)
