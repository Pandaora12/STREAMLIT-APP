import streamlit as st
import database
import pandas as pd

database.create_table()

def cadastro_produto():
    with st.form(key='cadastro_form'):
        id_produto = st.text_input('ID')
        nome = st.text_input('Nome')
        valor_unitario = st.number_input('Valor Unitário', min_value=0.0, format="%.2f")
        qtde_estoque = st.number_input('Quantidade em Estoque', min_value=0)

        submit_button = st.form_submit_button(label='Cadastrar Produto')
        
        if submit_button:
            if id_produto and nome:
                database.add_produto(id_produto, nome, valor_unitario, qtde_estoque)
                st.success(f'Produto {nome} cadastrado com sucesso!')
            else:
                st.error("Por favor, preencha todos os campos.")

def relatorio_produtos():
    produtos = database.get_produtos()
    produtos_df = pd.DataFrame(produtos, columns=['ID', 'Nome', 'Valor', 'QTDE'])
    st.write("Relatório de Produtos:")
    st.dataframe(produtos_df)

def atualizar_produto():
    id_produto = st.text_input('Código do Produto a ser Atualizado')
    
    if id_produto:
        produto = next((p for p in database.get_produtos() if p[0] == int(id_produto)), None)
        
        if produto:
            nome = st.text_input('Nome', produto[1])
            valor_unitario = st.number_input('Valor Unitário', min_value=0.0, format="%.2f", value=produto[2])
            qtde_estoque = st.number_input('Quantidade em Estoque', min_value=0, value=produto[3])

            if st.button('Atualizar Produto'):
                database.update_produto(int(id_produto), nome, valor_unitario, qtde_estoque)
                st.success(f'Produto {nome} atualizado com sucesso!')
        else:
            st.error('Produto não encontrado.')
    else:
        st.error('Informe o código do produto.')

def excluir_produto():
    id_produto = st.text_input('Código do Produto a ser Excluído')
    if st.button('Excluir Produto'):
        if id_produto:
            produto = next((p for p in database.get_produtos() if p[0] == int(id_produto)), None)
            if produto:
                database.delete_produto(int(id_produto))
                st.success(f'Produto {id_produto} excluído com sucesso!')
            else:
                st.error('Produto não encontrado.')
        else:
            st.error('Informe o código do produto.')
st.title('Cadastro de Produtos')
option = st.selectbox('Escolha a ação', ['Cadastrar Produto', 'Relatório de Produtos', 'Atualizar Produto', 'Excluir Produto'])

if option == 'Cadastrar Produto':
    cadastro_produto()
elif option == 'Relatório de Produtos':
    relatorio_produtos()
elif option == 'Atualizar Produto':
    atualizar_produto()
elif option == 'Excluir Produto':
    excluir_produto()
