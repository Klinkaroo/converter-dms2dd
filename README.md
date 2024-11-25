# DMS2DD Converter

DMS2DD Converter is a Python script designed to simplify the process of digitizing airspace descriptions from the Canadian Designated Airspace Handbook (DAH). It converts latitude and longitude positions from Degrees, Minutes, and Seconds (DMS) format to Decimal Degrees (DD) format, making it easier to import the data into GIS applications like QGIS.

## Features
- **Input Format**: Reads airspace descriptions copied directly from the DAH into a plain text file.
- **Conversion**: Converts DMS positions to DD format.
- **Output Format**: Creates a formatted text file with:
  - Decimal Degrees positions placed on the left.
  - The original airspace description indented on the right.
- **Ease of Use**: Designed for quick copy-paste into digitizing tools like QGIS.

## How It Works
1. Copy the airspace description from the **DAH** into a plain text file (e.g., `airspace_data.txt`).
2. Run the script with the text file as input.
3. The script outputs a converted file with the new format, ready for use.
### Example
#### Input File (airspace_data.txt)
```
N49°00'07.92" W122°33'17.10" Can/USA bdry \ to
N49°01'56.09" W122°33'17.10" to
N49°01'56.93" W122°29'12.14" thence clockwise around the arc of a circle of
5 miles                      radius centred on
N49°01'31.00" W122°21'38.00" (Abbotsford, BC - AD) \ to
N49°06'30.75" W122°21'38.00" to
N49°06'30.52" W122°14'10.65" thence clockwise around the arc of a circle of
7 miles                      radius centred on
N49°01'31.00" W122°21'38.00" (Abbotsford, BC - AD) \ to
N49°03'17.00" W122°11'20.90" to
N49°03'17.00" W122°07'24.00" to
N49°00'08.70" W122°07'24.00" Can/USA bdry \ thence westerly along the Can/USA bdry \ to
N49°00'07.92" W122°33'17.10" Can/USA bdry \ point of beginning
```
#### Output File (converted_data.txt)
```
49.002200,-122.554750     N49°00'07.92" W122°33'17.10" Can/USA bdry \ to
49.032247,-122.554750     N49°01'56.09" W122°33'17.10" to
49.032481,-122.486706     N49°01'56.93" W122°29'12.14" thence clockwise around the arc of a circle of
                          5 miles                      radius centred on
49.025278,-122.360556     N49°01'31.00" W122°21'38.00" (Abbotsford, BC - AD) \ to
49.108542,-122.360556     N49°06'30.75" W122°21'38.00" to
49.108478,-122.236292     N49°06'30.52" W122°14'10.65" thence clockwise around the arc of a circle of
                          7 miles                      radius centred on
49.025278,-122.360556     N49°01'31.00" W122°21'38.00" (Abbotsford, BC - AD) \ to
49.054722,-122.189139     N49°03'17.00" W122°11'20.90" to
49.054722,-122.123333     N49°03'17.00" W122°07'24.00" to
49.002417,-122.123333     N49°00'08.70" W122°07'24.00" Can/USA bdry \ thence westerly along the Can/USA bdry \ to
49.002200,-122.554750     N49°00'07.92" W122°33'17.10" Can/USA bdry \ point of beginning
```
The converted file places the Decimal Degrees on the left and indents the original DMS coordinates on the right, ready for direct use in GIS digitizing workflows.

### Prerequisites
- Python 3.6 or newer installed on your system.

### Running the Script
1. Place your input file (e.g., `airspace_data.txt`) in the same directory as the script.
2. Run the script with the following command:
   ```bash
   python3 converter.py
   ```
3. The converted file (`converted_data.txt`) will be created in the same directory.

## Future Plans
One day, I aim to enhance the script to:
- Automatically generate a points file from the airspace description, streamlining the digitization process for GIS tools.
- Automatically generate the points and be capable of handling arcs to draw all lines and create polygons. 

## Contributing
Feel free to contribute improvements or additional features by submitting a pull request. Contributions are welcome to make the script more robust and versatile!

## License
This project is licensed under the GNU Affero General Public License v3.0. See the LICENSE file for details.
