#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const csvPath = path.resolve('/Users/austinsonger/code/grc-toolkit/secure-controls-framework-scf-2025-4.xlsx - Risk Catalog.csv');
const risksPath = path.resolve('/Users/austinsonger/code/grc-toolkit/GRC-Toolkit/data/risks.json');

function parseCSV(input) {
  const rows = [];
  let row = [];
  let field = '';
  let i = 0;
  let inQuotes = false;

  while (i < input.length) {
    const ch = input[i];
    const next = input[i + 1];

    if (inQuotes) {
      if (ch === '"' && next === '"') {
        field += '"';
        i += 2;
        continue;
      }
      if (ch === '"') {
        inQuotes = false;
        i++;
        continue;
      }
      field += ch;
      i++;
      continue;
    }

    if (ch === '"') {
      inQuotes = true;
      i++;
      continue;
    }
    if (ch === ',') {
      row.push(field);
      field = '';
      i++;
      continue;
    }
    if (ch === '\n') {
      row.push(field);
      rows.push(row);
      row = [];
      field = '';
      i++;
      continue;
    }
    if (ch === '\r') {
      i++;
      continue;
    }

    field += ch;
    i++;
  }

  row.push(field);
  rows.push(row);
  return rows;
}

function clean(value) {
  return (value || '').replace(/\s+/g, ' ').trim();
}

function toRiskId(scfRiskId) {
  const m = /^R-([A-Z]{2,6})-(\d+)$/.exec(scfRiskId);
  if (!m) return null;
  return `RISK-${m[1]}-${m[2].padStart(3, '0')}`;
}

function mapControls(grouping, riskCode, csfFunction, title, description) {
  const g = (grouping || '').toLowerCase();
  const rc = (riskCode || '').toUpperCase();
  const f = (csfFunction || '').toLowerCase();
  const text = `${title} ${description}`.toLowerCase();

  if (rc.includes('AC') || g.includes('access')) return ['CTRL-AC-001'];
  if (rc.includes('AM') || g.includes('asset')) return ['CTRL-CM-001'];
  if (rc.includes('BC') || g.includes('continuity') || text.includes('outage') || text.includes('recovery')) return ['CTRL-CP-001'];
  if (rc.includes('IR') || g.includes('incident')) return ['CTRL-IR-001'];
  if (rc.includes('AU') || g.includes('audit') || g.includes('logging') || text.includes('monitor') || text.includes('log')) return ['CTRL-AU-001'];
  if (rc.includes('SC') || g.includes('communication') || text.includes('encryption') || text.includes('key')) return ['CTRL-SC-001'];
  if (f.includes('protect')) return ['CTRL-CM-001'];
  if (f.includes('recover')) return ['CTRL-CP-001'];
  if (f.includes('detect')) return ['CTRL-AU-001'];
  if (f.includes('respond')) return ['CTRL-IR-001'];
  return ['CTRL-CM-001'];
}

const csv = fs.readFileSync(csvPath, 'utf8');
const rows = parseCSV(csv);
const riskRe = /^R-[A-Z]{2,6}-\d+$/;
let currentGroup = '';
const imported = [];

for (const row of rows) {
  const cols = row.map(clean);
  const idx = cols.findIndex((c) => riskRe.test(c));
  if (idx === -1) continue;

  const scfRiskCode = cols[idx];
  const riskId = toRiskId(scfRiskCode);
  if (!riskId) continue;

  const grouping = idx > 0 && cols[idx - 1] ? cols[idx - 1] : currentGroup;
  if (grouping) currentGroup = grouping;

  const title = cols[idx + 1] || `SCF Risk ${scfRiskCode}`;
  const description = cols[idx + 2] || `Risk imported from SCF catalog (${scfRiskCode}).`;
  const csfFunction = cols[idx + 3] || 'Unknown';

  const mappedControls = mapControls(currentGroup, scfRiskCode, csfFunction, title, description);

  imported.push({
    risk_id: riskId,
    title,
    description,
    likelihood: 3,
    impact: 3,
    mapped_controls: mappedControls,
    risk_owner: `SCF Risk Owner - ${currentGroup || 'Unassigned'}`,
    set_theory_relationships: [
      {
        relation: mappedControls.length > 1 ? 'intersects_with' : 'subset_of',
        rationale: 'semantic',
        source_scope: 'risk_scenario_set',
        target_scope: 'control_requirement_set',
        confidence_alignment: 'medium'
      }
    ],
    source_catalog: {
      name: 'Secure Controls Framework (SCF) 2025.4 Risk Catalog',
      source_risk_code: scfRiskCode,
      risk_grouping: currentGroup || 'Unspecified',
      nist_csf_function: csfFunction || 'Unknown'
    }
  });
}

const out = {
  version: '2.0.0',
  generated_at: '2026-03-17',
  risks: imported
};

fs.writeFileSync(risksPath, JSON.stringify(out, null, 2) + '\n');
console.log(`Imported ${imported.length} SCF risks into ${risksPath}`);
