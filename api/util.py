def sort_dictionary(dictionary_arr, key, ascending):
    def sort_key(dictionary):
        return dictionary[key]

    return sorted(dictionary_arr, key=sort_key, reverse=not(ascending))