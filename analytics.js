// analytics.js

(function() {
    if (window.analytics) return;
    window.analytics = {};

    // Helper function to send data to your server
    function sendToServer(data) {
        fetch('https://your-analytics-server.com/track', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }).catch(error => console.error('Analytics error:', error));
    }

    window.analytics.trackPageView = function() {
        const data = {
            eventType: 'pageview',
            url: window.location.href,
            timestamp: new Date().toISOString()
        };
        sendToServer(data);
    };

    window.analytics.trackEvent = function(eventCategory, eventAction, eventLabel) {
        const data = {
            eventType: 'event',
            category: eventCategory,
            action: eventAction,
            label: eventLabel,
            timestamp: new Date().toISOString()
        };
        sendToServer(data);
    };

    window.analytics.trackPageView();
})();
