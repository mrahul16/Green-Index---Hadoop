# Green Index

Calculation of Green Index of a satellite image of a geographical area using Hadoop Map-Reduce

- Store RGB values of all pixels of the satellite image of an area in a file
- Upload it to HDFS
- Mapper calculates percentage of pixels that are a shade or tint of green
- Reducer finds average of values from mapper
- This average is the Green Index
