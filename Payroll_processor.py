'''
   This code reads employee data from a text file, processes it, and displays a formatted report of employees, adding at the end the total payroll amount. The def functions allow to escalate the code in the future.
   Esse código lê os dados dos funcionários de um arquivo de texto, processa-os e exibe um relatório formatado dos funcionários, adicionando ao final o valor total da folha de pagamento. As funções permitem escalar o código no futuro. Utilizando descrições em inglês para treinamento efetivo da linguagem.

   If you want to test the code with a file example, below is the content of the "employees.txt" file:

 João Pedro Cavalcante : Desenvolvimento Back-end : 7.500
 Ana Beatriz Silveira : UX/UI Design : 6.200
 Carlos Eduardo Moreira : Infraestrutura e Redes : 5.850
 Beatriz Farias Mendonça : Ciência de Dados : 9.200
 Marcos Rocha Azevedo : Segurança da Informação : 8.750
 Helena Souza Arantes : Engenharia de Software : 11.000
 Ricardo Gomes Castro : Suporte Técnico L2 : 4.200
 Patrícia Lima Silva : Gestão de Projetos (PM) : 10.600
 Lucas Martins Peixoto : Desenvolvimento Front-end : 6.900
 Fernanda Dias Albuquerque : QA / Quality Assurance : 7.150
 Thiago Neves Ferreira : Cloud Computing : 8.300
 Juliana Paes Guimarães : Marketing Digital : 5.800
 Gabriel Torres Machado : Desenvolvimento Mobile : 7.950
 Sofia Albuquerque Lins : Inteligência Artificial : 12.500
 André Villanova Costa : Analista de Sistemas : 6.100

    Copy and paste the content into a text file in your editor.

'''
def treat_data(file_path):
     # Creating the dictionary.
    employees_data = {}
     # Using encoding = "utf-8" to handle accented characters like 'André' (acute accent).
    try:
        with open (file_path, "r", encoding = "utf-8") as f :
            for line in f:
                line = line.strip()# Strip will remove the break line.
                if ":" in line:
                     # Split is to break the lines into parts.
                    name, department, salary_str = line.split(":")
                     # Converting salary string to float for calculations.
                    salary_value = float(salary_str.replace(".", "").strip())
                     # Adding salary_value to the dictionary.
                    employees_data[name.strip()] = {"dept":department.strip(), "salary": salary_value}
        return employees_data
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")    
        return None # No return value expected for this operation.    


def main():
    # Calling the function.
    data = treat_data("employees.txt")

    if data:
        # Printing the header.
        header = f"{'FUNCIONÁRIO':<30} | {'DEPARTAMENTO':<30} | {'SALÁRIO':<15}"
        print(header)
        print("_"*len(header))
        
        for name, info in data.items():
            print(f"{name.strip():<30} | {info['dept']:<30} | R${info['salary']:>9.2f}")
        
        # Calculating the total payroll.
        total = 0
        for info in data.values():
            total += info['salary']

        print("_"*len(header))
        print(f"{'TOTAL DA FOLHA DE PAGAMENTOS': <60} | R${total:.2f}")

if __name__ == "__main__":# This condition checks if the script is being run directly (as the main program).
     main()
    main()
