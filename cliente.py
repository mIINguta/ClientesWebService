from suds.client import Client
url = "http://localhost:2000/ValidaCNPJ?wsdl"  
client = Client(url)
CNPJ = input("Digite o CNPJ: ")
response= client.service.isCNPJ(CNPJ)
print(response)



     
                  
