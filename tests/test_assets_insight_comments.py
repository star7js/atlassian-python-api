# coding=utf-8
"""Unit tests for Assets/Insight comment creation payloads."""

from unittest.mock import patch

import pytest

from atlassian.assets import AssetsCloud
from atlassian.insight import Insight


@pytest.fixture
def assets_server():
    return AssetsCloud(url="https://test.example.com", username="u", password="p", cloud=False)


@pytest.fixture
def insight_server():
    return Insight(url="https://test.example.com", username="u", password="p", cloud=False)


class TestAssetsInsightComments:
    @patch.object(AssetsCloud, "post")
    def test_assets_add_comment_uses_body(self, mock_post, assets_server):
        mock_post.return_value = {"id": 1}
        result = assets_server.add_comment_to_object("hello", object_id=42, role=0)
        mock_post.assert_called_once_with(
            "rest/assets/1.0/comment/create",
            data={"comment": "hello", "objectId": 42, "role": 0},
        )
        assert result == {"id": 1}

    @patch.object(Insight, "post")
    def test_insight_add_comment_uses_body(self, mock_post, insight_server):
        mock_post.return_value = {"id": 2}
        result = insight_server.add_comment_to_object("hello", object_id=7, role=1)
        mock_post.assert_called_once_with(
            "rest/insight/1.0/comment/create",
            data={"comment": "hello", "objectId": 7, "role": 1},
        )
        assert result == {"id": 2}
