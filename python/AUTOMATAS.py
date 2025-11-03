import tkinter as tk
from tkinter import ttk, messagebox
import sys

# -----------------------------------------------------------------
# FUNCIÓN 1: El Perrito Guardián (contiene 'aba')
# -----------------------------------------------------------------
def probar_afd_perrito(cadena: str) -> tuple[bool, str]:
    """
    Prueba una cadena contra el AFD que acepta si contiene 'aba'.
    Devuelve (resultado, traza_string).
    """
    estado_actual = 'q0'
    estados_finales = {'q3'}
    transiciones = {
        'q0': {'a': 'q1', 'b': 'q0'},
        'q1': {'a': 'q1', 'b': 'q2'},
        'q2': {'a': 'q3', 'b': 'q0'},
        'q3': {'a': 'q3', 'b': 'q3'}
    }

    traza_lista = [f"Inicio: {estado_actual}"]

    if not cadena:
        es_aceptada = estado_actual in estados_finales
        veredicto = "Aceptado (ε)" if es_aceptada else "Rechazado (ε)"
        traza_lista.append(f"Fin. Estado final: {estado_actual} ({veredicto})")
        return (es_aceptada, "\n".join(traza_lista))

    for simbolo in cadena:
        if simbolo not in transiciones[estado_actual]:
            traza_lista.append(f"Símbolo '{simbolo}' inválido. RECHAZADA.")
            return (False, "\n".join(traza_lista))
        
        estado_siguiente = transiciones[estado_actual][simbolo]
        traza_lista.append(f"Leyó '{simbolo}': {estado_actual} -> {estado_siguiente}")
        estado_actual = estado_siguiente

    es_aceptada = estado_actual in estados_finales
    veredicto = "Aceptado" if es_aceptada else "Rechazado"
    traza_lista.append(f"Fin. Estado final: {estado_actual} ({veredicto})")
    
    return (es_aceptada, "\n".join(traza_lista))

# -----------------------------------------------------------------
# FUNCIÓN 2: El Gatito (longitud múltiplo de 3)
# -----------------------------------------------------------------
def probar_afd_gatito(cadena: str) -> tuple[bool, str]:
    """
    Prueba una cadena contra el AFD que acepta longitud múltiplo de 3.
    Devuelve (resultado, traza_string).
    """
    estado_actual = 'q0'
    estados_finales = {'q0'}
    transiciones = {
        'q0': {'a': 'q1', 'b': 'q1'},
        'q1': {'a': 'q2', 'b': 'q2'},
        'q2': {'a': 'q0', 'b': 'q0'}
    }
    
    # (El resto del código de traza es idéntico al del Perrito)
    traza_lista = [f"Inicio: {estado_actual}"]
    if not cadena:
        es_aceptada = estado_actual in estados_finales
        veredicto = "Aceptado (ε)" if es_aceptada else "Rechazado (ε)"
        traza_lista.append(f"Fin. Estado final: {estado_actual} ({veredicto})")
        return (es_aceptada, "\n".join(traza_lista))
    for simbolo in cadena:
        if simbolo not in transiciones[estado_actual]:
            traza_lista.append(f"Símbolo '{simbolo}' inválido. RECHAZADA.")
            return (False, "\n".join(traza_lista))
        estado_siguiente = transiciones[estado_actual][simbolo]
        traza_lista.append(f"Leyó '{simbolo}': {estado_actual} -> {estado_siguiente}")
        estado_actual = estado_siguiente
    es_aceptada = estado_actual in estados_finales
    veredicto = "Aceptado" if es_aceptada else "Rechazado"
    traza_lista.append(f"Fin. Estado final: {estado_actual} ({veredicto})")
    return (es_aceptada, "\n".join(traza_lista))

# -----------------------------------------------------------------
# FUNCIÓN 3: El Loro (paridad de 'a's pares)
# -----------------------------------------------------------------
def probar_afd_loro(cadena: str) -> tuple[bool, str]:
    """
    Prueba una cadena contra el AFD que acepta paridad par de 'a's.
    Devuelve (resultado, traza_string).
    """
    estado_actual = 'qe'
    estados_finales = {'qe'}
    transiciones = {
        'qe': {'a': 'qo', 'b': 'qe'},
        'qo': {'a': 'qe', 'b': 'qo'}
    }

    # (El resto del código de traza es idéntico al del Perrito)
    traza_lista = [f"Inicio: {estado_actual}"]
    if not cadena:
        es_aceptada = estado_actual in estados_finales
        veredicto = "Aceptado (ε)" if es_aceptada else "Rechazado (ε)"
        traza_lista.append(f"Fin. Estado final: {estado_actual} ({veredicto})")
        return (es_aceptada, "\n".join(traza_lista))
    for simbolo in cadena:
        if simbolo not in transiciones[estado_actual]:
            traza_lista.append(f"Símbolo '{simbolo}' inválido. RECHAZADA.")
            return (False, "\n".join(traza_lista))
        estado_siguiente = transiciones[estado_actual][simbolo]
        traza_lista.append(f"Leyó '{simbolo}': {estado_actual} -> {estado_siguiente}")
        estado_actual = estado_siguiente
    es_aceptada = estado_actual in estados_finales
    veredicto = "Aceptado" if es_aceptada else "Rechazado"
    traza_lista.append(f"Fin. Estado final: {estado_actual} ({veredicto})")
    return (es_aceptada, "\n".join(traza_lista))

# -----------------------------------------------------------------
# FUNCIÓN 4: El Conejo (termina en 'bb')
# -----------------------------------------------------------------
def probar_afd_conejo(cadena: str) -> tuple[bool, str]:
    """
    Prueba una cadena contra el AFD que acepta si termina en 'bb'.
    Devuelve (resultado, traza_string).
    """
    estado_actual = 'q0'
    estados_finales = {'q2'}
    transiciones = {
        'q0': {'a': 'q0', 'b': 'q1'},
        'q1': {'a': 'q0', 'b': 'q2'},
        'q2': {'a': 'q0', 'b': 'q2'}
    }
    
    # (El resto del código de traza es idéntico al del Perrito)
    traza_lista = [f"Inicio: {estado_actual}"]
    if not cadena:
        es_aceptada = estado_actual in estados_finales
        veredicto = "Aceptado (ε)" if es_aceptada else "Rechazado (ε)"
        traza_lista.append(f"Fin. Estado final: {estado_actual} ({veredicto})")
        return (es_aceptada, "\n".join(traza_lista))
    for simbolo in cadena:
        if simbolo not in transiciones[estado_actual]:
            traza_lista.append(f"Símbolo '{simbolo}' inválido. RECHAZADA.")
            return (False, "\n".join(traza_lista))
        estado_siguiente = transiciones[estado_actual][simbolo]
        traza_lista.append(f"Leyó '{simbolo}': {estado_actual} -> {estado_siguiente}")
        estado_actual = estado_siguiente
    es_aceptada = estado_actual in estados_finales
    veredicto = "Aceptado" if es_aceptada else "Rechazado"
    traza_lista.append(f"Fin. Estado final: {estado_actual} ({veredicto})")
    return (es_aceptada, "\n".join(traza_lista))

# -----------------------------------------------------------------
# ### CAMBIO ### PRUEBAS AUTOMÁTICAS (REFACTORIZADO)
# -----------------------------------------------------------------
def run_automatic_tests() -> tuple[bool, list]:
    """
    Ejecuta las trazas de ejemplo del PDF.
    Devuelve (all_passed, results_list)
    """
    print("--- Ejecutando pruebas automáticas en segundo plano... ---")
    
    # Lista de todas las pruebas a ejecutar
    # Formato: (función, nombre, cadena, esperado_bool)
    tests_to_run = [
        (probar_afd_perrito, "Perrito", "aba", True),
        (probar_afd_perrito, "Perrito", "aab", False),
        (probar_afd_perrito, "Perrito", "baba", True),
        (probar_afd_gatito, "Gatito", "", True),
        (probar_afd_gatito, "Gatito", "aaa", True),
        (probar_afd_gatito, "Gatito", "ab", False),
        (probar_afd_gatito, "Gatito", "ababab", True),
        (probar_afd_loro, "Loro", "", True),
        (probar_afd_loro, "Loro", "aa", True),
        (probar_afd_loro, "Loro", "a", False),
        (probar_afd_loro, "Loro", "bababa", False),
        (probar_afd_conejo, "Conejo", "abb", True),
        (probar_afd_conejo, "Conejo", "bba", False),
        (probar_afd_conejo, "Conejo", "bb", True),
    ]

    results_list = []
    all_passed = True

    for (func, nombre, cadena, esperado_bool) in tests_to_run:
        (obtenido_bool, traza) = func(cadena)
        
        paso_test = (obtenido_bool == esperado_bool)
        if not paso_test:
            all_passed = False
            
        results_list.append({
            "automata": nombre,
            "cadena": f"'{cadena}'" if cadena else "ε",
            "esperado": "Aceptada" if esperado_bool else "Rechazada",
            "obtenido": "Aceptada" if obtenido_bool else "Rechazada",
            "status": "OK" if paso_test else "FALLO"
        })

    if all_passed:
        print("--- ¡ÉXITO! Todas las pruebas automáticas pasaron. ---")
    else:
        print("--- ¡FALLO! Una o más pruebas automáticas fallaron. ---")
        
    print("--- Lanzando interfaz gráfica... ---")
    return (all_passed, results_list)


# -----------------------------------------------------------------
# ### CAMBIO ### FUNCIÓN PRINCIPAL (TKINTER REESTRUCTURADO)
# -----------------------------------------------------------------
def main():
    
    # 1. Ejecutar las pruebas ANTES de crear la ventana
    (all_tests_passed, test_results) = run_automatic_tests()

    # 2. Crear la interfaz gráfica
    root = tk.Tk()
    root.title("Probador de AFDs (Tarea U3T1 - Raúl Rodríguez)")
    root.geometry("600x750") # ### CAMBIO: Ventana mucho más alta

    main_frame = ttk.Frame(root, padding="15")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # --- ### NUEVO: Panel de Pruebas Automáticas ### ---
    test_frame = ttk.LabelFrame(main_frame, text="Panel de Pruebas Automáticas (Casos Base)", padding="10")
    test_frame.pack(fill=tk.X, expand=True)

    # --- La "casilla" que dice si funcionan ---
    status_text = "Estado: ¡ÉXITO! (Lógica de autómatas verificada)"
    status_color = "green"
    if not all_tests_passed:
        status_text = "Estado: ¡FALLO! (Revise la lógica o las pruebas)"
        status_color = "red"
        
    label_status = ttk.Label(test_frame, text=status_text, font=("Helvetica", 12, "bold"), foreground=status_color)
    label_status.pack(pady=5)
    
    # --- La "mini-tabla" (Treeview) ---
    cols = ("Autómata", "Cadena", "Esperado", "Obtenido", "Status")
    tree = ttk.Treeview(test_frame, columns=cols, show="headings", height=len(test_results))
    
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor=tk.CENTER)
    
    tree.column("Autómata", width=80)
    tree.column("Cadena", width=80)

    # Definir etiquetas de color
    tree.tag_configure("OK", background="pale green")
    tree.tag_configure("FALLO", background="#FFB0B0") # Un rojo claro

    # Llenar la tabla con los resultados
    for result in test_results:
        tag = result["status"] # "OK" o "FALLO"
        tree.insert("", tk.END, values=(
            result["automata"],
            result["cadena"],
            result["esperado"],
            result["obtenido"],
            result["status"]
        ), tags=(tag,))

    tree.pack(fill=tk.X, expand=True, pady=5)
    
    ttk.Separator(main_frame, orient='horizontal').pack(fill='x', pady=15)

    # --- ### Panel Interactivo ### ---
    interactive_frame = ttk.LabelFrame(main_frame, text="Probador Interactivo", padding="10")
    interactive_frame.pack(fill=tk.BOTH, expand=True)

    # --- Fila de Entrada ---
    ttk.Label(interactive_frame, text="Cadena a probar (solo 'a' y 'b'):").pack(fill=tk.X, pady=5)
    
    cadena_var = tk.StringVar()
    entry_cadena = ttk.Entry(interactive_frame, textvariable=cadena_var, font=("Courier", 12))
    entry_cadena.pack(fill=tk.X, pady=5)

    # --- Lógica de Botones (Sin cambios) ---
    def on_button_click(afd_function, afd_name):
        cadena = cadena_var.get().strip()
        
        if not all(c in {'a', 'b'} for c in cadena):
            if cadena: 
                messagebox.showerror("Error de Alfabeto", "La cadena solo puede contener 'a' y 'b'.")
                return

        (es_aceptada, traza_string) = afd_function(cadena)

        if es_aceptada:
            resultado_var.set(f"ACEPTADA")
            label_resultado.config(foreground="green")
        else:
            resultado_var.set(f"RECHAZADA")
            label_resultado.config(foreground="red")
        
        resultado_contexto_var.set(f"[{afd_name}] - Cadena probada: '{cadena}'")
        trace_var.set(traza_string)

    # --- Botones ---
    btn_frame = ttk.Frame(interactive_frame)
    btn_frame.pack(fill=tk.X, pady=10)
    
    btn_perrito = ttk.Button(btn_frame, text="1. Perrito (contiene 'aba')",
                             command=lambda: on_button_click(probar_afd_perrito, "Perrito"))
    btn_perrito.pack(fill=tk.X, pady=2)

    btn_gatito = ttk.Button(btn_frame, text="2. Gatito (múltiplo de 3)",
                            command=lambda: on_button_click(probar_afd_gatito, "Gatito"))
    btn_gatito.pack(fill=tk.X, pady=2)

    btn_loro = ttk.Button(btn_frame, text="3. Loro (paridad 'a's)",
                          command=lambda: on_button_click(probar_afd_loro, "Loro"))
    btn_loro.pack(fill=tk.X, pady=2)

    btn_conejo = ttk.Button(btn_frame, text="4. Conejo (termina en 'bb')",
                            command=lambda: on_button_click(probar_afd_conejo, "Conejo"))
    btn_conejo.pack(fill=tk.X, pady=2)

    # --- Filas de Resultado ---
    resultado_contexto_var = tk.StringVar()
    resultado_contexto_var.set("Esperando prueba...")
    label_contexto = ttk.Label(interactive_frame, textvariable=resultado_contexto_var, font=("Helvetica", 10))
    label_contexto.pack(pady=(15, 0))

    resultado_var = tk.StringVar()
    resultado_var.set("")
    label_resultado = ttk.Label(interactive_frame, textvariable=resultado_var, font=("Helvetica", 16, "bold"), relief="solid", padding=10)
    label_resultado.pack(pady=5, fill=tk.X)
    
    # --- Widget para la traza ---
    trace_var = tk.StringVar()
    trace_var.set("Aquí aparecerá la traza paso a paso...")
    
    label_trace = ttk.Label(
        interactive_frame, 
        textvariable=trace_var, 
        font=("Courier", 10),
        justify=tk.LEFT,
        relief="sunken",
        padding=10,
        wraplength=550
    )
    label_trace.pack(pady=5, fill=tk.BOTH, expand=True)

    # --- ### CAMBIO: Deshabilitar si las pruebas fallaron ### ---
    if not all_tests_passed:
        # Deshabilitar todos los widgets del panel interactivo
        for widget in interactive_frame.winfo_children():
            # A winfo_children() no le gusta que lo iteres y deshabilites al mismo tiempo
            # Así que lo hacemos de forma segura
            if isinstance(widget, (ttk.Entry, ttk.Button, ttk.LabelFrame)):
                widget.config(state=tk.DISABLED)
            # Para el frame de botones, deshabilitar los botones internos
            if isinstance(widget, ttk.Frame):
                for btn in widget.winfo_children():
                    btn.config(state=tk.DISABLED)
        
        # Actualizar etiquetas para mostrar el bloqueo
        resultado_contexto_var.set("Panel deshabilitado.")
        resultado_var.set("PRUEBAS FALLIDAS")
        label_resultado.config(foreground="red")
        trace_var.set("La lógica base de los autómatas falló.\n\n"
                        "Por favor, corrige el código (las funciones 'probar_afd_...') "
                        "antes de usar el probador interactivo.")


    # Iniciar el bucle de la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
