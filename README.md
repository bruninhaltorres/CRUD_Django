# API Django
Desafio Back-End - WeniTech

Esse repositório foi criado no intuito de compartilhar o projeto desenvolvido, por mim, para o processo seletivo da WeniTech.
Foi utilizado Python e Django REST.

### Pré requisitos:
1. Python
2. Pip
3. Django 

### Passo a passo:

1. Faça o download do repositório como preferir. Uma das opções é usando o comando `git clone <link_do_repositorio>`;
2. Vá até a pasta onde se encontra o executavel *manage.py* : `cd CRUD_Django/apiwenimusic`;
3. Baixe a extensão: `pip install djangorestframework`;  
*Fique atento aos erros, o pip pode estar desatualizado!*
4. Execute o comando `python manage.py makemigrations` para criar novas migrações, com base nas alterações feitas em seus modelos;
5. Em seguida o comando `python manage.py migrate` para aplicar alterações criadas pelo comando anterior;
6. Crie um super usuário: `python manage.py createsuperuser`;
7. Agora, coloque a aplicação pra rodar: `python manage.py runserver`;
8. Abra o seu servidor de preferência e busque por <http://localhost:8000/> ou [clique aqui](http://localhost:8000/).

### Especificações:

1. Toda música precisa de um artista;
2. O artista não precisa ter uma música;
3. As playlists não podem ter o mesmo nome e podem ter várias músicas.

### Utilizando o site:

* Sendo sua primeira vez no site, você terá que fazer o login com o super usuário, criado no passo 6, para que tenha acesso as ações do CRUD. Acesse: http://localhost:8000/admin. 
* Em seguida, faça a sua primeira adição.  
*É recomendável que se inicie adicionando um Artista, por causa das especificações já citadas.*
* Artista: Adicionar e Listar: (http://localhost:8000/Artista)  
* Musicas: Adicionar e Listar: (http://localhost:8000/Musicas)  
* Playlist: Adicionar e Listar: (http://localhost:8000/Playlist) 
* Em todos os casos, para fazer Atualização e Deleção, é só adicionar o id na urls do objeto que será usado.  
Ex: localhost:8000/Artista/2  
Vai atualizar ou deletar o Artista com id igual a 2.
