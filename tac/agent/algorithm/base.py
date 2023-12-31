from abc import ABC, abstractmethod
from tac.utils import api


class Algorithm(ABC):
    """Abstract base class for reinforcement learning algorithms, to define the interface for all algorithms"""

    def __init__(self, agent, global_nets=None):
        # TODO: with flat spec, currently different to SLM Lab implementation
        self.agent = agent
        self.algorithm_spec = agent.spec["algorithm_spec"]
        self.name = self.algorithm_spec["name"]
        self.memory_spec = agent.spec["memory_spec"]
        self.net_spec = agent.spec["net_spec"]

        self.init_algorithm_params()

        # TODO
        self.init_nets(global_nets)

    @abstractmethod
    @api
    def init_algorithm_params(self):
        """Initialize other algorithm parameters"""
        raise NotImplementedError

    @abstractmethod
    @api
    def init_nets(self, global_nets=None):
        """Initialize the neural network from the net_spec"""
        raise NotImplementedError

    @api
    def calc_pdparam(self, x, net=None):
        """
        To get the pdparam for action policy sampling, do a forward pass of the appropriate net, and pick the correct
        outputs.
        The pdparam will be the logits for discrete prob. dist., or the mean and std for continuous prob. dist.
        """
        raise NotImplementedError

    @api
    def act(self, state):
        """Standard act method."""
        raise NotImplementedError
        # return action

    @abstractmethod
    @api
    def sample(self):
        """Samples a batch from memory"""
        raise NotImplementedError
        # return batch

    @abstractmethod
    @api
    def train(self):
        """Implement algorithm train, or throw NotImplementedError"""
        raise NotImplementedError

    @abstractmethod
    @api
    def update(self):
        """Implement algorithm update, or throw NotImplementedError"""
        raise NotImplementedError

    @api
    def save(self, ckpt=None):
        """Save net models for algorithm given the required property self.net_names"""
        # if not hasattr(self, 'net_names'):
        #     logger.info('No net declared in self.net_names in init_nets(); no models to save.')
        # else:
        #     net_util.save_algorithm(self, ckpt=ckpt)
        raise NotImplementedError

    @api
    def load(self):
        """Load net models for algorithm given the required property self.net_names"""
        # if not hasattr(self, 'net_names'):
        #     logger.info('No net declared in self.net_names in init_nets(); no models to load.')
        # else:
        #     net_util.load_algorithm(self)
        # # set decayable variables to final values
        # for k, v in vars(self).items():
        #     if k.endswith('_scheduler') and hasattr(v, 'end_val'):
        #         var_name = k.replace('_scheduler', '')
        #         setattr(self.body, var_name, v.end_val)
        raise NotImplementedError
