import React from 'react';
import { Typography, Box, Grid, Paper, List, ListItem, ListItemText, Divider } from '@mui/material';
import { mockHealthRecords, mockAppointments } from '../mockData';

function Dashboard() {
  return (
    <Box sx={{ flexGrow: 1, p: 3 }}>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Recent Health Records
            </Typography>
            <List>
              {mockHealthRecords.map((record, index) => (
                <React.Fragment key={record.id}>
                  <ListItem alignItems="flex-start">
                    <ListItemText
                      primary={record.type}
                      secondary={
                        <>
                          <Typography component="span" variant="body2" color="text.primary">
                            {record.date} - {record.doctor}
                          </Typography>
                          <br />
                          {record.diagnosis}
                        </>
                      }
                    />
                  </ListItem>
                  {index < mockHealthRecords.length - 1 && <Divider />}
                </React.Fragment>
              ))}
            </List>
          </Paper>
        </Grid>
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Upcoming Appointments
            </Typography>
            <List>
              {mockAppointments.map((appointment, index) => (
                <React.Fragment key={appointment.id}>
                  <ListItem alignItems="flex-start">
                    <ListItemText
                      primary={appointment.type}
                      secondary={
                        <>
                          <Typography component="span" variant="body2" color="text.primary">
                            {appointment.date} at {appointment.time}
                          </Typography>
                          <br />
                          {appointment.doctor} - {appointment.location}
                        </>
                      }
                    />
                  </ListItem>
                  {index < mockAppointments.length - 1 && <Divider />}
                </React.Fragment>
              ))}
            </List>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
}

export default Dashboard;