# Architecture

## Overview

The application follows a layered architecture.

``` text
Demo Data Generator
        │
        ▼
AI Pipeline
        │
        ▼
Services
        │
        ▼
SQLAlchemy ORM
        │
        ▼
SQLite
        │
        ▼
CSV Export
        │
        ▼
Power BI
```

## Layers

-   Demo Data: Synthetic email generation
-   AI: Classification, routing, sentiment, summary, reply generation
-   Services: Import and mapping
-   Database: SQLAlchemy ORM
-   Analytics: Business metrics
-   Export: CSV
-   Visualization: Power BI

## Design Principles

-   Clean Architecture
-   SOLID
-   Separation of Concerns
-   Dependency Injection where appropriate
