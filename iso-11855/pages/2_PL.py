import streamlit as st
from iso_11855.methodology import *

c1, c2, c3 = st.columns(3)

with c1:
    st.write("#### Wbudowany system płaszczyznowy")
    
    system_type = st.select_slider(
        label="System [A, B, C, D, H, I, J]",
        options=["A", "B", "C", "D", "H", "I", "J"])
    
    pl_placement = st.radio("Umiejscowienie", options=["podłoga", "ściana", "sufit"], horizontal=True)
    pl_purpose = st.radio("Przeznaczenie", options=["ogrzewanie", "chłodzenie"], horizontal=True)
    dict_pl_to_eng = {"podłoga": "floor",
                      "ściana": "wall",
                      "sufit": "ceiling",
                      "ogrzewanie": "heating",
                      "chłodzenie": "cooling"}
    eng_case_of_application = " ".join([dict_pl_to_eng.get(pl_word) for pl_word in [pl_placement, pl_purpose]])

    st.write("#### Warstwa wykończeniowa")
    s_u = st.number_input("Grubość warstwy ponad rurą [mm]", 
                        value=45, step=1, format="%i") / 1000
    R_k_B = st.number_input("Opór cieplny warstwy wykończeniowej [m2K/W]", 
                        value=0.10, step=0.05, format="%f")
    k_E = st.number_input("Współczynnik przewodności cieplnej jastrychu [W/mK]", 
                        value=1.8, step=0.1, format="%f")


with c2:
    if system_type != "D":
        st.write("#### Wężownica")

        external_diameter = st.number_input("Średnica zewnętrzna rury [mm]", 
                                    value=16, step=1, format="%i") / 1000
        wall_thickness = st.number_input("Grubość rury [mm]", 
                                    value=2.0, step=0.1, format="%f") / 1000
        conductivity = st.number_input("Współczynnik przewodności cieplnej rury [W/K]", 
                                    value=0.35, step=0.01, format="%f")
        embedded_pipe = EmbeddedPipe(name="rura",external_diameter=external_diameter,
                                    wall_thickness=wall_thickness, conductivity=conductivity)
        W = st.number_input("Rozstaw rur [cm]", value=10, step=5, format="%i") / 100
    else:
        st.write("#### System D jest prosty, czyż nie?")
        W = 0
        embedded_pipe = EmbeddedPipe(name="małe_rurki", 
                                    external_diameter=4, wall_thickness=0.5, conductivity=1)

    if system_type in "ACHIJ":
        st.write("#### Mocowanie")
        psi = st.number_input("Stosunek objętościowy spinek w wylewce [-]", 
        value=0.05, step=0.01, format="%f")
        k_W = st.number_input("Współczynnik przewodności cieplnej spinek [W/mK]", 
        value=0.22, step=0.05, format="%f")
    else:
        psi = 0
        k_W = 0

    if system_type != "D":
        st.write("#### Powłoka rury")
        d_M = external_diameter + st.number_input("Grubość powłoki [mm]", 
                                value=0.0, step=0.1, format="%f") / 1000
        k_M = st.number_input("Współczynnik przewodności cieplnej powłoki [W/mK]", 
                                value = 1.0, step=0.5, format="%f")
    else:
        d_M = 0
        k_M = 0

    if system_type == "B":
        st.write("#### Elementy dyfuzujące ciepło")
        s_WL = st.number_input("Grubość [mm]", 
        value=1.0, step=0.1, format="%f") / 1000
        k_WL = st.number_input("Współczynnik przewodności cieplnej [W/mK]",
        value=50.0, step=5.0, format="%f")
        L_WL = st.number_input("Szerokość [cm]", 
        value=10.0, step=5.0, format="%f") / 100
    else:
        s_WL = 0
        k_WL = 0 
        L_WL = 0


with c3:
    st.write("#### Temperatury")
    t_i = st.number_input("Temperatura w pomieszczeniu [*C]", value=20, step=1, format="%i")
    t_V = st.number_input("Temperatura zasilania [*C]",
        value=40, step=1, format="%i")
    t_R = st.number_input("Temperatura powrotu [*C]",
        value=35, step=1, format="%i")

    UFH = EmbeddedRadiantSystem(
        name="Standard",
        system_type=system_type,
        embedded_pipe=embedded_pipe,
        case_of_application=eng_case_of_application,
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

    st.write("#### Wyniki")
    st.write("Zastosowanie:", " ".join([pl_placement, pl_purpose]))
    st.write("Współczynnik przejmowania cieplnego:", round(UFH.alfa, 1), "W/m²K")
    st.write("Średnia logarytmiczna różnica temperatur:", round(UFH.deltat_H, 2),"K")
    st.write("Równoważny współczynnik przenikania ciepła:", round(UFH.K_H, 2), "W/m²K")
    st.write("Gęstość strumienia ciepła:", round(UFH.q, 1), "W/m2")
