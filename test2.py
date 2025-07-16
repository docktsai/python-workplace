mapping_project_id = {
    ("BMO","AWS","PROD"): "project_aws_prod",
    ("BMO","AWS","NON-PRD"): "project_aws_non-prod",


}
key = ("Clearpool","AWS")
key = ("BMO","AWS","NON-PRD")
x = mapping_project_id[key] if key in mapping_project_id else "condition not define!"
print(f"{x=}")