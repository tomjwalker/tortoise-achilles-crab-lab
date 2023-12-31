# tortoise-achilles-crab-lab
First deep reinforcement learning library, working through the easier Gymnasium Classic Control and Box2D environments; closely following Laura Graesser and Wah Loon Keng's book Foundations of Deep Reinforcement Learning and reimplementing their accompanying framework, SLM Lab. 

## Agent-Environment implementation
| Environment | Type | Training start | Training end | REINFORCE | SARSA | DQN | A2C | PPO | A3C | 
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Cartpole | Classic Control | <img src="./media/cartpole_unsolved.gif" style="float: left; margin-right: 10px;" width="150" /> | <img src="./media/cartpole_solved.gif" style="float: left; margin-right: 10px;" width="150" /> | (✓ mvp) |  |  |  |  |
| Pendulum | Classic Control |  |  |  |  |  |  |  |
| Mountain Car (Disc) | Classic Control |  |  |  |  |  |  |  |
| Acrobot | Classic Control |  |  |  |  |  |  |  |
| Lunar Lander | Box2D |  |  |  |  |  |  |  |
| Bipedal Walker | Box2D |  |  |  |  |  |  |  |

## DRL Algorithms
| Agent | Implemented? | Type | On / off policy | Action space // Discrete | Action space // Continuous | Learnt fn // v_pi | Learnt fn // q_pi | Learnt fn // pi | Pros | Cons | Notes |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| REINFORCE | ✓ | `Policy gradient` | `On` | ✓ | ✓ |  |  | ✓ | - Smooth action probability distribution (vs e.g. discontinuous e-greedy) <br> - Policy potentially simpler function to approximate than value functions <br> - Can approach deterministic policy | - High variance (without baseline) <br> - Sample inefficient <br>  -No guarantee of efficient exploration | Only simplest version implemented: next implement version with baseline  |
| SARSA |  | `Value-based` | `On` | ✓ |  |  | ✓ |  |  | - Limited to discrete action spaces |  |
| DQN |  | `Value-based` | `Off` | ✓ |  |  | ✓ |  |  | - Limited to discrete action spaces |  |
| DDQN |  | `Value-based` | `Off` | ✓ |  |  | ✓ |  | - Mitigation of overestimation bias <br> Improved training stability (target network reduces variance in Q value estimates) <br> - Better generalisation and faster learning speed | (vs DQN) <br> - Increased complexity (two separate Q networks) <br> - Higher computational cost |  |
| DDQN + PER |  | `Value-based` | `Off` | ✓ |  |  | ✓ | - Improved sample efficiency (focus on more informative experiences) <br> - Faster learning (focus on experiences with large TD errors) <br> - Better handling of rare events | - Increased complexity (maintaining experience priorities - although only small overhead) <br> - Potential for sample bias (prioritising experiences, rather than the underlying distribution from the environment) <br> - Hyperparameter sensitivity (introduces extra hyperparams) | - Limited to discrete action spaces | - Prioritised experience replay is an experience memory/buffer which prioritises experiences which are more useful for training (based on TD error, normalised across all experiences in buffer) |
| A2C |  | `Combined` | `On` | ✓ | ✓ | ✓ |  | ✓ | - Learnt reinforcement signal (from value function) can be more informative for a policy (dense) than (sparse) reward  <br> - Lower variance than Monte Carlo estimate of return (c.f. Reinforce) <br> - Increased sample efficiency over REINFORCE due to dense signal from value fn | - Training more complex - until value function generates reasonable signals, action selection is challenging |  |
| PPO |  | `Combined` | `On` | ✓ | ✓ | ✓ |  | ✓ | - Addresses performance collapse issue of simpler policy gradient algos (due to sensitivity to step size param during gradient ascent) <br> - Replaces A2C objective with a surrogate objective considering both pre-opt-step and post- policy networks <br> - More sample efficient than other policy methods | - (Common with other policy optimisation methods) risk of limited exploration <br> - Computational intensity <br> - Potential for conservative updates, which can slow learning time |  |


## Nomenclature
| Symbol / name | Meaning |
| :---: | :---: |
| $\pi_{\theta}$ | **Policy (parametrised)**: A function which outputs stochastic actions, given a state: $a \sim \pi(s)$. Neural net used as function approximator, with learnable parameters $\theta$ |
| $R(\tau)$ | Return of a trajectory (at time step 0; if mid-way through an episode, subscripted by t; $R_t(\tau)$ |
| $J(\pi_{\theta})$ | Objective function: expected return over all trajectories generated by an agent |
| $\nabla_{\theta}J(\pi_{\theta})$ | Policy gradient: used in gradient ascent update equation to maximise the objective |
| `frame` | A single time-step of an environment, $s_t$ |
| `experience` | A $(s_t, a_t, r_t)$ tuple, or alternatively, a $(s_t, a_t, r_t, s_{t+1}, done)$ tuple |
| Trajectory (roll-out): $\tau$ | **Trajectory**: a sequence of state-action-rewards, $s_t, a_t, r_t, ..., s_T, a_T, r_T$, sampled from a policy, $\tau \sim \pi$ |
| `episode` | A full set of experiences, from t = 0 to termination t = T. Trajectory is a sub-set of episode (e.g. a trajectory can be defined as a contiguous sequence starting from t > 0 |
| `session` | **Level 0**: Initialisation and training of RL agent using specific set of hyperparameters and random seed |
| `trial` | **Level 1**: Multiple sessions: same hyperparameters, different random seeds |
| `experiment` | **Level 2**: Different sets of hyperparameters, with a trial for each one |
