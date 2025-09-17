# 🐍 Automação de Cadastro de Produtos via CSV

Projeto Python para automação de cadastro de produtos a partir de arquivos **CSV** utilizando a biblioteca **PyAutoGUI**.

---

## 🚀 Funcionalidades

- Leitura de arquivos CSV com lista de produtos.  
- Automação de preenchimento em sistemas através do **PyAutoGUI**.  
- Execução passo a passo com intervalos configuráveis para evitar erros de digitação.  
- Logs básicos para acompanhar o processo.  
- Ferramenta auxiliar para captura de coordenadas do mouse em tela.  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**  
- **PyAutoGUI**  
- **Pandas**  

---

## 📂 Estrutura do Projeto

```
.
├── main.py        # Script principal para leitura do CSV e automação do cadastro
├── produtos.csv   # Base de produtos em CSV para cadastro automatizado
├── mouse.py       # Recurso auxiliar para capturar coordenadas do mouse na tela
└── README.md      # Documentação do projeto
```

---

## 📋 Pré-requisitos

- Ter o **Python 3.10+** instalado.  
- Instalar as dependências listadas abaixo.  

### Dependências

```txt
pyautogui
pandas
```

Instale-as com:  

```bash
pip install -r requirements.txt
```

ou crie manualmente um arquivo `requirements.txt` com o conteúdo acima.

---

## ▶️ Como usar

1. Prepare um arquivo `produtos.csv` com os campos necessários.  
2. Utilize o `mouse.py` para identificar as coordenadas dos campos de input na tela do sistema de destino.  
3. Ajuste o `main.py` com as coordenadas obtidas.  
4. Abra o sistema de destino (onde os produtos serão cadastrados).  
5. Execute o script principal:  

```bash
python main.py
```

---

## 📑 Exemplo de CSV

```csv
nome,descricao,preco,quantidade
Mouse Gamer,Mouse RGB com 6 botões,150.90,10
Teclado Mecânico,Switch Blue com iluminação,250.00,5
Monitor FullHD,24 polegadas 75Hz,899.99,3
```

---

## ⚠️ Observações

- A automação simula **cliques e digitação reais**, então evite mexer no mouse/teclado enquanto o script estiver rodando.  
- O tempo de delay entre ações pode ser configurado no código.  
- Recomenda-se testar primeiro em um ambiente de homologação ou tela de testes antes de usar em produção.  

---1    25.95   6.50        


## 📜 Licença

Este projeto é de uso livre para fins de estudo e melhorias. 🚀
