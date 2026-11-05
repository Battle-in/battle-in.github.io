def main():
    client = Client('Volodya', 9999)
    print(client)

class Client:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'Клиент [имя: f{self.name}, баланс: f{self.balance}'

if __name__ == '__main__':
    main()