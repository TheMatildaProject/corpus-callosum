# Corpus Callosum
The corpus callosum (/ˈkɔːrpəs kəˈloʊsəm/; Latin for "tough body"), also known as the callosal commissure, is a wide, flat bundle of neural fibers about 10 cm long beneath the cortex in the eutherian brain at the longitudinal fissure. It connects the left and right cerebral hemispheres and facilitates interhemispheric communication. It is the largest white matter structure in the brain, consisting of 200–250 million contralateral axonal projections.

In other words, this is the application responsible for interconnecting the different micro-services that compose [Matilda](http://matilda.edwardleoni.com]). Corpus Callosum receives actions from other parts of Matilda, such as her [Auditory Cortex](https://github.com/TheMatildaProject/auditory-cortex) and prioritises them on a queue. The queue of action fires other micro-services such as the [Broca's area](https://github.com/TheMatildaProject/brocas-area), [Eye in the sky](https://github.com/TheMatildaProject/eye-in-the-sky) and etc.

## Installation

### Docker
#### Build
`docker build . -t corpus-callosum:latest`

#### Run
`docker-compose up -d`

The above command will run Corpus Callosum, a Redis server to be used as queue manager and a worker.