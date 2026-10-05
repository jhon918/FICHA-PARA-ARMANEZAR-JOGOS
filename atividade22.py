# Cadastro de jogos em arquivo texto (games.txt)

ARQUIVO = "games.txt"
SEPARADOR = ";"

MENU = """
MENU
1 - Cadastrar novo item
2 - Listar cadastros
3 - Sair"""


def valida_int(pergunta, minimo, maximo):
    """Lê um inteiro entre minimo e maximo; repete até o valor ser válido."""
    while True:
        try:
            x = int(input(pergunta))
        except ValueError:
            print("Digite um número inteiro.")
            continue
        if minimo <= x <= maximo:
            return x
        print(f"Opção inválida. Digite um valor entre {minimo} e {maximo}.")


def lerTexto(pergunta):
    """Lê um texto que não seja vazio nem contenha o separador do arquivo."""
    while True:
        texto = input(pergunta).strip()
        if not texto:
            print("Esse campo não pode ficar vazio.")
        elif SEPARADOR in texto:
            print(f'Não use o caractere "{SEPARADOR}", ele separa os campos no arquivo.')
        else:
            return texto


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    """Acrescenta um registro no fim do arquivo (o modo "a" cria o arquivo se não existir)."""
    try:
        with open(nomeArquivo, "at", encoding="utf-8") as arq:
            arq.write(f"{nomeJogo}{SEPARADOR}{nomeVideogame}\n")
    except OSError as erro:
        print(f"Erro ao gravar no arquivo: {erro}")
    else:
        print("Jogo cadastrado com sucesso!")


def listarArquivo(nomeArquivo):
    """Mostra os registros lendo o arquivo uma linha por vez."""
    total = 0
    try:
        with open(nomeArquivo, "rt", encoding="utf-8", errors="replace") as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha:
                    continue
                jogo, _, videogame = linha.partition(SEPARADOR)
                total += 1
                print(f"{total:3}. {jogo} ({videogame})")
    except FileNotFoundError:
        pass  # arquivo ainda não existe = nenhum cadastro feito
    except OSError as erro:
        print(f"Erro ao ler o arquivo: {erro}")
        return

    if total == 0:
        print("Nenhum jogo cadastrado ainda.")


def main():
    while True:
        print(MENU)
        op = valida_int("Escolha a opção desejada: ", 1, 3)

        if op == 1:
            print("\nCadastro de novo item")
            nomeJogo = lerTexto("Nome do jogo: ")
            nomeVideogame = lerTexto("Nome do videogame: ")
            cadastrarJogo(ARQUIVO, nomeJogo, nomeVideogame)
        elif op == 2:
            print("\nListagem de itens")
            listarArquivo(ARQUIVO)
        else:
            print("Encerrando o programa.")
            break


if __name__ == "__main__":
    main()