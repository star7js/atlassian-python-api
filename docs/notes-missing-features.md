# Missing Features / Gaps Notes

Date: 2026-02-07
Scope: Local code inspection + upstream open issues snapshot (GitHub).

## Local Code Inspection Gaps (Actionable)
- Assets/Insight Cloud parity gaps: many methods raise `NotImplementedError` in cloud mode (attachments, comments, reindex, progress, schema CRUD, object type CRUD, config statustype CRUD). Files: `atlassian/assets.py`, `atlassian/insight.py`.
- Assets/Insight Object Schema CRUD stubs: `create_object_schema`, `update_object_schema`, `delete_object_schema`, `get_object_schema_attributes`. Files: `atlassian/assets.py`, `atlassian/insight.py`.
- Xray attachments unsupported: test step create/update explicitly notes attachments not supported. File: `atlassian/xray.py`.
- Bitbucket Server permissions: several permission operations raise `NotImplementedError`. Files: `atlassian/bitbucket/server/globalPermissions.py`, `atlassian/bitbucket/server/common/permissions.py`.

## Upstream Open Issues Snapshot (GitHub)
From https://github.com/atlassian-api/atlassian-python-api/issues

- #1613 "List page tree / hierarchy for a Confluence space" (opened 2026-01-25)
- #1610 "jira reindex foreground and reindex_status functions fail" (opened 2026-01-14)
- #1607 "examples/bitbucket/bitbucket_cloud_oo.py 401 error" (opened 2025-12-17)
- #1601 "HTTP 401 on download_attachments_from_page() but not get_attachments_from_content()" (opened 2025-11-26)
- #1599 "atlassian.confluence: Several functions not working as documented" (opened 2025-11-13)
- #1598 "Confluence bug: get_all_pages_from_space only loads first page" (opened 2025-11-10)
- #1597 "Statuspage component-groups URL is wrong" (opened 2025-10-31)
- #1596 "add_comment_to_object fails using params kwarg" (opened 2025-10-28)
- #1593 "atlassian-python-api \"Retry-After\" header too large" (opened 2025-10-08)
- #1590 "confluence.download_attachments_from_page only fetches 50 files" (opened 2025-09-25)
- #1589 "Datetime issues" (opened 2025-09-19)
- #1588 "Confluence New Implementation is documented, but not available in a release" (opened 2025-09-16)
