url = 'bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'
print(url)

indice_interrogação = url.find('?')

url_base = url[:indice_interrogação]
print(url_base)

url_parametros = url[indice_interrogação+1:]
print(url_parametros)

parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
        valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
        
print(valor)
