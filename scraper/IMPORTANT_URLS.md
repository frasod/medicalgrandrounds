# Important URLs for Scraping

This file maintains a repository of all important URLs discovered for grand rounds schedules. Keep this updated so we don't lose valuable links!

## Active Event URLs (Working/Verified)

### Yale Medicine
- **Main Calendar**: https://medicine.yale.edu/internal-medicine/genmed/education/medspirel/calendar/
- **Status**: ✅ Working - Returns 5+ upcoming events
- **Last Verified**: November 16, 2025

### Dartmouth Hitchcock
- **CME Portal**: https://dh.cloud-cme.com/default.aspx?P=6&EID=150850
- **Specific Event**: Nov 21, 2025 - "Free Clinics and Academic Health Centers" by Mohan Nadkarni
- **Status**: ✅ Working - Event details confirmed
- **Last Verified**: November 16, 2025

## Institutions to Target (From User-Provided List)

### Massachusetts General Hospital (MGH)
1. https://www.massgeneral.org/medicine/education/grand-rounds
2. https://www.massgeneral.org/psychiatry/education-and-training/grand-rounds
3. https://www.massgeneral.org/orthopaedics/education/grand-rounds
4. https://www.massgeneral.org/neurology/education-and-training/grand-rounds
5. https://www.massgeneral.org/surgery/education/grand-rounds

### Brigham and Women's Hospital
1. https://www.brighamandwomens.org/neurology/neurology-grand-rounds
2. https://www.brighamandwomens.org/medicine/medical-grand-rounds
3. https://www.brighamandwomens.org/psychiatry/about/psychiatry-grand-rounds
4. https://www.brighamandwomens.org/surgery/surgical-grand-rounds
5. https://www.brighamandwomens.org/emergency-medicine/education-and-training/grand-rounds
6. https://www.brighamandwomens.org/urology/professional-education/urology-grand-rounds

### Beth Israel Deaconess Medical Center (BIDMC)
1. https://www.bidmc.org/medical-education/grand-rounds/medical-grand-rounds
2. https://www.bidmc.org/medical-education/grand-rounds/surgical-grand-rounds
3. https://www.bidmc.org/medical-education/grand-rounds/psychiatric-grand-rounds

### Boston Children's Hospital
1. https://www.childrenshospital.org/research-and-innovation/research/grand-rounds

### Brown University/Rhode Island Hospital
1. https://www.brown.edu/academics/medical/about-us/departments/medicine/grand-rounds
2. https://www.brown.edu/academics/medical/about-us/departments/psychiatry-and-human-behavior/grand-rounds

### Dartmouth Health
1. https://dh.cloud-cme.com/default.aspx?P=6&EID=150850 ✅
2. https://med.dartmouth-hitchcock.org/education_cme.html

### UConn Health
1. https://health.uconn.edu/grand-rounds/

### Yale School of Medicine
1. https://medicine.yale.edu/internal-medicine/genmed/education/medspirel/calendar/ ✅
2. https://medicine.yale.edu/psychiatry/education/grand-rounds/

## Scraping Status by Institution

| Institution | URLs Found | Working Scrapers | Events in System |
|------------|-----------|------------------|------------------|
| Yale | 2 | 1 ✅ | 5 specific events |
| Dartmouth | 2 | 1 ✅ | 1 specific + 1 recurring |
| MGH | 5 | 1 ⚠️ | Recurring only |
| Brigham | 6 | 1 ❌ | Connection errors |
| BIDMC | 3 | 1 ⚠️ | 6 hardcoded events |
| Brown | 2 | 1 ⚠️ | Recurring only |
| Harvard | 0 | 1 ⚠️ | Recurring only |
| Boston Children's | 1 | 0 ❌ | Not implemented |
| UConn | 1 | 0 ❌ | Not implemented |

## Notes

- ✅ = Actively scraping with real event data
- ⚠️ = Implemented but needs improvement (recurring only, hardcoded, etc.)
- ❌ = Not working or not implemented

## Next Steps
1. Implement Boston Children's and UConn scrapers
2. Fix Brigham connection issues (try different user agents)
3. Extract more specific dates from MGH, Brown, Harvard sites
4. Set up automated email requests to get detailed schedules
