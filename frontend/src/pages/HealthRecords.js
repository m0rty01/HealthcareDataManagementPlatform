import React from 'react';
import { 
  Typography, 
  Box, 
  Grid, 
  Paper, 
  List, 
  ListItem, 
  ListItemText, 
  Divider,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  Chip
} from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { mockHealthRecords } from '../mockData';

function HealthRecords() {
  return (
    <Box sx={{ flexGrow: 1, p: 3 }}>
      <Typography variant="h4" gutterBottom>
        Health Records
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Your Health Records
            </Typography>
            <List>
              {mockHealthRecords.map((record) => (
                <Accordion key={record.id} sx={{ width: '100%', mb: 1 }}>
                  <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls={`record-${record.id}-content`}
                    id={`record-${record.id}-header`}
                  >
                    <Box sx={{ display: 'flex', alignItems: 'center', width: '100%', justifyContent: 'space-between' }}>
                      <Typography sx={{ flexGrow: 1 }}>{record.type}</Typography>
                      <Chip 
                        label={record.date} 
                        size="small" 
                        sx={{ ml: 2 }}
                      />
                    </Box>
                  </AccordionSummary>
                  <AccordionDetails>
                    <Box sx={{ mb: 2 }}>
                      <Typography variant="subtitle2" color="text.secondary">
                        Doctor
                      </Typography>
                      <Typography paragraph>
                        {record.doctor}
                      </Typography>
                      
                      <Typography variant="subtitle2" color="text.secondary">
                        Diagnosis
                      </Typography>
                      <Typography paragraph>
                        {record.diagnosis}
                      </Typography>
                      
                      <Typography variant="subtitle2" color="text.secondary">
                        Prescription
                      </Typography>
                      <Typography paragraph>
                        {record.prescription}
                      </Typography>
                      
                      <Typography variant="subtitle2" color="text.secondary">
                        Notes
                      </Typography>
                      <Typography>
                        {record.notes}
                      </Typography>
                    </Box>
                  </AccordionDetails>
                </Accordion>
              ))}
            </List>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
}

export default HealthRecords;