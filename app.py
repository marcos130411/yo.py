import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

# Título y Descripción
st.title("Calculadora de Rebajas💲💲🤑")
st.markdown("Bienvenido. Introduce tus datos para calcular tu rebaja.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio_original = st.sidebar.number_input("El precio original)", min_value=0, max_value=100000, value=60)
descuento = st.sidebar.slider("El descuento", 1, 100, 50)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
    
    # Fórmula Matemática: Peso entre altura al cuadrado
    ahorro = precio_original * (descuento / 100)
    precio_final = precio_original - ahorro
    
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Tu precio final es:", value=f"{precio_final:.2f}")
        
    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        if descuento < 30:
            st.warning("Vaya mierda de descuento")
        elif 18.5 <= descuento < 50:
            st.success("ni tan mal el descuento")
            st.balloons() # ¡Premio!
        elif 25 <= descuento < 75:
            st.success("buen descuento")
            st.balloons() # ¡Premio!
        else:
            st.error("si te quejas mueres")
            st.balloons() # ¡Premio!
            
    # Extra: Mostrar la fórmula usada (LaTeX)
    st.write("---")
    st.info("Fórmula matemática utilizada:")
    st.latex(r''' Precio final =  precio_original * (descuento / 100) ''')
