from graphviz import Digraph

# Create a Directed Graph for the User Journey Map
dot = Digraph("User Journey", format="png")
dot.attr(rankdir="TB", dpi="600", nodesep="1.0", ranksep="1.0")  # Top-to-bottom, higher resolution

# Define Styles
dot.attr("node", shape="rectangle", style="rounded,filled", color="lightblue", fontname="Helvetica", fontsize="14")

# Customer Steps
dot.node("C1", "Visit Website")
dot.node("C2", "Browse Gallery")
dot.node("C3", "Select Arrangement")
dot.node("C4", "Add to Cart")
dot.node("C5", "Checkout & Login/Signup")
dot.node("C6", "Enter Delivery Details\n(Date & Time)")
dot.node("C7", "Make Payment")
dot.node("C8", "Receive Order Confirmation")
dot.node("C9", "Receive Delivery Notifications")

# Florist Steps
dot.attr("node", shape="rectangle", style="rounded,filled", color="lightgreen", fontname="Helvetica", fontsize="14")
dot.node("F1", "Review Order in Dashboard")
dot.node("F2", "Prepare Flowers")
dot.node("F3", "Arrange Delivery")

# System Responses
dot.attr("node", shape="ellipse", style="filled", color="lightgrey", fontname="Helvetica", fontsize="14")
dot.node("S1", "Homepage Loads")
dot.node("S2", "Show Designs\n(Images, Prices, Stock)")
dot.node("S3", "Display Product Details")
dot.node("S4", "Cart Updated")
dot.node("S5", "Prompt Login or Guest Checkout")
dot.node("S6", "Validate Delivery Slot")
dot.node("S7", "Process Payment Securely")
dot.node("S8", "Notify Florist & Save Order")
dot.node("S9", "Update Order Status\n('In prep', 'Out for delivery')")

# Edges - Customer Flow
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

# Save Diagram to a Windows Path
output_path = r"D:\Vishant\Career\Quantic\Projects\Managing-Software-Engineering-Project\Diagrams\User_Journey_Flow"
dot.render(output_path, format="png", cleanup=True)

print(f"Diagram Saved to {output_path}.png")
