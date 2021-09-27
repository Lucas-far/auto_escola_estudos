

from random import choice as ch
from metodos.bdd import mtd_paint_random as ink

skip = ':\n'

questions = [
    f'As placas de advertência destinam-se a{skip}',

    f"""
    Com exceção da placa Cruz de Santo André. Sentido único e sentido duplo as demais placas que têm formato quadrado,
    fundo na cor amarela e símbolo preto, são placas de{skip}""",

    f"""
    Certificar-se de que dispões do espaço suficiente a de que a visibilidade lhe permite fazê-lo com segurança, deve 
    ser o comportamento do condutor para{skip}""",

    f"O recolhimento do certificado de licenciamento anual, mediante recibo, ocorre quando{skip}",

    f"""
    Quando os condutores e passageiros de motocicletas utilizarem esse veículo sem uso do capacete de segurança, a 
    penalidade será{skip}""",

    f"""
    O condutor deve sinalizar e deslocar, com antecedência, o seu veículo para a faixa mais à esquerda da sua mão de
    direção para{skip}""",

    f'Na inspeção de segurança veicular (estados obrigatórios) serão verificados, entre outros aspectos{skip}',
    f'As placas que têm a finalidade de informar aos usuários restrições no uso das vias são de{skip}',
    f'Diante da placa (R-33) (placa branca com setas giratórias em loop), você entende que{skip}',
    f'Em um cruzamento, o uso da luz amarela, isoladamente, significa que o condutor deve{skip}',
    f'O extintor de incêndios é um equipamento{skip}',
    f'Diante da placa (R-26) (placa branca com seta reta para cima), você entende que{skip}',

    f"""
    Se o proprietário não identificar o condutor que dirigia o veículo autuado, no prazo de quinze dias do recebimento 
    da notificação, será responsável pela infração{skip}""",

    f"""
    Dirigindo por uma via urbana a uma distância de cerca de 50m de um cruzamento, você percebe a luz amarela do 
    semáforo. Nessa situação você deve{skip}""",

    f"""
    Quando um condutor está dirigindo à frente de outro veículo e o mesmo pede passagem, o comportamento correto será
    {skip}""",

    f'Segundo o código de trânsito brasileiro, as vias urbanas classificam-se em{skip}',
    f'É infração grave, punível com multa e retenção do veículo para regularização{skip}',
    f'É considerada infração média de trânsito passível de multa{skip}',

    f"""
    Diante da placa (A-22) (placa amarela com linhas retas afunilando para o centro) você entende que adiante existe uma 
    ponte{skip}""",

    f"""
    Numa via, onde haja duas ou mais faixas sinalizadas para 80km/h, os veículos que desenvolveram velocidade menor 
    devem{skip}""",

    f'Diante da placa (A-2) (placa amarela triangular com curva p/ direita) você entende que existe adiante{skip}',
    f'Em um cruzamento, o veículo que se aproximar pela via à sua direita, terá preferência apenas se{skip}',

    f"""
    A falta de lanternas indicadoras de direção dianteiras de cor âmbar e traseiras de cor âmbar ou vermelha é infração
    {skip}""",

    f'Diante da placa (R-13) (Placa branca com boneco dirigindo trator indo pra esquerda), você entende que é{skip}',

    f"""
    Dirigindo um veículo, ao se aproximar de um cruzamento com sinal luminoso, você observa que a luz vermelha está 
    acesa. Neste caso, você deve{skip}""",

    f"""
    Conduzir o veículo efetuando transporte remunerado de pessoas ou bens, quando não for licenciado para esse fim, 
    salvo casos de força maior ou com permissão da autoridade competente{skip}""",

    f'A ultrapassagem de outro veículo em movimento deverá ser feita{skip}',
    f'Quando um condutor ultrapassar pela contramão outro veículo nos cruzamentos, terá como penalidade{skip}',

    f"""
    É infração de trânsito gravíssima, punida com multa, suspenção do direito de dirigir, retenção do veículo até a 
    apresentação de condutor habilitado e recolhimento do documento de habilitação, quando o condutor dirigir sob a
    influência de álcool em nível superior a""",

    f'Diante da placa (A-35) (placa amarela com uma vaca indo para à esquerda), você entende que nesta área{skip}',
    f'Qual dos equipamentos indicados é obrigatório?{skip}',
    f'O orgão máximo normativo do sistema nacional de trânsito é{skip}',

    f"Os sinais de trânsito, além de serem inscritos em placas e pintados no leito da via pública, podem ainda ser{skip}",
    f'Quando o condutor estacionar o veículo nos viadutos, pontes e túneis será punido com{skip}',
    f'Estão previstas quatro categorias de infração. Cada uma coresponde a um certo número de pontos. Para a infração{skip}',
    f'Aplicar boas relações humanas no trânsito é também{skip}',

    f"""
    Dirigindo um veículo, o condutor que encontrar crianças, pessoas idosas ou deficientes físicos atravessando a via,
    deve{skip}""",

    f"""
    O condutor e os passageiros não deverão abrir a porta do veículo, nem deixá-la aberta ao descer do veículo, sem
    antes{skip}""",

    f'O passageiro tenta irritá-la com uma discussão. Nessa situação, você{skip}',
    f'O condutor após passar sobre uma via alagada, deve testar a{skip}',

    f"""
    Ao chegar a um cruzamento não semaforizado e dotado de faixas de pedestres, você encontra uma mãe com um carrinho de
    bebê querendo fazer a travessia. Nessa situação você{skip}""",

    f'O que se deve fazer ao acender a luz do manômetro no painel?{skip}',
    f'Você está atrasado, saindo da garagem de um prédio, à noite. Você{skip}',

    f"""
    É impossível você desviar e seu veículo passa por um buraco grande de uma via em obras. Mais adiante, você nota 
    alguns ruídos diferentes no veículo. Nessa situação você{skip}""",

    f'Ao atravessar uma passagem de nível com uma ferrovia, sem cancela, você dev{skip}e',

    f"""
    Você acabou de almoçar e está com muito sono. Para chegar ao seu destino, há ainda um longo caminho pela frente. 
    Nessa situação você{skip}""",

    f"""
    Verificar se o espaço é suficiente, sinalizar com antecedência e retornar à faixa anterior, são procedimentos para
    executar uma{skip}""",

    f"""
    O veículo que você dirige tem sinal verde para atravessar o cruzamento, o condutor de outro veículo desobedece à
    sinalização e colide com o seu veículo. Neste acidente sem vítimas, deve-se{skip}""",

    f'Você percebe que o freio do seu veículo está baixo. O comportamento seguro é{skip}',
    f'No uso correto do freio de estacionamento de seu veículo, você deve{skip}'

]  # end

options = []

answers = [
    'Alertar o usuário da via para condições potencialmente perigosas, indicando sua natureza',
    'Advertência',
    'Ultrapassar outro veículo',
    'Houver suspeita de inautenticidade ou adulteração deste documento',
    'Multa, suspensão do direito de dirigir e recolhimento do documento de habilitação',
    'Fazer uma ultrapassagem',
    'Eixos e suspensão',
    'Regulamentação',
    'A circulação deve ser feita em rótula',
    'Parar, a menos que isto resulte em situação de perigo para os veículos que vêm atrás',
    'Obrigatório apenas para caminhões, micro-ônibus, ônibus e veículos que transportam produtos inflamáveis',
    'Só é permitido que você siga em frente',
    'O proprietário do veículo',
    'Manter a atenção, reduzir a marcha do seu veículo e parar',
    'Facilitar-lhe a passagem pelo lado esquerdo da via',
    'Vias locais, coletoras, arteriais e de trânsito rápido',
    'Transitar com o veículo produzindo fumaça, gases ou particular em níveis superiores aos fixados pelo CONTRAN',
    'Atirar objetos ou substâncias de dentro do veículo ou abandoná-los na via',
    'Mais estreita que a pista de rolamento',
    'Transitar na faixa da direita',
    'Existe adiante uma curva à direita',
    'O cruzamento não for sinalizado',
    'Punível com multa e retenção do veículo para regularização',
    'Proibida a circulação de toda espécie de máquinaria agrícola na área ou via sinalizada',
    'Diminuir a velocidade e parar o veículo',
    'Gravíssima com remoção do veículo e multa',
    'Pela esquerda, retornando à sua faixa de trânsito de origem o mais rápido possível, fazendo os sinais' + \
    ' convencionais e com segurança',
    'Multa',
    'Qualquer concentração de álcool por litro de sangue',
    'Poderá encontrar animais na pista',
    'O para-choque',
    'O conselho nacional de trânsito (CONTRAN)',
    'Luminosos, sonoros e por gestos',
    'Remoção do veículo e multa',
    'Média são computados quatro pontos',
    'Ser tolerante com os erros dos outros, priorizando sempre o aspecto segurança',
    'Parar o veículo e facilitar a travessia',
    'Se certificarem de que isso não constitui perigo para eles e para adultos usuários da via',
    'Desconsidera a fala do outro, respira fundo e continua seu trajeto com atenção',
    'Eficiência dos freios, acionando o pedal com simples toques',
    'Sinaliza para e permite a travessia dos pedestres',
    'Parar o veículo em local seguro e verificar o nível do óleo',
    'Dá farol alto, para antes da calçada e segue com a certeza de que não há pedestres',
    'Segue com cuidado e atenção redobrados e leva o veículo à oficina de sua confiança',
    'Para o veículo, olhar para ambos os lados e efetuar cruzamento com segurança',
    'Permanece no local do almoço até se sentir em condições para prosseguir',
    'Ultrapassagem segura',
    'De comum acordo, retirar os veículos para local seguro, anotar a placa do veículo envolvido e dados do outro ' + \
    'condutor, arrolando testemunhas',
    'Procurar imediatamente uma oficina mecânica',
    'Puxar a alavanca sem forçar além do necessário'

]  # end

# question = ch(questions)
# answer_official_index = questions.index(question)
# answer_official = answers[answer_official_index]
# print(len(questions), len(answers))

score_positive, score_negative = 0, 0

while True:

    question = ch(questions)
    answer_official_index = questions.index(question)
    answer_official = answers[answer_official_index]

    box = set({})
    box.add(answer_official)

    while len(box) < 5:
        box.add(ch(answers))

    box = list(box)
    # print(box)

    thread = f"""
    ----------------------------------------------------- PERGUNTA -----------------------------------------------------
    {ink(label=question)}\n
    a) {box[0]}
    b) {box[1]}
    c) {box[2]}
    d) {box[3]}
    e) {box[4]} 
    
    DIGITE A ALTERNATIVA APÓS A SETA -------> """

    answer_correct = f"""
    ----------------------------------------------- ALTERNATIVA CORRETA -----------------------------------------------
    {ink(label=answer_official)}"""

    answer = str(input(thread))

    conditions = {
        'a': box[0], 'b': box[1], 'c': box[2], 'd': box[3], 'e': box[4],
    }

    for key in conditions:
        if answer == key:
            answer = conditions[key]

    if answer == answer_official:
        score_positive += 1
    else:
        score_negative += 1
        print(answer_correct)

    score_now = f"""
    ---------------------------------------------------- PONTUAÇÃO ----------------------------------------------------
    Acertos || {ink(label=str(score_positive))}
    Erros   || {ink(label=str(score_negative))}"""

    print(score_now)
