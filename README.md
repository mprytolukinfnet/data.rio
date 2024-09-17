# Dashboard de Turismo - Data.Rio

Este projeto é um dashboard interativo desenvolvido com Streamlit para visualizar e analisar dados turísticos do portal Data.Rio. O objetivo é fornecer uma ferramenta para explorar e personalizar as visualizações dos dados, permitindo que os usuários obtenham insights valiosos sobre o setor de turismo.

## Funcionalidades
1. Upload de arquivos CSV com dados de turismo.
2. Filtros interativos usando checkboxes para proprietários e tipos de dados.
3. Download de dados filtrados.
4. Personalização da interface com cores customizáveis.
5. Visualizações de dados simples (gráficos de barra, pizza) e avançadas (histogramas, scatter plots).
6. Exibição de métricas básicas.
7. Persistência de dados e cache para otimizar o desempenho.

## Requisitos

- Python 3.8 ou superior
- `virtualenv` para criação de ambiente virtual
- Os pacotes listados no arquivo `requirements.txt`

## Instruções para configurar o ambiente e rodar o projeto

### 1. Clonar o Repositório

Clone este repositório na sua máquina local.

```bash
git clone https://github.com/mprytolukinfnet/data.rio.git
```

### 2. Criar um Ambiente Virtual

No diretório do projeto, crie um ambiente virtual usando `virtualenv`:

```bash
virtualenv venv
```

### 3. Ativar o Ambiente Virtual
- No Windows:
```bash
venv\Scripts\activate
```

- No Linux/Mac:
```bash
source venv/bin/activate
```

### 4. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

### 5. Executar o Dashboard
Para rodar a aplicação, execute o seguinte comando no terminal:
```bash
streamlit run app.py
```

A aplicação estará disponível no seu navegador, normalmente acessível no endereço http://localhost:8501.

## Baixar os dados para utilizar no Dashboard
Para baixar os dados compatíveis com o dashboard é necessário acessar [o site do Data.Rio](https://www.data.rio/search?groupIds=729990e9fbc04c6ebf81715ab438cae8), fazer a pesquisa desejada, e baixar o arquivo CSV clicando no símbolo de 3 pontos, e na opção "Export public catalog (CSV)". Será baixado um arquivo chamado `DATA RIO.csv`, que deve ser carregado no Dashboard.

## Estrutura do Projeto
- **app.py**: Contém o código principal do dashboard.
- **requirements.txt**: Lista de dependências necessárias para rodar o projeto.

## Observações
Certifique-se de que o arquivo CSV segue o padrão esperado para evitar erros de leitura.

Utilize a funcionalidade de "Selecionar/Desselecionar todos" para facilitar a escolha de múltiplos proprietários ou tipos de dados.
