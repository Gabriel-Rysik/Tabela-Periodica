from menu import exibir_menu # biblioteca importando a função do menu;
from banco_de_dados import tabelaPeriodica # Dicionário contendo o banco de dados;
from remover_acentos import limpar_texto # biblioteca importando a função para limpar acentuações.
import msvcrt

def programa_principal(): #função para rodar o programa_principal.
    executando = True
    print("-" * 80)
    print("---Tabela Periodica---")
    print("-" * 80)  
    print("\nPressione qualquer tecla para iniciar...")
    msvcrt.getch()

    while executando: #Loop principal.
        opcao = exibir_menu()

        if opcao == "0":
            print("\nPrograma encerrado. Até logo!")
            print("\nCréditos: Gabriel Rysik")
            print("-" * 80)
            executando = False
            break
            
        elif opcao == "1":
            busca_simbolo = True

            while busca_simbolo: 
                print("-" * 80)
                simbolo = input("\nDigite o Símbolo do elemento Químico: Ex:'H' para Hidrogênio: ").lower().strip()

                if simbolo in tabelaPeriodica:
                    elemento = tabelaPeriodica[simbolo]

                    print(f"\nElemento encontrado:")
                    print("-" * 80)
                    print(f"Nome: {elemento['nome']}")
                    print(f"Número Atômico: {elemento['numero_atomico']}")
                    print(f"Massa Molar: {elemento['massa_molar']} g/mol")
                    print(f"Grupo: {elemento['grupo']}")
                    print(f"Descoberto por: {elemento['descoberto_por']}")
                    print(f"Camada Eletrônica: {elemento['camada_eletronica']}")
                    print(f"Prótons: {elemento['protons']}")
                    print(f"Elétrons: {elemento['eletrons']}")
                    print(f"Nêutrons: {elemento['neutrons']}")
                    print("-" * 80)

                else:
                    print("\nErro! Símbolo não encontrado na tabela periódica.")
                    print("-" * 80)

                while True: #Loop para nova pesquisa.
                    encerrar = input("\nDeseja continuar? 'S' para Sim e 'N' para Não ou '0' para retornar ao menu: ").lower().strip()

                    if encerrar == "n":
                        print("\nPrograma encerrado. Até logo!")
                        print("-" * 80)
                        executando = False
                        busca_simbolo = False
                        break

                    elif encerrar == "0":
                        busca_simbolo = False
                        break

                    elif encerrar != "s":
                        print("\nOpção inválida! Voltando ao menu...")
                        print("-" * 80)
                        busca_simbolo = False
                        break
                    else:
                        print("\nReiniciando a busca...")
                        break

        elif opcao == "2":
            busca_nome = True

            while busca_nome:
                print("-" * 80)
                nome_elemento = input("Digite o nome do elemento: ")
                busca_limpa = limpar_texto(nome_elemento) # Limpa o texto do usuário;
                elemento_encontrado = None # Cria uma "pasta vazia" para guardar o resultado se achar.

                for simbolo_chave, dados in tabelaPeriodica.items(): # Varre o banco de dados;
                    nome_banco_limpo = limpar_texto(dados["nome"]) # Limpa o nome cadastrado no banco para comparação.
                    
                    if busca_limpa == nome_banco_limpo: # compara se o que o usuário digitou é igual ao que está no banco de dados;
                        elemento_encontrado = dados # Se sim, guarda os dados do elemento na "pasta vazia".
                        break


                if elemento_encontrado:
                    print(f"\nElemento encontrado:")
                    print("-" * 80)
                    print(f"Nome: {elemento_encontrado['nome']}")
                    print(f"Número Atômico: {elemento_encontrado['numero_atomico']}")
                    print(f"Massa Molar: {elemento_encontrado['massa_molar']} g/mol")
                    print(f"Grupo: {elemento_encontrado['grupo']}")
                    print(f"Descoberto por: {elemento_encontrado['descoberto_por']}")
                    print(f"Camada Eletrônica: {elemento_encontrado['camada_eletronica']}")
                    print(f"Prótons: {elemento_encontrado['protons']}")
                    print(f"Elétrons: {elemento_encontrado['eletrons']}")
                    print(f"Nêutrons: {elemento_encontrado['neutrons']}")
                    print("-" * 80)
                else:
                    print("\nErro! Nome do elemento não encontrado na tabela periódica.")
                    print("-" * 80)

                while True: #Loop para nova pesquisa.
                    encerrar = input("\nDeseja continuar? 'S' para Sim e 'N' para Não ou '0' para retornar ao menu: ").lower().strip()

                    if encerrar == "n":
                        print("\nPrograma encerrado. Até logo!")
                        print("\nCréditos: Gabriel Rysik")
                        print("-" * 80)
                        executando = False
                        busca_nome = False
                        break

                    elif encerrar == "0":
                        busca_nome = False
                        break

                    elif encerrar != "s":
                        print("\nOpção inválida! Voltando ao menu...")
                        print("-" * 80)
                        busca_nome = False
                        break
                    else:
                        print("\nReiniciando a busca...")
                        break
        else:
            print("\nErro! Opção Inválida!")

programa_principal()
