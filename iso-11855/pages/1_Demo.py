import streamlit as st
from iso_11855.methodology import *


c1, c2, c3 = st.columns(3)
with c1:
    st.write("### Embedded Pipe")
    external_diameter = (
        st.number_input("Pipe external diameter [mm]", value=16, step=1, format="%i")
        / 1000
    )
    wall_thickness = (
        st.number_input("Pipe wall thickness [mm]", value=2, step=1, format="%i") / 1000
    )
    conductivity = st.number_input(
        "Pipe conductivity [W/K]", value=0.35, step=0.01, format="%f"
    )
    embedded_pipe = EmbeddedPipe(
        name="pipe",
        external_diameter=external_diameter,
        wall_thickness=wall_thickness,
        conductivity=conductivity,
    )

with c2:
    st.write("### Embedded Radiant System")
    system_type = st.select_slider(
        label="System type [A, B, C, D, H, I, J]",
        options=["A", "B", "C", "D", "H", "I", "J"],
    )
    if system_type != "D":
        W = st.number_input("Pipe spacing [cm]", value=20, step=5, format="%i") / 100
    else:
        W = 0
    placement = st.select_slider("Location", options=["floor", "wall", "ceiling"])
    purpose = st.select_slider("Purpose", options=["heating", "cooling"])
    case_of_application = placement + " " + purpose

with c3:
    st.write("### Results")

    UFH = EmbeddedRadiantSystem(
        name="Generic",
        system_type=system_type,
        embedded_pipe=embedded_pipe,
        case_of_application=case_of_application,
        W=W,
    )

    st.write("Case of application: ", UFH.case_of_application)
    st.write("Heat flux: ", round(UFH.q, 1), "W/m2")
    st.write("Thermal transfer resistance: ", round(UFH.alfa, 2), "m²K/W")
    st.write(
        "Temperature difference between heating fluid and room: ",
        round(UFH.deltat_H, 2),
        "K",
    )
    st.write("Equivalent heat transmission coefficient: ", round(UFH.K_H, 2), "W/m²K")
