from app.demo_data.dataset_builder import DatasetBuilder


def main() -> None:
    builder = DatasetBuilder()

    dataset = builder.build_dataset(5)

    print(f"Generated {len(dataset)} emails.\n")

    for index, email in enumerate(dataset, start=1):
        print(f"Email {index}")
        print(email)
        print("-" * 80)


if __name__ == "__main__":
    main()