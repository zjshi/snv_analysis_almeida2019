import sys, argparse, random

import numpy as np

def parse_args():
    """ Return dictionary of command line arguments
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        usage=argparse.SUPPRESS)
    parser.add_argument('--catalog', type=str, dest='catalog', required=True,
        help="""Path to snp catalog file""")
    parser.add_argument('--name', type=str, dest='name', required=True,
        help="""A parameter specifying the name of the catalog""")
    parser.add_argument('--genome-info', type=str, dest='info_path', required=True,
		help="""Path to a tab-separated file specifying source information for every genome""")
    parser.add_argument('--out', type=str, dest='out', default='/dev/stdout',
        help="""Path to output file""")

    return vars(parser.parse_args())

def read_genome_info(fpath):
	info_map = {}

	with open(fpath) as fh:
		for line in fh:
			items = line.rstrip().split('\t')
			info_map[items[0]] = items[1]
	
	return info_map


def bin_snps(catalog_fpath, info_map):
	snp_bins = {}

	with open(catalog_fpath) as fh:
		header = next(fh).rstrip().split('\t')[1:]

		for line in fh:
			source_map = {}
			catalog_row = line.rstrip().split('\t')[1:]

			for j, val in enumerate(catalog_row):
				if int(val) == 1:
					assert header[j] in info_map
					source = info_map[header[j]]
					source_map[source] = 1
				else:
					pass
			
			bin_key = ','.join(sorted(source_map.keys()))
			if bin_key not in snp_bins:
				snp_bins[bin_key] = 1
			else:
				snp_bins[bin_key] = snp_bins[bin_key] + 1

	return snp_bins


def output(name, snp_bins, output_path):
	with open(output_path, 'w') as fh:
		for bin_key in sorted(snp_bins.keys()):
			fh.write("{}\t{}\t{}\n".format(name, bin_key, str(snp_bins[bin_key])))

def main():
	args = parse_args()

	name = args["name"]

	catalog_path = args["catalog"] 
	info_path = args["info_path"] 

	output_path = args["out"]

	info_map = read_genome_info(info_path)

	snp_bins = bin_snps(catalog_path, info_map)

	output(name, snp_bins, output_path)

if __name__ == "__main__":
	main()
