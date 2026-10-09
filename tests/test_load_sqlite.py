import pytest
from src import load_sqlite

def test_loader_fails_clearly_when_no_processed_inputs_exist(tmp_path, monkeypatch):
    monkeypatch.setattr(load_sqlite.config, "PROCESSED_DIR", tmp_path)
    with pytest.raises(FileNotFoundError, match="No processed CSV inputs"):
        load_sqlite.main()
