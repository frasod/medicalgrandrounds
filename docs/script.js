document.addEventListener('alpine:init', () => {
    Alpine.data('grandRoundsApp', () => ({
        allEvents: [],
        filteredEvents: [],
        lastUpdated: 'N/A',
        isLoading: true,
        filter: {
            region: '',
            state: '',
            keyword: ''
        },
        unique: {
            regions: [],
            states: []
        },

        init() {
            this.fetchData();
        },

        async fetchData() {
            try {
                const response = await fetch('data.json');
                if (!response.ok) throw new Error('Failed to load data.json');
                const data = await response.json();
                
                this.allEvents = data.events || [];
                this.lastUpdated = this.formatDate(data.last_updated, true);
                
                this.populateFilters();
                this.applyFilters();
            } catch (error) {
                console.error("Error fetching event data:", error);
                this.allEvents = [];
            } finally {
                this.isLoading = false;
            }
        },

        populateFilters() {
            const regions = new Set();
            const states = new Set();
            this.allEvents.forEach(event => {
                if (event.region) regions.add(event.region);
                if (event.state) states.add(event.state);
            });
            this.unique.regions = [...regions].sort();
            this.unique.states = [...states].sort();
        },

        applyFilters() {
            let events = this.allEvents;

            // Filter by Region
            if (this.filter.region) {
                events = events.filter(e => e.region === this.filter.region);
            }

            // Filter by State
            if (this.filter.state) {
                events = events.filter(e => e.state === this.filter.state);
            }

            // Filter by Keyword
            if (this.filter.keyword.length > 2) {
                const lowerKeyword = this.filter.keyword.toLowerCase();
                events = events.filter(e => 
                    (e.title && e.title.toLowerCase().includes(lowerKeyword)) ||
                    (e.institution && e.institution.toLowerCase().includes(lowerKeyword)) ||
                    (e.speaker && e.speaker.toLowerCase().includes(lowerKeyword)) ||
                    (e.department && e.department.toLowerCase().includes(lowerKeyword))
                );
            }

            this.filteredEvents = events;
        },

        formatDate(isoString, showTime = false) {
            if (!isoString) return 'Date not available';
            try {
                const date = new Date(isoString);
                const options = {
                    year: 'numeric',
                    month: 'long',
                    day: 'numeric',
                    timeZone: 'America/New_York' // Display in a consistent timezone
                };
                if (showTime) {
                    options.hour = 'numeric';
                    options.minute = 'numeric';
                    options.timeZoneName = 'short';
                }
                return date.toLocaleDateString('en-US', options);
            } catch (e) {
                return isoString; // Fallback to original string if parsing fails
            }
        }
    }));
});
