// Mock data for health records and appointments
export const mockHealthRecords = [
  {
    id: 1,
    date: '2024-02-01',
    type: 'General Checkup',
    doctor: 'Dr. Sarah Johnson',
    diagnosis: 'Routine examination - all vitals normal',
    prescription: 'Vitamin D supplements',
    notes: 'Follow up in 6 months'
  },
  {
    id: 2,
    date: '2024-01-15',
    type: 'Blood Test',
    doctor: 'Dr. Michael Chen',
    diagnosis: 'Slight iron deficiency',
    prescription: 'Iron supplements',
    notes: 'Recheck in 3 months'
  },
  {
    id: 3,
    date: '2023-12-20',
    type: 'Vaccination',
    doctor: 'Dr. Emily Wilson',
    diagnosis: 'Flu shot administered',
    prescription: 'None',
    notes: 'Annual flu vaccination complete'
  }
];

export const mockAppointments = [
  {
    id: 1,
    date: '2024-02-15',
    time: '10:00 AM',
    doctor: 'Dr. Sarah Johnson',
    type: 'Follow-up Consultation',
    location: 'Main Clinic - Room 204'
  },
  {
    id: 2,
    date: '2024-02-28',
    time: '2:30 PM',
    doctor: 'Dr. Robert Smith',
    type: 'Dental Checkup',
    location: 'Dental Wing - Room 105'
  },
  {
    id: 3,
    date: '2024-03-10',
    time: '11:15 AM',
    doctor: 'Dr. Michael Chen',
    type: 'Blood Test',
    location: 'Laboratory - Room 302'
  }
];