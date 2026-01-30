import sys
import math

"""
Game Coordinate System Module.
This script parses 3D coordinates from command-line strings, calculates 
their Euclidean distance from the origin (0,0,0), and demonstrates 
tuple unpacking for coordinate management.
"""

def main():
    """
    Main execution logic for coordinate processing.
    It splits input strings, validates integer conversion, calculates 
    3D distances, and performs tuple unpacking for the first valid position.
    """
    print("=== Game Coordinate System ===")

    if len(sys.argv) <= 1:
        print(
            "No coordinates provided. Usage: python3 ft_coordinate_system.py "
            "<x1,y1,z1> <x2,y2,z2> ..."
        )
        return

    first_valid = None

    for coord_str in sys.argv[1:]:
        print(f'Parsing coordinates: "{coord_str}"')
        try:
            parts = coord_str.split(",")
            x = int(parts[0])
            y = int(parts[1])
            z = int(parts[2])
            pos = tuple((x, y, z))
            print(f"Parsed position: {pos}")
            
            dist = math.sqrt(x**2 + y**2 + z**2)
            print(f"Distance between (0, 0, 0) and {pos}: {round(dist, 2)}")
            
            if first_valid is None:
                first_valid = pos
        except Exception as e:
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("Unpacking demonstration:")
    if first_valid is not None:
        px, py, pz = first_valid
        print(f"Player at x={px}, y={py}, z={pz}")
        print(f"Coordinates: X={px}, Y={py}, Z={pz}")

if __name__ == "__main__":
    main()
