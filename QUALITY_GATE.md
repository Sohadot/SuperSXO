# SuperSXO — Quality Gate

## Governing Principle

Failure in quality validation **must block publication**.

No page may be published without passing all applicable gates.

---

## Quality Gate Checklist

### 1. Route Gate

- [ ] Path is registered in `ROUTE_GOVERNANCE.md`
- [ ] Purpose is documented
- [ ] Status is `approved` (not `draft` or `planned`)
- [ ] Canonical URL is defined
- [ ] Page role is declared

### 2. SEO Metadata Gate

- [ ] `<title>` is present and controlled
- [ ] `<meta name="description">` is present and controlled
- [ ] One `<h1>` is present and singular
- [ ] Heading hierarchy is logical (H1 → H2 → H3)
- [ ] Canonical URL is set
- [ ] Indexability is explicitly declared

### 3. Content Quality Gate

- [ ] No placeholder text
- [ ] No filler paragraphs
- [ ] No unsupported claims
- [ ] No blocked claim types (see `CLAIM_POLICY.md`)
- [ ] Content meets minimum depth standard
- [ ] Claim classification is documented

### 4. Link Gate

- [ ] All internal links are valid (no 404s)
- [ ] No dead outbound links
- [ ] No orphaned pages (every page has at least one internal link pointing to it)
- [ ] Required internal links from route definition are present

### 5. Technical Gate

- [ ] Page passes HTML validator
- [ ] Page is accessible without JavaScript
- [ ] No `eval` usage
- [ ] No unescaped user input rendering
- [ ] No exposed credentials
- [ ] Security headers are configured (pre-deployment)

### 6. Performance Gate

- [ ] Page meets performance budget
- [ ] Images are optimized
- [ ] No render-blocking scripts without `defer` or `async`
- [ ] No unnecessary third-party scripts

### 7. Accessibility Gate

- [ ] Images have meaningful `alt` text
- [ ] Color contrast meets WCAG AA minimum
- [ ] Interactive elements are keyboard-navigable
- [ ] No content that requires motion or 3D to understand

### 8. Monetization Gate

- [ ] No unapproved monetization elements
- [ ] No random display ads
- [ ] No popups that damage asset dignity
- [ ] Any monetization element is approved in `MONETIZATION_BOUNDARY.md`

### 9. Security Gate

- [ ] No secrets in code
- [ ] No tracking scripts without approval
- [ ] No third-party scripts without review
- [ ] CSP header is planned or active

---

## Domain-Level Quality Requirements

The following must also be validated before any domain is considered live:

- sitemap integrity
- robots.txt accuracy
- canonical URL consistency across all pages
- structured data validity
- no duplicate title or description across routes

---

## Quality Gate Enforcement

The quality gate must be enforced:

- before any page is published
- before any route is added to the sitemap
- before any pull request is merged to main

Documentation of gate passage is required in `DECISION_LOG.md` for all significant releases.

---

## Quality Failure Handling

When a gate check fails:

1. Publication is blocked
2. The failure is documented in `DECISION_LOG.md`
3. The issue is resolved before re-review
4. No exceptions may be granted without explicit owner approval and a log entry
