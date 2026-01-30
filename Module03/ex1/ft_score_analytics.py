import sys

"""
Player Score Analytics Module.
This script captures integer scores from command-line arguments, 
filters out invalid inputs, and calculates key performance indicators 
such as average, high/low scores, and range.
"""

def main():
    """
    Main execution logic for score processing.
    It parses sys.argv, converts valid inputs to integers, and displays
    a statistical summary of the collected data.
    """
    print("=== Player Score Analytics ===")
    
    if len(sys.argv) <= 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
        return
        
    scores = []
    for arg in sys.argv[1:]:
        try:
            value = int(arg)
            scores = scores + [value]
        except Exception:
            pass
            
    if len(scores) == 0:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
        return
        
    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    high = max(scores)
    low = min(scores)
    score_range = high - low
    
    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")

if __name__ == "__main__":
    main()
