import argparse
from slurm_manager import SlurmClusterManager

def printClusterSpec(num_param_servers=1, num_workers=None, starting_port=None):
    manager = SlurmClusterManager(num_param_servers=1, num_workers=None, starting_port=None)
    _, job, task_id = manager.build_cluster_spec()
    wk_strings = manager._wk_strings
    ps_strings = manager._ps_strings

    print(wk_strings, ps_strings, job, task_id, sep=";")

printClusterSpec(num_param_servers = 1, starting_port=12000)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    description = 'get cluster spec')
    parser.add_argument('--num_param_servers', type=int, required=False, default=1, help = 'number of parameter servers')
    parser.add_argument('--num_worker_servers', type=int, required=False, default=1, help = 'number of worker servers')
    parser.add_argument('--starting_port', type=int, required=False, default=2222, help = 'starting port')

    args = parser.parse_args()

    printClusterSpec(args.num_param_servers, args.num_worker_servers, args.starting_port)

