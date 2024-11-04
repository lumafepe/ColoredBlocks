## Enunciado
    Foram dados blocos coloridos aos ninjas do dojo.
    Foi apontado que blocos foi dado a cada ninja.
    Agora prentende-se obter que ninjas já tem cada uma das cores para evitar dar mais blocos da mesma cor.

## Dados de entrada

- cores_dos_jogadores (Dicionário): Chave: Nome do jogador, Valor: Lista de blocos coloridos que o jogador tem

## Resposta esperada

- Dicionário: Chave: Bloco Colorido, Valor: Set de jogadores que tem esse bloco

## Como utilizar

Deves editar a função `agrupar_jogadores_por_cor` no ficheiro `preencher.py` de forma a automatizar a função sem ser necessário interagires com o terminal.

## Exemplo 1

Dados de entrada:
```python
{
    'Jogador1': ['amarelo', 'vermelho', 'verde', 'turquesa'],
    'Jogador2': ['azul', 'ciano', 'verde', 'vermelho', 'roxo'],
    'Jogador3': ['laranja', 'castanho', 'ciano'], 'Jogador4': ['magenta', 'vermelho', 'rosa', 'roxo'],
    'Jogador5': ['vermelho', 'limão', 'verde'], 'Jogador6': ['ciano', 'azul', 'rosa', 'laranja']
}
```

Resposta:
```python
{
    'amarelo': {'Jogador1'},
    'vermelho': {'Jogador4', 'Jogador1', 'Jogador5', 'Jogador2'},
    'verde': {'Jogador5', 'Jogador1', 'Jogador2'},
    'turquesa': {'Jogador1'}, 
    'azul': {'Jogador6', 'Jogador2'},
    'ciano': {'Jogador6', 'Jogador3', 'Jogador2'},
    'roxo': {'Jogador4', 'Jogador2'},
    'laranja': {'Jogador6', 'Jogador3'},
    'castanho': {'Jogador3'},
    'magenta': {'Jogador4'},
    'rosa': {'Jogador4', 'Jogador6'},
    'limão': {'Jogador5'}
}
```

