import unittest

from cambioml_protobuf import documents_pb2


class TestDocumentsProto(unittest.TestCase):
    def test_page_creation(self):
        page = documents_pb2.Page(page_number=1)
        page.page_value["key1"] = "value1"
        self.assertEqual(page.page_number, 1)
        self.assertEqual(page.page_value["key1"], "value1")

    def test_metadata_creation(self):
        metadata = documents_pb2.Metadata(
            file_type="pdf", document_name="Test Document"
        )
        metadata.additional_info["author"] = "John Doe"
        self.assertEqual(metadata.file_type, "pdf")
        self.assertEqual(metadata.document_name, "Test Document")
        self.assertEqual(metadata.additional_info["author"], "John Doe")

    def test_document_creation(self):
        document = documents_pb2.Document()
        page = document.pages.add(page_number=1)
        page.page_value["key1"] = "value1"
        document.metadata.file_type = "pdf"
        document.metadata.document_name = "Test Document"
        self.assertEqual(len(document.pages), 1)
        self.assertEqual(document.metadata.file_type, "pdf")

    def test_documents_creation(self):
        documents = documents_pb2.Documents()
        document = documents.documents.add()
        document.pages.add(page_number=1)
        document.metadata.file_type = "pdf"
        self.assertEqual(len(documents.documents), 1)

    def test_serialization_and_deserialization(self):
        documents = documents_pb2.Documents()
        document = documents.documents.add()
        document.pages.add(page_number=1)
        document.metadata.file_type = "pdf"

        # serialization
        serialized_documents = documents.SerializeToString()
        # deserialization
        deserialized_documents = documents_pb2.Documents()
        deserialized_documents.ParseFromString(serialized_documents)
        self.assertEqual(
            deserialized_documents.documents[0].metadata.file_type,
            documents.documents[0].metadata.file_type,
        )


if __name__ == "__main__":
    unittest.main()
