# Software Development Process

## [Software Development Process](https://en.wikipedia.org/wiki/Software_development_process)

### Ways to divide software development into phases

Sticking to a process aims to improve design, product management and project management. Many methodologies rely on having their own definition of deliverables and artifacts that are to be created by the team using the process.

Most modern processes are "agile" and other methodologies are waterfall (linear framework), prototyping (iterative framework), iterative and incremental development (combined linear-iterative framework), spiral development (idem), rapid application development (iterative framework), and extreme programming.

## [Scrum Methodology](https://www.mountaingoatsoftware.com/agile/scrum)

### An agile way to manage software development

Scrum leaves it up to the development team to figure how best to proceed and solve the problems they are presented. It is based on desired outcome and timeboxes called sprints. The whole team is engaged in the organization of tasks and task assignments. Artifacts generated from Scrum development are the product itself, the product backlog - functionalties to be added to the product, and burndown charts.

## [Waterfall Model](https://en.wikipedia.org/wiki/Waterfall_model)

### A Sequential design approach of engineering design

>In Royce's original waterfall model, there are these 6 following phases:
>
>* System and software requirements
>* Analysis
>* Design
>* Coding
>* Testing
>* Operations

Requirements are outlined in product requirements documents. They are then analysed to produce models, schema and business rules. These would form a framework for the software architecture. The coding phase is where development and integration happens. Finally, testing and operations go hand in hand, with the debugging of defects and the maintenance, installation of completed systems.

## [Best Coding Practices](https://en.wikipedia.org/wiki/Best_coding_practices)

### Set of informal rules to improve quality of software

#### Why?

##### Ninety-ninety rule

Tom Cargill says: "The first 90% of the code accounts for the first 90% of the development time. The remaining 10% of the code accounts for the other 90% of the development time."

#### So there is need of guidance

To prevent exceeding timetables, we stick to informal rules that allow to improve software.

#### Defining Software Quality

>According to Sommerville, software can be generalised into these attributes to qualify its quality:
>* Maintainability
>* Dependability
>* Efficiency
>* Usability

>Weinberg has these four targets when it comes to good programming:
>* Does a program meet its specifications
>* Is the program produced on schedule (and within budget)?
>* How adaptable is the program to cope with changing requirements?
>* Is the program efficient enough for the environment in which it is used?

>Hoare has these seventeen objectives to meet for good programs:
>* Clear definition of purpose
>* Simplicity of use
>* Ruggedness
>* Early availability
>* Reliability
>* Extensibility in the light of experience
>* Brevity
>* Efficiency
>* Minimum cost to develop
>* Conformity to any relevant standards
>* Clear, accurate, and precise user documents 

## [Power of 10](https://web.cecs.pdx.edu/~kimchris/cs201/handouts/The%20Power%20of%2010%20-%20Rules%20for%20Developing%20Safety%20Critical%20Code.pdf)

## Measurably improve software reliability and verifiability

The Power of 10 consists of 10 verifiable, strict and clear set of coding rules that assists in the analysis of critical software components for properties. By following the rules, runaway programs, problems relating to pointers and the dynamic allocation of memory are eliminated.

<img src="images/Power10_LL.png"
     alt="Rules chart"
     style="float: left; margin-right: 10px;" />

***

# CubeSat

## [CubeSat Wiki](https://en.wikipedia.org/wiki/CubeSat)

### A miniaturized satellite for space research

#### Facts

* 10x10x10 cubes and made of aluminum alloy.
* History: 1999, and first launched in 2003. Simplified microsatellite development.
* Launcher-payload encapsulation
* When in very LEO (low Earth orbits), radiation can be ignored. Chance of SEU (single event upset) is low.
* Handles task in parallel, attitude control, power management, payload operation, and primary control tasks.
* Mindful of tumbling. Have to detumble. Use reaction wheels (imparting moments), thrusters (imparting couples) or magnetorquers (imparting turning moment) with use of star trackers, Sun sensors, Earth sensors, *angular rate sensors* or electronic gyroscope, and GPS receivers and antennas.
* Location can be determined using on-board GPS which can be costy or relaying radar tracking data from Mission Control
* Propulsion helps slow orbital decay. Propulsion choice are all double-edged.
* Power: Needs battery controlled by a dedicated electrical power system (EPS). Pointing solar arrays.
* Telecom uses VHF, UHF, L-, S-, C- and X-band. Spring loaded antennas.

## [Cubesat Space Protocol](https://en.wikipedia.org/wiki/Cubesat_Space_Protocol)

### 