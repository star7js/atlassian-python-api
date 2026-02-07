# coding=utf-8
"""Unit tests for StatusPage component group endpoints."""

from unittest.mock import patch

import pytest

from atlassian.statuspage import StatusPage


@pytest.fixture
def statuspage():
    return StatusPage(url="https://status.example.com", token="test-token")


class TestStatusPageComponentGroups:
    @patch.object(StatusPage, "post")
    def test_page_create_component_group(self, mock_post, statuspage):
        mock_post.return_value = {"id": "cg1"}
        result = statuspage.page_create_component_group(
            page_id="page1",
            description="desc",
            components_group={"name": "Group", "components": ["c1"]},
        )
        mock_post.assert_called_once_with(
            "v1/pages/page1/component-groups",
            data={"description": "desc", "components_group": {"name": "Group", "components": ["c1"]}},
        )
        assert result == {"id": "cg1"}

    @patch.object(StatusPage, "get")
    def test_page_get_list_of_component_groups(self, mock_get, statuspage):
        mock_get.return_value = [{"id": "cg1"}]
        result = statuspage.page_get_list_of_component_groups(page_id="page1", per_page=50, page=2)
        mock_get.assert_called_once_with(
            "v1/pages/page1/component-groups",
            params={"per_page": 50, "page": 2},
        )
        assert result == [{"id": "cg1"}]

    @patch.object(StatusPage, "get")
    def test_page_get_component_group(self, mock_get, statuspage):
        mock_get.return_value = {"id": "cg1"}
        result = statuspage.page_get_component_group(page_id="page1", component_group_id="cg1")
        mock_get.assert_called_once_with("v1/pages/page1/component-groups/cg1")
        assert result == {"id": "cg1"}

    @patch.object(StatusPage, "patch")
    def test_page_update_component_group(self, mock_patch, statuspage):
        mock_patch.return_value = {"id": "cg1"}
        result = statuspage.page_update_component_group(
            page_id="page1",
            component_group_id="cg1",
            description="desc",
            component_group={"name": "Group"},
        )
        mock_patch.assert_called_once_with(
            "v1/pages/page1/component-groups/cg1",
            data={"description": "desc", "component_group": {"name": "Group"}},
        )
        assert result == {"id": "cg1"}

    @patch.object(StatusPage, "delete")
    def test_page_delete_component_group(self, mock_delete, statuspage):
        mock_delete.return_value = {"deleted": True}
        result = statuspage.page_delete_component_group(page_id="page1", component_group_id="cg1")
        mock_delete.assert_called_once_with("v1/pages/page1/component-groups/cg1")
        assert result == {"deleted": True}

    @patch.object(StatusPage, "get")
    def test_page_get_component_group_uptime(self, mock_get, statuspage):
        mock_get.return_value = {"uptime": 99.9}
        result = statuspage.page_get_uptime_for_component_group(
            page_id="page1",
            component_group_id="cg1",
            start="2025-01-01",
            end="2025-01-31",
        )
        mock_get.assert_called_once_with(
            "v1/pages/page1/component-groups/cg1/uptime",
            params={"start": "2025-01-01", "end": "2025-01-31"},
        )
        assert result == {"uptime": 99.9}
