from dependency_injector import containers, providers


class Company:
    def __init__(self, name: str, city: str, enterprise: str) -> None:
        self.name = name
        self.city = city
        self.enterprise = enterprise

    def getNameCompany(self):
        print(f"The company name is {self.name}")

    def getCityCompany(self):
        print(f"The company is located in {self.city} city")

    def getEnterpriCompany(self):
        print(f"Enterprises belong to the form of business {self.enterprise}")


class Employee:
    def __init__(self, name: str, age: int, company: Company) -> None:
        self.name = name
        self.age = age
        self.company = company

    def getEmployee(self):
        employee = f"""
                Employee name: {self.name}
                Employee age: {self.age}
                Employee company: {self.company.name}
                City: {self.company.city}
                Enterprises: {self.company.enterprise}
        """
        print(employee)


class Container(containers.DeclarativeContainer):

    company = providers.Singleton(
        Company,
        "TMA Solution",
        "Quy Nhon City",
        "Private enterprise"
    )

    employee = providers.Factory(
        Employee,
        "Minh Long",
        22, company
    )

def main():
    employee = Container.employee()
    employee.getEmployee()
    employee.company.getNameCompany()
    employee.company.getCityCompany()
    
if __name__ == "__main__":
    main()