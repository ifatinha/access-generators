"""
Módulo de Geração de Senhas Seguras

Este módulo fornece uma função para gerar senhas seguras e aleatórias. A senha gerada é composta
por uma combinação de letras maiúsculas e minúsculas, dígitos e caracteres de pontuação, garantindo
uma alta segurança e imprevisibilidade.

A função principal deste módulo é:
- `password_generator()`: Gera uma senha segura de 12 caracteres.

Exemplo de uso:
    >>> import password_module
    >>> print(password_module.password_generator())
    'A1b@C2d#EfG!'

Importações:
- `string`: Fornece constantes de strings para caracteres alfabéticos e de pontuação.
- `secrets`: Fornece funções para gerar números e escolhas seguras e criptograficamente fortes.
"""

import string
import secrets


def password_generator():
    """
    Gera uma senha segura de 12 caracteres.

    A senha gerada é composta por uma combinação aleatória de letras maiúsculas e minúsculas,
    dígitos e caracteres de pontuação. Utiliza o módulo `secrets` para garantir que a senha
    seja segura e imprevisível.

    Returns:
        str: Uma senha segura de 12 caracteres.

    Exemplo:
        >>> print(password_generator())
        'A1b@C2d#EfG!'
    """

    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for _ in range(12))

    return password


print("Hoje é quinta feira. " for _ in range(5))
