# Global-Solution---Gabriela-Mari-Julia-Gomes-Maria-Eduarda
Sistema de monitoramento ambiental por satélite desenvolvido em Python — Global Solutions 2026 | FIAP

Simulação de processamento de dados ambientais detectados por satélites. O sistema registra eventos como desmatamento, queimadas e variações climáticas, analisa padrões e gera relatórios estratégicos.
---
Funcionalidades
Registro de múltiplos eventos ambientais detectados por satélite
Coleta de dados geográficos (país, região, cidade) e métricas (área, intensidade, ocorrências)
Validação automática das entradas do usuário
Análise estatística completa dos eventos registrados
Relatório detalhado com identificação do evento mais crítico
---
Como usar
Pré-requisitos
Python 3.8 ou superior instalado
Nenhuma biblioteca externa necessária (usa apenas recursos nativos do Python)
Executando o programa
```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/monitoramento-satelite.git
 
# Acesse a pasta
cd monitoramento-satelite
 
# Execute o programa
python monitoramento_satelite.py
```
Exemplo de execução
```
Quantos eventos serão registrados? 2
 
📍 EVENTO 1 DE 2
Tipo de evento: Desmatamento
País: Brasil
Região: Amazônia
Cidade: Manaus
Área afetada (km²): 1500.5
Intensidade (1 a 10): 9
Número de ocorrências: 45
```
---
Dados coletados por evento
Campo	Descrição	Restrição
Tipo de evento	Desmatamento, queimada, etc.	Texto livre
País	País de ocorrência	Texto livre
Região	Região geográfica	Texto livre
Cidade	Cidade mais próxima	Texto livre
Área afetada	Em km²	Deve ser > 0
Intensidade	Gravidade do evento	Entre 1 e 10
Ocorrências	Focos detectados	Mínimo 1
---
Análises geradas
Total de eventos registrados
Soma total das áreas afetadas (km²)
Média de intensidade dos eventos
Evento com maior área afetada
Região com maior número de ocorrências
Densidade média (ocorrências ÷ área)
Quantidade de eventos acima da média de intensidade
Evento mais crítico (maior índice de intensidade × área)
---
Estrutura do projeto
```
monitoramento-satelite/
│
├── monitoramento_satelite.py   # Código principal
└── README.md                   # Este arquivo
```
---
Autor
Desenvolvido como atividade acadêmica de simulação de sistemas de monitoramento ambiental por, Gabriela Mari, Julia Gomes e Maria Eduarda
