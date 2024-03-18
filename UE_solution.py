#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script contains a solution to the Urban Economics project.
"""


class TransportationNetwork:
    def __init__(self, parameters):
        self.parameters = parameters

    def travel_time(self, link, flow):
        if link not in self.parameters:
            raise ValueError("Invalid link identifier")
        alpha, beta = self.parameters[link]
        return alpha + beta * flow

def find_equilibrium_flow(network, max_iterations, tolerance):
    # Initialize flow on each link
    flows = {link: 10 for link in network.parameters}
    iterations = []
    link_travel_times = {}
    # Iterative algorithm
    for _ in range(max_iterations):
        # Calculate travel time for each route
        travel_times = {link: network.travel_time(link, flows[link]) for link in flows}

        # Track travel times over iterations
        for link in travel_times:
            if link in link_travel_times:
                link_travel_times[link].append(travel_times[link])
            else:
                link_travel_times[link] = [travel_times[link]]

        # Find the minimum travel time among all routes
        min_time = min(travel_times.values())

        # Update flows based on Wardrop's principle
        for link in flows:
            if travel_times[link] == min_time:
                flows[link] = 10
            else:
                flows[link] = 0
        iterations.append(flows)
        # Check for convergence
        if max(abs(flows[link] - 10) for link in flows) < tolerance:
            break

    return flows, link_travel_times
def travel_time(self, link, flow):
    if link not in self.parameters:
        raise ValueError("Invalid link identifier")
    alpha, beta = self.parameters[link]
    return alpha + beta * flow

# Define parameters for each link
parameters = {
    'AB': (2, 0.1),
    'AD': (3, 0.2),
    'BC': (4, 0.15),
    'DE': (5, 0.25),
    'EC': (3, 0.1)
}

# Create an instance of the transportation network
network = TransportationNetwork(parameters)

# Set convergence criteria
max_iterations = 100
tolerance = 0.01

# Find equilibrium flow
equilibrium_flow, link_travel_times = find_equilibrium_flow(network, max_iterations, tolerance)

# Output the equilibrium flow distribution
print("Equilibrium Flow Distribution:")
for link, flow in equilibrium_flow.items():
    print("Flow on", link, ":", flow)
    print("Travel time on", link, ":", network.travel_time(link, flow))

print("link travel times:", link_travel_times)

# Plot the convergence of travel times and equilibrium flow
import matplotlib.pyplot as plt
for link, times in link_travel_times.items():
    plt.plot(times, label=link)
# plot the equilibrium flow
plt.plot([equilibrium_flow[link] for link in equilibrium_flow], label="Equilibrium Flow", linestyle='--')
# ylim to make the plot look better
plt.ylim(-2, 15)
plt.title("Convergence of Travel Times and Equilibrium Flow")
plt.xlabel("Iteration")
plt.ylabel("Travel Time")
plt.legend()
plt.show()
