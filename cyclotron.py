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


def cyclotron(particle_type, matrix):
    if len(matrix) < 4:
        print("Matrix must be at least 4x4")

        return "Matrix must be at least 4x4"

    cy = Cyclotron(matrix)

    if particle_type == "e":
        cy.accelerate_electron()

    elif particle_type == "p":
        cy.accelerate_proton()

    elif particle_type == "n":
        cy.accelerate_neutron()

    print(cy)

    return cy


def main():
    size = int(input("Enter the size of the cyclotron(minimum 4): "))

    particle_type = str(input("Enter the particle type (e/p/n): ")).lower()

    matrix = [["1" for _ in range(size)] for _ in range(size)]

    cyclotron(particle_type, matrix)


if __name__ == "__main__":
    main()
