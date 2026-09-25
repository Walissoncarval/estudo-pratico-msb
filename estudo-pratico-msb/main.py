import sys
from src.views import limpar_tela, desenhar_painel_principal, pausar
from src.screens import (
    tela_materiais,
    tela_flashcards,
    tela_questoes,
    tela_cebraspe,
    tela_fgv,
    tela_revisoes,
    tela_banco_de_erros,
    tela_tutor_msb,
    tela_configuracoes,
    executar_rota_cirurgica,
    sair_sistema,
)

ACOES = {
    "1": lambda: None,
    "inicio": lambda: None,
    "painel": lambda: None,
    "2": tela_materiais,
    "materiais": tela_materiais,
    "meus materiais": tela_materiais,
    "3": tela_flashcards,
    "flashcards": tela_flashcards,
    "4": tela_questoes,
    "questoes": tela_questoes,
    "questões": tela_questoes,
    "5": tela_cebraspe,
    "cebraspe": tela_cebraspe,
    "6": tela_fgv,
    "fgv": tela_fgv,
    "7": tela_revisoes,
    "revisoes": tela_revisoes,
    "revisões": tela_revisoes,
    "8": tela_banco_de_erros,
    "banco de erros": tela_banco_de_erros,
    "erros": tela_banco_de_erros,
    "9": tela_tutor_msb,
    "tutor": tela_tutor_msb,
    "tutor msb": tela_tutor_msb,
    "10": tela_configuracoes,
    "configuracoes": tela_configuracoes,
    "configurações": tela_configuracoes,
    "11": executar_rota_cirurgica,
    "rota": executar_rota_cirurgica,
    "executar": executar_rota_cirurgica,
    "0": sair_sistema,
    "sair": sair_sistema,
    "exit": sair_sistema,
}

def main():
    while True:
        limpar_tela()
        desenhar_painel_principal()
        entrada = input("Digite o número da opção ou nome do comando: ").strip().lower()

        funcao = ACOES.get(entrada)
        if funcao:
            funcao()
        else:
            print(f"\n[!] Comando '{entrada}' inválido. Tente novamente.")
            pausar()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSessão encerrada. Bons estudos!")
        sys.exit(0)