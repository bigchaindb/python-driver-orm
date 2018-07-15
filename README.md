# python-driver-orm

Orm implementation of official python driver

> A CRAB-based python ORM for BigchainDB.

[![Build Status](https://travis-ci.org/bigchaindb/python-driver-orm.svg?branch=master)](https://travis-ci.org/bigchaindb/python-driver-orm)

CRAB is the CRUD model in databases applied to blockchains:

| Database   | Blockchain   |
| ---------- | ------------ |
| **C**reate | **C**reate   |
| **R**ead   | **R**etrieve |
| **U**pdate | **A**ppend   |
| **D**elete | **B**urn     |

## Table of Contents

-   [Setup](#setup)
-   [Usage](#usage)
-   [Examples](#examples)
    -   [Create an asset](#example-create-an-asset)
    -   [Retrieve assets](#example-retrieve-assets)
    -   [Append a transaction](#example-append-a-transaction)
    -   [Burn an asset](#example-burn-an-asset)
-   [License](#license)

## Setup

```bash
$ pip install bigchaindb_orm
```

## Usage

```python
from bigchaindb_orm import Orm

bdb_orm = Orm('https://test.bigchaindb.com', {
    'app_id': '',
    'app_key': ''
})

# define( < model name > , < additional information > )
# < model name >: represents the name of model you want to store
# < additional inf. >: any information you want to pass about the model (can be string or object)
# note: cannot be changed once set!
bdb_orm.define("myModel", "https://schema.org/v1/myModel")

# generate keypair
alice = Orm.keypair()
```

## Examples

All examples need bdb_orm initialized as described in usage

### Example: Create an asset

```python
# from the defined models in our bdb_orm we create an asset with Alice as owner
asset = bdb_orm.models.myModel.create({
    'data': {'name': 'Zero'},
    'keypair': alice
})

# asset is an object with all our data and functions
# asset.id equals the id of the asset
# asset.data is data of the last (unspent) transaction
# asset.tx_history gives the full raw transaction history
# Note: Raw transaction history has different object structure then asset. You can find specific data change in metadata property.
print(asset.id)
```

### Example: Retrieve assets

```python
# get all objects with retrieve()
# or get a specific object with retrieve(object.id)
assets = bdb_orm.models.myModel.retrieve()
for asset in assets:
    print(asset.id)
```

## License

```
Copyright 2018 BigchainDB GmbH

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
