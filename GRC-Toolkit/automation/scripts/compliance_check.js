#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

function loadJson(path) {
  return JSON.parse(fs.readFileSync(path, 'utf8'));
}

const controlsDoc = loadJson('data/controls.json');
const controls = Array.isArray(controlsDoc.controls) && controlsDoc.controls.length > 0
  ? controlsDoc.controls
  : (Array.isArray(controlsDoc.grctoolkit_controls) ? controlsDoc.grctoolkit_controls : []);
const mappingFiles = fs
  .readdirSync('data')
  .filter((name) => name.endsWith('_mappings.json'))
  .sort();

const mappings = mappingFiles.flatMap((name) => {
  const dataset = loadJson(path.join('data', name));
  return Array.isArray(dataset.mappings) ? dataset.mappings : [];
});
const risks = loadJson('data/risks.json').risks;
const threats = loadJson('data/threats.json').threats;

const controlIds = new Set(controls.map((c) => c.control_id));
const mappingIssues = mappings.filter((m) => !controlIds.has(m.normalized_control_id));
const riskIssues = risks.filter((r) => r.mapped_controls.some((id) => !controlIds.has(id)));

console.log(JSON.stringify({
  summary: {
    controls: controls.length,
    mapping_files: mappingFiles.length,
    mappings: mappings.length,
    risks: risks.length,
    threats: threats.length
  },
  mapping_issues: mappingIssues,
  risk_issues: riskIssues,
  status: mappingIssues.length === 0 && riskIssues.length === 0 ? 'PASS' : 'FAIL'
}, null, 2));
