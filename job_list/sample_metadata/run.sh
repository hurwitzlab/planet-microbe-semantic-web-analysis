#!/bin/bash

#split
# sed -n '1,100p' input/input_full.csv > input/1.csv
# sed -n '101,200p' input/input_full.csv > input/2.csv
# sed -n '201,300p' input/input_full.csv > input/3.csv
# sed -n '301,400p' input/input_full.csv > input/4.csv
# sed -n '401,500p' input/input_full.csv > input/5.csv
# sed -n '501,600p' input/input_full.csv > input/6.csv
# sed -n '601,700p' input/input_full.csv > input/7.csv
# sed -n '701,800p' input/input_full.csv > input/8.csv
# sed -n '801,900p' input/input_full.csv > input/9.csv
# sed -n '901,1000p' input/input_full.csv > input/10.csv
# sed -n '1001,1100p' input/input_full.csv > input/11.csv
# sed -n '1101,1200p' input/input_full.csv > input/12.csv
# sed -n '1201,1300p' input/input_full.csv > input/13.csv
# sed -n '1301,1400p' input/input_full.csv > input/14.csv
# sed -n '1401,1500p' input/input_full.csv > input/15.csv
# sed -n '1501,1600p' input/input_full.csv > input/16.csv
# sed -n '1601,1700p' input/input_full.csv > input/17.csv
# sed -n '1701,1800p' input/input_full.csv > input/18.csv
# sed -n '1801,1900p' input/input_full.csv > input/19.csv
# sed -n '1901,2002p' input/input_full.csv > input/20.csv
#
# ## get experiment numbers
# python3 trace_to_sra.py -i input/1.csv -o exp/1.csv
# python3 trace_to_sra.py -i input/2.csv -o exp/2.csv
# python3 trace_to_sra.py -i input/3.csv -o exp/3.csv
# python3 trace_to_sra.py -i input/4.csv -o exp/4.csv
# python3 trace_to_sra.py -i input/5.csv -o exp/5.csv
# python3 trace_to_sra.py -i input/6.csv -o exp/6.csv
# python3 trace_to_sra.py -i input/7.csv -o exp/7.csv
# python3 trace_to_sra.py -i input/8.csv -o exp/8.csv
# python3 trace_to_sra.py -i input/9.csv -o exp/9.csv
# python3 trace_to_sra.py -i input/10.csv -o exp/10.csv
# python3 trace_to_sra.py -i input/11.csv -o exp/11.csv
# python3 trace_to_sra.py -i input/12.csv -o exp/12.csv
# python3 trace_to_sra.py -i input/13.csv -o exp/13.csv
# python3 trace_to_sra.py -i input/14.csv -o exp/14.csv
# python3 trace_to_sra.py -i input/15.csv -o exp/15.csv
# python3 trace_to_sra.py -i input/16.csv -o exp/16.csv
# python3 trace_to_sra.py -i input/17.csv -o exp/17.csv
# python3 trace_to_sra.py -i input/18.csv -o exp/18.csv
# python3 trace_to_sra.py -i input/19.csv -o exp/19.csv
# python3 trace_to_sra.py -i input/20.csv -o exp/20.csv
#
# ## get full metadata
#
# python3 parse_sra.py -i exp/1.csv -o output/1.csv
# python3 parse_sra.py -i exp/2.csv -o output/2.csv
# python3 parse_sra.py -i exp/3.csv -o output/3.csv
# python3 parse_sra.py -i exp/4.csv -o output/4.csv
# python3 parse_sra.py -i exp/5.csv -o output/5.csv
# python3 parse_sra.py -i exp/6.csv -o output/6.csv
# python3 parse_sra.py -i exp/7.csv -o output/7.csv
# python3 parse_sra.py -i exp/8.csv -o output/8.csv
# python3 parse_sra.py -i exp/9.csv -o output/9.csv
# python3 parse_sra.py -i exp/10.csv -o output/10.csv
# python3 parse_sra.py -i exp/11.csv -o output/11.csv
# python3 parse_sra.py -i exp/12.csv -o output/12.csv
# python3 parse_sra.py -i exp/13.csv -o output/13.csv
# python3 parse_sra.py -i exp/14.csv -o output/14.csv
# python3 parse_sra.py -i exp/15.csv -o output/15.csv
# python3 parse_sra.py -i exp/16.csv -o output/16.csv
# python3 parse_sra.py -i exp/17.csv -o output/17.csv
# python3 parse_sra.py -i exp/18.csv -o output/18.csv
# python3 parse_sra.py -i exp/19.csv -o output/19.csv
# python3 parse_sra.py -i exp/20.csv -o output/20.csv

# join files with accession	and experiment numbers
cat exp/1.csv exp/2.csv exp/3.csv exp/4.csv exp/5.csv exp/6.csv exp/7.csv exp/8.csv exp/9.csv exp/10.csv exp/11.csv exp/12.csv exp/13.csv exp/14.csv exp/15.csv exp/16.csv exp/17.csv exp/18.csv exp/19.csv exp/20.csv > experiment_accessions.csv

# join output files
cat output/1.csv output/2.csv output/3.csv output/4.csv output/5.csv output/6.csv output/7.csv output/8.csv output/9.csv output/10.csv output/11.csv output/12.csv output/13.csv output/14.csv output/15.csv output/16.csv output/17.csv output/18.csv output/19.csv output/20.csv > sra_metadata.csv
