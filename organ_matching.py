
import heapq

# 1. Donor Data
donors = [
    {"id": "D1", "blood": "A", "organ": "Kidney", "location": 10},
    {"id": "D2", "blood": "B", "organ": "Liver", "location": 20},
    {"id": "D3", "blood": "O", "organ": "Kidney", "location": 15},
    {"id": "D4", "blood": "AB", "organ": "Heart", "location": 30},
    {"id": "D5", "blood": "A", "organ": "Liver", "location": 25}
]

# 2. Recipient Data
recipients = [
    {"id": "R1", "blood": "A", "organ": "Kidney",
     "urgency": 9, "location": 12},
    {"id": "R2", "blood": "B", "organ": "Liver",
     "urgency": 7, "location": 22},
    {"id": "R3", "blood": "O", "organ": "Kidney",
     "urgency": 8, "location": 18},
    {"id": "R4", "blood": "AB", "organ": "Heart",
     "urgency": 10, "location": 28},
    {"id": "R5", "blood": "A", "organ": "Liver",
     "urgency": 6, "location": 24}
]


# 3. Compatibility Function
def is_compatible(donor, recipient):
    return (
        donor["blood"] == recipient["blood"]
        and donor["organ"] == recipient["organ"]
    )


# 4. Cost Function: g(n)
def cost(donor, recipient):
    distance = abs(donor["location"] - recipient["location"])
    urgency_penalty = 10 - recipient["urgency"]

    return distance + urgency_penalty


# 5. Heuristic Function: h(n)
def heuristic(donor, recipient):
    distance = abs(donor["location"] - recipient["location"])
    urgency_bonus = recipient["urgency"]

    return max(0, distance - urgency_bonus)


# 6. A* Search Algorithm
def a_star_matching(donors, recipients):
    priority_queue = []

    # Check every donor-recipient pair
    for donor in donors:
        for recipient in recipients:

            # Check compatibility
            if is_compatible(donor, recipient):

                # Calculate cost and heuristic
                g = cost(donor, recipient)
                h = heuristic(donor, recipient)
                f = g + h

                # Store the match in the priority queue
                heapq.heappush(
                    priority_queue,
                    (
                        f,
                        g,
                        donor["id"],
                        recipient["id"],
                        donor,
                        recipient
                    )
                )

    # Check whether any compatible match exists
    if not priority_queue:
        print("No compatible donor-recipient match found.")
        return None

    # Get the match with the lowest f-value
    best_match = heapq.heappop(priority_queue)

    f, g, donor_id, recipient_id, donor, recipient = best_match

    # Display the result
    print("\n===== ORGAN DONOR-RECIPIENT MATCHING =====")
    print("Donor ID       :", donor["id"])
    print("Recipient ID   :", recipient["id"])
    print("Organ          :", donor["organ"])
    print("Blood Group    :", donor["blood"])
    print("Distance       :", abs(
        donor["location"] - recipient["location"]
    ))
    print("Recipient Urgency:", recipient["urgency"])
    print("Cost g(n)      :", g)
    print("Heuristic h(n) :", heuristic(donor, recipient))
    print("Total f(n)     :", f)

    return donor, recipient


# 7. Execute the Program
result = a_star_matching(donors, recipients)
