from app.ai.pipeline import AIPipeline


def main() -> None:
    pipeline = AIPipeline()

    result = pipeline.analyze(
        customer_name="James Wilson",
        subject="Battery drains quickly",
        body=(
            "My NovaPhone X battery is draining very fast "
            "and I would like a replacement."
        ),
    )

    print(result)


if __name__ == "__main__":
    main()