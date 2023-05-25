import json
import os
import sys
import simplekml


def JsonToKml(json_file):
    """Convert a json file to KML file"""
    # Create KML file
    output_file = simplekml.Kml()
    # Open Json file input
    with open(json_file) as input_file:
        # Parse file
        coordonnees = json.load(input_file)
        # Run over coordonnees
        for point in coordonnees:
            id = point['id']
            lat = point['lat']
            long = point['lng']
            new_point = output_file.newpoint(name=id, coords=[(long, lat)])
            new_point.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/paddle/blu-circle.png'
    # Save file
    name = os.path.splitext(json_file)[0]
    output_file.save(name + ".kml")



def test():
    # Verify if program works correctly
    for i in range(1, 6):
        JsonToKml(f"traj{i}.json")

def main():
    # Error if there isn't the good number of parameter
    if len(sys.argv) != 2:
        raise Exception("Le script ne doit prendre en paramètre que le fichier json à convertir.")
    # Get name from the command line
    json_file = sys.argv[1]
    # Execute convert json to kml
    JsonToKml(json_file)
    # Display success message
    print(f"{json_file} a été converti avec succès !")

if __name__ == "__main__":
    main()
