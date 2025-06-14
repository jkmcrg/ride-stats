#!/usr/bin/env python3

import sys
import gpxpy
import gpxpy.gpx
from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate the great circle distance between two points on the earth."""
    R = 6371  # Earth's radius in kilometers

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c

    return distance * 1000  # Convert to meters

def format_distance(meters):
    """Format distance in feet if less than a mile, otherwise in miles."""
    feet = meters * 3.28084  # Convert meters to feet
    miles = feet / 5280  # Convert feet to miles
    
    if miles < 1:
        return f"{feet:.0f} ft"
    else:
        return f"{miles:.2f} mi"

def format_elevation(meters):
    """Format elevation in feet."""
    feet = meters * 3.28084  # Convert meters to feet
    return f"{feet:.0f} ft"

def analyze_gpx(gpx_file_path):
    try:
        with open(gpx_file_path, 'r') as gpx_file:
            gpx = gpxpy.parse(gpx_file)
    except Exception as e:
        print(f"Error reading GPX file: {e}")
        sys.exit(1)

    total_distance = 0
    elevation_gain = 0
    elevation_loss = 0
    climbing_distance = 0
    descending_distance = 0

    for track in gpx.tracks:
        for segment in track.segments:
            prev_point = None
            for point in segment.points:
                if prev_point:
                    # Calculate distance between points
                    distance = haversine_distance(
                        prev_point.latitude, prev_point.longitude,
                        point.latitude, point.longitude
                    )
                    total_distance += distance

                    # Calculate elevation changes
                    elevation_diff = point.elevation - prev_point.elevation
                    if elevation_diff > 0:
                        elevation_gain += elevation_diff
                        climbing_distance += distance
                    elif elevation_diff < 0:
                        elevation_loss += abs(elevation_diff)
                        descending_distance += distance

                prev_point = point

    # Print statistics
    print(f"Total Distance: {format_distance(total_distance)}")
    print(f"Elevation Gain: {format_elevation(elevation_gain)}")
    print(f"Elevation Loss: {format_elevation(elevation_loss)}")
    print(f"Distance Climbing: {format_distance(climbing_distance)}")
    print(f"Distance Descending: {format_distance(descending_distance)}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python gpx_stats.py <path_to_gpx_file>")
        sys.exit(1)

    gpx_file_path = sys.argv[1]
    analyze_gpx(gpx_file_path)

if __name__ == "__main__":
    main() 
