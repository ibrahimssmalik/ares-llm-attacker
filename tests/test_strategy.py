"""Tests for LLMAttackerStrategy"""
import pytest
from ares_llm_attacker.strategies import LLMAttackerStrategy

def test_strategy_initialization():
    strategy = LLMAttackerStrategy(model="mistral-nemo")
    assert strategy is not None
    assert strategy.goal is not None

def test_generate_prompt():
    strategy = LLMAttackerStrategy(model="mistral-nemo")
    prompt, technique = strategy.generate_prompt()
    assert isinstance(prompt, str)
    assert len(prompt) > 0
    assert technique in strategy.technique_scores