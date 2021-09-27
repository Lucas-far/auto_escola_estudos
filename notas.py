

from random import choice
from time import sleep

# ...•

notas = f"""
    [ item 1 ] ------------------------------------- Habilitação (pré-requisitos) -------------------------------------
      • Ser penalmente imputável (responsável por seus atos) (não significa ser < de 18 anos) 
      • Saber ler e escrever (ser alfabetizado)
      • Portar documento de identidade (foto mandatória)
      • Portar um cadastro de pessoa física (apenas o número já é suficiente); 
      
    [ item 2 ] ------------------------------- Habilitação inicial/provisória (validade) -------------------------------
        • 1 ano (a partir da data de cadastro do candidato no sistema BINCO e RENACH)
        • BINCO  = Base índice nacional de condutores
        • RENACH = Registro Nacional de condutores habilitados;
        
    [ item 3 ] ------------------------ Habilitação (exames médicos e psicológicos) (detalhes) ------------------------
        • Duração de 5 anos para pessoas de até 65 anos        
        • Duração de 3 anos para pessoas com mais de 65 anos;
        
    [ item 4 ] ------------------------------------ Habilitação (processos) (grade) ------------------------------------  
        1 • Avaliação psicológica             (exame)    Exame de aptidão física e mental
        2 • Curso teórico técnico (45h)       (exame)    Exame teórico técnico
        3 • Curso prático de direção (20h)    (exame)    Exame prático de direção
        
        2 • Legislação de trânsito (18h)      • Direção defensiva (16h)    • Primeiros socorros (4h)
          • Meio ambiente e cidadania (4h)    • Mecânica básica de veículos (3h)
            
        3 • Primeira habilitação (20h)    • Adição ou mudança de categoria (15h);
        
        DETALHES
            -> No item 2, a presença é feita via identidade biométrica
            -> No item 2, a aproveitamento é de 70%
            -> No item 3, 20% da carga horária deve ser cumprida pela noite;
            
    [ item 5 ] ------------------------------------------ Habilitação (LADV) ------------------------------------------
        • Documento obrigatório para o treinamento de aulas de direção, expedido pelo DETRAN
        • O requisito é a aprovação em 2 dos 3 processos (Avaliação Psicológica e Curso teórico técnico) 
        • O conteúdo do documento
            -> Orgão expeditor, Nome, Identidade, CPF, RENACH (id), Categoria (sigla), CFC (nome da escola), Validade;
            
    [ item 6 ] ----------------------------------------- Habilitação (detalhe) -----------------------------------------   
        • Qualquer aluno em aula prática sem um instrutor, será suspenso por 6 meses (sinônimos são desprezíveis);
        
    [ item 7 ] --------------------------------------- Habilitação (categorias) ---------------------------------------
        • A, B, A e B, ACC, ACC e B;
        
    [ item 8 ] ---------------------------- Habilitação provisória (aprovação) (reprovação) ----------------------------
        • Aprovação nas 3 etapas, conferindo o documento PPD (permissão para dirigir) ou ACC, válidas por 1 ano
        • Tempo de espera superior a 15 dias, para nova tentativa (treinamento complementar sugerido, não mandatório);
        
    [ item 9 ] ------------------------- Habilitação (transição de provisória para definitiva) -------------------------
        • Solicitada pelo portador de uma habilitação PPD ou ACC, após 1 ano da sua obtenção, para poder adquirir
          a habilitação definitiva CNH ou ACC definitiva
        
        • CONDIÇÃO: não ter cometido qualquer infração GRAVE/GRAVÍSSIMA    ou    não ser reincidente em infrações MÉDIAS
                    não pode cometer mais de 1 infração média, sendo assim o foco na reincidência
                    
        • CONSEQUÊNCIA: reiniciação do processo de habilitação;
        
    [ item 10 ] --------------------------------------- Habilitação (documentos) ---------------------------------------
        • PPD (permissão para dirigir) (categorias: A, B, A e B) (provisória)
        • ACC (autorização para conduzir ciclomotores)           (provisória por 1 ano)
        • CNH (carteira nacional de habilitação)                 (definitiva);
        
    [ item 11 ] ---------------------------------------- Veículos ciclomotores ----------------------------------------
        • Ciclomotor  -> ciclo motorizado de 2/3 rodas, de 50 cilindradas (pot. = 50 cm cúbicos), velocidade até 50km/h
        • Motoneta    -> Veículo automotor de 2 rodas conduzido sentado (pernas juntas)
        • Motocicleta -> Veículo automotor de 2 rodas conduzido montado (pernas separadas);
        
    [ item 12 ] --------------------------------------- Habilitação (categorias) ---------------------------------------
        • A = Veículo de 2/3 rodas com ou sem carro lateral
        • B = Passageiro até 8 lugares (- condutor) de carga <= 3500 PBT
        • C = Passageiro até 8 lugares (- condutor) de carga > 3500 PBT
        • D = Passageiro + de 8 lugares (- condutor) de carga > 3500 PTB 
        • E = Passageiro + de 8 lugares (- condutor) de carga > 6000 PTB (veículos articulados);
        
    [ item 13 ] - Habilitação (prazos de mudanças) -
         • de A para B = imediato  
         • de B para C = 1 ano  
         • de C para D = 1 ano  
         • de D para E = 1 ano  
    """.split(';')


if __name__ == '__main__':

    from metodos.bdd import mtd_paint_random

    autor = 'Roque Maitino Neto'
    u1_s1 = 'Unidade 1 - SEÇÃO 1 = INTRODUÇÃO A ENGENHARIA DE SOFTWARE (página 9 a 16)'

    # print(len(u1_secao_1))
    #
    # for index, string in enumerate(u1_secao_1):
    #     index = index + 1
    #     print([index], string, '\n')

    # while True:
    #
    #     print(u1_s1, mtd_paint_random(label=choice(u1_secao_1)))
    #     sleep(0.01)

