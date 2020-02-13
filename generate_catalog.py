import sys, argparse

def parse_args():
    """ Return dictionary of command line arguments
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        usage=argparse.SUPPRESS)
    parser.add_argument('--shared', type=str, dest='shared_list', required=True,
        help="""Path to list identidiers of the shared snps""")
    parser.add_argument('--in-list', type=str, dest='in_paths', required=True,
        help="""Path to file containing paths of all input files, which should be the direct output files from mummur4 snps program""")
    parser.add_argument('--out', type=str, dest='out', default='/dev/stdout',
        help="""Path to output file""")

    return vars(parser.parse_args())


def read_shared_snps(fpath):
	shared_snps = []

	with open(fpath) as fh:
		for line in fh:
			snp_id = line.rstrip()
			shared_snps.append(snp_id)

	return shared_snps

def gen_catalog(shared_snps, fpaths):
	catalog = []

	for fpath in fpaths:
		temp_dict = {}
		with open(fpath) as fh:
			for i in range(5):
				next(fh)

			for line in fh:
				items = line.rstrip().split()
				snp_id = "{}||{}||{}||{}".format(items[13], items[0], items[1], items[2])

				temp_dict[snp_id] = 1

		catalog_vec = []
		for snp_id in shared_snps:
			if snp_id in temp_dict:
				catalog_vec.append("1")
			else:
				catalog_vec.append("0")

		catalog.append(catalog_vec)

		sys.stderr.write("Done processing {}\n".format(fpath))

	return catalog


def make_header(fpaths):
	header = ["snp_id"]

	for fpath in fpaths:
		fname = fpath.split('/')[-1].split('.')[0]
		header.append(fname)

	return header


def output(shared_snps, snp_catalog, header, output_path):
	assert len(header) == len(snp_catalog) + 1

	for catalog_vec in snp_catalog:
		assert len(shared_snps) == len(catalog_vec)

	with open(output_path, 'w') as fh:
		fh.write("{}\n".format("\t".join(header)))	

		for i, snp_id in enumerate(shared_snps):
			fh.write("{}\n".format("\t".join([snp_id] + [catalog_vec[i] for catalog_vec in snp_catalog])))

def main():
	args = parse_args()

	shared_path = args["shared_list"] 
	path_list = args["in_paths"]

	output_path = args["out"]

	in_fpaths = []

	shared_snps = read_shared_snps(shared_path)
	with open(path_list) as fh:
		for line in fh:
			genome_pair = line.rstrip().split('.')[0].split('-')
			if genome_pair[0] == genome_pair[1]:
				pass
			else:
				in_fpaths.append(line.rstrip())

	assert len(in_fpaths) > 0

	catalog = gen_catalog(shared_snps, in_fpaths)

	header = make_header(in_fpaths)

	output(shared_snps, catalog, header, output_path)

if __name__ == "__main__":
	main()
