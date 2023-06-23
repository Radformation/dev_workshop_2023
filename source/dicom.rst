=====
DICOM
=====

:material-regular:`manage_accounts;2em`: :bdg-success:`beginner` :bdg-info:`intermediate`

:material-regular:`terminal;2em`: :bdg-primary:`Python`, :bdg-primary:`C#`, :bdg-primary:`Java`

.. important::

  While learning is important, we feel it's even more important to have a problem or project in mind as you learn so that
  specific techniques are immediately relevant as you proceed.

Background
----------

DICOM, which stands for Digital Imaging and Communications in Medicine, is a widely adopted standard for managing and exchanging medical imaging and related data. It plays a crucial role in the field of healthcare by enabling interoperability and seamless integration of medical imaging devices, systems, and applications.


Background of DICOM
"""""""""""""""""""

DICOM was developed by the National Electrical Manufacturers Association (NEMA) and the American College of Radiology (ACR) in the early 1980s. It was created to address the challenges of sharing and exchanging medical images and associated information in a standardized format.

The DICOM standard specifies the rules and protocols for encoding, transmitting, storing, and retrieving medical images and related data. It defines the structure and semantics of medical imaging objects, as well as the communication protocols necessary for exchanging these objects between different systems and devices.

Importance of DICOM in the medical field
""""""""""""""""""""""""""""""""""""""""

DICOM plays a vital role in modern healthcare for several reasons:

* **Interoperability**: DICOM enables seamless interoperability among different medical imaging devices, such as MRI machines, CT scanners, ultrasound systems, and more. It ensures that these devices can produce and exchange medical images that can be accurately interpreted and used across various systems and healthcare institutions.

* **Standardization**: DICOM provides a standardized format for medical images, allowing healthcare professionals to easily share and compare images across different platforms. This standardization promotes consistency, quality, and accuracy in medical imaging diagnostics and treatment planning.

* **Efficient data management**: DICOM facilitates the organization, storage, and retrieval of medical images and associated information. By following the DICOM standard, healthcare organizations can efficiently manage large volumes of medical imaging data, making it accessible whenever needed.

* **Collaboration and research**: DICOM allows medical researchers and professionals to share medical images and data for collaborative studies and research purposes. This capability promotes advancements in medical knowledge, enhances diagnostic accuracy, and drives innovation in medical imaging technologies.

Overview of DICOM standard and its components
"""""""""""""""""""""""""""""""""""""""""""""

The DICOM standard comprises various components that define the rules and specifications for managing medical imaging data. These components include:

DICOM Information Object Definitions (IODs): IODs represent the different types of medical imaging objects, such as images, series, studies, and patient information. Each IOD defines the structure, attributes, and relationships of the specific object type.

Attribute-based data structure: DICOM adopts an attribute-based data model, where each object consists of a set of attributes with defined values and meanings. These attributes contain essential information about the medical image, patient, acquisition parameters, and more.

DICOM network communication (DICOM association): DICOM utilizes a network communication model called DICOM association, which allows different devices and systems to establish connections and exchange medical images and related data.

DICOM service classes and their functionalities: DICOM defines a set of service classes, each with specific functionalities for performing different operations. These include image acquisition, storage, query and retrieval, printing, and more.

DICOM File Format: DICOM specifies a standardized file format for storing medical images and associated metadata. This format ensures compatibility and interoperability among different systems and software applications.

Understanding the fundamentals of DICOM is essential for developers working with medical imaging systems and applications. It provides the necessary foundation for building interoperable, efficient, and secure solutions that contribute to improved patient care and medical research.

Challenges
""""""""""

Working with DICOM data and integrating DICOM functionalities into applications can present certain challenges. Understanding these challenges and following best practices helps ensure successful development and deployment of DICOM-based solutions. This section discusses common challenges encountered when working with DICOM and provides some best practices to overcome them.

* **Challenge 1: Data Compatibility and Interoperability**

  DICOM data comes in various formats and encodings, making data compatibility and interoperability a significant challenge. To address this challenge, it is essential to ensure that DICOM data is correctly encoded and conforms to the DICOM standard. Validating incoming DICOM data, performing proper data normalization, and using standardized DICOM libraries for data processing help achieve compatibility and interoperability across different systems and applications.

* **Challenge 2: Security and Privacy**

  DICOM data often contains sensitive patient information, making security and privacy critical concerns. Best practices include implementing proper access controls, encryption, and secure communication protocols to protect patient data during transmission and storage. Compliance with relevant privacy regulations, such as HIPAA (Health Insurance Portability and Accountability Act), is crucial to safeguard patient privacy.

* **Challenge 3: Performance and Scalability**

  DICOM applications often deal with large volumes of data, including high-resolution images and patient records. Efficient data handling, optimized algorithms, and scalable infrastructure are key to address performance and scalability challenges. Utilizing efficient data storage and retrieval mechanisms, implementing caching strategies, and leveraging distributed computing technologies can enhance performance and ensure scalability.

* **Challenge 4: Workflow Integration**

  Integrating DICOM functionality seamlessly into existing healthcare workflows can be complex. Best practices involve understanding the specific workflow requirements and designing applications that align with existing clinical and administrative processes. Standardized interfaces, such as HL7 (Health Level Seven), can be used to exchange information between DICOM and other healthcare systems, ensuring smooth integration and interoperability.

* **Challenge 5: Testing and Validation**

  Thorough testing and validation are crucial to ensure the accuracy and reliability of DICOM applications. Best practices include designing comprehensive test cases that cover various scenarios, including edge cases and error conditions. Validating DICOM conformance, interoperability, and performance through testing frameworks and tools helps identify and address issues before deployment.

* **Challenge 6: Maintenance and Updates**

  DICOM is a dynamic standard, with periodic updates and additions. Keeping up with the evolving standard and maintaining DICOM-based applications require ongoing effort. Best practices involve staying informed about DICOM updates and releases, utilizing version control systems for managing codebase changes, and regularly updating DICOM libraries and dependencies.

Following these best practices and addressing the challenges inherent to working with DICOM data contribute to the development of robust, secure, and interoperable DICOM solutions. By embracing these practices, developers can build applications that effectively manage medical imaging data, ensure patient privacy, and seamlessly integrate into healthcare workflows.

DICOM Associations
------------------

DICOM associations are a fundamental concept in DICOM network communication. An association represents a logical connection or session established between two DICOM devices to facilitate communication and exchange of medical images and related information. It enables the devices to negotiate communication parameters, exchange DICOM messages, and perform various DICOM services.

Here are some key aspects of DICOM associations:

* **Association Establishment**: The process of establishing an association involves a series of steps, including network connection establishment, negotiation of communication parameters, and authentication. During association establishment, devices identify themselves using Application Entity Titles (AE Titles) to ensure proper identification and routing of messages.

* **Communication Parameters**: DICOM devices negotiate various communication parameters during association establishment. These parameters include supported transfer syntaxes (compression and encoding formats), maximum message size, presentation contexts (defining which services are supported), and other settings.

* **Presentation Contexts**: DICOM uses presentation contexts to define the services and transfer syntaxes supported by each device in an association. A presentation context associates a service class (such as Storage, Query/Retrieve, or Verification) with one or more transfer syntaxes. Devices negotiate and agree upon a set of presentation contexts to determine the services they can exchange during the association.

* **Association Roles**: In a DICOM association, each device plays a specific role. The initiating device is called the Association Requestor (AR) or Service Class User (SCU). The device that accepts the association request is called the Association Acceptor (AA) or Service Class Provider (SCP). The AR/SCU typically initiates DICOM services, such as C-STORE or C-FIND, while the AA/SCP provides the requested services.

* **Message Exchange**: Once the association is established, devices can exchange DICOM messages within the association. Messages are sent as command objects and data objects, containing DICOM commands and data, respectively. Devices take turns sending and receiving messages based on the agreed-upon roles and the requested DICOM services.

* **Association Release and Abort**: When communication is completed, devices release the association to gracefully terminate the session. Either device can initiate the association release. Alternatively, an association can be aborted if an error or abnormal condition occurs, causing an immediate termination of the association.

DICOM associations enable interoperability between different DICOM devices, such as PACS systems, modalities, workstations, and printers. They provide a standardized framework for communication, ensuring consistent and reliable exchange of medical images and associated data.

Client-Server Roles
"""""""""""""""""""

In DICOM, SCU (Service Class User) and SCP (Service Class Provider) are two important roles in the client-server communication model.

* **SCU (Service Class User)**:
  The SCU is the client-side entity responsible for initiating DICOM network connections and sending DICOM requests to perform specific operations or services. It is typically an application or system that makes requests to retrieve, store, or query DICOM objects from a remote device. The SCU initiates the association with the SCP and sends DICOM requests to request specific actions or services.

* **SCP (Service Class Provider)**:
  The SCP is the server-side entity that listens for incoming DICOM network connections and provides the requested services or operations. It receives DICOM requests from SCUs and performs the requested actions, such as retrieving, storing, or querying DICOM objects. The SCP is responsible for handling the incoming requests, processing them, and sending appropriate responses back to the requesting SCUs.

In a DICOM network, SCUs and SCPs work together to establish associations and exchange DICOM messages. The SCU initiates the communication by requesting a service, and the SCP responds to those requests by providing the requested service. The roles of SCU and SCP can be implemented in the same application or divided between different devices or systems, depending on the specific network architecture and requirements.

Network Actions
"""""""""""""""

DICOM defines several network actions or services that devices can invoke to perform specific operations. Here are descriptions of some typical DICOM network actions:

C-FIND (Query/Retrieve)
^^^^^^^^^^^^^^^^^^^^^^^

C-FIND is a DICOM network action used to query a remote device for specific DICOM objects based on search criteria. The requesting device (SCU) sends a query message to the remote device (SCP), specifying search criteria such as patient name, study date, or modality. The SCP responds with a list of matching objects without transferring the actual image data.

.. tab-set-code::

  .. code-block:: python

    from pydicom import Dataset
    from pydicom.uid import ExplicitVRLittleEndian
    from pynetdicom import AE

    # Create a DICOM dataset with query criteria
    query_dataset = Dataset()
    query_dataset.PatientName = "John Doe"

    # Create a DICOM AE (Application Entity)
    ae = AE()

    # Add presentation context for C-FIND
    ae.add_requested_context("PatientRootQueryRetrieveInformationModelFind")

    # Associate with the remote SCP
    assoc = ae.associate("remote_ip", remote_port)

    # Send C-FIND request
    responses = assoc.send_c_find(query_dataset, query_model="P")

    # Process the responses
    for status, dataset in responses:
        if status.Status == 0xFF00:
            # C-FIND response success
            print("Patient Found:", dataset.PatientName)
        else:
            # C-FIND response failure
            print("Failed to find patient:", status)

    # Release the association
    assoc.release()

  .. code-block:: c#

    using EvilDICOM.Core;
    using EvilDICOM.Network;
    using EvilDICOM.Network.Enums;
    using EvilDICOM.Network.Messaging;

    // Create a DICOM client
    DICOMClient client = new DICOMClient();

    // Connect to the remote DICOM server
    client.Connect("remote_ip", remote_port);

    // Create a C-FIND request
    DICOMObject query = new DICOMObject();
    query.Add(DICOMTags.PatientName, "John Doe");

    // Send C-FIND request
    DICOMSCU scu = client.GetSCU();
    DICOMObjects results = scu.Find(query, QueryRetrieveLevel.PATIENT, SopClass.PatientRootQueryRetrieveInformationModelFind);

    // Process the C-FIND response
    foreach (DICOMObject result in results)
    {
        // Extract found information
        string patientName = result.GetString(DICOMTags.PatientName);
        Console.WriteLine("Patient Found: " + patientName);
    }

    // Release the client resources
    client.Release();


C-MOVE (Retrieve)
^^^^^^^^^^^^^^^^^

C-MOVE is used to request the transfer of DICOM objects from a remote device (SCP) to the requesting device (SCU). The SCU sends a C-MOVE request specifying the query criteria, and the SCP retrieves the matching objects and sends them to the SCU. This action allows the SCU to retrieve specific DICOM objects or entire studies from the SCP.

.. tab-set-code::

  .. code-block:: python

    from pydicom import Dataset
    from pydicom.uid import ExplicitVRLittleEndian
    from pynetdicom import AE

    # Create a DICOM dataset with query criteria
    query_dataset = Dataset()
    query_dataset.PatientName = "John Doe"

    # Create a DICOM AE (Application Entity)
    ae = AE()

    # Add presentation context for C-MOVE
    ae.add_requested_context("PatientRootQueryRetrieveInformationModelMove")

    # Associate with the remote SCP
    assoc = ae.associate("remote_ip", remote_port)

    # Send C-MOVE request
    responses = assoc.send_c_move(
        query_dataset, query_model="P", move_destination="move_destination"
    )

    # Process the responses
    for status, dataset in responses:
        if status.Status == 0xFF00:
            # C-MOVE response success
            print("Received image for patient:", dataset.PatientName)
        else:
            # C-MOVE response failure
            print("Failed to retrieve image:", status)

    # Release the association
    assoc.release()

  .. code-block:: c#

    using EvilDICOM.Core;
    using EvilDICOM.Network;
    using EvilDICOM.Network.Enums;
    using EvilDICOM.Network.Messaging;

    // Create a DICOM client
    DICOMClient client = new DICOMClient();

    // Connect to the remote DICOM server
    client.Connect("remote_ip", remote_port);

    // Create a C-MOVE request
    DICOMObject query = new DICOMObject();
    query.Add(DICOMTags.PatientName, "John Doe");

    // Send C-MOVE request
    DICOMSCU scu = client.GetSCU();
    DICOMObjects results = scu.Move(query, QueryRetrieveLevel.PATIENT, "move_destination");

    // Process the C-MOVE response
    foreach (DICOMObject result in results)
    {
        // Extract retrieved information
        string patientName = result.GetString(DICOMTags.PatientName);
        Console.WriteLine("Received image for patient: " + patientName);
    }

    // Release the client resources
    client.Release();


C-STORE (Storage)
^^^^^^^^^^^^^^^^^

C-STORE is used to transmit DICOM objects, typically medical images, from one device (SCU) to another (SCP) for storage. The SCU sends a C-STORE request along with the DICOM object to the SCP, which stores the object in its database. This action is commonly used when sending images from modalities to PACS servers for archiving.

.. tab-set-code::

  .. code-block:: python

    from pydicom import dcmread
    from pynetdicom import AE

    # Read DICOM object from file
    dicom_file = "path/to/dicom.dcm"
    dataset = dcmread(dicom_file)

    # Create a DICOM AE (Application Entity)
    ae = AE()

    # Add presentation context for C-STORE
    ae.add_requested_context("1.2.840.10008.5.1.4.1.1.2")

    # Associate with the remote SCP
    assoc = ae.associate("remote_ip", remote_port)

    # Send C-STORE request
    status = assoc.send_c_store(dataset)

    # Process the C-STORE response
    if status:
        # C-STORE response success
        print("DICOM object stored successfully")
    else:
        # C-STORE response failure
        print("Failed to store DICOM object")

    # Release the association
    assoc.release()

  .. code-block:: c#

    using EvilDICOM.Core;
    using EvilDICOM.Network;

    // Create a DICOM client
    DICOMClient client = new DICOMClient();

    // Connect to the remote DICOM server
    client.Connect("remote_ip", remote_port);

    // Create a DICOM object to store
    DICOMObject dicomObject = new DICOMObject();
    dicomObject.Add(DICOMTags.PatientName, "John Doe");

    // Send C-STORE request
    DICOMSCU scu = client.GetSCU();
    bool success = scu.Store(dicomObject, "path/to/dicom.dcm");

    // Process the C-STORE response
    if (success)
    {
        // C-STORE response success
        Console.WriteLine("DICOM object stored successfully");
    }
    else
    {
        // C-STORE response failure
        Console.WriteLine("Failed to store DICOM object");
    }

    // Release the client resources
    client.Release();


C-GET (Retrieve)
^^^^^^^^^^^^^^^^

C-GET is similar to C-MOVE but with a different data flow. In C-GET, the requesting device (SCU) initiates a query to a remote device (SCP) and receives the retrieved DICOM objects directly from the SCP, without involving intermediate storage. This action allows the SCU to retrieve specific DICOM objects or studies directly from the SCP.

.. tab-set-code::

  .. code-block:: python

    from pydicom import Dataset
    from pydicom.uid import ExplicitVRLittleEndian
    from pynetdicom import AE

    # Create a DICOM dataset with query criteria
    query_dataset = Dataset()
    query_dataset.PatientName = "John Doe"

    # Create a DICOM AE (Application Entity)
    ae = AE()

    # Add presentation context for C-GET
    ae.add_requested_context("PatientRootQueryRetrieveInformationModelGet")

    # Associate with the remote SCP
    assoc = ae.associate("remote_ip", remote_port)

    # Send C-GET request
    responses = assoc.send_c_get(query_dataset, query_model="P")

    # Process the responses
    for status, dataset in responses:
        if status.Status == 0xFF00:
            # C-GET response success
            print("Received image for patient:", dataset.PatientName)
        else:
            # C-GET response failure
            print("Failed to retrieve image:", status)

    # Release the association
    assoc.release()

  .. code-block:: c#

    using EvilDICOM.Core;
    using EvilDICOM.Network;
    using EvilDICOM.Network.Enums;
    using EvilDICOM.Network.Messaging;

    // Create a DICOM client
    DICOMClient client = new DICOMClient();

    // Connect to the remote DICOM server
    client.Connect("remote_ip", remote_port);

    // Create a C-GET request
    DICOMObject query = new DICOMObject();
    query.Add(DICOMTags.PatientName, "John Doe");

    // Send C-GET request
    DICOMSCU scu = client.GetSCU();
    DICOMObjects results = scu.Query(query, QueryRetrieveLevel.PATIENT, SopClass.StudyRootQueryRetrieveInformationModelGet);

    // Process the C-GET response
    foreach (DICOMObject result in results)
    {
        // Extract retrieved information
        string patientName = result.GetString(DICOMTags.PatientName);
        Console.WriteLine("Received image for patient: " + patientName);
    }

    // Release the client resources
    client.Release();


C-ECHO (Verification)
^^^^^^^^^^^^^^^^^^^^^

C-ECHO is a basic DICOM network action used to check the connectivity and availability of a remote DICOM device. The SCU sends a C-ECHO request to the SCP, and the SCP responds with a C-ECHO confirmation. This action is commonly used to test the network connection and verify the availability of a remote device.

.. tab-set-code::

  .. code-block:: python

      from pynetdicom import AE

      # Create a DICOM AE (Application Entity)
      ae = AE()

      # Add presentation context for C-ECHO
      ae.add_requested_context("1.2.840.10008.1.1")

      # Associate with the remote SCP
      assoc = ae.associate("remote_ip", remote_port)

      # Send C-ECHO request
      status = assoc.send_c_echo()

      # Process the C-ECHO response
      if status:
          # C-ECHO response success
          print("DICOM device is reachable")
      else:
          # C-ECHO response failure
          print("Failed to establish connection or device is not reachable")

      # Release the association
      assoc.release()

  .. code-block:: c#

      using EvilDICOM.Core;
      using EvilDICOM.Network;

      // Create a DICOM client
      DICOMClient client = new DICOMClient();

      // Connect to the remote DICOM server
      client.Connect("remote_ip", remote_port);

      // Send C-ECHO request
      DICOMSCU scu = client.GetSCU();
      bool success = scu.Echo();

      // Process the C-ECHO response
      if (success)
      {
          // C-ECHO response success
          Console.WriteLine("DICOM device is reachable");
      }
      else
      {
          // C-ECHO response failure
          Console.WriteLine("Failed to establish connection or device is not reachable");
      }

      // Release the client resources
      client.Release();


These network actions enable various operations in a DICOM network, such as querying for patient data, retrieving images, storing data, and verifying connectivity. Each action serves a specific purpose and plays a crucial role in the exchange and management of medical images and related information within a DICOM network.

Libraries
---------


There are several common code libraries that developers often use to parse, manipulate, and process DICOM files. Here is a list of popular code libraries:

* pydicom: It is a widely used Python library for reading, modifying, and writing DICOM files. It provides an easy-to-use interface for accessing DICOM tags and pixel data.

* DCMTK (DICOM Toolkit): DCMTK is a comprehensive collection of libraries and applications for implementing DICOM functionality. It includes tools for file conversion, network communication, image processing, and more. It is written in C++ and provides command-line utilities along with a programming interface.

* GDCM (Grassroots DICOM): GDCM is an open-source implementation of the DICOM standard in C++. It offers functionalities for reading, writing, and manipulating DICOM files. GDCM supports various platforms and provides APIs for different programming languages, including C++, Python, and Java.

* dcm4che: dcm4che is a Java-based library for working with DICOM data. It offers a comprehensive set of tools for reading, writing, and manipulating DICOM files, as well as networking capabilities for DICOM communication. It is widely used in the healthcare industry.

* fo-dicom: fo-dicom is a DICOM library for .NET platforms, including C# and VB.NET. It provides a simple and intuitive API for handling DICOM files and supports various DICOM operations, such as querying, retrieving, and storing DICOM data.

* Cornerstone: Cornerstone is a JavaScript library for displaying and interacting with medical images, including DICOM files, in web browsers. It provides a powerful set of tools for viewing and manipulating images, as well as performing annotations and measurements.

* ClearCanvas: ClearCanvas is an open-source framework for developing medical imaging applications. It includes a DICOM toolkit that allows developers to build DICOM-enabled applications in C#.NET. ClearCanvas provides a rich set of APIs and a visual development environment.

* itk.js: itk.js is an open-source JavaScript library that brings the capabilities of the Insight Toolkit (ITK) to the web. ITK is a powerful image processing library widely used in the medical imaging field. itk.js allows developers to perform advanced image processing tasks on DICOM data directly in the browser.

These are just a few examples of the common code libraries used in DICOM. Each library has its own features, programming language support, and community. The choice of library depends on the specific requirements and the programming language you are using for your application.

Other Resources
---------------

Here are a few resources where you can access the DICOM Standard documentation:

* **DICOM Standard Official Website** The official website of the DICOM Standard provides access to the current version of the standard, as well as past versions. You can find the DICOM Standard at the following link: `DICOM Standard Official Website <https://www.dicomstandard.org/disclaimer/standard>`__

* **DICOM Standard Publications** The DICOM Standard is published as a set of documents that define the different aspects of the standard. These documents include the DICOM Part 3: Information Object Definitions, which provides detailed information about the attributes and data elements. You can find these publications on the DICOM Standard Official Website or through various DICOM organizations and vendors.

* **DICOM Data Dictionary** The DICOM Data Dictionary is a useful resource that provides a searchable database of DICOM attributes, their definitions, and associated data elements. It allows you to search for specific tags, browse through the tag hierarchy, and access detailed information about each attribute. You can access the DICOM Data Dictionary at the following link: `DICOM Data Dictionary <https://dicom.innolitics.com/ciods>`__

By referring to these resources, you can explore the DICOM Standard documentation and access the information needed to understand the definitions and meanings of DICOM tags.

Lastly, the new beta feature of the Innolitics website lets you upload a DICOM file and view the tags. This is extremely helpful for quick
inspection without needing any other tools but a browser. Navigate to the "File Editor (beta)" section: `Innolitics web site <https://dicom.innolitics.com/ciods>`__

Development Examples
--------------------

The following examples are meant to be bite-sized references for individual actions you may want to
take with DICOM files or networks.

Loading files
"""""""""""""

.. tab-set-code::

  .. code-block:: python

    import pydicom

    # Load a DICOM file
    ds = pydicom.dcmread("path/to/dicom/file.dcm")

    # Access the patient's name attribute
    patient_name = ds.PatientName
    print("Patient Name:", patient_name)

  .. code-block:: c#

      using EvilDICOM.Core;

      // Load a DICOM file
      DicomFile file = new DicomFile("path/to/dicom/file.dcm");
      file.Load();

      // Access the patient's name attribute
      string patientName = file.Dataset.GetSingleValueOrDefault<string>(DicomTag.PatientName);
      Console.WriteLine("Patient Name: " + patientName);

  .. code-block:: java

    import org.dcm4che3.data.Attributes;
    import org.dcm4che3.data.Tag;
    import org.dcm4che3.io.DicomInputStream;

    // Load DICOM file and read specific tags
    DicomInputStream dis = new DicomInputStream(new File("path/to/dicomfile.dcm"));
    Attributes attrs = dis.readDataset(-1, -1);
    String patientName = attrs.getString(Tag.PatientName);
    String studyDate = attrs.getString(Tag.StudyDate);

    // Print the retrieved values
    System.out.println("Patient Name: " + patientName);
    System.out.println("Study Date: " + studyDate);


Saving new or modified files
""""""""""""""""""""""""""""

.. tab-set-code::

  .. code-block:: python

    import pydicom

    # Create a new DICOM dataset
    ds = pydicom.Dataset()
    ds.PatientName = "John Doe"
    ds.PatientID = "12345"

    # Save the dataset to a DICOM file
    ds.save_as("path/to/save/dicom/file.dcm")

  .. code-block:: c#

    using EvilDICOM.Core;

    // Create a new DICOM dataset
    DicomDataset dataset = new DicomDataset();
    dataset.Add(DicomTag.PatientName, "John Doe");
    dataset.Add(DicomTag.PatientID, "12345");

    // Save the dataset to a DICOM file
    DicomFile file = new DicomFile(dataset);
    file.Save("path/to/save/dicom/file.dcm");

  .. code-block:: java

    import org.dcm4che3.data.Attributes;
    import org.dcm4che3.data.Tag;
    import org.dcm4che3.io.DicomOutputStream;

    // Load DICOM file and modify specific tags
    DicomInputStream dis = new DicomInputStream(new File("path/to/dicomfile.dcm"));
    Attributes attrs = dis.readDataset(-1, -1);
    attrs.setString(Tag.PatientName, VR.PN, "John Doe");
    attrs.setString(Tag.StudyDescription, VR.LO, "New Study Description");

Adding or removing tags
"""""""""""""""""""""""

.. note::

  There are multiple ways to access tags in ``pydicom``. Below is an example using the DICOM tag number.

.. tab-code-set::

  .. code-block:: python

    import pydicom

    # Read a DICOM file
    ds = pydicom.dcmread("path/to/dicom/file.dcm")

    # Add a custom tag
    ds.add_new([0x0011, 0x0011], "SH", "CustomTagValue")

    # Remove an existing tag
    del ds[0x0010, 0x0010]  # Delete the PatientName tag

    # Save the modified DICOM file
    ds.save_as("path/to/save/modified/file.dcm")

  .. code-block:: c#

    using EvilDICOM.Core;
    using EvilDICOM.Core.Element;
    using EvilDICOM.Core.Enums;
    using EvilDICOM.Core.Selection;

    // Read a DICOM file
    DicomFile file = new DicomFile("path/to/dicom/file.dcm");
    file.Load();

    // Add a custom tag
    DicomElement customTag = new LongString(TagHelper.CustomTag, "CustomTagValue");
    file.Dataset.Add(customTag);

    // Remove an existing tag
    file.Dataset.Remove(TagHelper.PatientName);

    // Save the modified DICOM file
    file.Save("path/to/save/modified/file.dcm");

  .. code-block:: java

    import org.dcm4che3.data.Attributes;
    import org.dcm4che3.data.Tag;
    import org.dcm4che3.io.DicomOutputStream;

    // Load DICOM file and modify specific tags
    DicomInputStream dis = new DicomInputStream(new File("path/to/dicomfile.dcm"));
    Attributes attrs = dis.readDataset(-1, -1);
    attrs.setString(Tag.PatientName, VR.PN, "John Doe");
    attrs.setString(Tag.StudyDescription, VR.LO, "New Study Description");

    // Save modified dataset to a new DICOM file
    DicomOutputStream dos = new DicomOutputStream(new File("path/to/modified.dcm"));
    dos.writeDataset(null, attrs);
    dos.close();


Getting Pixel Data
""""""""""""""""""

.. tab-set-code::

  .. code-block:: python

    import pydicom

    # Load a DICOM file
    ds = pydicom.dcmread("path/to/dicom/file.dcm")

    # Access the pixel data attribute
    pixel_data = ds.pixel_array
    print("Pixel Data:", pixel_data)

  .. code-block:: c#

    using EvilDICOM.Core;

    // Load a DICOM file
    DicomFile file = new DicomFile("path/to/dicom/file.dcm");
    file.Load();

    // Access the pixel data attribute
    int[] pixelData = file.Dataset.Get<int[]>(DicomTag.PixelData);
    Console.WriteLine("Pixel Data: " + pixelData);

  .. code-block:: java

    import org.dcm4che3.data.Attributes;
    import org.dcm4che3.data.Tag;
    import org.dcm4che3.imageio.plugins.dcm.DicomImageReadParam;
    import org.dcm4che3.imageio.stream.FileImageInputStream;
    import org.dcm4che3.io.DicomInputStream;

    import java.awt.image.BufferedImage;
    import java.io.File;
    import java.io.IOException;

    import javax.imageio.ImageIO;

    public class DICOMPixelAccessExample {

        public static void main(String[] args) throws IOException {
            // Load the DICOM file
            File dicomFile = new File("path/to/dicom.dcm");
            DicomInputStream dicomInputStream = new DicomInputStream(dicomFile);
            Attributes attributes = dicomInputStream.readDataset();

            // Access pixel data
            FileImageInputStream imageInputStream = new FileImageInputStream(dicomFile);
            DicomImageReadParam param = new DicomImageReadParam();
            param.setWindowCenter(attributes.getFloat(Tag.WindowCenter));
            param.setWindowWidth(attributes.getFloat(Tag.WindowWidth));
            BufferedImage image = ImageIO.read(imageInputStream, param);

            // Access individual pixel values
            int width = image.getWidth();
            int height = image.getHeight();

            // Access pixel at (x, y)
            int x = 0;
            int y = 0;
            int pixel = image.getRGB(x, y);
            int red = (pixel >> 16) & 0xFF;
            int green = (pixel >> 8) & 0xFF;
            int blue = pixel & 0xFF;

            System.out.println("Pixel at (" + x + ", " + y + "):");
            System.out.println("Red: " + red);
            System.out.println("Green: " + green);
            System.out.println("Blue: " + blue);

            // Release resources
            dicomInputStream.close();
            imageInputStream.close();
        }
    }


Modifying Pixel Data in-place
"""""""""""""""""""""""""""""

.. tab-set-code::

  .. code-block:: python

    import pydicom
    from PIL import Image

    # Read a DICOM file
    ds = pydicom.dcmread("path/to/dicom/file.dcm")

    # Access the pixel array
    pixel_array = ds.pixel_array

    # Perform image processing operations (using external libraries like PIL)
    image = Image.fromarray(pixel_array)
    image = image.crop((100, 100, 300, 300))
    image = image.resize((512, 512))

    # Convert the modified image back to a pixel array
    modified_pixel_array = np.array(image)

    # Update the pixel data in the DICOM file
    ds.PixelData = modified_pixel_array.tobytes()

    # Save the modified DICOM file
    ds.save_as("path/to/save/modified/file.dcm")

  .. code-block:: c#

    using EvilDICOM.Core;
    using EvilDICOM.Core.Element;
    using EvilDICOM.Core.Helpers;
    using EvilDICOM.Core.IO.Writing;
    using EvilDICOM.Core.Selection;

    // Read a DICOM file
    DicomFile file = new DicomFile("path/to/dicom/file.dcm");
    file.Load();

    // Access the pixel data
    PixelData pixelData = PixelDataFactory.Create(file);

    // Perform image processing operations (using external libraries like ImageSharp)
    pixelData.Crop(100, 100, 300, 300);
    pixelData.Resize(512, 512);

    // Update the pixel data in the DICOM file
    file.Dataset.Replace(pixelData.DataElement);

    // Save the modified DICOM file
    file.Save("path/to/save/modified/file.dcm", DicomWriteOptions.Default);


Anonymize files
"""""""""""""""

.. danger::

    Anonymization is not always perfect. Do your own due diligence to ensure you don't compromise protected health information (PHI).

.. tab-set-code::

  .. code-block:: python

    import pydicom

    # Load a DICOM file
    ds = pydicom.dcmread("path/to/dicom/file.dcm")

    # Anonymize the DICOM dataset
    ds.remove_private_tags()
    ds.PatientID = ""
    ds.PatientName = "Anonymous"

    # Save the anonymized dataset to a new DICOM file
    ds.save_as("path/to/save/anonymized/file.dcm")

  .. code-block:: c#

    using EvilDICOM.Core;
    using EvilDICOM.Network;

    // Load a DICOM file
    DicomFile file = new DicomFile("path/to/dicom/file.dcm");
    file.Load();

    // Anonymize the DICOM dataset
    file.Dataset.Anonymize();

    // Save the anonymized dataset to a new DICOM file
    file.Save("path/to/save/anonymized/file.dcm");

  .. code-block:: java

    import org.dcm4che3.data.Attributes;
    import org.dcm4che3.data.Tag;
    import org.dcm4che3.data.VR;
    import org.dcm4che3.data.anonymize.AgeRetainModify;
    import org.dcm4che3.data.anonymize.DateTimeShift;
    import org.dcm4che3.data.anonymize.Keep;
    import org.dcm4che3.data.anonymize.Retain;
    import org.dcm4che3.data.anonymize.RetainExcept;
    import org.dcm4che3.data.anonymize.SeriesDescriptionModifier;
    import org.dcm4che3.data.anonymize.StudyDescriptionModifier;
    import org.dcm4che3.io.DicomOutputStream;
    import org.dcm4che3.util.TagUtils;

    import java.io.File;
    import java.io.IOException;

    public class DICOMAnonymizerExample {

        public static void main(String[] args) throws IOException {
            // Load the original DICOM file
            File originalFile = new File("path/to/original.dcm");
            Attributes dataset = TagUtils.loadDicomObject(originalFile);

            // Create the DICOM anonymizer
            DICOMAnonymizer anonymizer = new DICOMAnonymizer();

            // Specify the anonymization rules
            anonymizer.setRules(
                    new Retain(Tag.PatientID),
                    new AgeRetainModify(),
                    new DateTimeShift(Tag.StudyDate),
                    new RetainExcept(Tag.StudyInstanceUID),
                    new RetainExcept(Tag.SeriesInstanceUID),
                    new RetainExcept(Tag.SOPInstanceUID),
                    new Keep("AccessionNumber"),
                    new Keep("ReferringPhysicianName"),
                    new StudyDescriptionModifier(),
                    new SeriesDescriptionModifier()
            );

            // Anonymize the dataset
            anonymizer.anonymize(dataset);

            // Save the anonymized dataset to a new DICOM file
            File anonymizedFile = new File("path/to/anonymized.dcm");
            DicomOutputStream dos = new DicomOutputStream(anonymizedFile);
            dos.writeDataset(null, dataset);
            dos.close();

            System.out.println("DICOM anonymization completed. Anonymized file saved as: " + anonymizedFile.getAbsolutePath());
        }
    }


Perform a C-FIND against an AE
""""""""""""""""""""""""""""""

.. tab-set-code::

  .. code-block:: python

    import pydicom
    from pydicom import Dataset
    from pydicom.uid import UID

    # Create a C-FIND request dataset
    find_dataset = Dataset()
    find_dataset.QueryRetrieveLevel = "STUDY"
    find_dataset.PatientName = "*"
    find_dataset.Modality = "CT"

    # Establish a connection to the PACS server
    from pydicom.network import Association

    ae = {"AET": "MY_AE_TITLE", "Address": "pacs.example.com", "Port": 11112}
    assoc = Association(ae)

    # Send the C-FIND request
    results = assoc.send_c_find(
        find_dataset, query_model=UID.StudyRootQueryRetrieveInformationModelFIND
    )

    # Handle the C-FIND response
    for status, result_dataset in results:
        if status.Status == 0xFF00:
            # Print the retrieved study information
            print("Study Instance UID:", result_dataset.StudyInstanceUID)
            print("Study Description:", result_dataset.StudyDescription)
        else:
            # Print the status of the C-FIND response
            print("C-FIND Status:", status)

    # Release the association
    assoc.release()


  .. code-block:: c#

    using EvilDICOM.Core;
    using EvilDICOM.Network;
    using EvilDICOM.Network.DIMSE;
    using EvilDICOM.Network.Enums;
    using EvilDICOM.Network.Helpers;
    using EvilDICOM.Network.Querying;
    using EvilDICOM.Network.Readers;

    class Program
    {
        static void Main(string[] args)
        {
            // Create a C-FIND request
            var findRequest = new DICOMSCUQuery
            {
                QueryLevel = QueryRetrieveLevel.STUDY,
                Query = new DICOMObject()
                    .Add(DICOMTags.PatientsName, "*")
                    .Add(DICOMTags.Modality, "CT")
            };

            // Establish a connection to the PACS server
            var server = new DICOMSCP("pacs.example.com", 11112, "MY_AE_TITLE");
            server.Start();

            // Send the C-FIND request
            var findResponse = server.Find(findRequest);

            // Handle the C-FIND response
            foreach (var result in findResponse)
            {
                if (result.Status == 0x0000)
                {
                    var study = result.Dataset;
                    // Print the retrieved study information
                    Console.WriteLine("Study Instance UID: " + study.Get(DICOMTags.StudyInstanceUID));
                    Console.WriteLine("Study Description: " + study.Get(DICOMTags.StudyDescription));
                }
                else
                {
                    // Print the status of the C-FIND response
                    Console.WriteLine("C-FIND Status: " + result.Status.ToString("X4"));
                }
            }

            // Stop the server and release resources
            server.Stop();
        }
    }


  .. code-block:: java

    import org.dcm4che3.data.Attributes;
    import org.dcm4che3.data.Tag;
    import org.dcm4che3.data.UID;
    import org.dcm4che3.net.*;
    import org.dcm4che3.util.StringUtils;

    // Establish DICOM association with the PACS server
    Connection conn = new Connection();
    conn.setHostname("pacs.example.com");
    conn.setPort(11112);
    conn.setCalledAET("MY_AE_TITLE");
    conn.setCalling(new ApplicationEntity("CLIENT_AE_TITLE"));
    conn.setTlsEnabled(false);
    conn.setConnectTimeout(5000);
    conn.setAcceptTimeout(10000);
    conn.setReleaseTimeout(10000);
    conn.setPackPDV(true);
    conn.setMaxPDULength(16352);

    Association assoc = conn.connect();

    // Perform a C-FIND query to retrieve studies
    Attributes searchAttrs = new Attributes();
    searchAttrs.setString(Tag.QueryRetrieveLevel, VR.CS, "STUDY");
    searchAttrs.setString(Tag.PatientName, VR.PN, "*");
    searchAttrs.setString(Tag.Modality, VR.CS, "CT");

    QRResponseHandler qrResponseHandler = new QRResponseHandler() {
        @Override
        public void onCFindRSP(Association as, Attributes attrs) {
            // Process each retrieved study
            System.out.println("Study Instance UID: " + attrs.getString(Tag.StudyInstanceUID));
            System.out.println("Study Description: " + attrs.getString(Tag.StudyDescription));
        }
    };

    assoc.cfind(UID.StudyRootQueryRetrieveInformationModelFIND, searchAttrs, null, qrResponseHandler);

    // Release the association
    assoc.release();


Create an AE server (SCP)
"""""""""""""""""""""""""

DICOM network communication involves establishing connections with DICOM devices and exchanging DICOM messages. DICOM libraries provide APIs to handle DICOM network communication, enabling developers to implement DICOM service classes and perform operations such as querying and retrieving studies, storing and forwarding images, and printing DICOM reports.

.. tab-set-code::

  .. code-block:: python

    from pydicom import AE, debug

    # Create an Application Entity (AE) for communication
    ae = AE()

    # Set AE title and other communication parameters
    ae.ae_title = b"MY_AE_TITLE"
    ae.port = 11112
    ae.add_requested_context("1.2.840.10008.1.1")  # Add DICOM Presentation Context

    # Start listening for incoming associations
    ae.start_server(("", ae.port), block=True)

  .. code-block:: java

    import org.dcm4che3.net.Association;
    import org.dcm4che3.net.AssociationListener;
    import org.dcm4che3.net.AssociationState;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;

    public class MyAssociationListener implements AssociationListener {

        private static final Logger logger = LoggerFactory.getLogger(MyAssociationListener.class);

        @Override
        public void associationAccepted(Association association) {
            logger.info("Association accepted: {}", association.getAssociationID());
        }

        @Override
        public void associationConnected(Association association) {
            logger.info("Association connected: {}", association.getAssociationID());
        }

        @Override
        public void associationClosed(Association association) {
            logger.info("Association closed: {}", association.getAssociationID());
        }

        @Override
        public void associationAborted(Association association) {
            logger.info("Association aborted: {}", association.getAssociationID());
        }

        @Override
        public void connectionClosed(Association association) {
            logger.info("Connection closed: {}", association.getAssociationID());
        }

        @Override
        public void connectionFailed(Association association, Throwable throwable) {
            logger.error("Connection failed: {}", association.getAssociationID(), throwable);
        }

        @Override
        public void connectionClosedOnError(Throwable throwable) {
            logger.error("Connection closed on error", throwable);
        }

        @Override
        public void associationStatePduReceived(Association association, AssociationState associationState, boolean b) {
            logger.info("Association state PDU received: {}", associationState);
        }
    }


Next Steps
----------

As you become comfortable with manipulating and loading DICOM, you should find a problem to solve and solve it.
Here are some seed ideas:

.. note::

  There are already a number of libraries that tackle some of these things, but they may not
  suit your needs, may be old, or you may simply add another option to the list of options available to
  the community if you choose to open-source your solution.


* **DICOM Viewer**
  Develop a graphical user interface (GUI) application that allows users to load and view DICOM images. Implement features such as window leveling, zooming, panning, and measurement tools to enhance the viewing experience.

* **DICOM Metadata Extractor**
  Create a script that extracts and presents the metadata information from DICOM files. This project can involve parsing DICOM headers and displaying relevant information like patient demographics, imaging parameters, and study details.

* **DICOM to NIfTI Converter**
  Build a tool that converts DICOM series into NIfTI (Neuroimaging Informatics Technology Initiative) format. This project can be particularly useful for researchers and developers working with neuroimaging data.

* **DICOM Anonymizer**
  Develop a script that anonymizes DICOM files by removing or obfuscating sensitive patient information while preserving the imaging data. Privacy and data protection are crucial in medical imaging, and this project can aid in maintaining compliance with regulations.

* **DICOM Image Processing**
  Explore image processing techniques and apply them to DICOM images. Implement operations such as filtering, segmentation, registration, or feature extraction to enhance the images or extract meaningful information for analysis.

* **DICOM Network Communication**
  Create a client-server application that enables the transfer of DICOM files over a network. Implement DICOM network protocols (e.g., DICOM C-STORE) to establish communication and facilitate the exchange of medical images between systems.

* **DICOM Data Analysis**
  Develop a script or application that performs data analysis on a collection of DICOM images. This can involve statistical analysis, visualization, or generating reports based on the imaging data.

* **DICOM Image Reconstruction**
  Implement algorithms for reconstructing 2D or 3D images from DICOM image slices. This project can involve techniques like computed tomography (CT) reconstruction or magnetic resonance imaging (MRI) reconstruction.
