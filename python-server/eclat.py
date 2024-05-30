def eclat(matrix, min_support):
    def eclat_recursive(prefix, items, min_support, frequent_itemsets):
        while items:
            i, itids = items.pop()
            new_prefix = prefix + [i]
            frequent_itemsets.append((new_prefix, len(itids)))
            new_items = []
            for j, jtids in items:
                intersection = itids & jtids
                if len(intersection) >= min_support:
                    new_items.append((j, intersection))
            eclat_recursive(new_prefix, new_items, min_support, frequent_itemsets)

    # Convert matrix to a list of sets
    transactions = [set(row) for row in matrix]
    
    # Create initial items with their transaction ids
    item_tidsets = {}
    for tid, transaction in enumerate(transactions):
        for item in transaction:
            if item not in item_tidsets:
                item_tidsets[item] = set()
            item_tidsets[item].add(tid)
    
    # Filter items by minimum support
    items = [(item, tidset) for item, tidset in item_tidsets.items() if len(tidset) >= min_support]
    
    # Sort items to ensure deterministic output
    items = sorted(items, key=lambda x: len(x[1]), reverse=True)
    
    frequent_itemsets = []
    eclat_recursive([], items, min_support, frequent_itemsets)
    
    return frequent_itemsets