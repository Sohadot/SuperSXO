# SuperSXO — Deployment Policy

## Purpose

This document governs how SuperSXO.com is deployed. It exists to prevent unsafe deployment paths, manual overrides, and unauthorized publication of unpublished routes.

---

## Deployment Method

- Deployment uses **GitHub Actions** exclusively.
- The deployment workflow is `.github/workflows/deploy-pages.yml`.
- No manual deployment from the local filesystem is permitted for production.

---

## Deployable Artifact

- `output/` is the **only** deployable artifact.
- No deployment from the repository root.
- No deployment from `docs/`.
- No manual editing of `output/` for production.
- The `output/` directory is generated exclusively by `scripts/build.py`.

---

## Route Publication Requirements

- Public routes must be listed in `data/routes.json` with `status: published`.
- Content sources must have `source_status: approved_for_build`.
- Routes not meeting both conditions are excluded from the build output.

---

## Quality Gate

- The sovereign quality gate (`scripts/quality_gate.py`) must pass **before** the build.
- The sovereign quality gate must pass **after** the build.
- Deployment is blocked if either gate fails.

---

## Workflow Permissions

- The deployment workflow uses **least-privilege permissions**:
  - `contents: read`
  - `pages: write`
  - `id-token: write`
- No additional permissions are granted to the deployment workflow.

---

## Cloudflare Policy

- No Cloudflare API token is used in the publishing workflow.
- Cloudflare may be used later **only** for DNS, TLS, security, and edge controls after nameserver delegation.
- Cloudflare is not a deployment target; it is an edge and security layer.

---

## Prohibited Actions

- No deployment from the repository root.
- No deployment from `docs/`.
- No manual editing of `output/` for production.
- No Cloudflare API token in the publishing workflow.
- No unsafe scripts, JavaScript, analytics, tracking, forms, payment links, affiliate links, or heavy 3D in any deployed artifact.
- No routes may be deployed without passing the sovereign quality gate.
