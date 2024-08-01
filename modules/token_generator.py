"""
Módulo para geração de tokens seguros.

Este módulo fornece funções para gerar tokens hexadecimais aleatórios utilizando o módulo `secrets`,
que é projetado para gerar dados criptograficamente seguros.

Funções:
- token_generator: Gera um token hexadecimal aleatório de 16 caracteres.

Exemplo de uso:
    >>> import nome_do_modulo
    >>> nome_do_modulo.token_generator()
    '5f4dcc3b5aa765d61d8327deb882cf99'
"""

import secrets


def token_generator():
    """
    Gera um token hexadecimal aleatório.

    Este método utiliza o módulo `secrets` para gerar um token seguro de 16 caracteres hexadecimais (8 bytes).

    Returns:
        str: Um token hexadecimal aleatório com 16 caracteres.

    Exemplo:
        >>> token_generator()
        '5f4dcc3b5aa765d61d8327deb882cf99'
    """
    return secrets.token_hex(16)
