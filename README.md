## About the connector
The OCR API provides a simple way of parsing images and multi-page PDF documents (PDF OCR) and getting the extracted text results returned in a JSON format.
<p>This document provides information about the OCRSpace Connector, which facilitates automated interactions, with a OCRSpace server using FortiSOAR&trade; playbooks. Add the OCRSpace Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with OCRSpace.</p>

### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-ocr-space`

## Prerequisites to configuring the connector
- You must have the URL of OCRSpace server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the OCRSpace server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>OCRSpace</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>URL of the ocr.space connector endpoint server to which you will connect and perform the automated operations.<br>
<tr><td>API Key<br></td><td>API key required for authentication.<br>
<tr><td>Language<br></td><td>Language used for OCR. If no language is specified, English 'eng' is taken as default.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Parse Image<br></td><td>Simple way of parsing images and multi-page PDF documents (PDF OCR) and getting the extracted text results.<br></td><td>parse_image <br/>Utilities<br></td></tr>
</tbody></table>

### operation: Parse Image
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Image Source Type<br></td><td>Select image source type that is how you want to provide image.<br>
<strong>If you choose 'url'</strong><ul><li>imageURL: URL of remote image file (Make sure it has the right content type).</li></ul><strong>If you choose 'file'</strong><ul><li>Type: Type of file that you want to submit to VirusTotal for analysis. Type can be an Attachment ID or a File IRI.</li><li>Reference ID: Reference ID that is used to access the attachment metadata from the FortiSOAR� Attachments module.
In the playbook, this defaults to the{{vars.attachment_id}} value or the {{vars.file_iri}} value.</li></ul><strong>If you choose 'base64image'</strong><ul><li>Base64Image: Submitting file via base64.</li><li>File Type: Type of submitted file via base64.</li></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ParsedResults": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "TextOverlay": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "FileParseExitCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ParsedText": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ErrorMessage": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ErrorDetails": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "TextOverlay": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "FileParseExitCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ParsedText": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ErrorMessage": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ErrorDetails": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "OCRExitCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "IsErroredOnProcessing": false,
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ErrorMessage": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ErrorDetails": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "SearchablePDFURL": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ProcessingTimeInMilliseconds": ""
</code><code><br>}</code>
## Included playbooks
The `Sample - ocr-space - 1.0.0` playbook collection comes bundled with the OCRSpace connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the OCRSpace connector.

- Parsing: Base64 Image Details
- Parsing: Image File
- Parsing: Image URL

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
