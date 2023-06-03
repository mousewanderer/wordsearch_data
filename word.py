def word_search(doc_list, keyword):
  indices = [] 
  for i, doc in enumerate(doc_list):
    tokens = doc.split()
    normalized = [token.rstrip('.,').lower() for token in tokens]
    if keyword.lower() in normalized:
      indices.append(i)
  return indices

def multi_word_search(doc_list, keywords):
  keyword_to_indices = {}
  for keyword in keywords:
    keyword_to_indices[keyword] = word_search(documents, keyword)
  return keyword_to_indices
  
  def multi_word_search(documents, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(documents, keyword)
    return keyword_to_indices
