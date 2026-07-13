from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Settings:
    """Application configuration."""

    app_name: str = "AI Customer Communications Analytics Platform"
    company_name: str = "NovaTech Electronics"

    # Modes
    demo_mode: bool = True

    # Directories
    data_dir: Path = PROJECT_ROOT / "data"
    database_dir: Path = data_dir / "database"
    exports_dir: Path = data_dir / "exports"
    logs_dir: Path = data_dir / "logs"
    sample_data_dir: Path = data_dir / "sample_data"

    # Database
    database_name: str = "customer_communications.db"

    @property
    def database_path(self) -> Path:
        return self.database_dir / self.database_name


settings = Settings()