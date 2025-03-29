import React, { useState, useEffect } from 'react';

export const IndustrySelector = ({ value, onChange, status, onFinalize }) => {
  const [industries, setIndustries] = useState([]);
  const [subIndustries, setSubIndustries] = useState([]);
  
  useEffect(() => {
    async function fetchIndustries() {
      try {
        const response = await fetch('/api/business/industries');
        if (response.ok) {
          const data = await response.json();
          setIndustries(data.industries);
        }
      } catch (error) {
        console.error('Error fetching industries:', error);
      }
    }
    
    fetchIndustries();
  }, []);
  
  // Fetch sub-industries when main industry changes
  useEffect(() => {
    if (!value.mainIndustry) return;
    
    async function fetchSubIndustries() {
      try {
        const response = await fetch(`/api/business/subindustries?industry=${value.mainIndustry}`);
        if (response.ok) {
          const data = await response.json();
          setSubIndustries(data.subIndustries);
        }
      } catch (error) {
        console.error('Error fetching sub-industries:', error);
      }
    }
    
    fetchSubIndustries();
  }, [value.mainIndustry]);
  
  return (
    <div className="industry-selector">
      <div className="field-group">
        <label>
          Main Industry Category
          <span className="required-indicator">*</span>
        </label>
        
        <select
          value={value.mainIndustry || ''}
          onChange={(e) => onChange({
            ...value,
            mainIndustry: e.target.value,
            subIndustry: '' // Reset sub-industry when main industry changes
          })}
          disabled={status === 'finalized'}
        >
          <option value="">Select Industry</option>
          {industries.map(industry => (
            <option key={industry.id} value={industry.id}>{industry.name}</option>
          ))}
        </select>
        
        {value.mainIndustry && (
          <>
            <label>
              Industry Subcategory
            </label>
            
            <select
              value={value.subIndustry || ''}
              onChange={(e) => onChange({
                ...value,
                subIndustry: e.target.value
              })}
              disabled={status === 'finalized'}
            >
              <option value="">Select Subcategory</option>
              {subIndustries.map(subIndustry => (
                <option key={subIndustry.id} value={subIndustry.id}>{subIndustry.name}</option>
              ))}
            </select>
          </>
        )}
        
        {value.mainIndustry && (
          <button 
            onClick={onFinalize}
            disabled={status === 'finalized'}
            className={status === 'finalized' ? 'finalized' : ''}
          >
            {status === 'finalized' ? 'Industry Finalized' : 'Finalize Industry Selection'}
          </button>
        )}
      </div>
      
      {value.mainIndustry && (
        <div className="industry-context">
          <h4>Industry Insights</h4>
          <p>Based on your industry selection, here are some key factors to consider:</p>
          
          <div className="industry-stats">
            <div className="stat-item">
              <span className="stat-label">Average Startup Costs</span>
              <span className="stat-value">$50,000 - $150,000</span>
            </div>
            <div className="stat-item">
              <span className="stat-label">Success Rate</span>
              <span className="stat-value">68%</span>
            </div>
            <div className="stat-item">
              <span className="stat-label">Avg. Revenue (Year 1)</span>
              <span className="stat-value">$125,000</span>
            </div>
          </div>
          
          <div className="industry-regulations">
            <h5>Common Regulations</h5>
            <ul>
              <li>Business license requirements</li>
              <li>Industry-specific permits</li>
              <li>Tax considerations</li>
            </ul>
          </div>
        </div>
      )}
    </div>
  );
};