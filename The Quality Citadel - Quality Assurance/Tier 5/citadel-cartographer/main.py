import xml.etree.ElementTree as ET
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


def parse_robot_output(xml_file_path):
    """
    Parses a Robot Framework output.xml file and extracts test case data.
    """
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    test_data = []

    for test in root.findall('.//test'):
        name = test.get('name')
        status = test.find('status').get('status')
        tags = [tag.text for tag in test.findall('tags/tag')]

        test_data.append({
            "Test Name": name,
            "Status": status,
            "Tags": ", ".join(tags) if tags else "N/A"
        })

    # --- Start of new code ---
    # Sort the list of dictionaries by the "Test Name"
    test_data.sort(key=lambda x: x['Test Name'])
    # --- End of new code ---

    return pd.DataFrame(test_data)


@app.route('/')
def dashboard():
    """
    This function runs when a user visits the main page of our web app.
    """
    output_file = "data/output.xml"
    df = parse_robot_output(output_file)
    test_results = df.to_dict(orient='records')
    return render_template('index.html', tests=test_results)


if __name__ == "__main__":
    app.run(debug=True)