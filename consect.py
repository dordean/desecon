# Assuming parse_knowledge function is defined as follows
def parse_knowledge(root, section):
    return root[section]

# Example usage
root_data = {
    'eligibility': {
        'minimum_age': 18,
        'other_criteria': '...'
    }
}

eligibility_minimum_age = parse_knowledge(root_data, 'eligibility')['minimum_age']
print(eligibility_minimum_age)  # Output: 18
