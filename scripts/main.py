from code.config import read_config
from code.pipelines.data_gathering import DataGathering

config = read_config()

dg = DataGathering(config)

result = dg.run()