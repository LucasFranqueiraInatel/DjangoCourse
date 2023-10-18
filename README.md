# Comandos Utilizados

- Instalar os pacotes:

  `pip install -r requirements.txt`


- Criar um projeto do [Django](https://docs.djangoproject.com/en/4.2/intro/tutorial01/):

  `django-admin startproject proj .`


- Executando o servidor:

  `python manage.py runserver`


- Configurar o runserver para rodar/debug direto pelo Pycharm.


- Criar um novo app:

  `django-admin startapp cadastros`


- Criar as migrações e Executar as alterações no BD:

  `python manage.py makemigrations`

  `python manage.py migrate`


- Criar um superUsuário:

  `python manage.py createsuperuser`


- Rodar o Docker

  `docker-compose -f .\docker-compose.dev.yml build`
  `docker-compose -f .\docker-compose.dev.yml up`

# Opcional

- Baixar o ipython

  `pip install ipython`

# Referencias

- [Django Shotcuts](https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/)
- [ccbv.co.uk](https://ccbv.co.uk/)