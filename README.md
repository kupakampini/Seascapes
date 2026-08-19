# 🛰️ Autonomous USV Marine Rover Dashboard — Mauritius

### 🌊 RCMRD Arts & Maps Competition 2026 — University / Professional Category
**Project Theme:** *Acting Locally for Global Impact*  
**Target Geography:** Blue Bay Marine Park & Mahebourg Lagoon, Republic of Mauritius  
**Author Major:** Mechatronics and Robotics Engineering, University of Mauritius

---

## 📌 Project Overview
This project presents an integrated hardware-software framework that bridges mechatronics engineering with remote sensing data to automate localized maritime conservation. It features an interactive, multi-view **Streamlit** GIS dashboard powered by an open-source, solar-powered **Unmanned Surface Vehicle (USV)** architecture designed to monitor coral bleaching and coastal microclimate shifts in real-time.

By collecting localized data points via edge intelligence and cross-referencing them against global geospatial datasets, this platform empowers the **Mauritian Ministry of Environment** to implement swift local conservation actions while supplying critical telemetry to international climate monitoring registries.

---

## 🛠️ System Architecture

### 🤖 1. Hardware & Mechatronics Propulsion
The platform simulates data acquisition from a physical surface vessel utilizing an advanced robotics framework:
*   **Propulsion System:** A custom *Differential Drive Thruster Setup* (dual parallel marine thrusters). By eliminating mechanical rudders, the vessel navigates shallow lagoons safely without entanglement in plastic debris or seaweed.
*   **Power Rail Network:** Onboard LiPo battery bank charged dynamically by an omnidirectional deck solar panel matrix for long-endurance autonomous mission cycles.
*   **Sensor Payload Block:** Subsurface industrial solid-state pH and analog water temperature probes combined with a downward-facing optical camera pod.
*   **Edge Compute Core:** An embedded micro-controller running a lightweight convolutional neural network (MobileNet-SSD) to evaluate benthic substrate frames at the edge with under `15ms` of processing latency.

### 🌐 2. Open Geospatial Data Ingestion (The Two-Dataset Rule)
To satisfy the rigid technical criteria of the RCMRD competition, this application dynamically references macro-level spatial layers from two open data nodes:
1.  **Dataset 1 ([Protected Planet](https://protectedplanet.net)):** Ingests official vector spatial boundary polygons for the Marine Protected Areas (MPAs) of Mauritius to establish strict geofenced operational mission profiles.
2.  **Dataset 2 ([ArcGIS Hub REMSS Server](https://arcgis.com)):** Imports daily satellite-derived global Sea Surface Temperature (SST) continuous raster layers to validate localized rover observations against regional historical baselines.

---

## 💻 Dashboard Interface Features

*   **View 1: Mission Control Map** – An interactive GIS tracker centered over the Blue Bay Marine Park using live Folium map layers to track active deployment trajectories and telemetry density metrics.
*   **View 2: Environmental Telemetry** – Houses an *Actionable Control Trigger Engine*. When scrolling through log indices where variables exceed structural thresholds (SST > 27.5°C or pH < 8.0), the interface instantly throws a neon-red system warning panel and swaps the map marker for a glowing **High-Risk Alarm Pin (`!`)**.
*   **View 3: Computer Vision Stream** – Integrates a *Live Mission Stream Simulation* toggle switch. Turning it on fires an automated script that cycles frames every 400ms, altering metadata code blocks, classification labels, geospatial density **Heatmaps**, and custom interactive donut **Pie Charts** on the fly.
*   **View 4: Policy & Action Hub** – Formulates spatial marine restrictions by drawing vector **buffer fence circles** directly on risk hotspots. Features a functional data portal allowing administrators to export data as an ISO 19115 Geospatial Metadata compliant CSV string for instant integration into global registries like the **Global Coral Reef Monitoring Network (GCRMN)**.

---

## 📂 Repository File Directory
```text
Python Projects/
├── .streamlit/
│   └── config.toml          # Streamlit internal server settings
├── static/
│   ├── background.png       # App landing page background panel layer
│   └── breakdown.png        # USV mechanical schematic engineering diagram
├── seascapes2.py            # Main application Python script source code
└── README.md                # Submission project documentation log
```

---

## 🚀 Local Installation & Deployment

### 📋 Prerequisites
Ensure you have Python 3.8+ installed on your local computer machine.

### ⚙️ Steps to Boot the Server
1. Clone or download this project folder repository onto your machine.
2. Open your terminal application inside the project folder directory and install the required core geospatial and data visualization libraries:
   ```bash
   pip install streamlit streamlit-folium folium pandas numpy plotly
   ```
3. Boot up the Streamlit engine server:
   ```bash
   streamlit run seascapes2.py
   ```
4. Access the live interface in your web browser at `http://localhost:8501`.

---

## 🌍 Competition Compliance Notice
This project aligns with the **RCMRD Arts & Maps 2026 theme: "Acting Locally for Global Impact"** by proving that localized mechatronic automated assets can rapidly identify macro-environmental crises (like coral reef bleaching), enforce local protection parameters, and upscale island findings into standard open formats for global monitoring.
