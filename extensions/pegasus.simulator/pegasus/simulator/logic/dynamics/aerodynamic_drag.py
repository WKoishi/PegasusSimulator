import numpy as np
from pegasus.simulator.logic.state import State

class AerodynamicDrag:

    def __init__(self, linear_drag_coef = [0.0] * 3, drag_moment_coef = [0.0] * 3):
        
        self.linear_drag_coef = np.array(linear_drag_coef)
        self.drag_moment_coef = np.array(drag_moment_coef)

        self.linear_drag_force = np.zeros(3, dtype=np.float64)
        self.drag_moment = np.zeros(3, dtype=np.float64)

    @property
    def drag(self):
        return self.linear_drag_force, self.drag_moment
    
    def update(self, state: State, dt: float):
        for i in range(3):
            self.linear_drag_force[i] = - self.linear_drag_coef[i] * np.power(state.linear_body_velocity[i], 2)
            self.drag_moment[i] = - self.drag_moment_coef[i] * np.power(state.angular_velocity[i], 2)

        return self.linear_drag_force, self.drag_moment
        


    




