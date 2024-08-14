# Token e Senha Generator

Este projeto é uma ferramenta simples em Python para gerar tokens e senhas de acesso. Ele é útil para criar senhas seguras e tokens únicos para autenticação e outros usos de segurança.

## Funcionalidades

- Geração de senhas seguras com opções de comprimento e complexidade.
- Geração de tokens hexadecimais únicos para autenticação ou identificadores únicos.

## Requisitos

- Python 3.6 ou superior

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/token-senha-generator.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd token-senha-generator
    ```

3. Instale as dependências (se houver):

    ```bash
    pip install -r requirements.txt
    ```

## Módulos

### `password_module`

Este módulo fornece uma função para gerar senhas seguras e aleatórias.

#### Função

- `password_generator(length=12, include_symbols=True)`: Gera uma senha segura de comprimento especificado. O parâmetro `include_symbols` define se símbolos serão incluídos (padrão é True).

#### Exemplo de Uso

```python
import password_module
print(password_module.password_generator())
