// Speed Insights initialization for static HTML site
// This script uses the @vercel/speed-insights web package to track performance metrics

import { injectSpeedInsights } from './speed-insights-lib.js';

// Initialize Speed Insights when the DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    injectSpeedInsights();
  });
} else {
  // DOM is already ready
  injectSpeedInsights();
}
