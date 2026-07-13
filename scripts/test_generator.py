from app.demo_data.synthetic_generator import SyntheticEmailGenerator


def main() -> None:
    generator = SyntheticEmailGenerator()

    email = generator.generate_email()

    print(email)


if __name__ == "__main__":
    main()