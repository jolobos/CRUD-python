import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='digoloko',
    database='testesgbd',
)


cursor = conexao.cursor()
# le o banco
while True:
    selecionar = int(input('Digite um numero para ação no banco de dados: 1-ler, '
                           '2-inserir, 3 -alterar, 4-deletar => '))

    if selecionar <= 4:
        #ler ou read
        if selecionar == 1:
            comando = 'SELECT * FROM produtos'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print('Lista de produtos:')
            for c, e in enumerate(resultado):
                print(f'      nome: {resultado[c][1]} - valor: {resultado[c][2]} - descrição: {resultado[c][3]}')
            break
         #inserir ou create
        if selecionar == 2:
            nome = str(input('Digite o  nome do produto: '))
            valor = float(input('Digite o valor do produto: '))
            descricao = str(input('Digite a descrição do produto: '))
            comando = f'INSERT INTO produtos (nome, valor, descricao) VALUES ("{nome}", {valor}, "{descricao}") '
            cursor.execute(comando)
            conexao.commit()
            print('Produto inserido com sucesso!')
            break
        #alterar ou update
        if selecionar == 3:
            comando = 'SELECT id_produto, nome FROM produtos'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            for c, e in enumerate(resultado):
                print(f'numero: {resultado[c][0]} - produto: {resultado[c][1]}')

            escolha = int(input('Digite o numero corespondente ao produto que será alterado: '))
            nome = str(input('Digite o novo nome do produto: '))
            valor = float(input('Digite o novo valor do produto: '))
            descricao = str(input('Digite a nova descrição do produto: '))
            comando = f'UPDATE produtos SET nome = "{nome}",valor = {valor}, descricao = "{descricao}" WHERE id_produto = {escolha}'
            cursor.execute(comando)
            conexao.commit()
            print('Produto alterado com sucesso!')
            break
        if selecionar == 4:
            comando = 'SELECT id_produto, nome FROM produtos'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            for c, e in enumerate(resultado):
                print(f'numero: {resultado[c][0]} - produto: {resultado[c][1]}')

            escolha = int(input('Digite o numero corespondente ao produto que será deletado: '))
            comando = f'DELETE FROM produtos WHERE id_produto = {escolha}'
            cursor.execute(comando)
            conexao.commit()
            print('o produto foi deletado com sucesso!!!')
            break
    print('ERRO!!! Por favor, digite um numero valido de 1 á 4!!!!')
#edita o banco




cursor.close()
conexao.close()
