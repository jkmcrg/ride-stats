# GPX Statistics Analyzer

A Python script that analyzes GPX files and provides useful statistics about your route, including distance and elevation metrics.

## Features

- Calculates total distance
- Measures elevation gain and loss
- Tracks distance spent climbing and descending

## Requirements

- Python 3.x
- gpxpy library

## Installation

1. Clone this repository or download the files
2. Install the required dependency:
```bash
pip install -r requirements.txt
```

## Usage

Run the script from the command line, providing the path to your GPX file:

```bash
python gpx_stats.py path/to/your/route.gpx
```

## Example Output

For a longer route:
```
Total Distance: 5.23 mi
Elevation Gain: 1,234 ft
Elevation Loss: 1,200 ft
Distance Climbing: 2.15 mi
Distance Descending: 3.08 mi
```

For a shorter route:
```
Total Distance: 4,500 ft
Elevation Gain: 123 ft
Elevation Loss: 120 ft
Distance Climbing: 2,000 ft
Distance Descending: 2,500 ft
```

## Notes

- The script uses the Haversine formula to calculate distances between GPS coordinates, accounting for the Earth's curvature
- Elevation changes are calculated between consecutive points in the GPX file

## Error Handling

The script will display an error message if:
- The GPX file cannot be found
- The GPX file is invalid or corrupted
- The script is run without providing a file path
