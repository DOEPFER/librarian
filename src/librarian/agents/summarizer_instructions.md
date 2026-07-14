# 1. Nome do arquivo
- **Comprimento:** Máximo de **75 caracteres** (desconsiderando a extensão e o caminho). Se necessário, abrevie o nome do arquivo.
- **Conteúdo:** Defina o nome com base no **título** do documento/livro, a **edição** e o **nome do principal autor**.
- Considere os metadados "{title}" e "{author}", para ajudar na definição do nome do arquivo.
- **Formatação:** O nome do arquivo deve estar em **minúsculas** e no **idioma original do documento/livro**. Use **hífen ("-")** em vez de espaços.
- **Extensão:** **Não inclua a extensão** do arquivo (ex: ".pdf").
## Exemplos:
- "name": "python-para-financas-johnson-2ed"
- "name": "introducao-machine-learning-turing"

# 2. Tags
- Crie uma lista de **mínimo de 3 e máximo de 5 tags** relevantes sobre o assunto/tema/subtema/tópico do documento, ordenadas, da mais similar ao documento a menos similar.
- **Formato:** As tags devem ser retornadas como uma lista em formato string, **em inglês**, separadas por **vírgula e um espaço**. Use **hífen ("-")** em vez de espaços.
## Exemplos:
- "tags": ["python", "finance", "pandas", "backtesting", "machine-learning"]
- "tags": ["mathematics", "linear-algebra", "analytical-geometry"]
- "tags": ["biology", "genetics", "dna", "rna"]
- "tags": ["mathematics", "statistics", "probability", "python", "data-science"]

# 3. Resumo
- Crie um resumo objetivo com base na amostra "{sample}" que recebeu.
- **Limite:** Máximo de **4 frases curtas** ou **100 palavras** (o que for atingido primeiro).
- **Foco:** O resumo deve cobrir o assunto/tema/subtema/tópico, a abordagem e a relevância do documento.
## Exemplos:
- "summary": "Este guia aborda os fundamentos da programação Python aplicados ao mercado financeiro. Apresenta bibliotecas essenciais como Pandas e NumPy para análise de dados e backtesting de estratégias de investimento. É um recurso prático e introdutório para analistas."