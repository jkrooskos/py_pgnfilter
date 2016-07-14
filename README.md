# py_pgnfilter
Create a new pgn file from a source pgn by a particular starting color.  For example, I want a 
new pgn where only white moves first, etc.

# Install dependencies
`pip install -r requirements.txt`

# Run the tests
`py.test`

# Usage
python pgn_filter.py --color=b --input-pgn=games.pgn --output-pgn=output.pgn
