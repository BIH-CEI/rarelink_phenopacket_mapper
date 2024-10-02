Introduction
============

This Python library is intended to facilitate the process of creating and validating Phenopackets. The library provides
a set of classes and functions that can be used to create Phenopackets from any bespoke tabular format. The library is
designed to be easy to use and flexible, allowing users to create Phenopackets that conform to the GA4GH Phenopacket
schema.

To optimally use this library, it is recommended to have a basic understanding of the Phenopacket schema, what it's
purpose is, what a Phenopacket is and what it can be used for. The authors of this library have compiled a short
introduction to the schema below. However, for a deeper dive, please refer to the resources and publications on the
schema linked below.

If you are familiar with the Phenopacket schema, keep reading in the `Motivation Section`_.

Phenopackets
------------

Why Phenopackets?
~~~~~~~~~~~~~~~~~
The Phenopacket schema was designed by the Global Alliance for Genomics and Health (GA4GH) as part of an array of
coordinated, interoperable standards for genomics and healthcare. The schema is intended to provide a standardised
format for exchanging genomic, phenotypic, clinical, and other related health data according to the FAIR principles. [1]

The schema was further developed to address the need for data suitable for genotype-phenotype-correlations, machine
learning and deep phenotyping. Phenotypic information is of high clinical importance, providing insights into the
diagnosis, prognosis, and treatment of diseases. [2]

The current version of the schema is v2.

What are Phenopackets?
~~~~~~~~~~~~~~~~~~~~~~

A Phenopacket is a standardized structural format for recording data about an individual's phenotypic and genotypic
data, as well as other relevant clinical information. At its core, a Phenopacket is made up of building blocks, some of
the most important ones are listed in **Table 1** below. The schema is defined using Google's protobuf. This enables
the syntactic validation of Phenopackets and the generation of code in multiple programming languages. [3]

+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Building Block    | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+===================+====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| Individual        | The subject of the Phenopacket is represented by an Individual element. This element intends to represent an individual human or other organism. In this documentation, we explain the element using the example of a human proband in a clinical investigation.                                                                                                                                                                                                                                                                                   |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PhenotypicFeature | This element is intended to be used to describe a phenotype that characterizes the subject of the Phenopacket. For medical use cases the subject will generally be a patient or a proband of a study, and the phenotypes will be abnormalities described by an ontology such as the Human Phenotype Ontology. The word phenotype is used with many different meanings including disease entity, but in this context we mean An individual phenotypic feature, observed as either present or absent (excluded), with possible onset, and modifiers. |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Measurement       | The measurement element is used to record individual measurements. It can capture quantitative, ordinal (e.g., absent/present), or categorical measurements.                                                                                                                                                                                                                                                                                                                                                                                       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Biosample         | A Biosample refers to a unit of biological material from which the substrate molecules (e.g. genomic DNA, RNA, proteins) for molecular analyses (e.g. sequencing, array hybridisation, mass-spectrometry) are extracted. Examples would be a tissue biopsy, a single cell from a culture for single cell genome sequencing or a protein fraction from a gradient centrifugation. Several instances (e.g. technical replicates) or types of experiments (e.g. genomic array as well as RNA-seq experiments) may refer to the same Biosample.        |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Interpretation    | This message intends to represent the interpretation of a genomic analysis, such as the report from a diagnostic laboratory.                                                                                                                                                                                                                                                                                                                                                                                                                       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Disease           | The word phenotype is used with many different meanings, including “the observable traits of an organism”. In medicine, the word can be used with at least two different meanings. It is used to refer to some observed deviation from normal morphology, physiology, or behavior. In contrast, the disease is a diagnosis, i.e., an inference or hypothesis about the cause underlying the observed phenotypic abnormalities. Occasionally, physicians use the word phenotype to refer to a disease, but we do not use this meaning here.         |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MedicalAction     | This element describes medications, procedures, other actions taken for clinical management. The element is a list of options.                                                                                                                                                                                                                                                                                                                                                                                                                     |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MetaData          | This element contains structured definitions of the resources and ontologies used within the phenopacket. It is considered to be a required element of a valid Phenopacket and application Q/C software should check this.                                                                                                                                                                                                                                                                                                                         |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Table 1:** Building blocks of a Phenopacket. Definitions are taken from the `Read the Docs`_ page of the Phenopacket
schema. [10/02/2024]

.. _`Motivation Section`:

Motivation
----------

While the Phenopacket Schema is a powerful tool for representing clinical data, building Phenopackets comes with a steep
learning curve. The most suitable method of creating Phenopackets from local clinical or genomic data is to define a
mapping in a programming language such as Python or Java. This can quickly become a hurdle, as the schema defines a very
specific data format to which users need to adhere to. While this ensures computability of the data, it increases the
effort needed to produce Phenopackets.

Since the spread of the standard, more users might be interested to use it for exchanging and analyzing clinical data
available to them. However, many of those interested might be clinicians, geneticists, or other healthcare professionals
who are not familiar with programming languages. This library aims to bridge this gap by providing a simple and
intuitive way to create Phenopackets from any bespoke tabular data format. The library is designed to be intuitive and
flexible, allowing users to create Phenopackets that conform to the GA4GH Phenopacket schema.

Features
--------

TLDR
----
* Phenopackets are a data standard for exchanging bundled information on the genotype, phenotype, and other clinical data of an individual.
* Phenopackets are build to be both machine- and human-readable, and to enable analysis by SotA algorithms such as Machine Learning.
* Creating Phenopackets from local data can be a challenge, especially to non-programmers, such as clinicians.
* This library is intended to bridge the gap between the technical definition of the schema and its end users, facilitating the creation of Phenopackets.
* Features include parsing of simple and complex data types (e.g., dates or ontology concepts), automated mapping to the schema, and post-validation of the created Phenopackets.


Publications
~~~~~~~~~~~~

1. Ladewig, M. S., Jacobsen, J. O. B., Wagner, A. H., Danis, D., Kassaby, B. E., Gargano, M., Groza, T., Baudis, M., Steinhaus, R., Seelow, D., Bechrakis, N. E., Mungall, C. J., Schofield, P. N., Elemento, O., Smith, L., McMurry, J. A., Munoz‐Torres, M., Haendel, M. A., & Robinson, P. N. (2022). GA4GH Phenopackets: A Practical Introduction. Advanced Genetics, 4(1). https://doi.org/10.1002/ggn2.202200016
2. Jacobsen, J. O. B., Baudis, M., Baynam, G. S., Beckmann, J. S., Beltran, S., Buske, O. J., Callahan, T. J., Chute, C. G., Courtot, M., Danis, D., Elemento, O., Essenwanger, A., Freimuth, R. R., Gargano, M. A., Groza, T., Hamosh, A., Harris, N. L., Kaliyaperumal, R., Lloyd, K. C. K., . . . Robinson, P. N. (2022). The GA4GH Phenopacket schema defines a computable representation of clinical data. Nature Biotechnology, 40(6), 817–820. https://doi.org/10.1038/s41587-022-01357-4
3. Danis, D., Jacobsen, J. O. B., Wagner, A. H., Groza, T., Beckwith, M. A., Rekerle, L., Carmody, L. C., Reese, J., Hegde, H., Ladewig, M. S., Seitz, B., Munoz-Torres, M., Harris, N. L., Rambla, J., Baudis, M., Mungall, C. J., Haendel, M. A., & Robinson, P. N. (2023). Phenopacket-tools: Building and validating GA4GH Phenopackets. PLoS ONE, 18(5), e0285433. https://doi.org/10.1371/journal.pone.0285433
4. Danis, D., Bamshad, M. J., Bridges, Y., Cacheiro, P., Carmody, L. C., Chong, J. X., Coleman, B., Dalgleish, R., Freeman, P. J., Graefe, A. S. L., Groza, T., Jacobsen, J. O. B., Klocperk, A., Kusters, M., Ladewig, M. S., Marcello, A. J., Mattina, T., Mungall, C. J., Munoz-Torres, M. C., . . . Robinson, P. N. (2024). A corpus of GA4GH Phenopackets: case-level phenotyping for genomic diagnostics and discovery. medRxiv (Cold Spring Harbor Laboratory). https://doi.org/10.1101/2024.05.29.24308104


Resources
~~~~~~~~~~~~

a. `Phenopackets Website`_
b. GitHub_
c. `Read the Docs`_
d. `GA4GH`_

.. _`Phenopackets Website`: http://phenopackets.org/
.. _GitHub: https://github.com/phenopackets
.. _`Read the Docs`: https://phenopacket-schema.readthedocs.io/en/latest/
.. _`GA4GH`: https://www.ga4gh.org/product/phenopackets/

