def expected_dominant_offspring(couples):
    # Probability of dominant phenotype for each pairing
    dominant_probs = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    
    # Expected dominant offspring per pairing = 2 * couples * dominant probability
    expected_dominants = sum(2 * couples[i] * dominant_probs[i] for i in range(6))
    
    return expected_dominants