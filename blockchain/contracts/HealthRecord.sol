// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HealthRecord {
    struct Record {
        string dataHash;      // IPFS hash of the encrypted data
        address owner;        // Patient's address
        uint256 timestamp;    // When the record was created
        mapping(address => bool) authorizedProviders;  // Healthcare providers with access
    }
    
    // Mapping from patient address to their records
    mapping(address => Record[]) private patientRecords;
    
    // Events
    event RecordAdded(address indexed patient, uint256 recordIndex);
    event AccessGranted(address indexed patient, address indexed provider);
    event AccessRevoked(address indexed patient, address indexed provider);
    
    // Add a new health record
    function addRecord(string memory _dataHash) public {
        Record storage newRecord = patientRecords[msg.sender].push();
        newRecord.dataHash = _dataHash;
        newRecord.owner = msg.sender;
        newRecord.timestamp = block.timestamp;
        
        emit RecordAdded(msg.sender, patientRecords[msg.sender].length - 1);
    }
    
    // Grant access to a healthcare provider
    function grantAccess(address provider, uint256 recordIndex) public {
        require(recordIndex < patientRecords[msg.sender].length, "Record does not exist");
        require(msg.sender == patientRecords[msg.sender][recordIndex].owner, "Not the owner");
        
        patientRecords[msg.sender][recordIndex].authorizedProviders[provider] = true;
        emit AccessGranted(msg.sender, provider);
    }
    
    // Revoke access from a healthcare provider
    function revokeAccess(address provider, uint256 recordIndex) public {
        require(recordIndex < patientRecords[msg.sender].length, "Record does not exist");
        require(msg.sender == patientRecords[msg.sender][recordIndex].owner, "Not the owner");
        
        patientRecords[msg.sender][recordIndex].authorizedProviders[provider] = false;
        emit AccessRevoked(msg.sender, provider);
    }
    
    // Check if a provider has access to a record
    function hasAccess(address patient, address provider, uint256 recordIndex) public view returns (bool) {
        require(recordIndex < patientRecords[patient].length, "Record does not exist");
        return patientRecords[patient][recordIndex].authorizedProviders[provider];
    }
    
    // Get record details (only if authorized)
    function getRecord(address patient, uint256 recordIndex) public view returns (string memory, uint256) {
        require(recordIndex < patientRecords[patient].length, "Record does not exist");
        require(
            msg.sender == patient || 
            patientRecords[patient][recordIndex].authorizedProviders[msg.sender],
            "Not authorized"
        );
        
        Record storage record = patientRecords[patient][recordIndex];
        return (record.dataHash, record.timestamp);
    }
} 