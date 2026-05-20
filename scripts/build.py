#!/usr/bin/env python3
"""
SuperSXO static site builder.

Generates static HTML only for routes satisfying all of:
  - status: published in data/routes.json
  - source_status: approved_for_build in matching content/pages/*.json
  - all required_internal_links resolve to published routes

Safety rules enforced at build time:
  - Only registered, published routes are built.
  - Only content with approved_for_build status is rendered.
  - Internal links to unpublished routes abort the build.
  - Navigation is filtered to published routes only.
  - No JavaScript, tracking, external scripts, or monetization injected.
  - Root index.html generated only for route "/".
  - Subdirectory index.html generated for all other routes.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
ROUTES_FILE = REPO_ROOT / "data" / "routes.json"
NAVIGATION_FILE = REPO_ROOT / "data" / "navigation.json"
CONTENT_DIR = REPO_ROOT / "content" / "pages"
TEMPLATES_DIR = REPO_ROOT / "templates"
OUTPUT_DIR = REPO_ROOT / "output"

CTA_DEFINITIONS = {
    "explore_framework": {
        "label": "Explore the SXO Framework",
        "href": "/sxo-framework/",
    },
    "take_score": {
        "label": "Take the SXO Score",
        "href": "/sxo-score/",
    },
    "request_audit": {
        "label": "Request an SXO Audit",
        "href": "/sxo-audit/",
    },
    "contact_acquisition": {
        "label": "Contact for Acquisition",
        "href": "/acquisition/",
    },
}


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def render(template: str, ctx: dict) -> str:
    """Replace {{ key }} placeholders with context values."""
    for key, value in ctx.items():
        template = template.replace(
            f"{{{{ {key} }}}}", str(value) if value is not None else ""
        )
    return template


def load_template(name: str) -> str:
    return (TEMPLATES_DIR / name).read_text(encoding="utf-8")


def load_component(name: str) -> str:
    return (TEMPLATES_DIR / "components" / name).read_text(encoding="utf-8")


def render_nav_items(items: list, published_paths: set) -> str:
    """Render <li><a> list items filtered to published routes only."""
    html = []
    for item in items:
        if item.get("path") in published_paths:
            html.append(
                f'<li><a href="{item["path"]}">{item["label"]}</a></li>'
            )
    return "\n      ".join(html)


def render_cta_block(allowed_cta: list, published_paths: set) -> str:
    """Render CTA anchor tags for route-permitted, published targets only."""
    links = []
    for cta_type in allowed_cta:
        defn = CTA_DEFINITIONS.get(cta_type)
        if defn and defn["href"] in published_paths:
            links.append(
                f'<a class="cta-link cta-{cta_type}" href="{defn["href"]}">'
                f'{defn["label"]}</a>'
            )
    return "\n    ".join(links)


def render_related_links(
    required_links: list, published_paths: set, routes_map: dict
) -> str:
    """Render related link list items for published routes only."""
    items = []
    for path in required_links:
        if path in published_paths:
            title = routes_map.get(path, {}).get("title", path)
            items.append(f'<li><a href="{path}">{title}</a></li>')
    return "\n      ".join(items)


def render_page_body(content: dict) -> str:
    """Render page sections from approved content."""
    sections = []
    for section in content.get("required_sections", []):
        name = section.get("name", "section")
        heading = name.replace("_", " ").title()
        body = section.get("content", "")
        sections.append(
            f'<section class="page-section" data-section="{name}">\n'
            f'    <h2>{heading}</h2>\n'
            f'    <p>{body}</p>\n'
            f'  </section>'
        )
    return "\n  ".join(sections)


def render_route_context(route: dict) -> str:
    tmpl = load_component("route-context.html")
    return render(tmpl, {
        "route_role": route.get("role", ""),
        "ux_layer": route.get("ux_layer", ""),
        "claim_level": route.get("claim_level", ""),
        "monetization_allowed": str(route.get("monetization_allowed", False)).lower(),
        "publication_status": route.get("status", ""),
    })


def render_header(nav_data: dict, published_paths: set) -> str:
    tmpl = load_component("header.html")
    primary_items = render_nav_items(
        nav_data["navigation"]["primary"], published_paths
    )
    cta_parts = []
    for item in nav_data["navigation"].get("commercial_cta", []):
        if item.get("path") in published_paths:
            cta_parts.append(
                f'<a href="{item["path"]}" class="cta-link">{item["label"]}</a>'
            )
    return render(tmpl, {
        "primary_nav_items": primary_items,
        "commercial_cta_items": "\n    ".join(cta_parts),
    })


def render_footer(nav_data: dict, published_paths: set) -> str:
    tmpl = load_component("footer.html")
    footer_items = render_nav_items(
        nav_data["navigation"]["footer"], published_paths
    )
    return render(tmpl, {"footer_nav_items": footer_items})


def render_full_page(
    route: dict,
    content: dict,
    nav_data: dict,
    published_paths: set,
    routes_map: dict,
) -> str:
    """Render a complete HTML page from route, content, and templates."""
    route_context = render_route_context(route)
    header = render_header(nav_data, published_paths)
    footer = render_footer(nav_data, published_paths)

    page_tmpl = load_template("page.html")
    page_html = render(page_tmpl, {
        "route_context": route_context,
        "route_path": route["path"],
        "page_heading": content.get("h1", content.get("title", "")),
        "page_summary": content.get("summary", ""),
        "page_body": render_page_body(content),
        "related_links": render_related_links(
            route.get("required_internal_links", []), published_paths, routes_map
        ),
        "allowed_cta": render_cta_block(
            route.get("allowed_cta", []), published_paths
        ),
    })

    robots = "index, follow" if route.get("indexable", True) else "noindex, nofollow"

    base_tmpl = load_template("base.html")
    return render(base_tmpl, {
        "title": content.get("title", route.get("title", "")),
        "meta_description": content.get("meta_description", ""),
        "canonical": route.get("canonical", ""),
        "robots": robots,
        "body_class": route.get("role", "page"),
        "header": header,
        "content": page_html,
        "footer": footer,
    })


def write_page(route_path: str, html: str) -> Path:
    """Write rendered HTML to output/ with correct file layout."""
    if route_path == "/":
        out_file = OUTPUT_DIR / "index.html"
    else:
        clean = route_path.strip("/")
        out_dir = OUTPUT_DIR / clean
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "index.html"
    out_file.write_text(html, encoding="utf-8")
    return out_file


def load_content_sources() -> dict:
    sources = {}
    if not CONTENT_DIR.is_dir():
        return sources
    for f in CONTENT_DIR.glob("*.json"):
        try:
            data = load_json(f)
            key = data.get("route")
            if key:
                sources[key] = data
        except (json.JSONDecodeError, KeyError):
            pass
    return sources


def main() -> None:
    for required in (ROUTES_FILE, NAVIGATION_FILE):
        if not required.exists():
            print(f"ERROR: {required.relative_to(REPO_ROOT)} not found.")
            sys.exit(1)

    routes_data = load_json(ROUTES_FILE)
    all_routes = (
        routes_data.get("routes", [])
        if isinstance(routes_data, dict)
        else routes_data
    )
    nav_data = load_json(NAVIGATION_FILE)
    content_sources = load_content_sources()

    registered_paths = {r.get("path") for r in all_routes if r.get("path")}
    published_routes = [r for r in all_routes if r.get("status") == "published"]
    published_paths = {r["path"] for r in published_routes}
    routes_map = {r["path"]: r for r in all_routes}

    if not published_routes:
        print("No published routes found. Build skipped safely.")
        return

    # --- Pre-build validation ---
    errors = []
    buildable = []

    for route in published_routes:
        path = route["path"]

        if path not in registered_paths:
            errors.append(
                f"Route '{path}' is published but not registered in routes.json"
            )
            continue

        content = content_sources.get(path)
        if not content:
            errors.append(
                f"Route '{path}': no content source file found in content/pages/"
            )
            continue

        if content.get("source_status") != "approved_for_build":
            errors.append(
                f"Route '{path}': content source_status is "
                f"'{content.get('source_status')}' — must be 'approved_for_build'"
            )
            continue

        link_errors = []
        for link in route.get("required_internal_links", []):
            if link not in published_paths:
                link_errors.append(
                    f"Route '{path}': required internal link '{link}' "
                    f"is not published — cannot build with broken internal links"
                )
        errors.extend(link_errors)

        if not link_errors:
            buildable.append((route, content))

    if errors:
        for err in errors:
            print(f"  BUILD ERROR: {err}")
        sys.exit(1)

    # --- Generate output ---
    print(f"{len(buildable)} route(s) approved for build.")
    OUTPUT_DIR.mkdir(exist_ok=True)

    built = 0
    for route, content in buildable:
        html = render_full_page(route, content, nav_data, published_paths, routes_map)
        out_file = write_page(route["path"], html)
        print(f"  BUILT: {route['path']} → {out_file.relative_to(REPO_ROOT)}")
        built += 1

    print(f"Build complete. {built} page(s) generated in output/")


if __name__ == "__main__":
    main()
