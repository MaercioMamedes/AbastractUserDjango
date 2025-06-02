# Projeto de Estudo: Customizando Autenticação e Modelo de Usuário no Django

## Descrição do Projeto

Este projeto é um estudo de caso focado na **personalização completa do sistema de autenticação e do modelo de usuário** padrão do Django 4.2. O objetivo é demonstrar como substituir o modelo de usuário padrão (`django.contrib.auth.models.User`) por um modelo **totalmente customizado**.

O estudo abrange a criação de um modelo de usuário que herda de `AbstractBaseUser` e a implementação de um gerenciador de modelo (`Manager`) que herda de `BaseUserManager`. Ele também mostra a configuração necessária no `settings.py` para que o Django utilize este modelo customizado.

## Objetivos de Estudo

*   Entender a estrutura do sistema de autenticação do Django.
*   Aprender a substituir o modelo de usuário padrão por um **modelo customizado** (`AUTH_USER_MODEL`).
*   Implementar um modelo de usuário que herde de `AbstractBaseUser` para fornecer a base para senhas hashed e redefinições de senha tokenizadas.
*   Definir os campos essenciais para um modelo de usuário customizado, como `USERNAME_FIELD` e `REQUIRED_FIELDS`.
*   Escrever um gerenciador de modelo customizado que herde de `BaseUserManager` e implemente os métodos `create_user` e `create_superuser`.
*   Explorar a compatibilidade do modelo de usuário customizado com o Django Admin e formas embutidas, se aplicável.
*   Aprender a referenciar o modelo de usuário de forma segura em outras partes da aplicação usando `settings.AUTH_USER_MODEL` ou `get_user_model()`.

## Pré-requisitos

*   Python 3.x instalado.
*   Django 4.x instalado (`pip install Django`).
*   Conhecimento básico de Python e Django.

## Configuração e Execução

1. **Clone o repositório:**
    ```bash
    git clone <url-do-seu-repositorio>
    cd <nome-da-pasta-do-projeto>
    ```

2. **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt # Certifique-se de ter um arquivo requirements.txt com 'Django'
    ```

4. **Configure o modelo de usuário customizado:**
    *   Crie um app Django para conter o modelo de usuário customizado, por exemplo, `customauth`.
    *   **No arquivo `settings.py` do seu projeto, defina `AUTH_USER_MODEL` para apontar para o seu modelo customizado ANTES de rodar qualquer migração**. Por exemplo:
        ```python
        # settings.py
        INSTALLED_APPS = [
            # ... outros apps
            'customauth', # Seu app customizado deve estar aqui.
            # ...
        ]
        AUTH_USER_MODEL = 'customauth.MyUser' # Substitua MyUser pelo nome do seu modelo
        ```
    *   Crie o seu modelo de usuário customizado (por exemplo, em `customauth/models.py`), herdando de `AbstractBaseUser` e definindo o `Manager` customizado.
    *   Crie o seu gerenciador de modelo customizado (por exemplo, em `customauth/models.py`), herdando de `BaseUserManager`.

5. **Crie e aplique as migrações:**
    ```bash
    python manage.py makemigrations customauth # Crie a migração para seu app customauth
    python manage.py migrate # Aplique todas as migrações pendentes, incluindo a do seu modelo customizado
    ```
    **Nota:** O modelo referenciado por `AUTH_USER_MODEL` deve ser criado na primeira migração do seu app (`0001_initial`) para evitar problemas de dependência.

6. **Crie um superusuário:**
    ```bash
    python manage.py createsuperuser
    ```
    Você será solicitado a fornecer os campos definidos em `REQUIRED_FIELDS` no seu modelo customizado, além do campo definido por `USERNAME_FIELD` e a senha.

7. **Rode o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

## Uso e Testes

*   Acesse o Django Admin (geralmente em `http://127.0.0.1:8000/admin/`). Use as credenciais do superusuário que você criou para testar a autenticação via seu modelo e backend.
*   Implemente views e URLs para testar a autenticação e login no frontend da sua aplicação. O método `django.contrib.auth.authenticate()` pode ser usado para verificar as credenciais contra os backends configurados.

## Considerações Adicionais

*   **Django Admin:** Se seu modelo customizado não herda de `AbstractUser`, você precisará definir uma classe `ModelAdmin` customizada para fazê-lo funcionar corretamente com o Admin. Um exemplo completo para um modelo baseado em `AbstractBaseUser` e compatível com Admin está incluído na documentação.
*   **Permissões:** Se você precisar do sistema de permissões do Django, pode incluir `PermissionsMixin` na herança do seu modelo customizado. Caso contrário, você pode implementar os métodos `has_perm`, `has_module_perms`, etc., diretamente no seu modelo ou backend customizado.
*   **Referenciando o Usuário:** Sempre use `settings.AUTH_USER_MODEL` ou `get_user_model()` ao criar relacionamentos (ForeignKey, ManyToManyField) com o modelo de usuário em outros modelos ou ao conectar sinais, para garantir compatibilidade se o modelo de usuário for trocado no futuro.
*   **Usuários Inativos:** Por padrão, `ModelBackend` e `RemoteUserBackend` proíbem a autenticação de usuários com `is_active=False`. Se você criar um backend customizado, precisará implementar essa verificação se desejar.

Este README serve como um guia inicial para configurar e entender o projeto de estudo. Para detalhes mais aprofundados, consulte a documentação oficial do Django sobre customização de autenticação e modelos de usuário.

```
