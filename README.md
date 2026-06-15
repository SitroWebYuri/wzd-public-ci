# WzD Public CI

This repository is a public CI mirror for the WzD / HomeWerk Service project.

Purpose:
- run GitHub Actions checks on a public repository;
- keep the private development repository separate;
- publish only cleaned project files that are safe for public CI.

This repository must not contain:
- private customer data;
- real addresses, phone numbers, e-mail messages, scans, PDFs, photos or invoices;
- secrets, tokens, passwords or `.env` files;
- internal stage handoff files from the private repository;
- historical private reports unless explicitly sanitized.

Main private working repository remains: `SitroWebYuri/main`.

Working project path used by CI mirror:

```text
WzD/homewerk-service/
```
