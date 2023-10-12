def is_eligible_to_vote(age):
  """Returns True if the given age is eligible to vote, False otherwise."""
  return age >= 18

# Example usage:
print(is_eligible_to_vote(17))  # False
print(is_eligible_to_vote(18))  # True
print(is_eligible_to_vote(19))  # True
