import os
import streamlit as st 

# Configuración inicial de la página
st.title("🏦 Cajero Automático")

# Usamos 'session_state' para que el saldo y la moneda no se borren 
# cada vez que la página se actualice al presionar un botón.
if 'saldo' not in st.session_state:
    st.session_state.saldo = 0.0
if 'moneda' not in st.session_state:
    st.session_state.moneda = "USD"
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

# --- SECCIÓN 1: LOGIN (Tu primer bucle while/break) ---
if not st.session_state.autenticado:
    cedula = st.text_input("Ingrese su número de cédula", type="password")
    if st.button("Ingresar"):
        if cedula == "1234567890":
            st.session_state.autenticado = True
            st.rerun() # Esto recarga la página ya autenticado
        else:
            st.error("Cédula incorrecta")
else:
    # --- SECCIÓN 2: CONFIGURACIÓN INICIAL ---
    st.sidebar.header("Configuración de cuenta")
    nuevo_saldo = st.sidebar.number_input("Configura tu saldo inicial:", value=st.session_state.saldo)
    opcion_moneda = st.sidebar.selectbox("Seleccione su moneda", ["1. USD", "2. Bs"])
    
    if st.sidebar.button("Actualizar Datos"):
        st.session_state.saldo = nuevo_saldo
        st.session_state.moneda = "USD" if "1" in opcion_moneda else "Bs"
        st.success("Datos actualizados")

    # --- SECCIÓN 3: MENÚ DE OPERACIONES (Tu segundo bucle while) ---
    st.subheader(f"Bienvenido. Saldo disponible: {st.session_state.saldo} {st.session_state.moneda}")
    
    opcion = st.radio(
        "Selecciona una opción:",
        ["Revisa tu saldo", "Retirar dinero", "Depositar (Transferir)", "Salir"]
    )

    if opcion == "Revisa tu saldo":
        st.info(f"Tu saldo actual es de: {st.session_state.saldo} {st.session_state.moneda}")

    elif opcion == "Retirar dinero":
        monto_retiro = st.number_input("Monto a retirar:", min_value=0.0)
        if st.button("Confirmar Retiro"):
            if monto_retiro <= st.session_state.saldo:
                st.session_state.saldo -= monto_retiro
                st.success(f"Se ha retirado {monto_retiro} {st.session_state.moneda}")
                st.write(f"Nuevo saldo: {st.session_state.saldo}")
            else:
                st.error("Saldo insuficiente")

    elif opcion == "Depositar (Transferir)":
        destinatario = st.text_input("Destinatario:")
        monto_transf = st.number_input("Monto a transferir:", min_value=0.0)
        if st.button("Confirmar Transferencia"):
            if monto_transf <= st.session_state.saldo:
                st.session_state.saldo -= monto_transf
                st.success(f"Se ha transferido {monto_transf} {st.session_state.moneda} a {destinatario}")
                st.write(f"Nuevo saldo: {st.session_state.saldo}")
            else:
                st.error("Saldo insuficiente")

    elif opcion == "Salir":
        if st.button("Cerrar Sesión"):
            st.session_state.autenticado = False
            st.rerun()

    
 # streamlit run cajero_ag.py   
 #a
