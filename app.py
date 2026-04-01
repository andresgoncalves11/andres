import os
import streamlit as st      
os.system('clear')


st.title("Sistema de Registro y Acceso")

# Creamos la "memoria" para guardar el usuario y la clave
if 'db_nombre' not in st.session_state:
    st.session_state.db_nombre = ""
if 'db_clave' not in st.session_state:
    st.session_state.db_clave = ""
if 'registrado' not in st.session_state:
    st.session_state.registrado = False

# --- SECCIÓN DE REGISTRO ---
if not st.session_state.registrado:
    st.subheader("¿Hola, eres nuevo en la aplicación? Regístrate ahora mismo")
    
    nombre_reg = st.text_input("Crea tu nombre de usuario")
    clave_reg = st.text_input("Crea una contraseña", type="password")
    confirmar_reg = st.text_input("Confirma tu contraseña", type="password")
    
    if st.button("Registrarme"):
        if clave_reg == confirmar_reg and nombre_reg != "":
            st.session_state.db_nombre = nombre_reg
            st.session_state.db_clave = clave_reg
            st.session_state.registrado = True
            st.success("Registro exitoso. Ahora accede a tu cuenta.")
            st.rerun() # Recarga para mostrar el login
        else:
            st.error("Las contraseñas no coinciden o el nombre está vacío.")

# --- SECCIÓN DE LOGIN ---
else:
    st.subheader("Ahora ingresa a tu cuenta")
    
    nombre_login = st.text_input("Ingresa tu nombre")
    clave_login = st.text_input("Ingresa tu contraseña", type="password")
    
    if st.button("Iniciar Sesión"):
        # Tu lógica: nombre == nombre_correcto and contraseña == contraseña_correcta
        if nombre_login == st.session_state.db_nombre and clave_login == st.session_state.db_clave:
            st.success(f"Acceso concedido. Bienvenido a tu cuenta, {nombre_login}.")
            st.balloons() # Un pequeño efecto visual de éxito
        else:
            st.error("Nombre o contraseña incorrectos. Por favor, inténtalo de nuevo.")
    
    if st.button("Volver al registro"):
        st.session_state.registrado = False
        st.rerun()
