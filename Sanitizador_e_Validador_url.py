import html

def sanitizar_url(url_bruta: str) -> str:
    """Remove espaços, padroniza maiúsculas e neutraliza caracteres perigosos."""
    url_limpa = url_bruta.strip().lower()
    return html.escape(url_limpa)

def validar_url(url_sanitizada: str) -> bool:
    """Verifica se a URL cumpre os requisitos estritos de segurança."""
    if url_sanitizada.startswith("https://") and url_sanitizada.endswith(".com"):
        return True
    return False

# --- Fluxo Principal de Execução ---
if __name__ == "__main__":
    entrada = input("Digite a URL para validação: ")
    
    # Executa a pipeline de segurança
    url_tratada = sanitizar_url(entrada)
    
    if validar_url(url_tratada):
        print(f"✅ URL válida e segura para cadastro: {url_tratada}")
    else:
        print("❌ URL inválida! Bloqueado pela política de segurança.")