# tests/test_models.py
import torch

def test_model_output_shape():
    model = MyModel()
    dummy_input = torch.randn(1, 3, 224, 224)  # Example input
    output = model(dummy_input)
    assert output.shape == (1, 10)  # Check output shape