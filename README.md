Quantic MSSE Managing Software Engineering Project - Florists Website Project with Mockup Wireframes

# Lily's Florist — Website Requirements & Design
 
> Quantic MSSE · Managing Software Engineering Project
> Author: **Vishant Prasad** · August 2025
 
Requirements engineering and UX design package for an e-commerce website for **Lily's Florist**, a small florist business. Covers the full front end of the software lifecycle: client discovery, user stories, requirements specification, test cases, traceability, user journeys, sitemaps, annotated wireframes and high-fidelity mockups.
 
**This is a design and requirements project. No website code is implemented.**
 
📄 **[Read the full report (PDF)](Managing-Software-Engineering-Project-Vishant-Prasad.pdf)**
 
---
 
## Preview
 
| Wireframe | Mockup |
|---|---|
| ![Homepage wireframe](Wireframes/Lily's%20Florist%20Wireframes%201.png) | ![Homepage mockup](Mockups/Mockup%20(1).png) |
 
---
 
## Problem
 
Lily needs a site where customers can order flowers, browse designs and schedule delivery or pickup, while she manages orders and inventory in one place.
 
Client pain points identified during discovery:
 
| ID | Pain point | Theme |
|---|---|---|
| P1 | Customers unsure whether an order went through | Order transparency & confirmation |
| P2 | Delivery timing stressful for last-minute or surprise gifts | Scheduling & reliability |
| P3 | Flowers in stock sometimes differ from website photos | Product accuracy vs availability |
| P4 | Repeat orders require re-explaining preferences | Personalisation & repeat ordering |
 
---
 
## Approach
 
1. **Requirements gathering** — Simulated client interview with a "Lily the Florist" AI persona ([transcript](Lilys-Florist/ChatGPT-Lily%20the%20Florist%20-%20Interview.pdf)).
2. **User stories** — 19 stories across customer and florist/admin roles.
3. **Requirements specification** — 22 functional and 10 non-functional requirements.
4. **Test cases** — 34 test cases mapped to requirements.
5. **Traceability** — Requirements-to-test matrix generated with [ReqFlow](https://goeb.github.io/reqflow/).
6. **User journey** — Flowchart and swimlane diagrams generated with Python + Graphviz.
7. **Information architecture** — Sitemaps for customer and admin views.
8. **Wireframes** — 13 annotated low-fidelity screens.
9. **Mockups** — 19 high-fidelity screens.
---
 
## Scope
 
**Customer-facing**
- Gallery with images, prices and live stock availability
- Cart, guest or account checkout
- Delivery date and time slot scheduling
- Secure card and digital wallet payments
- Order confirmation and status notifications (email/SMS)
- Order history, one-click reorder, saved favourites
- Loyalty points and discounts
- Blog for seasonal updates and flower care tips
**Florist / admin**
- Real-time inventory management
- Order list, order detail and fulfilment tracking
### Screens designed
 
Homepage · Gallery · Store · Product · Cart · Checkout (Account → Delivery → Payment → Confirmation) · Customer Dashboard · Admin Order List · Admin Inventory · Admin Order Detail
 
---
 
## Repository Structure
 
```
.
├── Managing-Software-Engineering-Project-Vishant-Prasad.pdf   # Final submitted report
├── Managing-Software-Engineering-Project.docx                 # Editable source
├── PDF-Exports/            # Report split by section
├── Lilys-Florist/
│   ├── ChatGPT-Lily the Florist - Interview.pdf               # Requirements interview
│   └── Requirements/
│       ├── user-stories.txt          # US-001 … US-019
│       ├── system-requirements.txt   # FR-001 … FR-022, NFR-001 … NFR-010
│       ├── tests.txt                 # TC-001 … TC-034
│       ├── reqflow.cfg               # ReqFlow configuration
│       └── traceability.html         # Generated traceability matrix
├── Diagrams/
│   ├── User-Journey.py               # Graphviz flowchart generator
│   ├── Swimlane-Style.py             # Graphviz swimlane generator
│   └── *.png / *.pdf                 # User journey + sitemap outputs
├── Wireframes/             # Annotated low-fidelity wireframes
├── Mockups/                # High-fidelity mockups
└── Assests/                # Image assets used in mockups
```
 
---
 
## Reproducing Artefacts
 
### User journey diagrams
 
```bash
pip install graphviz          # also requires Graphviz system binaries
cd Diagrams
python User-Journey.py
python Swimlane-Style.py
```
 
### Traceability matrix
 
```bash
cd Lilys-Florist/Requirements
reqflow trac -c reqflow.cfg -x html > traceability.html
```
 
---
 
## Key Deliverables
 
| Deliverable | Location |
|---|---|
| Full report | [PDF](Managing-Software-Engineering-Project-Vishant-Prasad.pdf) |
| User stories | [user-stories.txt](Lilys-Florist/Requirements/user-stories.txt) |
| Requirements (FR/NFR) | [system-requirements.txt](Lilys-Florist/Requirements/system-requirements.txt) |
| Test cases | [tests.txt](Lilys-Florist/Requirements/tests.txt) |
| Traceability matrix | [traceability.html](Lilys-Florist/Requirements/traceability.html) |
| User journey | [Flowchart](Diagrams/User_Journey_Flow.png) · [Swimlane](Diagrams/User_Journey_Swimlane.png) |
| Sitemaps | [Views PDF](Diagrams/Sitemap%20Planning%20-%20Views.pdf) |
| Annotated wireframes | [PDF](Wireframes/Annotated-Wireframes.pdf) |
| Mockups | [PDF](Mockups/Mockups-Merged.pdf) |
 
---
 
## Skills Demonstrated
 
Requirements elicitation · User story writing · Functional & non-functional specification · Test case design · Requirements traceability · User journey mapping · Information architecture · Wireframing · UI mockups · Diagrams-as-code
 
---
 
## License
 
[MIT](LICENSE)
 
Lily's Florist is a fictional client created for academic purposes. Stock images in `Assests/` belong to their respective owners.
 
