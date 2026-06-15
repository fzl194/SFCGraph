# -*- coding: utf-8 -*-
"""Business graph API routes."""
from fastapi import APIRouter, Query
from dataclasses import asdict
from .service import get_service, LAYER_FILES

router = APIRouter(prefix="/api/v1/business-graph", tags=["business-graph"])


@router.get("/domains")
def list_domains():
    """List all business domains with their scenarios (for top-level cards)."""
    svc = get_service()
    domains = svc.list_domains()
    result = []
    for d in domains:
        result.append({
            "domain_id": d.domain_id,
            "domain_name": d.domain_name,
            "summary": d.summary,
            "scenario_count": len(d.scenarios),
            "scenarios": [
                {
                    "scenario_id": s.scenario_id,
                    "scenario_name": s.scenario_name,
                    "dir_path": s.dir_path,
                    "summary": s.summary,
                    "object_counts": s.object_counts,
                }
                for s in d.scenarios
            ],
        })
    return {"domains": result}


@router.get("/domains/{domain_name}")
def get_domain(domain_name: str):
    """Get one domain by name."""
    svc = get_service()
    d = svc.get_domain(domain_name)
    if not d:
        return {"error": "Domain not found", "domain_name": domain_name}
    return {
        "domain_id": d.domain_id,
        "domain_name": d.domain_name,
        "summary": d.summary,
        "scenarios": [
            {
                "scenario_id": s.scenario_id,
                "scenario_name": s.scenario_name,
                "dir_path": s.dir_path,
                "summary": s.summary,
                "object_counts": s.object_counts,
            }
            for s in d.scenarios
        ],
    }


@router.get("/scenarios/{scenario_id}")
def get_scenario(scenario_id: str):
    """Get scenario metadata + layer index."""
    svc = get_service()
    scen = svc.get_scenario(scenario_id)
    if not scen:
        return {"error": "Scenario not found", "scenario_id": scenario_id}
    layers = [
        {"layer_id": lid, "layer_name": lname, "file_name": fname}
        for lid, fname, lname in LAYER_FILES
    ]
    return {
        "scenario_id": scen.scenario_id,
        "scenario_name": scen.scenario_name,
        "domain_id": scen.domain_id,
        "domain_name": scen.domain_name,
        "dir_path": scen.dir_path,
        "summary": scen.summary,
        "object_counts": scen.object_counts,
        "layers": layers,
    }


@router.get("/scenarios/{scenario_id}/layers")
def list_layers(scenario_id: str):
    """Get all layers with parsed sections and tables."""
    svc = get_service()
    scen = svc.get_scenario(scenario_id)
    if not scen:
        return {"error": "Scenario not found", "scenario_id": scenario_id}
    layers = svc.list_layers(scenario_id)
    return {
        "scenario_id": scenario_id,
        "scenario_name": scen.scenario_name,
        "layers": [_layer_to_dict(l) for l in layers],
    }


@router.get("/scenarios/{scenario_id}/layers/{layer_id}")
def get_layer(scenario_id: str, layer_id: str):
    """Get one layer detail."""
    svc = get_service()
    layer = svc.get_layer(scenario_id, layer_id)
    if not layer:
        return {"error": "Layer not found", "scenario_id": scenario_id, "layer_id": layer_id}
    return _layer_to_dict(layer)


@router.get("/scenarios/{scenario_id}/layers/{layer_id}/raw")
def get_raw_md(scenario_id: str, layer_id: str):
    """Get raw MD content for a layer (for DocViewer fallback)."""
    svc = get_service()
    raw = svc.get_raw_md(scenario_id, layer_id)
    return {"content": raw, "scenario_id": scenario_id, "layer_id": layer_id}


@router.get("/scenarios/{scenario_id}/graph")
def get_scenario_graph(scenario_id: str):
    """Get complete graph (objects + edges) for a scenario."""
    svc = get_service()
    graph = svc.get_graph(scenario_id)
    if not graph:
        return {"error": "Scenario not found", "scenario_id": scenario_id}
    return graph.to_dict()


def _layer_to_dict(layer) -> dict:
    """Convert LayerDoc dataclass to JSON-serializable dict."""
    return {
        "layer_id": layer.layer_id,
        "layer_name": layer.layer_name,
        "file_name": layer.file_name,
        "title": layer.title,
        "sections": [
            {
                "level": s.level,
                "title": s.title,
                "tables": [
                    {
                        "headers": t.headers,
                        "rows": t.rows,
                        "title": t.title,
                    }
                    for t in s.tables
                ],
                "paragraphs": s.paragraphs[:3],  # truncate long paragraphs
            }
            for s in layer.sections
        ],
        "section_count": len(layer.sections),
    }
