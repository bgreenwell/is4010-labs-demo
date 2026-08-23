import pytest
import json
import os
import tempfile
from week08.favorites import FavoritesManager

# Fixture to create a temporary favorites file
@pytest.fixture
def temp_favorites_file():
    # Create a temp file
    fd, path = tempfile.mkstemp()
    os.close(fd)
    
    # Return the path to the test
    yield path
    
    # Cleanup after test
    if os.path.exists(path):
        os.remove(path)

# Fixture for the manager using the temp file
@pytest.fixture
def manager(temp_favorites_file):
    return FavoritesManager(temp_favorites_file)

def test_add_favorite(manager):
    """Test adding a new favorite."""
    assert manager.add("home", "Cincinnati, OH") is True
    assert manager.get_location("home") == "Cincinnati, OH"

def test_add_duplicate_favorite(manager):
    """Test adding a duplicate favorite returns False."""
    manager.add("home", "Cincinnati, OH")
    assert manager.add("home", "New York, NY") is False
    # Should still be original
    assert manager.get_location("home") == "Cincinnati, OH"

def test_remove_favorite(manager):
    """Test removing an existing favorite."""
    manager.add("work", "Columbus, OH")
    assert manager.remove("work") is True
    assert manager.get_location("work") is None

def test_remove_nonexistent_favorite(manager):
    """Test removing a favorite that doesn't exist."""
    assert manager.remove("nonexistent") is False

def test_list_all_favorites(manager):
    """Test listing all favorites."""
    manager.add("home", "Cincinnati")
    manager.add("work", "Columbus")
    
    favorites = manager.list_all()
    assert len(favorites) == 2
    assert "home" in favorites
    assert "work" in favorites
    assert favorites["home"] == "Cincinnati"

def test_case_insensitive_lookup(manager):
    """Test that lookups are case-insensitive."""
    manager.add("Home", "Cincinnati")
    assert manager.get_location("home") == "Cincinnati"
    assert manager.get_location("HOME") == "Cincinnati"

def test_persistence(temp_favorites_file):
    """Test that data persists between manager instances."""
    # First manager saves data
    mgr1 = FavoritesManager(temp_favorites_file)
    mgr1.add("vacation", "Hawaii")
    
    # Second manager loads data
    mgr2 = FavoritesManager(temp_favorites_file)
    assert mgr2.get_location("vacation") == "Hawaii"

def test_load_corrupted_file(temp_favorites_file):
    """Test handling of corrupted JSON file."""
    with open(temp_favorites_file, 'w') as f:
        f.write("{invalid json")
    
    # Should not crash, just start empty
    mgr = FavoritesManager(temp_favorites_file)
    assert len(mgr.list_all()) == 0

def test_load_non_existent_file(temp_favorites_file):
    """Test loading when file doesn't exist."""
    if os.path.exists(temp_favorites_file):
        os.remove(temp_favorites_file)
        
    # Should create new empty state without error
    mgr = FavoritesManager(temp_favorites_file)
    assert len(mgr.list_all()) == 0
