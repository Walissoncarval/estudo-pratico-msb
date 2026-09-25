import sys
from src.views import limpar_tela, pausar

def tela_materiais():
    limpar_tela()
    print("=" * 60)
    print("               MEUS MATERIAIS & RESUMOS")
    print("=" * 60)
    print("1. [PDF] Direito Administrativo - Atos e Poderes (v2.1)")
    print("2. [PDF] Informática - Segurança e Redes (v1.0)")
    print("3. [PDF] Língua Portuguesa - Sintaxe e Concordância")
    print("4. Adicionar novo material")
    pausar()

def tela_flashcards():
    limpar_tela()
    print("=" * 60)
    print("                      FLASHCARDS")
    print("=" * 60)
    print("Cartões pendentes para hoje: 38")
    print("  • 15 cartões de Direito Administrativo (Urgência Alta)")
    print("  • 23 cartões de Informática")
    print("\n[R] Iniciar Revisão Espaçada (SRS)")
    print("[N] Criar Novo Baralho / Card")
    pausar()

def tela_questoes():
    limpar_tela()
    print("=" * 60)
    print("                  BANCO GERAL DE QUESTÕES")
    print("=" * 60)
    print("Total no banco: 12.450 questões comentadas")
    print("Filtros disponíveis: Banca, Ano, Cargo, Dificuldade.")
    pausar()

def tela_cebraspe():
    limpar_tela()
    print("=" * 60)
    print("                  MODO BANCA: CEBRASPE")
    print("=" * 60)
    print("Regra de penalização: 1 questão errada anula 1 certa.")
    print("Média recente nesta banca: 71%")
    pausar()

def tela_fgv():
    limpar_tela()
    print("=" * 60)
    print("                    MODO BANCA: FGV")
    print("=" * 60)
    print("Foco: Interpretação contextual e análise de casos práticos.")
    print("Média recente nesta banca: 65%")
    pausar()

def tela_revisoes():
    limpar_tela()
    print("=" * 60)
    print("                   CRONOGRAMA DE REVISÕES")
    print("=" * 60)
    print("• Revisão 24h: Atos Administrativos (Pendente)")
    print("• Revisão 7d:  Controle de Constitucionalidade (Concluída)")
    print("• Revisão 30d: Redes de Computadores (Agendada para amanhã)")
    pausar()

def tela_banco_de_erros():
    limpar_tela()
    print("=" * 60)
    print("                      BANCO DE ERROS")
    print("=" * 60)
    print("Você possui 47 questões marcadas para reanálise.")
    print("Principal ponto fraco: Competência vs. Discricionariedade.")
    pausar()

def tela_tutor_msb():
    limpar_tela()
    print("=" * 60)
    print("                     TUTOR VIRTUAL MSB")
    print("=" * 60)
    print("Assistente pronto para tirar dúvidas ou destrinchar gabaritos.")
    pausar()

def tela_configuracoes():
    limpar_tela()
    print("=" * 60)
    print("                     CONFIGURAÇÕES")
    print("=" * 60)
    print("Usuário: Walisson (Concurseiro)")
    print("Plano: Rumo à Aprovação (Ativo)")
    print("Meta diária de estudos: 120 minutos")
    pausar()

def executar_rota_cirurgica():
    limpar_tela()
    print("=" * 60)
    print("          INICIANDO SESSÃO CIRÚRGICA DIRECIONADA")
    print("=" * 60)
    print("Tópico: Direito Administrativo -> Atributos do Ato")
    print("Diagnóstico: Taxa de acerto em 52% (Abaixo do alvo de 93%)")
    print("\nCarregando bateria de 10 questões focadas em suas deficiências...")
    pausar()

def sair_sistema():
    limpar_tela()
    print("=" * 50)
    print("  Progresso salvo com sucesso.")
    print("  Bons estudos e até a posse, Walisson!")
    print("=" * 50)
    sys.exit(0)