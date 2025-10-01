import json
import os
import sys

def gerar_cardapio_html(dados):
    """Gera o HTML para a lista do cardápio."""
    html_content = ""
    for item in dados:
        html_content += f"""
        <div class="cardapio-item">
            <span class="nome">{item['nome']}</span>
            <span class="preco">{item['preco']}</span>
        </div>
        """
    return html_content

def gerar_jogos_html(dados):
    """Gera o HTML para a lista de jogos."""
    html_content = ""
    for jogo in dados:
        html_content += f"""
        <div class="jogo-card">
            <img src="{jogo['imagem']}" alt="{jogo['nome']}">
            <p>{jogo['nome']}</p>
        </div>
        """
    return html_content

def carregar_dados_json(caminho_arquivo):
    """Carrega dados de um arquivo JSON de forma segura."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERRO: Arquivo não encontrado em '{caminho_arquivo}'.")
        return None
    except json.JSONDecodeError:
        print(f"ERRO: O arquivo '{caminho_arquivo}' não é um JSON válido.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
        return None

def main():
    """Função principal que orquestra a geração do site."""
    print("Iniciando o gerador de site para o Bar de Jogos...")

    # Definição de pastas
    pasta_site_output = 'site'
    pasta_templates = 'templates'
    
    # Garante que o diretório de saída exista
    if not os.path.exists(pasta_site_output):
        os.makedirs(pasta_site_output)

    # Verifica se os caminhos foram passados via linha de comando
    # Caminhos para os arquivos JSON de dados
    caminho_cardapio_json = os.path.join("dados", "cardapio.json")
    caminho_jogos_json = os.path.join("dados", "jogos.json")


    # Carrega os dados dos arquivos
    dados_cardapio = carregar_dados_json(caminho_cardapio_json)
    dados_jogos = carregar_dados_json(caminho_jogos_json)

    # Se algum arquivo de dados falhar, o programa encerra
    if dados_cardapio is None or dados_jogos is None:
        print("Um ou mais arquivos de dados não puderam ser lidos. Abortando a geração do site.")
        sys.exit(1) # Encerra o script com um código de erro

    # Caminho para o template e para o arquivo de saída
    template_path = os.path.join(pasta_templates, 'template_index.html')
    output_path = os.path.join(pasta_site_output, 'index.html')

    # Lê o conteúdo do template
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"ERRO: Arquivo de template não encontrado em '{template_path}'. Abortando.")
        sys.exit(1)

    # Gera o HTML dinâmico
    html_cardapio = gerar_cardapio_html(dados_cardapio)
    html_jogos = gerar_jogos_html(dados_jogos)

    # Substitui os marcadores no template pelo conteúdo gerado
    pagina_final = template_content.replace('<!-- CARDAPIO_PLACEHOLDER -->', html_cardapio)
    pagina_final = pagina_final.replace('<!-- JOGOS_PLACEHOLDER -->', html_jogos)


    # Escreve o arquivo HTML final
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(pagina_final)

    print(f"\nSite gerado com sucesso! A página principal está em: '{output_path}'")

if __name__ == "__main__":
    main()