---
title: "HSDIP"
date: 2024-01-31
draft: false
---

# Heuristics and Search for Domain-Independent Planning (HSDIP 2024)

ICAPS'24 Workshop \
Banff, Canada \
June 2, 2024

## Aim and Scope of the Workshop

Heuristics and search algorithms are the two key components of heuristic search, one of the main approaches to many variations of domain-independent planning, including classical planning, temporal planning, planning under uncertainty and adversarial planning. This workshop seeks to understand the underlying principles of current heuristics and search methods, their limitations, ways for overcoming those limitations, as well as the synergy between heuristics and search.

The HSDIP workshop has always been welcoming of multidisciplinary work, for example, drawing inspiration from operations research (like row and column generation algorithms), convex optimization (like gradient optimization for hybrid planning), constraint programming, or satisfiability.

The workshop is meant to be an open and inclusive forum, and we encourage papers that report on work in progress or that do not fit the mold of a typical conference paper. Non-trivial negative results are welcome to the workshop, but we expect the authors to argue for the significance of the presented results.

## Workshop Schedule

HSDIP is scheduled on the June 2.

---
[08:50 - 10:00] - **Opening & Invited Talk**
* **Opening Remarks**
* **Opportunities and Challenges for Domain-Independent Planning with Deep Reinforcement Learning** ([PDF slides](../hsdip-papers/slides-invited-talk.pdf))  
  Forest Agostinelli

---
[10:00 - 10:30] - Coffee Break

---
[10:30 - 12:00] - Session 1
* **Hitting Set Heuristics for Overlapping Landmarks in Satisficing Planning** ([PDF](../hsdip-papers/paper_14.pdf), also presented at [SoCS 2024](https://socs24.search-conference.org/))  
  Clemens Büchner, Remo Christen, Salomé Eriksson, Thomas Keller
* **Consolidating LAMA with Best-First Width Search** ([PDF](../hsdip-papers/paper_3.pdf))  
  Augusto B. Corrêa, Jendrik Seipp
* **Reasonable Landmark Orderings for Lifted Classical Planning** ([PDF](../hsdip-papers/paper_7.pdf))  
  Marcel Schubert, Julia Wichlacz, Daniel Höller
* **A Lifted Backward Computation of hAdd** ([PDF](../hsdip-papers/paper_9.pdf))  
  Pascal Lauer, Alvaro Torralba, Daniel Höller, Jörg Hoffmann
* **Gotta Catch 'Em All! Sequence Flaws in CEGAR for Classical Planning** ([PDF](../hsdip-papers/paper_17.pdf))  
  Martín Pozo, Carlos Linares Lopez, Alvaro Torralba

---
[12:00 - 13:30] - Lunch

---
[13:30 - 15:00] - Session 2
* **PDBs Go Numeric: Pattern-Database Heuristics for Simple Numeric Planning** ([PDF](../hsdip-papers/paper_13.pdf))  
  Daniel Gnad, Lee-or Alon, Eyal Weiss, Alexander Shleyfman
* **Merge-and-Shrink Heuristics for Stochastic Shortest-Path Problems with Prune Transformations**   ([PDF](../hsdip-papers/paper_16.pdf))  
  Thorsten Klößner, Alvaro Torralba, Marcel Steinmetz, Silvan Sievers
* **Crafting a Pogo Stick in Minecraft with Heuristic Search** ([PDF](../hsdip-papers/paper_15.pdf))  
  Yarin Benyamin, Argaman Mordoch, Shahaf S. Shperberg, Roni Stern
* **Cost Partitioning For Multiple Sequence Alignment** ([PDF](../hsdip-papers/paper_2.pdf))  
  Mika Skjelnes, Daniel Gnad, Jendrik Seipp
* **Comparing Rubik's Cube Solvability in Domain-Independent Planners Using Standard Planning Representations for Insights and Synergy with Upcoming Learning Methods** ([PDF](../hsdip-papers/paper_10.pdf))  
  Bharath C. Muppasani, Vishal Pallagani, Biplav Srivastava, Forest Agostinelli
* **Some Orders Are Important: Partially Preserving Orders in Top-Quality Planning** ([PDF](../hsdip-papers/paper_4.pdf), also presented at [SoCS 2024](https://socs24.search-conference.org/))  
  Michael Katz, Junkyu Lee, Jungkoo Kang, Shirin Sohrabi

---
[15:00 - 15:30] - Coffee Break

---
[15:30 - 17:00] - Session 3
* **The Bench Transition System and Stochastic Exploration** ([PDF](../hsdip-papers/paper_11.pdf), also presented at [SoCS 2024](https://socs24.search-conference.org/))  
  Dawson Tomasz, Richard A. Valenzano
* **Separate Generation and Evaluation for Parallel Greedy Best-First Search** ([PDF](../hsdip-papers/paper_8.pdf))  
  Takumi Shimoda, Alex Fukunaga
* **Expected Runtime Comparisons Between Breadth-First Search and Constant-Depth Restarting Random Walks** ([PDF](../hsdip-papers/paper_12.pdf))  
  Daniel Platnick, Richard A. Valenzano
* **Choosing a Classical Planner with Graph Neural Networks** ([PDF](../hsdip-papers/paper_6.pdf))  
  Jana Vatter, Ruben Mayer, Hans-Arno Jacobsen, Horst Samulowitz, Michael Katz
* **Metareasoning Needs Distributions: Put Up or Shut Up Games** ([PDF](../hsdip-papers/paper_5.pdf))  
  Sean Mariasin, Andrew I. Coles, Erez Karpas, Wheeler Ruml, Eyal S. Shimony, Shahaf S. Shperberg
  
---


## Invited Speaker

**Forest Agostinelli**  

**Title:** Opportunities and Challenges for Domain-Independent Planning with Deep Reinforcement Learning ([PDF slides](../hsdip-papers/slides-invited-talk.pdf))  

**Abstract:** Deep reinforcement learning has been shown to be able to learn domain-specific heuristic functions
in a largely domain-independent fashion. This has allowed practitioners to apply heuristic search to fields such 
as puzzle solving, quantum computing, and chemical reactions without domain-specific heuristic knowledge. 
Furthermore, this has led to improved performance when compared to existing domain-independent planners. However, 
analyzing deep neural networks to obtain theoretical guarantees is still an open area of research and training 
a deep neural network can take days. On the other hand, existing domain-independent planners are amenable to 
analysis and can often readily be applied to new problem instances or domains without significant computational 
overhead. In this talk, I will describe how deep reinforcement learning can be used to learn heuristic functions 
to guide heuristic search. Next, I will present ongoing research on obtaining admissible heuristic functions. Finally, 
I will give an overview of ongoing research on training deep neural networks to generalize across problem instances 
and even across domains. The code for many of these algorithms is publicly available at 
[DeepXube](https://github.com/forestagostinelli/deepxube).

**Short Bio:** Forest Agostinelli is an assistant professor at the University of South Carolina. His research 
aims to use artificial intelligence to automate the discovery of new knowledge. He looks to apply his research 
to fields such as puzzle solving, chemical synthesis, robotics, quantum computing, theorem proving, program 
synthesis, and education. He led the creation of DeepCubeA, an artificial intelligence algorithm capable of 
solving puzzles such as the Rubik’s cube without human guidance. DeepCubeA has since been applied to problems 
in quantum computing, chemical reactions, cryptography, and parking lot optimization. He earned his Ph.D. 
from the University of California, Irvine under the supervision of Professor Pierre Baldi. His homepage 
is located at [here](https://cse.sc.edu/~foresta/).


## Topics of Interest

Examples of typical topics for submissions to this workshop are:
- automatic derivation of heuristic estimators for domain-independent planning
- formal results showing equivalence or dominance between heuristics
- novel heuristic methods dealing with planning with numeric variables and effects, partial observability and non-deterministic action effects
- heuristic estimators for domain-independent planning via procedures or  suitably defined encodings of declarative descriptions of planning tasks into Satisfiability or Optimisation
- novel search techniques for domain-independent planning that explicitly aim at exploiting effectively the properties of existing heuristics
- empirical observations of synergies between heuristics and search in domain-independent planning
- challenging domains for existing combinations of heuristics and search algorithms
- applications of machine learning in heuristic search, e.g., learning heuristics, adaptive search strategies, or heuristic selection
- interesting algorithmic optimizations for the calculation of a  heuristic or the execution of a search

## Important Dates

**Submission deadline:**  
~~April 4, 2024~~ (UTC-12 timezone)

**Author feedback period:**  
~~April 22-24, 2024~~

**Notification:**  
~~April 26 2024~~

**Workshop:**  
June 2 2024

## Submission Details

The workshop will adopt a **two-track submission system** to better distinguish papers previously published at other venues (with formal proceedings) and unpublished work. Previously published papers can be submitted non-anonymously in the exact same format in which it appeared before. For unpublished work, please format submissions in AAAI style (see instructions in the Author Kit at https://www.aaai.org/authorkit24-3) and keep them to  at most 9 pages including references. The track should be indicated at submission time. Authors considering submitting to the  workshop papers rejected from the main conference, please ensure you do your  utmost to address the comments given by ICAPS reviewers. Please do not submit papers that are already accepted for the main conference to the workshop.

Submissions will be made through CMT: https://cmt3.research.microsoft.com/HSDIP2024/

The following conditions apply:

- Submissions will be double blind in general and single blind to the area chair.
- Accepted papers will be published as PDFs on the workshop webpage.
- Reviews and discussions between reviewers and organizers will be private.

Previously published papers are only assessed based on their relevance to the workshop by a member of the organizing committee and will not receive a full review. Unpublished work will be reviewed by a member of the organizing committee, and/or external reviewers selected by the organizing committee, according to the usual criteria such as relevance to the workshop, significance of the contribution, and technical quality. There will be an opportunity for a rebuttal where authors can clarify questions of the reviewers.

At least one author of each accepted paper must attend the workshop in order to present the paper.

### Policy on Previously Published Materials and Papers under Review

Submissions sent to other conferences are allowed. It is the responsibility of the authors to ensure that those venues allow for papers submitted to be already published in "informal" ways (e.g. on proceedings or websites without associated ISSN/ISBN). In particular, we welcome submissions sent to the IJCAI conference, and we aim to have the workshop submission deadline after SoCS notification.

## Workshop Committee

### Organizing Committee

**Imène Ait Abderrahim**, Khemis Miliana University, Algeria  
**Clemens Büchner**, University of Basel, Switzerland  
**Roy Fox**, University of California, Irvine, USA  
**Daniel Gnad**, Linköping University, Sweden  
**Sofia Lemons**, 2U, Maryland, USA

Contact: <hsdip@googlegroups.com>  

### Program Committee

**Imène Ait Abderrahim**, Khemis Miliana University, Algeria  
**Clemens Büchner**, University of Basel, Switzerland  
**Remo Christen**, University of Basel, Switzerland  
**Simon Dold**, University of Basel, Switzerland  
**Salomé Eriksson**, University of Basel, Switzerland  
**Roy Fox**, University of California, Irvine, USA  
**Daniel Gnad**, Linköping University, Sweden  
**Thorsten Klößner**, Saarland University, Germany  
**Pascal Lauer**, Saarland University, Germany  
**Sofia Lemons**, 2U, Maryland, USA  
**Florian Pommerening**, University of Basel, Switzerland  
**David Speck**, Linköping University, Sweden  
**Alvaro Torralba**, Aalborg University, Denmark  

