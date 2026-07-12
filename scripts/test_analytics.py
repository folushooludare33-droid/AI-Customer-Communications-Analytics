from app.analytics.email_analytics import EmailAnalytics
from app.database.session import SessionLocal
from app.models.customer_email import CustomerEmail


def main() -> None:
    with SessionLocal() as session:
        emails = session.query(CustomerEmail).all()

    print(f"Total Emails: {EmailAnalytics.total_emails(emails)}")
    print()

    print("Category")
    print(EmailAnalytics.count_by_category(emails))
    print()

    print("Department")
    print(EmailAnalytics.count_by_department(emails))
    print()

    print("Priority")
    print(EmailAnalytics.count_by_priority(emails))
    print()

    print("Sentiment")
    print(EmailAnalytics.count_by_sentiment(emails))
    print()

    print(f"Open: {EmailAnalytics.open_emails(emails)}")
    print(f"Closed: {EmailAnalytics.closed_emails(emails)}")


if __name__ == "__main__":
    main()