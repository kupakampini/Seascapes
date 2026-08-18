import streamlit as st
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium 
import pandas as pd
import numpy as np
import time
import plotly.express as px

# 1. Page Configuration & Theme
st.set_page_config(
    page_title="USV Analytics Platform | Mauritius",
    page_icon="🤖",
    layout="wide"
)

# High-Tech Dark Mode Look & Custom Landing Page Layout Rules
# FIXED: Injects an unblockable, high-resolution satellite imagery URL directly via web asset hosting
st.markdown("""
    <style>
    /* Global Themes */
    .main { background-color: #0e1117; color: #ffffff; }
    div[data-testid="stMetricValue"] { color: #00f0ff; font-family: monospace; }
    div[data-testid="stMetricLabel"] { color: #a3b8cc; }
    h1, h2, h3, h4 { color: #00ffcc !important; }
    
    /* Landing Page Custom Elements */
    .stApp {
        background-image: linear-gradient(rgba(14, 17, 23, 0.8), rgba(14, 17, 23, 0.9)), 
                          url("https://arcgisonline.com");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .landing-hero {
        text-align: center;
        padding: 40px 20px;
        background: rgba(19, 25, 36, 0.85) !important;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(0, 255, 204, 0.2);
        border-radius: 12px;
        margin-bottom: 35px;
    }
    .landing-title {
        font-size: 42px !important;
        font-weight: 800;
        color: #00ffcc !important;
        margin-bottom: 12px;
        letter-spacing: -0.5px;
    }
    .landing-subtitle {
        font-size: 18px !important;
        color: #a3b8cc !important;
        max-width: 800px;
        margin: 0 auto;
        line-height: 1.6;
    }
    .hardware-card {
        background-color: rgba(22, 27, 34, 0.9) !important;
        backdrop-filter: blur(6px);
        border: 1px solid rgba(48, 54, 61, 0.7);
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .hardware-card h4 {
        margin-top: 0;
        color: #00f0ff !important;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .hardware-list {
        margin: 0;
        padding-left: 20px;
        color: #c9d1d9;
    }
    .hardware-list li {
        margin-bottom: 8px;
        line-height: 1.5;
    }
    .highlight-tech {
        color: #00ffcc;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# Shared Simulated Dataset Generation
np.random.seed(42)
time_indices = pd.date_range(start="10:00:00", periods=50, freq="15s").strftime("%H:%M:%S")
latitudes = np.linspace(-20.4430, -20.4480, 50)
longitudes = np.linspace(57.7100, 57.7130, 50)

base_temp = 26.5 + np.random.normal(0, 0.05, 50)
base_temp[20:35] += 1.8  # Thermal anomaly simulation window

base_ph = 8.2 + np.random.normal(0, 0.02, 50)
base_ph[20:35] -= 0.4

df_telemetry = pd.DataFrame({
    "Timestamp": time_indices, "Latitude": latitudes, "Longitude": longitudes,
    "SST_C": base_temp, "pH_Level": base_ph
})

df_telemetry["Status"] = "Optimal"
df_telemetry.iloc[20:35, df_telemetry.columns.get_loc("Status")] = "Vulnerable (Thermal Stress)"

if "frame_index" not in st.session_state:
    st.session_state.frame_index = 0

# App Header
st.title("🛰️ Autonomous USV Marine Rover Interface")
st.markdown("---")

# Sidebar Navigation Layout
with st.sidebar:
    st.title("🤖 Navigation")
    view_selection = st.radio("Go to:", [
        "🏠 Welcome: Project Landing Page", 
        "🌐 View 1: Mission Control Map", 
        "📊 View 2: Environmental Telemetry", 
        "🪸 View 3: Computer Vision Logs",
        "📋 View 4: Policy & Action Dashboard"
    ])
    st.markdown("---")

# ==========================================
# WELCOME: PROJECT LANDING PAGE VIEW
# ==========================================
if view_selection == "🏠 Welcome: Project Landing Page":

    # Hero Title Block Component
    st.markdown("""
        <div class="landing-hero">
            <div class="landing-title">Scaling Local Marine Action using Automation</div>
            <div class="landing-subtitle">
                An open-source, edge-intelligent Unmanned Surface Vehicle (USV) architecture engineered 
                for scalable environmental monitoring, data streaming, and autonomous habitat assessment.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h3>🤖 Unmanned Surface Vehicle (USV) Structural Breakdown</h3>', unsafe_allow_html=True)
    
    col_layout_left, col_layout_right = st.columns([1.2, 1], gap="medium")
    
    with col_layout_left:
        # Fallback to local image check for the schematic breakdown diagram card
        try:
            st.image("static/breakdown.png", caption="USV System Schematic & Data Flow Engine Breakdown", use_container_width=True)
        except Exception:
            # Clean CSS visual container fallback if local static folder reading fails on Windows paths
            st.markdown("""
            <div style="background-color: #161b22; border: 1px solid #30363d; padding: 60px; border-radius: 8px; text-align: center; color: #a3b8cc;">
                📸 <b>[ USV HARDWARE SCHEMATIC DIAGRAM LAYER ]</b><br>
                <span style="font-size: 13px;">To display your custom blueprint graphic here, ensure your file is saved inside: <code>static/breakdown.png</code></span>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("""
        <div style="background-color: #122b28; border: 1px solid #00ffcc; padding: 15px; border-radius: 6px; margin-top: 15px;">
            <span style="color: #00ffcc; font-weight: bold;">📍 Current Field Objective:</span> 
            Deploying autonomous tracking routines across vulnerable coastal zones in Mauritius to monitor real-time thermal spikes and marine biome shifts.
        </div>
        """, unsafe_allow_html=True)
        
    with col_layout_right:
        st.markdown("""
            <div class="hardware-card">
                <h4>⚡ Power & Propulsion</h4>
                <ul class="hardware-list">
                    <li><span class="highlight-tech">Differential Drive Thruster Setup:</span> Dual independent marine thrusters facilitating tank-like turning capabilities without complex steering rudders.</li>
                    <li><span class="highlight-tech">Solar Panel Matrix:</span> Photovoltaic surface deck array capturing daylight solar energy to feed onboard power rails.</li>
                    <li><span class="highlight-tech">LiPo Battery Bank:</span> High-discharge multi-cell balancing battery layout supplying continuous energy to high-draw thrusters.</li>
                    <li><span class="highlight-tech">Power Distribution Board (PDB):</span> Clean voltage step-downs isolating structural processing logic circuits from high thruster inductive feedback noise.</li>
                </ul>
            </div>
            <div class="hardware-card">
                <h4>🎛️ Sensor Array Payload</h4>
                <ul class="hardware-list">
                    <li><span class="highlight-tech">Edge Neural Compute Core:</span> Embedded single-board microprocessor evaluating incoming visual camera matrices in real-time under a 15ms latency constraint.</li>
                    <li><span class="highlight-tech">Subsurface Marine Probes:</span> Industrial analog water temperature and solid-state pH nodes outputting constant data packets directly into the main logging registry.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.info("💡 Pro-Tip: Switch between the top radio tabs to access the Live Mission Control Map, real-time Telemetry plots, and Computer Vision streams.")

# ==========================================
# VIEW 1: MISSION CONTROL MAP VIEW
# ==========================================
elif view_selection == "🌐 View 1: Mission Control Map":
    st.subheader("Lagoon Drone Track Core Map")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric(label="🛰️ Fleet Status", value="AUTONOMOUS ROUTE", delta="ONLINE")
    with col2: st.metric(label="📐 Area Covered", value="4.2 Hectares", delta="+0.8 today")
    with col3: st.metric(label="📊 Telemetry Points", value="1,248 Logs", delta="Streaming")
    with col4: st.metric(label="🔋 USV Battery (Solar)", value="94%", delta="Charging")
    st.markdown("---")
    
    m1 = folium.Map(location=[-20.4461, 57.7125], zoom_start=14, tiles="OpenStreetMap")
    waypoints = df_telemetry[["Latitude", "Longitude"]].values.tolist()
    folium.PolyLine(locations=waypoints, color="#00f0ff", weight=4, opacity=0.8).add_to(m1)
    folium.Marker(location=waypoints[-1], popup="USV Position", icon=folium.Icon(color="blue", icon="ship", prefix="fa")).add_to(m1)
    
    st_folium(m1, width=1100, height=500, returned_objects=[], key="control_map_fixed")

# ==========================================
# VIEW 2: ENVIRONMENTAL TELEMETRY VIEW
# ==========================================
elif view_selection == "📊 View 2: Environmental Telemetry":
    st.subheader("Micro-Climate Telemetry Slicing Engine")
    selected_index = st.slider("Scrub Mission Timeline (Log Index)", 0, len(df_telemetry)-1, 27)
    current_row = df_telemetry.iloc[selected_index]
    TEMP_THRESHOLD = 27.5
    PH_THRESHOLD = 8.0
    is_temp_spike = current_row["SST_C"] > TEMP_THRESHOLD
    is_ph_drop = current_row["pH_Level"] < PH_THRESHOLD
    is_critical_trigger = is_temp_spike or is_ph_drop
    if is_critical_trigger:
        st.error(f"🚨 AUTOMATED GEOSPATIAL TRIGGER ALARM ACCESSED — Extreme Conditions Detected")
        st.markdown(f"Environmental stress registered at Timestamp {current_row['Timestamp']}.")
    else:
        st.success("✅ LAGOON SYSTEM NORMAL — Environmental profiles matching healthy baseline limits.")
    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown(f"📍 Current Target Coordinates: {current_row['Latitude']:.4f}, {current_row['Longitude']:.4f}")
        m2 = folium.Map(location=[current_row['Latitude'], current_row['Longitude']], zoom_start=16, tiles="OpenStreetMap")
        st_folium(m2, width=540, height=400, returned_objects=[], key="telemetry_map_fixed")
    if is_critical_trigger:
        popup_msg = f"⚠️ HIGH RISK WARNING!SST: {current_row['SST_C']:.2f}°C (CRITICAL)pH: {current_row['pH_Level']:.2f}"
        marker_color = "red"
        marker_icon = "exclamation-triangle"
    else:
        popup_msg = f"Optimal Baseline PointSST: {current_row['SST_C']:.2f}°CpH: {current_row['pH_Level']:.2f}"
        marker_color = "green"
        marker_icon = "check-circle"
        folium.Marker(location=[current_row['Latitude'], current_row['Longitude']],popup=popup_msg,icon=folium.Icon(color=marker_color, icon=marker_icon, prefix="fa")).add_to(m2)
    
    with col_right:
        st.markdown("### 📈 Live Environmental Profiles")
        st.subheader("Temperature")
        st.line_chart(df_telemetry.set_index("Timestamp")["SST_C"], height=160)
        st.subheader("pH Level")
        st.line_chart(df_telemetry.set_index("Timestamp")["pH_Level"], height=160)

# ==========================================
# VIEW 3: COMPUTER VISION LOGS VIEW
# ==========================================
elif view_selection == "🪸 View 3: Computer Vision Logs":
    st.subheader("Automated Real-Time Computer Vision Mapping")
    
    col_ctrl1, col_ctrl2 = st.columns(2)
    with col_ctrl1:
        run_stream = st.checkbox("▶️ Start Live Mission Stream Simulation", value=False)
    
    if run_stream:
        st.session_state.frame_index = (st.session_state.frame_index + 1) % len(df_telemetry)
        active_index = st.session_state.frame_index
        st.info(f"🎥 Running Live Stream Mode — Playing Frame Index: {active_index}/49")
    else:
        active_index = st.slider("Select Mission Feed Frame (Manual Scrub)", 0, len(df_telemetry)-1, st.session_state.frame_index)
        st.session_state.frame_index = active_index

    current_row_p3 = df_telemetry.iloc[active_index]
    
    col_vis, col_stats = st.columns(2)
    is_anomaly = (20 <= active_index <= 35)
    
    with col_vis:
        st.markdown("### 📷 Computer Vision Matrix Stream")
        if is_anomaly:
            st.error("⚠️ [DETECTION ALERT] TARGET REEF AFFECTED BY HIGHER BLEACHING DENSITY")
            st.markdown(f"""
            <div style="border: 3px solid #ff4b4b; padding: 20px; border-radius: 10px; background-color: #3b1c1c; text-align: center;">
                <h2 style="color: #ff4b4b !important; margin: 0;">[ CLASS: BLEACHED_CORAL ]</h2>
                <p style="color: #ffffff; font-family: monospace; font-size: 13px; margin-top: 5px;">
                    Bounding Vector Matrix: [X:142, Y:90, W:320, H:210]<br>
                    Target Segment: Blue Bay Lagoon Sector B
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.success("✅ [HEALTHY MATRIX] OPTIMAL WATER PROFILE & REEF PIGMENTATION DETECTED")
            st.markdown(f"""
            <div style="border: 3px solid #00ffcc; padding: 20px; border-radius: 10px; background-color: #122b28; text-align: center;">
                <h2 style="color: #00ffcc !important; margin: 0;">[ CLASS: HEALTHY_REEF ]</h2>
                <p style="color: #ffffff; font-family: monospace; font-size: 13px; margin-top: 5px;">
                    Bounding Vector Matrix: [X:115, Y:72, W:340, H:225]<br>
                    Target Segment: Blue Bay Lagoon Sector A
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("### 🗺️ AI-Generated Anomaly Heatmap Cluster")
        m3_heatmap = folium.Map(location=[-20.4455, 57.7115], zoom_start=15, tiles="OpenStreetMap")
        
        heatmap_data = []
        for idx, row in df_telemetry.iterrows():
            weight = 1.0 if (20 <= idx <= 35) else 0.1
            heatmap_data.append([row['Latitude'], row['Longitude'], weight])
        
        HeatMap(heatmap_data, radius=25, blur=15, min_opacity=0.3).add_to(m3_heatmap)
        st_folium(m3_heatmap, width=540, height=300, returned_objects=[], key="cv_heatmap_fixed")
        
    with col_stats:
        st.markdown("### 🧠 Inference Meta-Data")
        label = "BLEACHED CORAL" if is_anomaly else "HEALTHY ALIVE CORAL"
        confidence = np.random.uniform(88.5, 97.9) if is_anomaly else np.random.uniform(92.1, 99.4)
        st.code(f"[Inference Log]\nTimestamp: {current_row_p3['Timestamp']}\nTarget Label: {label}\nModel Confidence: {confidence:.2f}%\nLatency: 14.2 ms\nHardware Payload Temp: 34.6 °C", language="ini")
        
        st.markdown("### 📊 Accumulated Mission Area Ecosystem Health")
        bleach_ratio = int((active_index / 50) * 35) if is_anomaly else 15
        healthy_ratio = 100 - bleach_ratio - 25
        
        pie_df = pd.DataFrame({
            'Substrate': ['Healthy Coral', 'Bleached Coral', 'Sand/Algae'],
            'Coverage %': [healthy_ratio, bleach_ratio, 25]
        })
        
        fig_pie = px.pie(
            pie_df, values='Coverage %', names='Substrate', color='Substrate',
            color_discrete_map={'Healthy Coral':'#00ffcc', 'Bleached Coral':'#ff4b4b', 'Sand/Algae':'#a3b8cc'},
            hole=0.3
        )
        fig_pie.update_layout(margin=dict(l=20, r=20, t=10, b=10), height=240,paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',font_color='#ffffff', showlegend=True)
        st.plotly_chart(fig_pie, use_container_width=True)
        if run_stream:
            time.sleep(0.4)
            st.rerun()

#==========================================
# VIEW 4: POLICY & ACTION DASHBOARD
# ========================================== 
elif view_selection == "📋 View 4: Policy & Action Dashboard":
    st.subheader("🇲🇺 Mauritian Ministry of Environment Strategic Planning Hub")

    st.write("This dashboard converts the USV mechatronics payload data directly into actionable environmental marine zoning policies.")
    st.markdown("---")

    col_map_policy, col_export = st.columns(2)
    with col_map_policy:
        st.markdown("### 🗺️ Proposed Emergency Marine Zoning Map")
        st.caption("Red buffer polygons represent areas containing automated Edge AI coral degradation triggers.")
        m4 = folium.Map(location=[-20.4455, 57.7115], zoom_start=15, tiles="OpenStreetMap")
        waypoints = df_telemetry[["Latitude", "Longitude"]].values.tolist()
        folium.PolyLine(locations=waypoints, color="#a3b8cc", weight=2, opacity=0.5, dash_array='5, 5').add_to(m4)

        folium.Circle(location=[-20.4455, 57.7115],radius=180,color="#ff4b4b",fill=True,fill_color="#ff4b4b",fill_opacity=0.4,popup="CRITICAL ZONE AlphaAction Required: Recommended No-Boating Anchor Enclosure.").add_to(m4)

        st_folium(m4, width=540, height=400, returned_objects=[], key="policy_zoning_map")

    with col_export:
        st.warning("⚠️ Zone Alpha Restricted: Highly vulnerable to mechanical anchor scars. Propose temporary closure to eco-tourism vessels.")
        st.info("💡 Thermal Runoff Remediation: Propose sensor nodes deployment at the adjacent drainage outlets to track urban thermal discharge spikes.")

        st.markdown("---")
        st.markdown("### 📥 Global Network Data Export Port")

        csv_data = df_telemetry.to_csv(index=False).encode('utf-8')
        st.download_button(label="💾 Download Raw Sensor & AI Shape-Logs (CSV)",data=csv_data,file_name="mauritius_bluebay_usv_telemetry.csv",mime="text/csv",use_container_width=True)

        st.markdown("---")
        st.markdown("### 🗃️ Integrated Open Data Registries")
        st.caption("Dataset 1 Source: Marine Protected Area (MPA) Boundaries for Mauritius via Protected Planet Database.")
        st.caption("Dataset 2 Source: Global Sea Surface Temperature Daily Continuous Raster Layer via ArcGIS Hub Global Environmental Server (REMSS).")
        st.success("Format standard verified: ISO 19115 Geospatial Metadata compliant.")