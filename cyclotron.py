class Cyclotron:
    def __init__(self, matrix):
        self.size = len(matrix)

        self.cyclotron = matrix

    def __str__(self):
        return "\n".join(" ".join(row) for row in self.cyclotron) + "\n"

    def accelerate_electron(self):
        for i in range(self.size):
            self.cyclotron[0][i] = "e"

            self.cyclotron[i][-1] = "e"

    def accelerate_proton(self):
        proton = "p"

        for i in range(self.size):
            self.cyclotron[0][i] = proton

            self.cyclotron[i][0] = proton

            self.cyclotron[-1][i] = proton

            self.cyclotron[i][-1] = proton

        self.cyclotron[-2][-2] = proton

        self.cyclotron[-1][-1] = "1"

    def accelerate_neutron(self):
        for i in range(self.size):
            self.cyclotron[0][i] = "n"

    def accelerate_particle(self, particle_type):
        if particle_type == "e":
            self.accelerate_electron()

        elif particle_type == "p":
            self.accelerate_proton()

        elif particle_type == "n":
            self.accelerate_neutron()
