# tensorflow_slurm_manager
working on a cluster manager for TF

Long story short, this script should parse the environment variables that slurm sets up on each node it gives you, and build the ClusterSpec from those variables (the generated string needs to be consistant across all nodes).  Furthermore, each computer is responsible for deciding what job/task and task_id, and hopefully that matches up with the cluster_spec string generated.  Those were the guiding thoughts I was having while writing it.  

This script will attempt to only assign one parameter server (`ps`) per physical node.  (I do not believe it will support more than one., but it's been a while since I wrote the code).  From there on out, it will start adding worker nodes until there have been enough worker nodes assigned.

