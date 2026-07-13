from app.ai.pipeline import AIPipeline
from app.demo_data.synthetic_generator import SyntheticEmailGenerator


def main() -> None:
    generator = SyntheticEmailGenerator()
    email = generator.generate_email()

    pipeline = AIPipeline()

    analysis = pipeline.analyze(
        customer_name=email.customer_name,
        subject=email.subject,
        body=email.body,
    )

    print(email)
    print()
    print(analysis)


if __name__ == "__main__":
    main()