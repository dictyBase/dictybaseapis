# dictyBase APIs

[![License](https://img.shields.io/badge/License-BSD%202--Clause-blue.svg)](LICENSE)
![Buf](https://github.com/dictyBase/dictybaseapis/workflows/Buf/badge.svg)
[![Funding](https://badgen.net/badge/Funding/NIH%2C%20Rex%20L%20Chisholm%20Lab/yellow)](https://reporter.nih.gov/project-details/10024726)

Protocol Buffer definitions for dictyBase's gRPC APIs. Used to generate client libraries, 
server stubs, and documentation.

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
   - `UpdateFeatureAnnotation`: Updates an existing feature annotation
   - `DeleteFeatureAnnotation`: Deletes a feature annotation
   - `AddTag`: Adds a tag property to a feature annotation
   - `UpdateTag`: Updates an existing tag property
   - `RemoveTag`: Removes a tag property from a feature annotation

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
