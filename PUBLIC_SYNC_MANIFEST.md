# Public Sync Manifest

This file defines what may be copied from the private repository into this public CI mirror.

Allowed paths after review:

```text
WzD/homewerk-service/backend/
WzD/homewerk-service/frontend/
WzD/homewerk-service/tools/
.github/workflows/
README.md
NOTICE.md
.gitignore
```

Blocked paths and file types:

```text
WzD/STAGE_*.md
WzD/H*.md
PDF, ZIP, image, scan, invoice, receipt and customer document files
.env and secret files
real customer data fixtures
workflow artifacts
private handoff reports
```

Sync rule:
- copy only source code and CI checks that can be public;
- do not copy private repository history;
- do not copy internal reports unless they are rewritten as public-safe summaries.
