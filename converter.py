import re

def dms_to_decimal(dms):
    """Convert DMS (Degrees, Minutes, Seconds) to Decimal Degrees."""
    # Match DMS patterns like 'N48°22'00.00"' or 'W123°55'00.00"'
    dms_pattern = re.match(r"([NSEW])(\d+)°(\d+)'(\d+\.\d+)\"", dms)
    
    if dms_pattern:
        direction = dms_pattern.group(1)
        degrees = int(dms_pattern.group(2))
        minutes = int(dms_pattern.group(3))
        seconds = float(dms_pattern.group(4))
        
        # Convert DMS to Decimal Degrees
        decimal_degrees = degrees + minutes / 60 + seconds / 3600
        
        # If it's South or West, make the Decimal Degrees negative
        if direction in ['S', 'W']:
            decimal_degrees *= -1
        
        return decimal_degrees
    else:
        raise ValueError(f"Invalid DMS format: {dms}")

def process_file(input_file, output_file):
    """Read DMS coordinates from a file, convert to Decimal Degrees, and save results."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if line:
                # Attempt to extract lat/long
                parts = re.split(r'\s+', line, maxsplit=2)
                if len(parts) >= 2:
                    lat_dms, lon_dms = parts[0], parts[1]
                    try:
                        lat_decimal = dms_to_decimal(lat_dms)
                        lon_decimal = dms_to_decimal(lon_dms)
                        # If valid coordinates are found, format the output
                        outfile.write(f"{lat_decimal:.6f},{lon_decimal:.6f}{' ' * 5}{line}\n")
                    except ValueError:
                        # If there are no valid coordinates, keep the line and align it
                        outfile.write(f"{' ' * 26}{line}\n")
                else:
                    # For lines without lat/long (e.g., "25 miles"), keep the line and align it
                    outfile.write(f"{' ' * 26}{line}\n")

if __name__ == "__main__":
    input_file = "airspace_data.txt"  # Replace with your input file
    output_file = "converted_data.txt"  # Replace with your output file
    process_file(input_file, output_file)
