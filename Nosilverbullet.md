# Homework 2 - No Silver Bullet
## By Carolyn Fulton
## Due January 31, 2025

### Questions

### 1. Essential Difficulties

*Definition:* intrinsic, unavoidable challenges due to the  inherent complexity of problems faced within software engineering. Problems due to the task which cannot be aided or improved upon by tools or techniques.

Brooks emphasizes that no amount of improvements in tools or practices can eliminate the core complexities of understanding, designing, and maintaining software systems as it continues to evolve.

Software complexity is a common example of this as systems become larger and more interconnected, they inherently become more difficult to design and understand, regardless of how much better your programming language or development environment is.

### 2. Accidental Difficulties

*Definition:* challenges in development from the tools, methods, and practices we use to create software and limitations within environment, languages, and processes used for development. These may be alleviated with improvement in technology but such improvements are likely to introduce new difficulties to this category.

Though these challenges present themselves through the development process due to approaches and not to the "nature" of software systems, they still significantly impact development capacity. The tools, languages, and methodologies used in software engineering along with their flaws dictate progress for developers and the field 

One example of this is programming language design which without careful consideration and design can be prone to bugs and have steep learning curves for developers. Though this has mitigated with time and improvement to such tools, it still presents itself to newer developers and in new ways with new languages.

### 3. Brooks' Four Essential Difficulties

- **Complexity:** As the need to represent real-world problems in an abstract way increases, software must account for various possibilities and edge cases which causes an exponential increase in complexity with growing systems, making it more difficult to accurately and completely represent systems.

*Example:* Modern e-commerce has grown with the introduction of things such as payment systems, recommendations, user accounts/reward systems and vast inventory management.

- **Coonformity:** There are expectations for software performance and appearance often imposed by business, external regulations, and users, which limits flexibility of software

*Example:* If it ain't broke, don't fix it! Some systems are traditionally produced along a basis idea that has been around for years to avoid user adjustment periods with introductory to new system structure.

- **Changeability:** Software systems must be designed to accommodate future changes, such as new features, bug fixes, or shifts in business needs. However, increased system flexibility in turn presents difficulty in maintaining consistency and possibly breaking existing functionality.

*Example:* A system built to track employee performance may be adapted over time as company policies evolve or new metrics are introduced but then there are difficult to implement without disrupting current structures.

- **Invisibility:** indistringuishable or unclear structure presents difficulty in building and maintaining effective software as developers attempt to understand, test and debug blindly.

*Example:* tracking how data flows across servers and debugging errors that occur in one part of the system can be challenging, especially when it's hard to visualize the interactions between all components.

### 4. Silver Bullets and Chemists

Brooks' metaphorical construct of a silver bullet dramatically imposses the desire for a singular, concise solution to all issues in software engineering and its development. As one may take care of a werewolf with one silver bullet, Brooks looks to indicate that the luxury used to kill such a mythical creature does not exist in the realm of software engineering.

Brooks argues that there does not exist a silver bullet and that there likely never will (especially from just one tool, development, or alteration in management technique) due to the inherent complexity of software engineering, the continuous evolution of the systems themselves and therefore we can only expect incremental changes to made with dedicated work towards such strides.

Brooks creates an analogy based on chemists, who primarily produce fundamental research and underlying science, and chemical engineers, who apply these principles to practical problems in design and technology. He compares this to the relationship between software engineers and computer scientists by describing the theoretical foundations originating through the work of computer scientists and the active implacation of these tools, structures and algorithms by the software engineers. This comparison communicates his point of both comparisons relate interdependent fields to one another.

### 5. Four More Important Concepts

- **Abstractions:** 

*Definition:* Simplified representaiton of complex systems, processes, or concepts which hides the underlying complexity but focuses on essential features. Helps avoid details that aren't important upon initial design

*Importance:* Management of large-scale complexities by dividing and conquering the problem(s) where the layer handles initial coordination.

- **Conversations:**

*Definition:* Communication and interaction between stakeholders to define and refine the software system’s requirements, features, and design. Stakeholders can be developers, users, product managers, and/or clients.

*Importance:* Critical to collaborative processes gaining feedback from various stages of the production of a product

- **Specification:** 

*Definition:* Details of a syetm's functional requirements (what the system should do) and non-functional requirements (how the system should perform), along with constraints, assumptions, and expectations.

*Importance:* Such provides clear direction through specifications of the project at hand and can be utilized in traceability to ensure expectations are met

- **Translation:** 

*Definition:* Process of converting a software specification or design into an executable form such as high-level requirements into source code and/or code into machine-readable formats (e.g., compiled or interpreted code).

*Importance:* Implements conceptual ideas into functioning software while concluding on specific architecture, algorithms, and data structures uses.

- **Iteration:**

*Definition:* Using repetitive cycles in code to build upon one another, forming upon a particular goal or output. Following iterations the software is reviewed, tested, and refined based on feedback and the cycle of cycles repeats.

*Importance:* Implements incremental development that is traceable if ever needed to revert and make more minor adjustments through the process to reaching the given specifications.
