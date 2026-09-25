import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione [ENTER] para voltar ao menu...")

def desenhar_painel_principal():
    print("""
+-----------------------------------------------------------------------------------+
|  ESTUDO PRÁTICO MSB                            [ Walisson (Concurseiro) | Sair ]  |
|  "Do PDF à aprovação."                                                            |
+-------------------+---------------------------------------------------------------+
|                   |                                                               |
|  [1] Início       |  [ PAINEL PRINCIPAL / GPS DE ESTUDOS ]                        |
|  [2] Materiais    |                                                               |
|  [3] Flashcards   |  +-------------------------+  +----------------------------+  |
|  [4] Questões     |  | MÉDIA GERAL: 78%        |  | META DE EXCELÊNCIA         |  |
|  [5] CEBRASPE     |  | (Hoje: 42 min estudados)|  | Alvo: > 93% por matéria    |  |
|  [6] FGV          |  +-------------------------+  +----------------------------+  |
|  [7] Revisões     |                                                               |
|  [8] Banco Erros  |  A PRÓXIMA AÇÃO RECOMENDADA (Rota Cirúrgica)                  |
|  [9] Tutor MSB    |  +---------------------------------------------------------+  |
| [10] Configurações|  | Matéria: Direito Administrativo                         |  |
|                   |  | Subtema: Atos Administrativos -> Atributos (52%)        |  |
|                   |  | [11] EXECUTAR SESSÃO DE REVISÃO E QUESTÕES AGORA        |  |
|                   |  +---------------------------------------------------------+  |
|                   |                                                               |
|                   |  MAPA DE DEFICIÊNCIAS & DIAGNÓSTICO                           |
|                   |  * Direito Administrativo .......... [ 68% ] -> Crítico       |
|                   |  * Informática ..................... [ 88% ] -> Em Evolução  |
|                   |  * Língua Portuguesa ............... [ 94% ] -> Consolidado  |
|                   |                                                               |
+-------------------+---------------------------------------------------------------+
|  [0] Sair do Sistema                                                              |
+-----------------------------------------------------------------------------------+
""")