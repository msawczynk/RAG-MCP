from unstructured.partition.html import partition_html

def parse_html_content(html_content):
    elements = partition_html(text=html_content)
    # Process elements into chunks or documents
    documents = []
    for element in elements:
        if element.category in ['HTMLTitle', 'HTMLNarrativeText']:
            documents.append(element.text)
    return documents 