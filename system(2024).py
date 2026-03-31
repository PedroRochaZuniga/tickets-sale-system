#Analise Geral: O código realiza certas tarefas dependendo da escokha do usúario, dentro dele, ele poderá registrar uma venda, exibir um relatório
#sobre todas as compras, ou apenas sair do código, quando já realizou todas as vendas do dia. Para cada opção citada acima, determinadas funções são executadas,
#onde as mesmas recolhem informações para armazenar dados de vendas, e estes serem usados e apresentados no relatório total. De forma prática, simples e intuitiva>


from enum import Enum, auto

class FormaDePagamento(Enum):
    '''
    Determina as formas de pagamento disponíveis para comprar os tickets.
    '''
    PIX = auto()
    CARTÃO = auto()
    DINHEIRO = auto()

from enum import Enum, auto

class TipoDeUsuário(Enum):
    '''
    Determina o tipo de usuário que realizará o pagamento.
    '''
    ALUNO = auto()
    SERVIDORM3 = auto()
    DOCENTE = auto()
    SERVIDORP3 = auto()
    EXTERNO = auto()

from dataclasses import dataclass

@dataclass
class Venda:
    '''
    Representa os aspectos da venda (forma de pagamento, perfil do comprador,
    quantidade de tickets e o valor total da compra).
    '''
    Usuário : TipoDeUsuário
    Ticket : int
    Pagamento : FormaDePagamento
    Valor_total : float

#Entrada: A função recebe um valor de escolha do usuário, relacionada com o que o mesmo deseja realizar ( (1) registrar uma venda, (2) mostrar o relatório de vendas, (3) sair do progama)
#Saída: A função retornará uma execução, dependendo do valor de entrada, podendo registrar uma venda, visualizar o relatório ou sair.
def menu():
    '''
    Mostrar o menu para o operador do sistema, onde ele
    seleciona qual ação realizar a seguir.
    '''
    lst_vendas = []
    sair = False
    while not sair:
        opcao = int(input(
    '''
 Digite 1 - Registrar uma venda.
 Digite 2 - Exibir o relatório de vendas.
 Digite 3 - Sair.

 Escolha uma opção: '''))
        print(opcao)
        if opcao == 1:
                lst_vendas = registra_venda(lst_vendas)
        elif opcao == 2:
            print('')
            receita(lst_vendas)
            quantidade(lst_vendas)
            tick_por_usu(lst_vendas)
            grafico1(lst_vendas)
            tick_por_pag(lst_vendas)
            grafico2(lst_vendas)
        elif opcao == 3:
        	sair = True
        

# Entrada: A função recebe valores, os quais representam a categoria do comprador.
# Saída: A função devolve o preço de cada ticket, dependendo do tipo do comprador (aluno, servidor, docente, externo).
def valor_ticket(Usuário: float) -> float:
    '''
    Calcula o valor do ticket conforme o tipo de usuário.
    Exemplos:
    >>>valor_ticket(2)
    5.0
    >>>valor_ticket(4)
    10.0
    >>>valor_ticket(5)
    19.0
    >>>valor_ticket(1)
    5.0
    >>>valor_ticket(3)
    10.0
    '''
    if Usuário == (TipoDeUsuário.ALUNO).value:
        valor = 5.0
    elif Usuário == (TipoDeUsuário.SERVIDORM3).value:
        valor = 5.0
    elif Usuário == (TipoDeUsuário.DOCENTE).value:
    	valor = 10.0
    elif Usuário == (TipoDeUsuário.SERVIDORP3).value:
        valor = 10.0
    else:
    	valor = 19.0
    return valor

#Entrada: A função recebe a lista das vendas(lst_vendas).
#Saída: Devolve as informações de cada venda (usuário, tickets, pagamento, valor total).
def printar_lista_vendas(lst_vendas: list[Venda]):
    '''
    Apresenta as informações sobre uma venda.
    Exemplo:
    v1 = Venda(TipoDeUsuário.ALUNO,2,FormaDePagamento.PIX,10.0)
    v2 = Venda(TipoDeUsuário.DOCENTE,3,FormaDePagamento.CARTÃO,30.0)
    >>> printar_lista_vendas([v1,v2])
    Usuário: ALUNO
    Tickets: 2
    Pagamento: PIX
    Valor total: R$10.0
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Usuário: DOCENTE
    Tickets: 3
    Pagamento: CARTÃO
    Valor total: R$30.0
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''
    for venda in lst_vendas:
        print('Usuário:',venda.Usuário.name)
        print('Tickets:',venda.Ticket)
        print('Pagamento:',venda.Pagamento.name)
        print('Valor total: R$',venda.Valor_total, sep = '')
        print('~' * 60)

#Entrada: A função recebe a lista das vendas(lst_vendas).
#Saída: A função devolve a quantidade de tickets vendidos durante o dia(tick)
def quantidade(ficha_dia: list) -> int:
    '''
    Calcula a quantidade de tickets vendidos durante o dia.
    Exemplo:
    v1 = Venda(TipoDeUsuário.ALUNO,2,FormaDePagamento.PIX,10.0)
    v2 = Venda(TipoDeUsuário.EXTERNO,5,FormaDepagamento.CARTÃO,95.0)
    >>>quantidade([v1,v2])
    Total de tickets vendidos: 7 tickets.
    '''
    tick = 0
    for i in ficha_dia:
        tick = tick + i.Ticket
    return print(
        'Total de tickets vendidos:',tick, 'tickets.')

#Entrada: A função recebe a lista das vendas(lst_vendas).
#Saida: A função devolve a receita do dia em reais em relação a quantidade de tickets vendidos(soma).
def receita(rec_dia: list)-> float:
    '''
    Exibe no relatório a receita total das vendas durante o dia
    Exmeplo:
    v1 = Venda(TipoDeUsuário.ALUNO,2,FormaDePagamento.PIX,10.0)
    v2 = Venda(TipoDeUsuário.EXTERNO,5,FormaDepagamento.CARTÃO,95.0)
    >>>receita([v1,v2])
    Receita do dia: R$105.0
    '''
    soma = 0
    for i in rec_dia:
        soma = soma + i.Valor_total    
    return print(
        'Receita do dia: R$',soma, sep = '')
    
#Entrada: A função receberá valores que responderam a aspectos da venda, como tipo de usuário ( 1 para aluno, 2 para servidores até 3 sal mínimo, 3 para docentes, 4 para servidores com mais de 3 salários mínimos e 5 para a comunidade externa),
# quantidade de tickets que irá comprar (int) , resultado da função valor_ticket e irá colocar essas informações dentro de uma lista vazia (lst_vendas), conforme são registradas mais vendas
#Saída: A função devolve a lista das vendas (lst_vendas) com os aspectos de cada venda inseridos nos valores de entrada e saída.
def registra_venda(lst_vendas :list) -> list:
    '''
    Caso o operador do sistema deseje registrar uma venda, esta função receberá as características
    do comprador, forma de pagamento, quanridade de tickets e então armazenará em uma lista,
    para apresentar no relatório das vendas durante o dia.
    '''
    Usuário = int(input(
    '''
 Digite 1 - Aluno.
 Digite 2 - Servidor até três salários min.
 Digite 3 - Docentes.
 Digite 4 - Servidor acima de três salários mín.
 Digite 5 - Comunidade externa.

 Escolha uma opção: '''))
    
    print(Usuário)
    Ticket = int(input('Quantidade de tickets à serem comprados: '))
    preço = float(valor_ticket(Usuário) * Ticket)
    print('Valor total: R$',preço, sep = '')
    Pagamento = int(input(
    '''
 (1)PIX.
 (2)CARTÃO.
 (3)DINHEIRO.

 Escolha uma opção: '''))
    print('')
    print('Pagamento efetuado!')
    print('')
    print('~' * 60)
    
    lst_vendas.append(Venda(
                Usuário = TipoDeUsuário(Usuário),
                Ticket = Ticket,
                Pagamento = FormaDePagamento(Pagamento),
                Valor_total = preço))

    printar_lista_vendas(lst_vendas)
    return lst_vendas

#Entrada: A função recebe uma lista(lst_vendas) e a usa para determinar o tipo do comprador (aluno, usuario, docente, servidor, externo) , sabendo a quantidade de tickets comprado separadamente.
#Saída: A função devolve uma lista ([tick_aluno, tick_servm3, tick_docente, tick_servp3, tick_externo]) que é composta pela quantidade de tickets comprados separadamente por cada usuário.
def tick_por_usu(lst_usu: list) -> list:
    '''
    Calcula a quantidade de tickets vendidos para cada tipo de usuário.
    Exemplo:
    v1 = Venda(TipoDeUsuário.ALUNO,2,FormaDePagamento.PIX,10.0)
    v2 = Venda(TipoDeUsuário.EXTERNO,5,FormaDepagamento.CARTÃO,95.0)
    >>>tick_por_usu([v1,v2])
    [2,0,0,0,5]
    
    '''
    tick_aluno = 0
    tick_servm3 = 0
    tick_docente = 0
    tick_servp3 = 0
    tick_externo = 0
    for i in lst_usu:
        if i.Usuário == TipoDeUsuário.ALUNO:
            tick_aluno = tick_aluno + i.Ticket
        elif i.Usuário == TipoDeUsuário.SERVIDORM3:
            tick_servm3 = tick_servm3 + i.Ticket
        elif i.Usuário == TipoDeUsuário.DOCENTE:
            tick_docente = tick_docente + i.Ticket
        elif i.Usuário == TipoDeUsuário.SERVIDORP3:
            tick_servp3 = tick_servp3 + i.Ticket
        elif i.Usuário == TipoDeUsuário.EXTERNO:
            tick_externo = tick_externo + i.Ticket

    return [tick_aluno, tick_servm3, tick_docente, tick_servp3, tick_externo]

#Entrada:A função recebe a lista da função tick_por_usu ([tick_aluno, tick_servm3, tick_docente, tick_servp3, tick_externo])
# e determina a porcentagem de vendas de tickets por alunos (porcent_aluno,porcent_servm3,porcent_servm3,porcent_servp3,porcent_externo).
#Saída: A função imprime a quantidade de tickets vendidos para cada tipo de usuário em unidades e a porcentagem de cada um, em forma numeral e de gráficos.
def grafico1(lst_usu: list):
    '''
    Calcula a porcentagem de tickets que foram vendidos para cada tipo de usuário,
    e apresenta esses valores na forma de um gráfico de barras.
    '''
    lista_total = tick_por_usu(lst_usu)
    total = (lista_total[0] + lista_total[1] + lista_total[2] + lista_total[3] + lista_total [4])
    porcent_aluno = (lista_total[0] / total) * 100
    porcent_servm3 = (lista_total[1] / total) * 100
    porcent_docente = (lista_total[2] / total) * 100
    porcent_servp3 = (lista_total[3] / total) * 100
    porcent_externo = (lista_total[4] / total) * 100

    print(
        '''Quantidades de tickets vendidos para cada tipo de usuário:
 -> Alunos:''', lista_total[0])
    print(' -> Servidores até três sal. mín.:', lista_total[1])
    print(' -> Docentes:', lista_total[2])
    print(' -> Servidores acima de três sal. mín.:', lista_total[3])
    print(' -> Comunidade externa:', lista_total[4])
    print('')

    '''
    Transformação para o gráfico:
    '''
    grafico_aluno = print('Alunos:                             [', (int(porcent_aluno)//5) * '=', ']', round(porcent_aluno,2),'%', sep = '')
    grafico_servm3 = print('Servidores até três sal. mín.:      [',(int(porcent_servm3)//5) * '=', ']', round(porcent_servm3,2),'%', sep = '')
    grafico_docente = print('Docente:                            [',(int(porcent_docente)//5) * '=', ']', round(porcent_docente,2),'%', sep = '')
    grafico_servp3 = print('Servidores acima de três sal. mín.: [',(int(porcent_servp3)//5) * '=', ']', round(porcent_servp3,2),'%', sep = '')
    grafico_externo = print('Externos:                           [',(int(porcent_externo)//5) * '=', ']', round(porcent_externo,2), '%', sep = '')
    print('Cada "=" vale 5%')

#Entrada: A função recebe uma lista(lst_vendas) e a usa para determinar o tipo de pagamento (pix, dinheiro, cartão) , sabendo a quantidade de tickets comprado separadamente.
#Saída: A função devolve uma lista ([tick_pix, tick_cartao, tick_din]) que é composta pela quantidade de tickets que foram comprados por cada método de pagamento.
def tick_por_pag(lst_pag: list) -> list:
    '''
     Calcula a quantidade de dinheiro que foram efetuados por cada forma de pagamento.
     Exemplo:
     v1 = Venda(TipoDeUsuário.ALUNO,2,FormaDePagamento.PIX,10.0)
     v2 = Venda(TipoDeUsuário.EXTERNO,5,FormaDepagamento.CARTÃO,95.0)
     >>>tick_por_pag([v1,v2])
     [10.0,95.0,0.0]
    '''
    tick_pix = 0
    tick_cartao = 0
    tick_din = 0
    for i in lst_pag:
        if i.Pagamento == FormaDePagamento.PIX:
            tick_pix = tick_pix + i.Valor_total
        elif i.Pagamento == FormaDePagamento.CARTÃO:
            tick_cartao = tick_cartao + i.Valor_total
        elif i.Pagamento == FormaDePagamento.DINHEIRO:
            tick_din = tick_din + i.Valor_total

    return [tick_pix, tick_cartao, tick_din]

#Entrada: A função recebe a lista da função tick_por_pag ([tick_pix, tick_cartao, tick_din])
# e determina a porcentagem de vendas de tickets por tipo de pagamento (porcent_pix,porcent_cartao,porcent_din,).
#Saída: A função imprime a quantidade de tickets vendidos para cada tipo de pagamento em unidades e a porcentagem de cada um, em forma numeral e de gráficos, cada '=' vale 5%.
def grafico2(lst_pag: list):
    '''
    Calcula a porcentagem de reais que foram acumulados para cada forma de pagamento,
    e apresenta esses valores na forma de um gráfico de barras.
    '''
    lst_forma = tick_por_pag(lst_pag)
    valor_sep = (lst_forma[0] + lst_forma[1] + lst_forma[2])
    porcent_pix = (lst_forma[0] / valor_sep) * 100
    porcent_cartao = (lst_forma[1] / valor_sep) * 100
    porcent_din = (lst_forma[2] / valor_sep) * 100

    print('')
    print(
        '''
Valor pago por cada forma de pagamento da receita do dia:
 -> PIX: R$''', lst_forma[0], sep = '')
    print(' -> Cartão: R$', lst_forma[1], sep = '')
    print(' -> Dinheiro: R$', lst_forma[2], sep = '')
    print('')

    '''
    Transformação para o gráfico:
    '''
    grafico_pix = print('PIX:       [', (int(porcent_pix)//5) * '=', ']', round(porcent_pix,2),'%', sep = '')
    grafico_cartao = print('Cartão:    [',(int(porcent_cartao)//5) * '=', ']', round(porcent_cartao,2),'%', sep = '')
    grafico_din = print('Dinheiro:  [',(int(porcent_din)//5) * '=', ']', round(porcent_din,2),'%', sep = '')
    print('Cada "=" equivale a 5%')

def main():
    menu()
main()
