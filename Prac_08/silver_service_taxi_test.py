from silver_service_taxi import SilverServiceTaxi


def main():
    tesla = SilverServiceTaxi("tesla", 200, 2)
    tesla.drive(18)
    print(tesla)


if __name__ == '__main__':
    main()