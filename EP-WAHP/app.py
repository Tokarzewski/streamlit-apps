import streamlit as st

st.set_page_config(
    page_title="EnergyPlus HeatPumpToWaterAir:EquationFit",
    layout="wide"
)

c1, c2, c3, c4 = st.columns(4)
with c1:
    # Rated capacities
    Rated_total_cooling_capacity = st.number_input('Rated_total_cooling_capacity', value = 23125.6)
    Rated_sensible_cooling_capacity = st.number_input('Rated_sensible_cooling_capacity', value = 16267.06)
    Rated_cooling_power_consumption = st.number_input('Rated_cooling_power_consumption', value = 23125.6/7.007757577)
    Rated_heating_capacity = st.number_input('Rated_heating_capacity', value = 19156.73)
    Rated_heating_power_consumption = st.number_input('Rated_heating_power_consumption', value = 19156.73/3.167053691)
    Rated_air_volume_flow_rate = st.number_input('Rated_air_volume_flow_rate', value = 1.0, format="%f")
    Rated_water_volume_flow_rate = st.number_input('Rated_water_volume_flow_rate', value = 0.00165, step=0.0001, format="%f")

with c2:
    # Total Cooling Capacity Coefficients
    A1 = st.number_input('Total Cooling Capacity Coefficients 1', value = -0.68126221, format="%f")
    A2 = st.number_input('Total Cooling Capacity Coefficients 2', value = 1.99529297, format="%f")
    A3 = st.number_input('Total Cooling Capacity Coefficients 3', value = -0.93611888, format="%f")
    A4 = st.number_input('Total Cooling Capacity Coefficients 4', value = 0.02081177, format="%f")
    A5 = st.number_input('Total Cooling Capacity Coefficients 5', value = 0.008438868, format="%f")
    # Sensible Cooling Capacity Coefficients
    B1 = st.number_input('Sensible Cooling Capacity Coefficients 1', value = 2.24209455, format="%f")
    B2 = st.number_input('Sensible Cooling Capacity Coefficients 2', value = 7.28913391, format="%f")
    B3 = st.number_input('Sensible Cooling Capacity Coefficients 3', value = -9.06079896, format="%f")
    B4 = st.number_input('Sensible Cooling Capacity Coefficients 4', value = -0.36729404, format="%f")
    B5 = st.number_input('Sensible Cooling Capacity Coefficients 5', value = 0.218826161, format="%f")
    B6 = st.number_input('Sensible Cooling Capacity Coefficients 6', value = 0.00901534, format="%f")
    # Cooling Power Consumption Coefficients
    C1 = st.number_input('Cooling Power Consumption Coefficients 1', value = -3.20456384, format="%f")
    C2 = st.number_input('Cooling Power Consumption Coefficients 2', value = 0.47656454, format="%f")
    C3 = st.number_input('Cooling Power Consumption Coefficients 3', value = 3.16734236, format="%f")
    C4 = st.number_input('Cooling Power Consumption Coefficients 4', value = 0.10244637, format="%f")
    C5 = st.number_input('Cooling Power Consumption Coefficients 5', value = -0.038132556, format="%f")

with c3:    
    # Heating Capacity Coefficients
    E1 = st.number_input('Heating Capacity Coefficients 1', value = -5.50102734, format="%f")
    E2 = st.number_input('Heating Capacity Coefficients 2', value = -0.96688754, format="%f")
    E3 = st.number_input('Heating Capacity Coefficients 3', value = 7.70755007, format="%f")
    E4 = st.number_input('Heating Capacity Coefficients 4', value = 0.031928881, format="%f")
    E5 = st.number_input('Heating Capacity Coefficients 5', value = 0.028112522, format="%f")
    # Heating Power Consumption Coefficient
    F1 = st.number_input('Heating Power Consumption Coefficient 1', value = -7.47517858, format="%f")
    F2 = st.number_input('Heating Power Consumption Coefficient 2', value = 6.40876653, format="%f")
    F3 = st.number_input('Heating Power Consumption Coefficient 3', value = 1.99711665, format="%f")
    F4 = st.number_input('Heating Power Consumption Coefficient 4', value = -0.050682973, format="%f")
    F5 = st.number_input('Heating Power Consumption Coefficient 5', value = 0.011385145, format="%f")

with c4:
    # Temperatures and flows from the simulation
    Entering_air_dry_bulb_temperature = st.number_input('Entering_air_dry_bulb_temperature', value = 33.00, step=0.1)
    Entering_air_wet_bulb_temperature = st.number_input('Entering_air_wet_bulb_temperature', value = 20.54, step=0.1)
    Entering_Water_Temperature = st.number_input('Entering_Water_Temperature', value = 36.26, step=0.1)
    Air_volume_flow_rate = st.number_input('Air_volume_flow_rate', value = 0.853, step=0.001, format="%f")
    Water_volumetric_flow_rate = st.number_input('Water_volumetric_flow_rate', value = 0.00165, step=0.001, format="%f")

    Twb_ratio = ( Entering_air_wet_bulb_temperature + 273.15 ) / 283.0
    Tw_ratio = ( Entering_Water_Temperature + 273.15 ) / 283.0
    Tdb_ratio = ( Entering_air_dry_bulb_temperature + 273.15 ) / 283.0
    Va_ratio = Air_volume_flow_rate / Rated_air_volume_flow_rate
    Vw_ratio = Water_volumetric_flow_rate / Rated_water_volume_flow_rate

    # Calculate the dimensionless outputs
    Qc_ratio = A1 + A2 * Twb_ratio + A3 * Tw_ratio + A4 * Va_ratio + A5 * Vw_ratio
    Qsc_ratio = B1 + B2 * Tdb_ratio + B3 * Twb_ratio + B4 * Tw_ratio + B5 * Va_ratio + B6 * Vw_ratio
    Pc_ratio = C1 + C2 * Twb_ratio + C3 * Tw_ratio + C4 * Va_ratio + C5 * Vw_ratio
    Qh_ratio = E1 + E2 * Twb_ratio + E3 * Tw_ratio + E4 * Va_ratio + E5 * Vw_ratio
    Ph_ratio = F1 + F2 * Twb_ratio + F3 * Tw_ratio + F4 * Va_ratio + F5 * Vw_ratio

    # Calculate the heat pump performance
    Total_cooling_capacity = Qc_ratio * Rated_total_cooling_capacity
    Sensible_cooling_capacity = Qsc_ratio * Rated_sensible_cooling_capacity
    Cooling_power_consumption = Pc_ratio * Rated_cooling_power_consumption
    Total_heating_capacity = Qh_ratio * Rated_heating_capacity
    Heating_power_consumption = Ph_ratio * Rated_heating_power_consumption
    Total_cooling_heat_rejection = Total_cooling_capacity + Cooling_power_consumption
    Total_heating_heat_absoprtion = Total_heating_capacity - Heating_power_consumption
    Cooling_COP = Total_cooling_capacity / Cooling_power_consumption
    Heating_COP = Total_heating_capacity / Heating_power_consumption

    st.write('Total_cooling_capacity ', round(Total_cooling_capacity))
    st.write('Sensible_cooling_capacity ', round(Sensible_cooling_capacity))
    st.write('Cooling_power_consumption ', round(Cooling_power_consumption))
    st.write('Cooling COP', round(Cooling_COP,3))
    st.write('')
    st.write('Total_heating_capacity ', round(Total_heating_capacity))
    st.write('Heating_power_consumption ', round(Heating_power_consumption))
    st.write('Heating_COP', round(Heating_COP,3))
    st.write('')
    st.write('Total_cooling_heat_rejection ', round(Total_cooling_heat_rejection))
    st.write('Total_heating_heat_absoprtion ', round(Total_heating_heat_absoprtion))