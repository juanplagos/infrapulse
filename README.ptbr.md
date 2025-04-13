[![English](https://img.shields.io/badge/English-blue.svg)](README.md)
[![Português](https://img.shields.io/badge/Português-green.svg)](README.ptbr.md)

![Status do Projeto](https://img.shields.io/badge/status-WIP-blue)

🚧 Este projeto ainda está em desenvolvimento e pode mudar frequentemente. Contém bugs. É destinado apenas para fins de aprendizado e experimentação.

💬 Feedbacks e contribuições são sempre bem-vindos! Sinta-se à vontade para abrir issues, fazer fork do projeto, enviar pull requests, etc. Toda ajuda é bem-vinda!

---

# Infrapulse

**Infrapulse** é uma coleção de scripts em Python que interagem com serviços AWS usando [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), o SDK Python oficial da AWS. A aplicação possui uma Interface de Usuário em Texto (TUI) construída com [Textual](https://textual.textualize.io/), fornecendo um painel interativo baseado em terminal para gerenciamento de recursos AWS. Este é um projeto de estudo com o objetivo de aprender e experimentar com o gerenciamento de recursos AWS via APIs, além de aprofundar meus conhecimentos em Python.

### Funcionalidades

- Gerenciamento simples de recursos AWS com scripts Python
- TUI desenvolvida com [Textual](https://textual.textualize.io/)
- Utiliza `boto3` para interagir com serviços AWS
- Ajuda na compreensão de automação e scripts AWS

### Pré-requisitos

- Python 3.x instalado
- Credenciais AWS configuradas (`aws configure` ou via funções IAM)
- (Opcional) [LocalStack](https://docs.localstack.cloud/getting-started/) para testar APIs AWS localmente

### Como usar

1. Clone este repositório:

```
git clone https://github.com/juanplagos/infrapulse.git
cd infrapulse
```
2. Crie um ambiente virtual e instale as dependências:

```
python -m venv venv
source venv/bin/activate
cd src
pip install .
```
3. Execute:

```python
python app.py
```
---