## Working with vector data
Our customer sent us their network data. Itʼs not in the best shape: the poles donʼt
line up with spans (a span is a segment of line between two poles), there are some
extra poles present in the dataset, some properties are missing values.
We need to turn this data into a dataset that is suitable for ingestion into systems. Specifically, we need two geojson files with the following
properties:

- **spans.geojson**
- **poles.geojson**
  
Required property Description

- circuitID identifier of the circuit the span belongs to
- spanID unique span identifier
- phasingType phasing type of the span: single-phase ,
- two-phase , three-phase
- pointA poleID of the first pole of the span
- pointB poleID of the second pole of the span

Write code to process the input data into the format defined above. You will need
to:
-  match each span to its corresponding poles geographically. This is necessary
to populate the properties pointA and pointB .
-  match data properties from the input files to the properties required by the system
-  make sure all the properties are populated.
  
Where the data is missing in the input data source (e.g. pole height is null), use
the value of the corresponding field from the pole or span geographically nearest.
Write python code that would work on any dataset of this shape. Feel free to use
any open-source libraries and packages. If you modify some values manually,
explain why it couldnʼt be automated in a script or workflow.
Your submission should be a zipped folder containing all the required code and
infrastructure to run your code, along with the two produced datasets
( spans.geojson and poles.geojson ). You should provide sufficient set-up
instructions or scripts for us to run your code (e.g. a Makefile or a Dockerfile). If
we canʼt run your code after five or so minutes of trying we will have to send it
back.

Required property Description
- poleID unique pole identifier
- heightInFt height of the pole in feet