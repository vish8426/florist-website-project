from graphviz import Digraph

# Create a Directed Graph for the User Journey Map
dot = Digraph("User Journey", format="png")
dot.attr(rankdir="TB", dpi="300", nodesep="0.8", ranksep="0.8")

# Define Styles
customer_style = {"shape": "rectangle", "style": "rounded,filled", "color": "lightblue", "fontname": "Helvetica"}
system_style = {"shape": "ellipse", "style": "filled", "color": "lightgrey", "fontname": "Helvetica"}
florist_style = {"shape": "rectangle", "style": "rounded,filled", "color": "lightgreen", "fontname": "Helvetica"}

# Swimlanes (Clusters)
# Customer Lane
with dot.subgraph(name="cluster_customer") as c:
    c.attr(label="Customer", style="filled", color="lightblue", fillcolor="aliceblue")
    c.node("C1", "Visit Website", **customer_style)
    c.node("C2", "Browse Gallery", **customer_style)
    c.node("C3", "Select Arrangement", **customer_style)
    c.node("C4", "Add to Cart", **customer_style)
    c.node("C5", "Checkout & Login/Signup", **customer_style)
    c.node("C6", "Enter Delivery Details\n(Date & Time)", **customer_style)
    c.node("C7", "Make Payment", **customer_style)
    c.node("C8", "Receive Order Confirmation", **customer_style)
    c.node("C9", "Receive Delivery Notifications", **customer_style)

# System Lane
with dot.subgraph(name="cluster_system") as s:
    s.attr(label="System", style="filled", color="lightgrey", fillcolor="whitesmoke")
    s.node("S1", "Homepage Loads", **system_style)
    s.node("S2", "Show Designs\n(Images, Prices, Stock)", **system_style)
    s.node("S3", "Display Product Details", **system_style)
    s.node("S4", "Cart Updated", **system_style)
    s.node("S5", "Prompt Login or Guest Checkout", **system_style)
    s.node("S6", "Validate Delivery Slot", **system_style)
    s.node("S7", "Process Payment Securely", **system_style)
    s.node("S8", "Notify Florist & Save Order", **system_style)
    s.node("S9", "Update Order Status\n('In prep', 'Out for delivery')", **system_style)

# Florist Lane
with dot.subgraph(name="cluster_florist") as f:
    f.attr(label="Florist", style="filled", color="lightgreen", fillcolor="honeydew")
    f.node("F1", "Review Order in Dashboard", **florist_style)
    f.node("F2", "Prepare Flowers", **florist_style)
    f.node("F3", "Arrange Delivery", **florist_style)

# Edges (Flow Across Swimlanes)
# Customer → System Interactions
dot.edge("C1", "S1")
dot.edge("S1", "C2")
dot.edge("C2", "S2")
dot.edge("S2", "C3")
dot.edge("C3", "S3")
dot.edge("S3", "C4")
dot.edge("C4", "S4")
dot.edge("S4", "C5")
dot.edge("C5", "S5")
dot.edge("S5", "C6")
dot.edge("C6", "S6")
dot.edge("S6", "C7")
dot.edge("C7", "S7")
dot.edge("S7", "C8")
dot.edge("C8", "S8")
dot.edge("S8", "F1")

# Florist Flow
dot.edge("F1", "F2")
dot.edge("F2", "F3")
dot.edge("F3", "S9")
dot.edge("S9", "C9")

# Save Diagram
output_path = r"D:\Vishant\Career\Quantic\Projects\Managing-Software-Engineering-Project\Diagrams\User_Journey_Swimlane"
dot.render(output_path, format="png", cleanup=True)

print(f"Swimlane Diagram Saved to {output_path}.png")
