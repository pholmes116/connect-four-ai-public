# Comparative Study of AI Algorithms for Connect Four

We developed and compared three AI agents (Monte Carlo Tree Search, Alpha-Beta Pruning, and Alpha-Beta with evaluation) for the game of Connect Four. Testing on both the standard board and rule variations, our experiments highlight tradeoffs between accuracy, efficiency, and adaptability, with Alpha-Beta plus evaluation performing strongest overall.

## Authors

Peter Holmes, Freya Nagel, Yonatan Paserman, Rebecca Wilhelmi

## Overview

This project evaluates three classical AI approaches to the game Connect Four:
- Monte Carlo Tree Search (MCTS)
- Alpha-Beta Pruning (AB)
- Alpha-Beta Pruning with a heuristic evaluation function (ABE)

We compared these algorithms on the standard 7×6 board as well as under modified game rules: different board sizes, a third player, and blocker stones. Performance was measured in terms of win percentage and average move time, with hyperparameter tuning conducted to balance efficiency and accuracy

## Project Structure

.\
├── code/\
│   ├── aima_python_master/\
│   └── connect4_ai_comparison.ipynb\
├── Papers/\
│   ├── A knowledge-based approach of connect 4.pdf\
│   ├── AI Connect Four Agent.pdf\
│   ├── Artificial Intelligence-Based Connect 4 Player Using Python.pdf\
│   ├── Comparison_of_Four_AI_Algorithms_in_Connect_Four.pdf\
│   ├── Implementing Artificial Intelligence Agent Within Connect Four.pdf\
│   ├── SOLVING CONNECT 4 USING OPTIMIZED MINIMAX AND MONTE CARLO TREE SEARCH.pdf\
│   └── Tommy_2017_IOP_Conf._Ser.__Mater._Sci._Eng._190_012044.pdf\
├── Report.pdf\
└── README.md

## Methods

- **Game environment**: Custom Connect Four implementation (built on AIMA-Python) with flexible rules for variants.
- **Algorithms**: MCTS with variable simulation counts and Alpha-Beta pruning with/without heuristic evaluation.
- **Experiments**:
  - Hyperparameter tuning on the standard 7×6 board.
  - Tournament-style evaluations across all algorithms.
  - Variants tested: different board sizes (4×4, 10×10, 2×15), 3-player version, and blocker stones.

## Findings

- **Standard board**: ABE consistently outperformed AB and MCTS in win rate.
- **Rule variations**: ABE was the most adaptable, winning across different board sizes, 3-player games, and blocker stone settings.
- **Tradeoffs**:
  - MCTS excelled in exploratory play but was computationally expensive.
  - Alpha-Beta with evaluation achieved faster decisions and maintained strong win rates.
- **Conclusion**: A hybrid approach combining MCTS (exploration) and Alpha-Beta (efficient exploitation) could be most effective in complex environments.

## Contact

For questions or contributions, reach out via GitHub Issues or email pholmes116@gmail.com.
