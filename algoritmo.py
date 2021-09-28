

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
    f'No uso correto do freio de estacionamento de seu veículo, você deve{skip}',
    f'O condutor que se preocupa em avisar ao outro que o pneu do seu veículo está murcho{skip}',
    f'Ao dirigir na cidade você quer fazê-lo com segurança, facilidade e rapidez. Para tanto você deve{skip}',
    f'Conhecer a cidade é um requisito essencial para uma circulação segura e funcional. Logo, você deve conhecer{skip}',
    f'Você e seus amigos vão comemorar a entrada do Ano Novo numa discoteca. Nessa situação, você{skip}',
    f'Você ouve, ao pisar no pedal do freio, um ruído semelhante ao barulho de atrito entre metais. Você{skip}',
    f'Nenhum condutor deverá frear bruscamente o veículo, salvo{skip}',

    f"""
    Quando ocorrer o afundamento do pedal de freio além da metade da distância entre a sua posição normal e o chão do
    veículo, você deve, primeiramente, verificar o nível de flúido de freio no reservatório. Se o nível estiver correto,
    você deve{skip}""",

    f'É dever do condutor de transporte coletivo{skip}',
    f'O condutor para dirigir com segurança, deve{skip}',
    f'Caso o filtro de ar seco esteja muito sujo, deve-se{skip}',

    f"""
    Trafegando em uma via, você se depara com um guarda de trânsito orientando os condutores a efetuarem um desvio. 
    Neste caso você deve""",

    f'Um cuidado com a bateria do veículo (válido para a maioria dos modelos - bateria não selada) é a{skip}',
    f'Assumir um comportamento seguro significa{skip}',
    f'O condutor acabou de ser demitido do seu emprego. Ele deve{skip}',
    f'Na necessidade de efetuar a troca de uma peça do sistema de freios do seu veículo, é aconselhável{skip}',
    f'Os riscos que podem ser oferecidos pelo veículo estão relacionados{skip}',
    f'Tendo verificado que é necessário completar o nível de água da bateria de seu veículo, você coloca{skip}',

    f"""
    Você está numa via de trânsito rápido com fluxo grande, a uma velocidade média de 60km/h. O veículo à sua frente 
    derrapa e freia brsucamente. Nessa situação você{skip}""",

    f'Em direção defensiva, HABILIDADE significa{skip}',

    f"""
    O condutor de veículo automotor envolvido em acidente de trânsito, sendo considerado culpado, além da punição que
    lhe for aplicável ou aplicada, deverá ser submetida a exames de aptidão física e mental, noções de primeiros 
    socorros e ainda a{skip}""",

    f'A única forma de eliminar o álcool do organismo é{skip}',

    f'Quando algém sofre um traumatismo e desmaia, o que é mais perigoso e comum em causar obstrução das vias áereas?{skip}',
    f'A baixa calibragem dos pneus pode causar{skip}',
    f'Uma das peças fundamentais do sistema de arrefecimento é{skip}',
    f'O condutor que avistar uma poça de água deverá{skip}',
    f'Que atitude deve-se tomar quando alguém que sofreu acidente e necessita de socorro é portador do vírus da AIDS?{skip}',

    f"""
    Linhas transversais inscritas na cor branca que através de efeito visual, estimulamos condutores a reduzirem a 
    velocidade, chamam-se linhas de estímulo{skip}""",

    f'Em caso de acidente{skip}',
    f'Qual o método mais indicado para conter uma hemorragia externa?{skip}',
    f'A finalidade do óleo lubrificante do motor é{skip}',
    f'Diante da placa (A-31) (Placa amarela com boneco dirigindo um trator para a <-) você entende que nesta área{skip}',
    f'Os gases emitidos pelos veículos são perigosos para à saúde do homem porque podem{skip}',
    f'A realização de qualquer ato público que interfira no trânsito depende de{skip}',

    f"""
    Quando o condutor precisa tomar um medicamento que produz um efeito de sonolência, é de sua responsabilidade e para
    a sua segurança{skip}""",

    f"""
    Em um acidente a vítima está dentro do veículo que tem fumaça em seu interior. Nessa situação, o que fazer após
    chegar a conclusão que não há risco pessoal?{skip}""",

    f'A inspeção de Segurança Veicular (nos estados com obrigatoriedade) tem por objetivo{skip}',
    f'As infrações previstas no Código Brasileiro de Trânsito são de natureza{skip}',
    f'Quando o veículo estiver estacionado impedindo a movimentação de outro veículo, o condutor será punido com{skip}',
    f'O flúido do freio deve ser trocado periodicamente porque{skip}',
    f'Os poluentes do ar especificados pelo Código de Trânsito Brasileiro são{skip}'

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
    'Transitar com o veículo produzindo fumaça, gases ou partículas em níveis superiores aos fixados pelo CONTRAN',
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
    'Puxar a alavanca sem forçar além do necessário',
    'Age com solidariedade e cortesia',
    'Conhecer as principais regiões e vias da cidade, vias de acesso e as diferentes vias urbanas e rodoviárias',
    'As zonas, regiões e bairros da cidade, suas vias de acesso e vias alternativas',
    'Combina quem não vai ingerir bebida alcoólica para dirigir na volta',
    'Providência uma revisão das pastilhas e dos discos de freio',
    'Por questão de segurança',
    'Providenciar uma revisão do sistema de freios, por técnico especializado',
    'Parar o veículo para embarque somente nos pontos estabelecidos',
    'Estar atento a tudo que acontece no trânsito',
    'Trocá-lo',
    'Colaborar com o guarda e fazer o desvio, pois a autoridade de trânsito sempre deve ser respeitada',
    'Verificação periódica do nível da água, de acordo com as recomendações do fabricante',
    'Perceber os riscos e agir para evitá-los ou controlá-los',
    'Manter-se tranquilo e redobrar a atenção no trânsito',
    'Substituir por uma peça original de fábrica',
    'As condições de funcionamento ao estado de conservação e modo de operação',
    'Água destilada',
    'Reduz a velocidade aos poucos e sinaliza para o condutor de trás',
    'Manejar o veículo com perícia',
    'Exame escrito sobre legislação de trânsito e exame de direção veicular',
    'O tempo, pois a eliminação se dá de maneira lenta, lavando de 6 à 8 horas',
    'A própria língua ao relaxar',
    'Danos, desgaste, instabilidade aos pneus',
    'A ventoinha',
    'Desacelerar suavemente, segurar firme o volante e manter o veículo em linha reta',
    'Prestar socorro à vítima com as devidas precauções',
    'à redução de velocidade',
    'é obrigação de todos prestar auxílio desde que não corra risco pessoal',
    'Aplicar pressão direta sobre o ferimento, com uma compressa seca e limpa (acho errado)',
    'Reduzir o atrito entre as peças',
    'Pode encontrar máquinas agrícolas na pista',
    'Agravar moléstias respiratórias como asma e bronquite',
    'Previa autorização da Autoridade de Trânsito',
    'Deixar de dirigir nesta condição',
    'Retirar a pessoa de dentro do carro, após imobilizá-la da melhor forma possível',
    'Contribuir para a segurança do trânsito',
    'Gravíssima, grave, média e leve',
    'Remoção do veículo e multa (2)',
    'é contaminado com água',
    'Gases'

]  # end

# question = ch(questions)
# answer_official_index = questions.index(question)
# answer_official = answers[answer_official_index]
# print(len(questions), len(answers))
#
# box_questions, box_answers = [], []
# for string in questions:
#     box_questions.append(questions.count(string))
#
# for string in answers:
#     box_answers.append(answers.count(string))
#
# print(2 in box_questions)
# print(2 in box_answers)

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
