from app.database.session import SessionLocal
from app.demo_data.dataset_builder import DatasetBuilder
from app.services.email_import_service import EmailImportService


def main() -> None:
    builder = DatasetBuilder()

    dataset = builder.build_dataset(500)

    importer = EmailImportService()

    with SessionLocal() as session:
        importer.import_emails(
            session=session,
            emails=dataset,
        )

    print(f"Imported {len(dataset)} emails successfully.")


if __name__ == "__main__":
    main()