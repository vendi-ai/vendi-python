import json

import pytest
from requests import HTTPError

from conftest import vendi_client
from vendi.datasets.schema import Dataset


def test_upload_dataset_get_load_and_delete_it(vendi_client):
    with open("data/conversation.jsonl", "r") as f:
        data_jsonl = [json.loads(jline) for jline in f.read().splitlines()]

    dataset_id = vendi_client.datasets.upload(data=data_jsonl, name="my_dataset", dataset_type="conversation")
    assert dataset_id is not None
    assert isinstance(dataset_id, Dataset)

    dataset = vendi_client.datasets.get(dataset_id.id)

    uploaded_data = dataset.load_data()
    assert len(uploaded_data) == len(data_jsonl)
    vendi_client.datasets.delete(dataset_id.id)

    with pytest.raises(HTTPError) as exc:
        vendi_client.datasets.get(dataset_id.id)
    assert exc.value.response.status_code == 404
