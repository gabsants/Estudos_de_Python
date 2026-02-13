"""
Este código automatiza a criação de e-mails corporativos para novos associados.
O sistema valida o nome completo, trata exceções e garante a unidade do e-mail
através da geração de números aleatórios e verificação em lista simulada.
"""

from random import randint

# Lista global simulada (em um sistema real, isso viria de um banco de dados)
# Colocamos fora da função para que ela não seja resetada toda vez que a função rodar
EMAILS_EXISTENTES = ["ana.silva22@empresa.com", "carlos.oliveira10@empresa.com"]

def gerar_email_corporativo(nome_completo):
    
    # Tratamento inicial: remove espaços extras e verifica se está vazio.
    nome = nome_completo.strip()
    
    if not nome:
        return "Erro: O nome não pode ser vazio."

    # Separação de partes do nome para garantir nome e sobrenome.
    partes_nome = nome.split()

    if len(partes_nome) < 2:
        return "Erro: É necessário o nome completo (nome e sobrenome) para gerar o e-mail."

    # Extração do primeiro e último nome em minúsculas.
    primeiro_nome = partes_nome[0].lower()
    ultimo_nome = partes_nome[-1].lower()

    # Lógica de geração de e-mail com garantia de exclusividade.
    tentativa_email = ""
    while True:
        numero_aleatorio = randint(10, 99)
        tentativa_email = primeiro_nome + "." + ultimo_nome + str(numero_aleatorio) + "@empresa.com"
        
        # Verifica se o e-mail já existe na nossa "base de dados"(lista) simulada.
        if tentativa_email not in EMAILS_EXISTENTES:
            EMAILS_EXISTENTES.append(tentativa_email)
            break
            
    return f"Sucesso! E-mail criado: {tentativa_email}"

def principal():
    """Função principal que gerencia a interface com o usuário."""
    print("=== Sistema de Cadastro de E-mail Corporativo ===")
    
    try:
        entrada_usuario = input("Digite seu nome completo: ")
        
        # Chamada da função de lógica
        resultado = gerar_email_corporativo(entrada_usuario)
        print(resultado)
        
    except Exception as e:
        # Captura erros inesperados para não travar o sistema.
        print(f"Ocorreu um erro inesperado no sistema: {e}")

if __name__ == "__main__":
    # Garante que o script rode apenas se executado diretamente.
    principal()
