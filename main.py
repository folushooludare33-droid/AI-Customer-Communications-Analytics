"""
AI Customer Communications Analytics Platform

Application entry point.
"""

from app.database.session import SessionLocal
from app.demo_data.dataset_builder import DatasetBuilder
from app.exporters.csv_exporter import CSVExporter
from app.services.email_import_service import EmailImportService
from app.database.initialize_database import initialize_database

def main() -> None:
    initialize_database()

    print("Generating synthetic dataset...")

    builder = DatasetBuilder()
    dataset = builder.build_dataset(500)

    print(f"Generated {len(dataset)} emails.")

    with SessionLocal() as session:
        print("Importing into database...")

        importer = EmailImportService()
        importer.import_emails(
            session=session,
            emails=dataset,
        )

        print("Exporting CSV...")

        exporter = CSVExporter()
        output_path = exporter.export(session)

    print()
    print("Pipeline completed successfully.")
    print(f"CSV exported to: {output_path}")


if __name__ == "__main__":
    main()