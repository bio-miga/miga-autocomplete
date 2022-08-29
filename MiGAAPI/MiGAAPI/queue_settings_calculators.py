import math

from airavata.model.experiment.ttypes import ExperimentModel
from airavata_django_portal_sdk.decorators import queue_settings_calculator


def get_genomes_input_value(experiment_model: ExperimentModel):
    for exp_input in experiment_model.experimentInputs:
        if exp_input.name == "Input Genome Files":
            return exp_input.value
    return None


def get_num_genomes(experiment_model: ExperimentModel):
    genomes_input_value = get_genomes_input_value(experiment_model)
    num_genomes = len(genomes_input_value.split(",")) if genomes_input_value else 0
    return num_genomes


@queue_settings_calculator(
    id="miga-quadratic-walltime", name="MiGA - Quadratic Walltime for Fast Indexing"
)
def miga_quadratic_walltime(request, experiment_model: ExperimentModel):
    # See https://airavata.apache.org/api-docs/master/experiment_model.html#Struct_ExperimentModel for ExperimentModel fields
    num_genomes = get_num_genomes(experiment_model)
    # minimum of 1 core, max of 4096
    total_core_count = max(1, min(num_genomes, 4096))
    if total_core_count < 128:
        queue_name = "shared"
        node_count = 1
    else:
        queue_name = "compute"
        node_count = math.ceil(total_core_count / 128)
    # https://xsede-manual.microbial-genomes.org/allocation#for-database-indexing-and-genome-dereplication
    # time = (5n + n^2/10)/cores, with a minimum of 60
    walltime_limit = max(
        60, (5 * num_genomes + num_genomes**2 / 10) / total_core_count
    )
    result = {}
    result["totalCPUCount"] = total_core_count
    result["queueName"] = queue_name
    result["nodeCount"] = node_count
    result["wallTimeLimit"] = walltime_limit
    return result


@queue_settings_calculator(id="miga-linear-walltime", name="MiGA - Linear Walltime")
def miga_linear_walltime(request, experiment_model: ExperimentModel):
    # See https://airavata.apache.org/api-docs/master/experiment_model.html#Struct_ExperimentModel for ExperimentModel fields
    num_genomes = get_num_genomes(experiment_model)
    # minimum of 1 core, max of 4096
    total_core_count = max(1, min(num_genomes, 4096))
    if total_core_count < 128:
        queue_name = "shared"
        node_count = 1
    else:
        queue_name = "compute"
        node_count = math.ceil(total_core_count / 128)
    # https://xsede-manual.microbial-genomes.org/allocation#for-genome-classification-and-genome-typing
    # time = 10n / cores, with a minimum of 60
    walltime_limit = max(60, (10 * num_genomes) / total_core_count)
    result = {}
    result["totalCPUCount"] = total_core_count
    result["queueName"] = queue_name
    result["nodeCount"] = node_count
    result["wallTimeLimit"] = walltime_limit
    return result
