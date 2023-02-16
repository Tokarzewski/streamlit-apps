import streamlit as st
from iso_11855.methodology import *

c1, c2, c3 = st.columns(3)

with c1:
    st.write("#### Embedded Radiant System")
    system_type = st.select_slider(
        label="System type [A, B, C, D, H, I, J]",
        options=["A", "B", "C", "D", "H", "I", "J"],)
    placement = st.radio("Location", options=["floor", "wall", "ceiling"], horizontal=True)
    purpose = st.radio("Purpose", options=["heating", "cooling"], horizontal=True)
    case_of_application = placement + " " + purpose

    st.write("#### Covering")
    s_u = st.number_input("Thickness of layer above the pipe [mm]", 
                        value=45, step=1, format="%i") / 1000
    R_k_B = st.number_input("Thermal resistance of the floor covering [m2K/W]", 
                        value=0.10, step=0.05, format="%f")
    k_E = st.number_input("Thermal resistance of the floor covering [m2K/W]", 
                        value=1.8, step=0.1, format="%f")


with c2:
    if system_type != "D":
        st.write("#### Embedded Pipe")

        external_diameter = st.number_input("Pipe external diameter [mm]", 
                                    value=16, step=1, format="%i") / 1000
        wall_thickness = st.number_input("Pipe wall thickness [mm]", 
                                    value=2.0, step=0.1, format="%f") / 1000
        conductivity = st.number_input("Pipe conductivity [W/K]", 
                                    value=0.35, step=0.01, format="%f")
        embedded_pipe = EmbeddedPipe(name="pipe",external_diameter=external_diameter,
                                    wall_thickness=wall_thickness, conductivity=conductivity)
        W = st.number_input("Pipe spacing [cm]", value=10, step=5, format="%i") / 100
    else:
        st.write("#### System D is pretty simple, isn't it?")
        W = 0
        embedded_pipe = EmbeddedPipe(name="small_pipes", 
                                    external_diameter=4, wall_thickness=0.5, conductivity=1)

    if system_type in "ACHIJ":
        # studs
        st.write("#### Studs")
        psi = st.number_input("Volume ratio of the attachement studs in the screed", 
        value=0.05, step=0.01, format="%f")
        k_W = st.number_input("Thermal conductivity of the attachements studs [W/mK]", 
        value=0.50, step=0.05, format="%f")
    else:
        psi = 0
        k_W = 0

    if system_type != "D":
        st.write("#### Sheating")
        d_M = st.number_input("External diameter of sheating [mm]", 
                                value=17.0, step=0.1, format="%f") /1000
        k_M = st.number_input("Sheating material conductivity [W/mK]", 
                                value = 1.0, step=0.5, format="%f")
    else:
        d_M = 0
        k_M = 0

    if system_type != "B":
        s_WL = 0
        k_WL = 0 
        L_WL = 0
    else:
        st.write("#### Heat diffusion device")
        s_WL = st.number_input("Thickness of the heat conducting material [mm]", 
        value=2.0, step=0.1, format="%f") / 1000
        k_WL = st.number_input("Thermal conductivity of the heat conducting material [W/mK]",
        value=50.0, step=5.0, format="%f")
        L_WL = st.number_input("Width of heat conducting device [cm]", 
        value=10.0, step=5.0, format="%f") / 100


with c3:
    st.write("#### Temperatures")
    t_i = st.number_input("Design indoor temperature [*C]", value=20, step=1, format="%i")
    t_V = st.number_input("Design supply temperature of heating or cooling medium [*C]",
        value=40, step=1, format="%i")
    t_R = st.number_input("Design return temperature of heating or cooling medium [*C]",
        value=35, step=1, format="%i")

    UFH = EmbeddedRadiantSystem(
        name="Generic",
        system_type=system_type,
        embedded_pipe=embedded_pipe,
        case_of_application=case_of_application,
        W=W,
        d_M=d_M,
        k_M=k_M,
        s_WL=s_WL,
        k_WL=k_WL,
        L_WL=L_WL,
        s_u=s_u,
        R_k_B=R_k_B,
        k_E=k_E,
        psi=psi,
        k_W=k_W,
        t_i=t_i,
        t_V=t_V,
        t_R=t_R,
    )

    st.write("#### Results")
    st.write("Case of application:", UFH.case_of_application)
    st.write("Thermal transfer resistance:", round(UFH.alfa, 2), "m²K/W")
    st.write("Temperature difference between heating fluid and room:",
        round(UFH.deltat_H, 2),"K",)
    st.write("Equivalent heat transmission coefficient:", round(UFH.K_H, 2), "W/m²K")
    st.write("Heat flux:", round(UFH.q, 1), "W/m2")
