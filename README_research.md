# Project Zei  
## Research-Oriented Description (For Graduate School Review)

---

## 1. Project Positioning

Project Zei is an **experimental AI interaction prototype** exploring how a virtual character can maintain long-term personality stability, emotional coherence, and narrative consistency through a **multi-agent system architecture**.

Although users interact with Zei as a single virtual entity, the internal system separates interaction control, narrative logic, and persona conditioning into distinct modules. This project is positioned as a **practice-based research prototype**, not a finalized commercial product.

The purpose of this repository is to document the **research motivation, interaction logic, and system design assumptions** behind the prototype.

---

## 2. Problem Statement

Most existing virtual characters and chatbots rely on a single large language model to simultaneously handle:

- intent interpretation  
- logical reasoning  
- emotional tone  
- personality expression  
- memory and narrative continuity  

In long-term interaction scenarios, this single-model approach often leads to:

- personality drift  
- inconsistent emotional tone  
- broken narrative flow  
- loss of character believability  

These issues significantly reduce immersion and limit the potential of AI-driven interactive experiences, especially in applications related to companionship, service design, and narrative-based interaction.

---

## 3. Research Hypothesis

This project hypothesizes that:

> **Separating cognitive and expressive functions into a coordinated multi-agent architecture can improve long-term personality stability and narrative coherence in virtual agents.**

Rather than increasing model complexity, Project Zei explores whether **structural role separation**—combined with orchestration at the interaction layer—can serve as an effective design strategy for emotionally grounded AI interaction.

---

## 4. System Architecture Overview

Project Zei adopts a **three-module internal structure**, inspired by multi-agent coordination patterns:

### Interaction Module (Orchestrator)
- Interprets user intent  
- Manages dialogue flow  
- Integrates outputs from supporting modules into a single response  

### Narrative Logic Module (Planner)
- Maintains world rules and contextual grounding  
- Retrieves narrative memory and enforces character consistency  
- Supports multi-step reasoning for story continuity  

### Persona Conditioning Engine (Soul)
- Shapes emotional tone and stylistic expression  
- Stabilizes personality traits across interactions  
- Injects warmth and expressive nuance  

To the user, these modules remain invisible. Zei is experienced as one coherent character.

---

## 5. Current Stage and Research Boundary

Project Zei is currently at the **prototype validation stage**.

- The system demonstrates functional coordination between modules  
- Interaction stability is tested through conversational scenarios  
- Emotional tone and narrative flow are evaluated qualitatively  

At this stage, the project does **not** claim to provide a finalized solution to long-term AI companionship. Instead, it serves as a **research probe** for examining interaction structure, design assumptions, and future research directions.

---

## 6. Practice-Based Exploration Context

The prototype has been conceptually extended into experimental interaction scenarios, such as a virtual café environment (Zestory Café), to explore:

- ritual-based interaction  
- emotional engagement through repeated use  
- the role of narrative memory in service design  

These explorations focus on **interaction experience design**, rather than commercial deployment.

---

## 7. Authors & Contributions

**Yu-Hsiang Tseng**  
Interaction Design Researcher / AI System Prototyping  
- Defined the core research question on long-term personality stability in virtual agents  
- Designed the interaction logic, narrative structure, and persona modeling framework  
- Led the research-oriented system architecture and academic framing of the project  

**Brian Lin**  
Hardware Engineer / System Engineering Support  
- Contributed engineering perspectives and system-level feasibility discussions  
- Supported technical implementation considerations and hardware-oriented reasoning  

> *Project Zei is a collaborative work.  
> The research direction, interaction design focus, and academic framing presented in this repository reflect the individual research perspective of Yu-Hsiang Tseng.*

---

## 8. Future Research Direction

Aligned with the National Taipei University of Technology’s emphasis on the integration of **technology, design thinking, and human-centered interaction**, this research aims to further bridge **AI system architecture and interaction design methodology** within practical service and experiential contexts.

Future research may further explore:

- interaction rhythm and emotional feedback models  
- long-term memory structures for AI agents  
- multi-agent coordination in service design contexts  
- applications in companionship, cultural interaction, and personalized digital experiences  

These topics are intended to be developed through formal study in an interaction design graduate program.

---

## 9. Note for Reviewers

This repository is provided as **supplementary material for graduate-level review**.  
The focus is on research intent, interaction design thinking, and system architecture assumptions rather than polished product outcomes.

---

## Supplementary Materials (Prototype Reference)

The following materials are provided as supplementary references for reviewers who wish to explore the prototype context and interaction flow of Project Zei:

- Interactive Web Prototype (Zestory – Demo):  
  https://cynthia11fire.github.io/zestory/

- Extended Web Prototype (Experimental Version):  
  https://zestory.byethost11.com/

- System Demonstration Videos (YouTube):  
  https://youtu.be/LDejpkXsAVI  
  https://youtu.be/4Y9qFZHHX8U  

These materials are intended solely as supporting references.  
The primary focus of academic evaluation should remain on the design rationale and system architecture described above.
