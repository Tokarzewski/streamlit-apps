from . import functions as f
from dataclasses import dataclass, field


@dataclass
class EmbeddedPipe:
    name: str = "Default"
    external_diameter: float = 0.016 # External diameter of pipe [m]
    wall_thickness: float = 0.002 # Pipe wall thickness [m]
    conductivity: float = 0.35 # Thermal conductivity of the heat conducting material [W/mK]

default_embedded_pipe = EmbeddedPipe()

@dataclass
class EmbeddedRadiantSystem:
    name: str = 'Default'
    system_type: str = 'A' # System type (A, B, C, D, H, I, J)
    embedded_pipe: EmbeddedPipe = field(default_factory=default_embedded_pipe)
    case_of_application: str = 'floor heating'
    W: float = 0.10 # Pipe spacing [m]

    #Sheathing
    d_M: float = 0.016  # External diameter of sheathing [m]
    k_M: float = 1.0  # Sheathing material conductivity [W/mK]

    # heat diffusion device - only for system B
    s_WL: float = 0.002  # Thickness of the heat conducting material [m]
    k_WL: float = 50  # Thermal conductivity of the heat conducting material [W/mK]
    L_WL: float = 0.1  # Width of heat conducting device [m]

    # covering
    s_u: float = 0.045  # Thickness of layer above the pipe [m]
    R_k_B: float = 0.05  # Thermal resistance of the floor covering [m2K/W]
    k_E: float = 1.8  # Thermal conductivity of screed [W/mK]
    
    # fixing inserts
    psi: float = 0.05  # Volume ratio of the fixing inserts in the screed
    k_W: float = 0.5  # Thermal conductivity of the fixing inserts [W/mK]

    # temperatures
    t_i: float = 20.0  # Design indoor temperature [*C]
    t_V: float = 40.0  # Design supply temperature of heating or cooling medium [*C]
    t_R: float = 35.0  # Design return temperature of heating or cooling medium [*C]

    deltat_H: float = field(init=False)  # Medium differential temperature [K]
    q: float = field(init=False)  # Heat flux [W/m2]
    K_H: float = field(init=False)  # Equivalent heat transmission coefficient.

    def B_0(self):
        if self.system_type in "ACHIJ":
            return 6.7
        elif self.system_type in "BD":
            return 6.5
        else:
            return "There is no B_0 for system type: ", self.system_type

    def q_ACHIJ(self):
        """Heat transfer coefficient for system types A, C, H, I, J."""

        if 0.05 <= self.psi <= 0.15:
            k_E = f.k_E_prim(self.psi, self.k_E, self.k_W)
        else:
            k_E = self.k_E

        a_B = f.a_B1(self.alfa, k_E, self.R_k_B)
        a_W = f.a_W1(self.R_k_B)
        m_U = f.m_U(self.s_u)
        m_D = f.m_D(self.D)

        if self.W <= 0.375:
            a_U = f.a_U1(self.R_k_B, self.W)
            a_D = f.a_D(self.R_k_B, self.W)
            m_W = f.m_W(self.W)

            a_i = [a_B, a_W, a_U, a_D]
            m_i = [1, m_W, m_U, m_D]

            self.B = f.B1(
                B_0=self.B_0,
                a_i=a_i,
                m_i=m_i,
                W=self.W,
                k_R=self.embedded_pipe.conductivity,
                d_a=self.embedded_pipe.external_diameter,
                s_R=self.embedded_pipe.wall_thickness,
            )
            return f.q5(self.B, a_i, m_i, 1)

        else:
            a_U = f.a_U1(self.R_k_B, W=0.375)
            a_D = f.a_D(self.R_k_B, W=0.375)
            m_W = f.m_W(W=0.375)

            a_i = [a_B, a_W, a_U, a_D]
            m_i = [1, m_W, m_U, m_D]

            self.B = f.B1(
                B_0=self.B_0,
                a_i=a_i,
                m_i=m_i,
                W=self.W,
                k_R=self.embedded_pipe.conductivity,
                d_a=self.embedded_pipe.external_diameter,
                s_R=self.embedded_pipe.wall_thickness,
            )
            q_0375 = f.q5(self.B, a_i, m_i, 1)

            return f.q8(q_0375, self.W)

    def q_B(self):
        """Heat transfer coefficient for system type B."""
        a_U = f.a_U2(self.alfa, self.s_u, self.k_E)
        a_W = f.a_W2(self.s_u, self.k_E)
        b_u = f.b_u(self.W)
        a_K = f.a_K(self.W)
        K_WL = f.K_WL(self.s_WL, self.k_WL, b_u, self.s_u, self.k_E)

        if 0.05 <= self.W <= 0.45:
            m_W = f.m_W(self.R_k_B)
        
        if K_WL < 0.5:
            a_WL = f.a_WL2(K_WL, self.W, self.D)
        else:
            a_WL = f.a_WL3(K_WL, self.W, self.D)

        if self.L_WL < self.W:
            a_0 = f.a_WL2(0, self.W, self.D)
            a_WL = f.a_WL1(a_WL, a_0, self.L_WL, self.W)

        a_B = f.a_B2(a_U, a_W, m_W, a_WL, a_K, self.R_k_B, self.W)

        a_i = [a_B, a_W, a_U, a_WL, a_K]
        m_i = [1, m_W, 1, 1, 1]

        self.B = f.B1(
            B_0=self.B_0,
            a_i=a_i,
            m_i=m_i,
            W=self.W,
            k_R=self.embedded_pipe.conductivity,
            d_a=self.embedded_pipe.external_diameter,
            s_R=self.embedded_pipe.wall_thickness,
        )

        return f.q5(self.B, a_i, m_i, 1)

    def q_D(self):
        """Heat transfer coefficient for system type D."""
        a_U = f.a_U2(self.alfa, self.s_u, self.k_E)
        a_B = f.a_B3(a_U, self.R_k_B)

        a_i = [a_B, 1.06, a_U]
        m_i = [1, 1, 1]

        self.B = self.B_0

        return f.q5(self.B, a_i, m_i, 1)

    def q(self):
        if self.system_type in "ACHIJ":
            return self.q_ACHIJ()
        elif self.system_type == "B":
            return self.q_B()
        elif self.system_type == "D":
            return self.q_D()
        else:
            return "There is no q system type: ", self.system_type

    def __post_init__(self) -> None:
        self.B_0 = self.B_0()
        # XYZ use ISO 6946 to calculate alfa for calculating q.
        self.alfa = f.alfa(self.case_of_application)
        self.D = max(self.embedded_pipe.external_diameter, self.d_M)
        self.K_H = self.q(self)
        self.deltat_H = f.deltat_H(self.t_V, self.t_R, self.t_i)
        self.q = self.K_H * self.deltat_H
