#!/usr/bin/env node
const fs = require('fs');

function loadJson(path) {
  return JSON.parse(fs.readFileSync(path, 'utf8'));
}

const controls = loadJson('data/controls.json').controls;
const mappings = loadJson('data/mappings.json').mappings;
const risks = loadJson('data/risks.json').risks;

const controlIds = new Set(controls.map((c) => c.control_id));
const mappingIssues = mappings.filter((m) => !controlIds.has(m.normalized_control_id));
const riskIssues = risks.filter((r) => r.mapped_controls.some((id) => !controlIds.has(id)));

console.log(JSON.stringify({
  summary: {
    controls: controls.length,
    mappings: mappings.length,
    risks: risks.length
  },
  mapping_issues: mappingIssues,
  risk_issues: riskIssues,
  status: mappingIssues.length === 0 && riskIssues.length === 0 ? 'PASS' : 'FAIL'
}, null, 2));
