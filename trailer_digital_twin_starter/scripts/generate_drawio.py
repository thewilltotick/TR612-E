
import xml.etree.ElementTree as ET
import yaml, pathlib, html

root = pathlib.Path(__file__).resolve().parents[1]
graph = yaml.safe_load((root / "data_model" / "system_graph.yaml").read_text())

styles = {
    "battery": "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;",
    "fuse": "rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;",
    "disconnect_switch": "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;",
    "busbar": "rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;",
    "shunt": "rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;",
    "inverter_charger": "rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;",
    "solar_array": "rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d79b00;",
    "breaker": "rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;",
    "surge_protection": "rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;",
    "ac_source": "rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;",
    "ac_distribution_panel": "rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;",
    "ac_branch": "rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;",
    "dc_dc_converter": "rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;",
    "ups": "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;",
    "compute": "rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;",
    "relay_board": "rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;",
    "network_switch": "rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;",
    "network_load": "rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;",
    "camera": "rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;",
    "sensor": "rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;",
    "telemetry_interface": "rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;",
}
edge_styles = {
    "power_pos": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#cc0000;endArrow=none;",
    "power_neg": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#000000;dashed=1;endArrow=none;",
    "ac_line": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#0066cc;endArrow=none;",
    "data_power": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#6a00ff;endArrow=none;",
    "telemetry": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1;strokeColor=#666666;dashed=1;endArrow=blockThin;",
}
band_style = "rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#cccccc;dashed=1;"

mxfile = ET.Element("mxfile", host="app.diagrams.net", modified="2026-04-18T00:00:00Z", agent="OpenAI", version="24.7.17")
diagram = ET.SubElement(mxfile, "diagram", id="overview", name="Overview")
model = ET.SubElement(diagram, "mxGraphModel", dx="1600", dy="1000", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="1800", pageHeight="1200", math="0", shadow="0")
root_el = ET.SubElement(model, "root")
ET.SubElement(root_el, "mxCell", id="0")
ET.SubElement(root_el, "mxCell", id="1", parent="0")

next_id = 2
def add_vertex(cell_id, value, style, x, y, w=140, h=44, parent="1"):
    cell = ET.SubElement(root_el, "mxCell", id=str(cell_id), value=value, style=style, vertex="1", parent=parent)
    ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h), as_="geometry")
    return cell

def add_edge(cell_id, value, style, source, target, parent="1"):
    cell = ET.SubElement(root_el, "mxCell", id=str(cell_id), value=value, style=style, edge="1", parent=parent, source=str(source), target=str(target))
    ET.SubElement(cell, "mxGeometry", relative="1", as_="geometry")
    return cell

comp_to_cell = {}

for band in graph.get("diagram_layout", {}).get("bands", []):
    cid = next_id; next_id += 1
    add_vertex(cid, html.escape(band["label"]), band_style, band["x"], band["y"], band["w"], band["h"])
for comp in graph["components"]:
    cid = next_id; next_id += 1
    comp_to_cell[comp["id"]] = cid
    x, y = graph["diagram_layout"]["positions"][comp["id"]]
    label = html.escape(comp["label"]) + "<br><font style=\"font-size:10px;\">" + html.escape(comp["id"]) + "</font>"
    add_vertex(cid, label, styles.get(comp["type"], styles["sensor"]), x, y)

for link in graph["links"]:
    cid = next_id; next_id += 1
    value = html.escape(link["kind"])
    add_edge(cid, value, edge_styles[link["kind"]], comp_to_cell[link["from"]], comp_to_cell[link["to"]])

out_path = root / "diagrams" / "01_overview.drawio"
ET.ElementTree(mxfile).write(out_path, encoding="utf-8", xml_declaration=True)
print(f"Wrote {out_path}")
