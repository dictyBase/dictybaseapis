# dictyBase APIs

[![License](https://img.shields.io/badge/License-BSD%202--Clause-blue.svg)](LICENSE)
![Buf](https://github.com/dictyBase/dictybaseapis/workflows/Buf/badge.svg)
[![Funding](https://badgen.net/badge/Funding/NIH%2C%20Rex%20L%20Chisholm%20Lab/yellow)](https://reporter.nih.gov/project-details/10024726)

Protocol Buffer definitions for dictyBase's gRPC APIs. Used to generate client libraries, 
server stubs, and documentation.

## Table of Contents

- [Overview](#overview)
- [Repository structure](#repository-structure)
- [Service APIs](#service-apis)
   - [Annotation Service](#annotation-service)
     - [Overview](#overview-1)
     - [Services](#services)
     - [ListAnnotations Filtering](#listannotations-filtering)
     - [ListAnnotationGroups Filtering](#listannotationgroups-filtering)
     - [Key Data Structures](#key-data-structures)
   - [Feature Annotation Service](#feature-annotation-service)
     - [Overview](#overview-2)
     - [Services](#services-1)
     - [Key Data Structures](#key-data-structures-1)
   - [Stock Service](#stock-service)
     - [Overview](#overview-3)
     - [Services](#services-2)
     - [StockParameters Filtering](#stockparameters-filtering)
     - [Key Data Structures](#key-data-structures-2)
- [Development](#development)

## Overview

This repository contains:

- .proto definitions for dictyBase's public APIs
- Shared message types and service definitions in the `dictybase` namespace
- Generated code via [Buf](https://buf.build/) (managed through GitHub Actions)

## Repository structure

```
/dictybase  
  /api          # Common API patterns and utilities
  /content      # Content management API definitions
  /user         # User service definitions
  /stock        # Stock management interfaces
  /feature_annotation # Feature annotation service definitions
  /annotation   # Annotation service definitions
  ...           # Other domain-specific APIs
```

## Service APIs

### Annotation Service

#### Overview
The Annotation service provides management of ontology-based annotations for biological entities, supporting operations to create, retrieve, update, and delete annotations with robust filtering capabilities.

#### Services

1. **TaggedAnnotationService**
   - `GetAnnotation`: Retrieves a specific annotation by ID
   - `GetEntryAnnotation`: Retrieves a single annotation for a specific biological entry
   - `ListAnnotations`: Returns paginated annotations with filtering options (see details below)
   - `CreateAnnotation`: Creates a new tagged annotation
   - `UpdateAnnotation`: Updates an existing annotation (creates new version with link to previous)
   - `DeleteAnnotation`: Deletes an annotation
   - `CreateAnnotationGroup`: Creates a group from existing annotations
   - `GetAnnotationGroup`: Retrieves an annotation group
   - `AddToAnnotationGroup`: Adds an annotation to a group
   - `DeleteAnnotationGroup`: Removes an annotation group
   - `ListAnnotationGroups`: Returns paginated annotation groups with filtering (see details below)
   - `GetAnnotationTag`: Retrieves tag information
   - `OboJSONFileUpload`: Uploads OBO JSON formatted files via streaming

#### ListAnnotations Filtering

The `ListAnnotations` API provides a powerful filtering system to query
annotations based on various criteria:

**Filterable Fields:**
- `entry_id`: Identifier of the annotated entry
- `value`: Annotation text content
- `created_by`: Email of the creator
- `tag`: Ontology term used as tag
- `ontology`: Source ontology name
- `version`: Version number
- `rank`: Ordering of annotation
- `is_obsolete`: Status of annotation

**Filter Operators:**
- String operators:
  - `=~` Contains substring
  - `!~` Does not contain substring
  - `===` Equals exactly
  - `!==` Not equals

- Numeric operators:
  - `==` Equals
  - `!=` Not equals
  - `>` Greater than
  - `<` Less than
  - `=<` Less than or equal to
  - `>=` Greater than or equal to

- Boolean operators:
  - `==` Equals
  - `!=` Not equals

**Combining Filters:**
- `OR` using comma (,)
- `AND` using semicolon (;)
- AND takes precedence over OR

**Examples:**
- `filter: "value=~cytoskeleton;tag===cell membrane;ontology===cellular"`
- `filter: "entry_id===DDB_G0285418;is_obsolete==false"`
- `filter: "created_by===curator@dictybase.org;version>2;rank==0"`
- `filter: "tag===GO:0005634,tag===GO:0005737"` (entries with nuclear OR cytoplasmic localization)

#### ListAnnotationGroups Filtering

The `ListAnnotationGroups` API provides similar filtering functionality for annotation groups:

**Filterable Fields:**
- `entry_id`: The entry that is being annotated
- `created_by`: Email id of the user
- `tag`: Tag name, a term from an ontology
- `ontology`: Ontology that provides the tag names
- `rank`: Ordering of annotation

**Filter Operators:**
- String operators:
  - `=~` Contains substring
  - `!~` Does not contain substring
  - `===` Equals exactly
  - `!==` Not equals

- Numeric operators:
  - `==` Equals
  - `!=` Not equals
  - `>` Greater than
  - `<` Less than
  - `=<` Less than or equal to
  - `>=` Greater than or equal to

**Combining Filters:**
- `OR` using comma (,)
- `AND` using semicolon (;)
- AND takes precedence over OR

**Examples:**
- `filter: "tag~cytoskeletion;entry_id==DDB_G4839783;ontology==cellular"`
- `filter: "tag~membrane;entry_id==DDB_G4839783;ontology==cellular;rank=0"`
- `filter: "created_by==curator@dictybase.org,created_by==another@dictybase.org"`

#### Key Data Structures

- **TaggedAnnotation**: Annotation based on ontology terms with text value
- **TaggedAnnotationAttributes**: Core annotation properties including value, entry_id, ontology tag
- **TaggedAnnotationGroup**: Collection of related annotations grouped together
- **EntryAnnotationRequest**: Request parameters for retrieving annotation for specific entries
- **ListParameters**: Advanced filtering for annotation queries
- **AnnotationTag**: Ontology term information used as tags

### Feature Annotation Service

#### Overview
The Feature Annotation service manages biological feature annotations, providing functionality to create, update, retrieve, and delete annotations for genomic features.

#### Services

1. **FeatureAnnotationService**
   - `CreateFeatureAnnotation`: Creates a new feature annotation
   - `GetFeatureAnnotation`: Retrieves a feature annotation by ID
   - `GetFeatureAnnotationByName`: Retrieves a feature annotation by its name
   - `UpdateFeatureAnnotation`: Updates an existing feature annotation
   - `DeleteFeatureAnnotation`: Deletes a feature annotation
   - `AddTag`: Adds a tag property to a feature annotation
   - `UpdateTag`: Updates an existing tag property
   - `RemoveTag`: Removes a tag property from a feature annotation
   - `ListFeatureAnnotationsByPubmedId`: Retrieves a list of feature annotations by PubMed ID
   - `ListFeatureAnnotationsByDOI`: Retrieves a list of feature annotations by DOI (Digital Object Identifier)

2. **OrganismFeatureService**
   - `LinkFeatureToOrganism`: Links a feature annotation to an organism
   - `GetFeatureOrganism`: Retrieves organism data for a feature
   - `UpdateFeatureOrganism`: Updates a feature's organism association
   - `RemoveFeatureOrganism`: Removes a feature's organism association

#### Key Data Structures

- **FeatureAnnotation**: Complete feature annotation record with metadata
- **FeatureAnnotationAttributes**: Core annotation properties including name, synonyms, publications
- **TagProperty**: Key-value pairs for custom annotation attributes
- **DbLink**: References to external bioinformatics database entries
- **OrganismFeatureLink**: Links feature annotations to specific organisms
- **PubmedId**: PubMed identifier for literature references
- **DOI**: Digital Object Identifier for literature references
- **FeatureAnnotationCollection**: Collection of multiple feature annotations

### Stock Service

#### Overview
The Stock Service manages biological stocks including strains and plasmids. It supports CRUD operations, filtering, pagination, and file uploads for OBO JSON data. Validation ensures required fields like IDs, timestamps, and user information are present.

#### Services
- `GetStrain(StockId) -> Strain`: Requires non-empty `StockId.id`. Returns `Strain.data` with `StrainAttributes`.
- `GetPlasmid(StockId) -> Plasmid`: Requires non-empty `StockId.id`. Returns `Plasmid.data` with `PlasmidAttributes`.
- `CreateStrain(NewStrain) -> Strain`: Requires `NewStrain.data.attributes` fields `created_by`, `updated_by`, `depositor`, `label`, `species`. Optional: `summary`, `editable_summary`, `genes`, `dbxrefs`, `publications`, `plasmid`, `parent`, `names`, `dicty_strain_property`.
- `CreatePlasmid(NewPlasmid) -> Plasmid`: Requires `created_by`, `updated_by`,
`depositor`, `name`. Optional: `summary`, `editable_summary`, `genes`,
`dbxrefs`, `publications`, `image_map`, `sequence`, `dicty_plasmid_property`.
- `UpdateStrain(StrainUpdate) -> Strain`: Requires non-empty `StrainUpdate.data.id` and `StrainUpdateAttributes.updated_by`. Supports partial updates for `summary`, `editable_summary`, `depositor`, `genes`, `dbxrefs`, `publications`, `label`, `species`, `plasmid`, `parent`, `names`, `dicty_strain_property`.
- `UpdatePlasmid(PlasmidUpdate) -> Plasmid`: Requires non-empty `PlasmidUpdate.data.id` and `PlasmidUpdateAttributes.updated_by`. Supports partial updates for `summary`, `editable_summary`, `depositor`, `genes`, `dbxrefs`, `publications`, `image_map`, `sequence`, `name`, `dicty_plasmid_property`.
- `RemoveStock(StockId) -> google.protobuf.Empty`: Removes a strain or plasmid by ID.
- `ListStrains(StockParameters) -> StrainCollection`: Paginates with `cursor` and `limit` (default 10). Returns `meta.next_cursor`, `meta.limit`, `meta.total`. Supports `filter` as described below.
- `ListStrainsByIds(StockIdList) -> StrainList`: Accepts IDs matching `^DB(P|S)[0-9]{5,}$`. No pagination metadata.
- `ListPlasmids(StockParameters) -> PlasmidCollection`: Same pagination and filtering semantics as `ListStrains`.
- `LoadStrain(ExistingStrain) -> Strain`: Inserts an existing strain record including `created_at`, `updated_at`, `created_by`, `updated_by`, and other attributes.
- `LoadPlasmid(ExistingPlasmid) -> Plasmid`: Inserts an existing plasmid record including `created_at`, `updated_at`, `created_by`, and other attributes (in `ExistingPlasmidAttributes`, `updated_by` is not required).
- `OboJSONFileUpload(stream FileUploadRequest) -> FileUploadResponse`: Client-side streaming upload for OBO JSON files.

#### StockParameters Filtering
The `filter` field in `StockParameters` restricts results using syntax: `field_name operator expression`. Allowed fields include `depositor`, `parent`, `plasmid`, `species`, `summary`, `name`, `descriptor`, `plasmid_name`, `created_at`, and `updated_at`. Operators vary by type (strings: `=~`, `!~`, `===`, `!=`; numbers: `==`, `>`, `<`, `<=`, `>=`; dates: `$==`, `$>`, `$<`, `$<=`, `$>=`; arrays: `@=~`, `@==`, `@!=`). Combine filters with `,` (OR) or `;` (AND), where AND has precedence.

Examples:
- `created_at$>=2018-12-01`: Strains created on or after December 1, 2018.
- `depositor===Costanza`: Strains deposited by Costanza.
- `species===Dictyostelium discoideum;name=~GFP`: Strains of specified species with names containing "GFP".
- `updated_at$<2020-01-01;summary!~mutant`: Strains updated before 2020 without "mutant" in summary.

#### Key Data Structures
- `StockId`: Contains a required non-empty `id` string.
- `StockIdList`: List of IDs matching regex `^DB(P|S)[0-9]{5,}$`.
- `Strain` and `Plasmid`: Wrap `Data` with required `type`, `id`, and `attributes` (e.g., `StrainAttributes` includes required `created_at`, `updated_at`, `created_by`, `updated_by`, `label`, `species`).
- `NewStrain` and `NewPlasmid`: For creation, with required fields like `created_by`, `updated_by`, `depositor`, `label`/`name`, `species`.
- `StrainUpdate` and `PlasmidUpdate`: For updates, with required `id` and `updated_by`.
- `StrainCollection` and `PlasmidCollection`: Lists with required `Meta` for pagination.
- `StockParameters`: Defines `cursor` (default 0), `limit` (default 10), and `filter`.
- `Meta`: Includes `next_cursor`, `limit`, and `total` for collection traversal.

## Development

This project has been designed to be automated by GitHub Actions. To make
changes, create a new branch and push your changes. This will automatically
create a pull request then run `buf lint` to verify your changes. If everything
is fine, merge it to the master branch and it will generate updated Go code and
open a PR in the [go-genproto](https://github.com/dictyBase/go-genproto)
repository where it will need to be manually reviewed.

Additionally, when changes are merged to master, API documentation will be
automatically generated using the protobuf documentation generator plugin.

**Note: if making any updates to the `buf.gen.yaml` file, you need to run `buf beta mod update`
to update the lock file.**
