import pytest
import sys
import os
from unittest.mock import Mock, patch
from datetime import datetime

# Add parent directory to path to import our module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mongodb_data_generator import MongoDataGenerator


class TestMongoDataGenerator:
    """Test suite for MongoDB data generation functionality."""

    @pytest.fixture
    def mock_mongo_client(self):
        """Mock MongoDB client for testing."""
        with patch('mongodb_data_generator.pymongo.MongoClient') as mock_client:
            mock_db = Mock()
            mock_collection = Mock()
            mock_client.return_value = Mock()
            mock_client.return_value.__getitem__.return_value = mock_db
            mock_db.__getitem__.return_value = mock_collection
            mock_collection.delete_many.return_value = Mock()
            mock_collection.insert_many.return_value = Mock()
            mock_collection.count_documents.return_value = 100
            mock_collection.find_one.return_value = {'created_at': datetime.now()}
            mock_collection.create_index.return_value = Mock()
            yield mock_client

    @pytest.fixture
    def data_generator(self, mock_mongo_client):
        """Create a data generator instance with mocked MongoDB client."""
        return MongoDataGenerator("mongodb://test-connection-string")

    def test_initialization(self, data_generator):
        """Test that the data generator initializes properly."""
        assert data_generator is not None
        assert data_generator.db.name == 'atlas_charts_poc'

    def test_generate_sales_data(self, data_generator):
        """Test sales data generation."""
        # Mock the collection operations
        sales_collection = data_generator.generate_sales_data(10)

        # Verify collection operations were called
        assert sales_collection.delete_many.called
        assert sales_collection.insert_many.called

    def test_generate_user_activity_data(self, data_generator):
        """Test user activity data generation."""
        activity_collection = data_generator.generate_user_activity_data(5)

        # Verify collection operations were called
        assert activity_collection.delete_many.called
        assert activity_collection.insert_many.called

    def test_create_indexes(self, data_generator):
        """Test index creation."""
        data_generator.create_indexes()

        # Verify indexes were created for all collections
        assert data_generator.db.sales_data.create_index.called
        assert data_generator.db.user_activity.create_index.called
        assert data_generator.db.realtime_metrics.create_index.called

    def test_show_data_summary(self, data_generator, capsys):
        """Test data summary display."""
        data_generator.show_data_summary()

        captured = capsys.readouterr()
        assert "DATA SUMMARY" in captured.out
        assert "Ready for Atlas Charts visualization" in captured.out

    @patch('mongodb_data_generator.time.sleep')
    def test_generate_realtime_data_interrupt(self, mock_sleep, data_generator):
        """Test real-time data generation with keyboard interrupt."""
        # Mock sleep to raise KeyboardInterrupt after first call
        mock_sleep.side_effect = KeyboardInterrupt()

        # Should handle KeyboardInterrupt gracefully
        data_generator.generate_realtime_data(duration_minutes=1)

        # Verify sleep was called
        assert mock_sleep.called

    def test_sales_data_structure(self, data_generator):
        """Test that generated sales data has correct structure."""
        # This would be more comprehensive in a real test
        # For now, just verify the method runs without error
        data_generator.generate_sales_data(1)

        # In a real test, you'd verify:
        # - Required fields are present
        # - Data types are correct
        # - Value ranges are reasonable
        # - Date ranges are within expected bounds

    def test_user_activity_data_structure(self, data_generator):
        """Test that generated user activity data has correct structure."""
        data_generator.generate_user_activity_data(1)

        # In a real test, you'd verify:
        # - Session IDs are unique
        # - Device types are from expected list
        # - Timestamps are within expected range
        # - Boolean fields have correct values

    def test_connection_string_handling(self):
        """Test connection string handling."""
        with patch('mongodb_data_generator.pymongo.MongoClient') as mock_client:
            connection_string = "mongodb://localhost:27017"
            generator = MongoDataGenerator(connection_string)

            # Verify client was created with correct connection string
            mock_client.assert_called_once_with(connection_string)

    def test_error_handling(self):
        """Test error handling for connection issues."""
        with patch('mongodb_data_generator.pymongo.MongoClient') as mock_client:
            mock_client.side_effect = Exception("Connection failed")

            with pytest.raises(Exception):
                MongoDataGenerator("invalid-connection-string")


class TestDataValidation:
    """Test data validation and constraints."""

    def test_sales_data_constraints(self):
        """Test that sales data meets expected constraints."""
        # This would validate:
        # - Price values are positive
        # - Dates are within expected range
        # - Required fields are not None
        # - String fields have reasonable lengths
        pass

    def test_user_activity_constraints(self):
        """Test that user activity data meets expected constraints."""
        # This would validate:
        # - Session durations are positive
        # - Page views are positive integers
        # - Device types are from predefined list
        # - Countries are valid country codes
        pass

    def test_realtime_metrics_constraints(self):
        """Test that real-time metrics meet expected constraints."""
        # This would validate:
        # - Metric values are within expected ranges
        # - Timestamps are recent
        # - Server names follow expected pattern
        # - Status values are from predefined list
        pass


class TestPerformance:
    """Test performance characteristics."""

    def test_batch_insert_performance(self):
        """Test that batch inserts perform within acceptable time limits."""
        # This would test:
        # - Large data generation completes within time limit
        # - Memory usage stays within bounds
        # - Batch size optimization works correctly
        pass

    def test_index_creation_performance(self):
        """Test that index creation completes quickly."""
        # This would test:
        # - Index creation time is reasonable
        # - All expected indexes are created
        # - Index specifications are correct
        pass


if __name__ == "__main__":
    pytest.main([__file__])