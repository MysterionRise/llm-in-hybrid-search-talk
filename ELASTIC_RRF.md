
# Creating an Index with Mapping

```
PUT test-index
{
  "mappings": {
    "properties": {
      "text": {
        "type": "text"
      },
      "embeddings": {
        "type": "dense_vector",
        "dims": 3,
        "index": true,
        "similarity": "l2_norm"
      },
      "price": {
        "type": "integer"
      }
    }
  }
}
```
This block defines an Elasticsearch index named `test-index`. It specifies the mapping, which is the schema describing the data in the index. The mapping includes three fields: `text`, `embeddings`, and `price`. The `text` field is of type `text`, suitable for full-text search. The `embeddings` field is a `dense_vector` of dimension 3, which will be used for similarity search and is set to use L2 normalization. The `price` field is an integer, indicating the cost of an item.

# Inserting Documents

```
PUT test-index/_doc/1
{
    "text" : "T-shirt",
    "embeddings" : [5, -1, 3],
    "price": 50
}
```

```
PUT test-index/_doc/2
{
    "text" : "Adidas t-shirt",
    "embeddings" : [-1, 3, 4],
    "price": 75
}
```

```
PUT test-index/_doc/3
{
    "text" : "awesome t-shirt shirt T-shirt",
    "embeddings" : [2, 5, 3],
    "price": 10
}
```

```
PUT test-index/_doc/4
{
    "text" : "T-shirt",
    "price": 50
}
```

```
PUT test-index/_doc/5
{
    "embeddings" : [5, -1, 3],
    "price": 50
}
```


# Executing a Search Query

```
GET test-index/_search
{
  "query": {
    "term": {
      "text": "awesome t-shirt"
    }
  },
  "knn": {
    "field": "embeddings",
    "query_vector": [
      2,
      4,
      3
    ],
    "k": 5,
    "num_candidates": 5
  },
  "rank": {
    "rrf": {
      "window_size": 5,
      "rank_constant": 1
    }
  },
  "size": 3,
  "aggs": {
    "price": {
      "terms": {
        "field": "price"
      }
    }
  }
}
```

This block represents a search query against `test-index`.
It combines a term query for "awesome t-shirt" with a k-nearest neighbor (KNN) query using a query vector, indicating the search for the top 5 nearest vectors. It also applies reciprocal rank fusion (RRF) for ranking results within a window of 5. The search is limited to the top 3 results (`"size": 3`) and includes an aggregation on the `price` field.
