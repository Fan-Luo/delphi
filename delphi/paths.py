import os
from pathlib import Path
import json

data_dir = Path(os.environ["DELPHI_DATA"])

adjectiveData = data_dir / "adjectiveData.tsv"
south_sudan_data = data_dir / "south_sudan_data.csv"
concept_to_indicator_mapping = data_dir / "concept_to_indicator_mapping.txt"
