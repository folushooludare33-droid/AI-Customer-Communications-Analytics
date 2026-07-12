from app.database.session import SessionLocal
from app.exporters.csv_exporter import CSVExporter


def main() -> None:
    exporter = CSVExporter()

    with SessionLocal() as session:
        path = exporter.export(session)

    print(f"CSV exported successfully to:\n{path}")


if __name__ == "__main__":
    main()