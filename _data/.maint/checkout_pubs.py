from pathlib import Path
import yaml
from collections import defaultdict


def format_citation(pub):
    """
    Format the citation entry from the private pub_journal.yml format
    into the required format for the public repository.
    """
    citation = pub.get("Citation (APA)", "")
    doi = pub.get("DOI", "")
    oa = pub.get("OA URL", "")

    formatted = citation.strip()
    if doi:
        formatted += f" doi:<a href='https://doi.org/{doi}'>{doi}</a>."
    if oa:
        formatted += f" (<a href='{oa}'>OA</a>)"
    return formatted


def transform_pub_journal(input_file, output_file):
    """
    Transform the pub_journal.yml into the target format.
    """
    with open(input_file, "r", encoding="utf-8") as f:
        publications = yaml.safe_load(f)

    # Organize by Year
    grouped_by_year = defaultdict(list)

    for pub in publications:
        year = pub.get("Year", "Before 2023")
        if isinstance(year, int) and year < 2023:
            year = "Before 2023"

        formatted_pub = {
            "Citations": pub.get("Citations", ""),
            "DOI": pub.get("DOI", ""),
            "OA": pub.get("OA URL", ""),
            "Year": pub.get("Year", ""),
            "Citation": format_citation(pub),
        }
        grouped_by_year[year].append(formatted_pub)

    # Convert to the required structure
    output_data = [
        {"Year": year, "Items": items}
        for year, items in sorted(grouped_by_year.items(), reverse=True)
    ]

    # Write the transformed YAML
    with open(output_file, "w", encoding="utf-8") as f:
        yaml.dump(output_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    print(f"Transformed data saved to {output_file}")


if __name__ == "__main__":
    input_file = Path("pub_journal.yml")
    output_file = Path("_data/pub_journal.yml")
    transform_pub_journal(input_file, output_file)
