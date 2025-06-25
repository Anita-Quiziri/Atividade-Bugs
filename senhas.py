senhas = {"Bruno.phyton@gmail.com":"Bruno44", "Brunao.net@gmail.com": "4Bruno4","Bruninho.git@gmail.com": "44Bruno"}

site = input("Digite o nome do site: ")

if site in senhas:
  print(f"A senha para o site {site} é: {senhas[site]}")
else:
  print(f"Senha não encontrada para o site {site}.")
