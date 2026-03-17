#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const repoRoot = path.resolve(__dirname, '..', '..');
const risksPath = path.join(repoRoot, 'data', 'risks.json');
const threatsPath = path.join(repoRoot, 'data', 'threats.json');

const risksDoc = JSON.parse(fs.readFileSync(risksPath, 'utf8'));
const threatsDoc = JSON.parse(fs.readFileSync(threatsPath, 'utf8'));

const threatById = new Map(threatsDoc.threats.map((t) => [t.threat_id, t]));

const mapByPrefix = {
  AC: ['THREAT-MT-002', 'THREAT-MT-009', 'THREAT-MT-010'],
  AM: ['THREAT-MT-009', 'THREAT-MT-010', 'THREAT-MT-005'],
  BC: ['THREAT-NT-008', 'THREAT-NT-014', 'THREAT-MT-007', 'THREAT-MT-026'],
  EX: ['THREAT-MT-016', 'THREAT-MT-018', 'THREAT-MT-007'],
  GV: ['THREAT-MT-011', 'THREAT-MT-015', 'THREAT-MT-016', 'THREAT-MT-018'],
  IR: ['THREAT-MT-002', 'THREAT-MT-006', 'THREAT-MT-014'],
  SA: ['THREAT-MT-022', 'THREAT-MT-023', 'THREAT-MT-020'],
  SC: ['THREAT-MT-002', 'THREAT-MT-010', 'THREAT-MT-020']
};

for (const risk of risksDoc.risks) {
  const m = /^RISK-([A-Z]{2,8})-\d{3}$/.exec(risk.risk_id || '');
  const prefix = m ? m[1] : '';
  const threatIds = (mapByPrefix[prefix] || ['THREAT-MT-002']).filter((id) => threatById.has(id));
  risk.threat_ids = threatIds;
}

const riskIdsByThreat = new Map();
for (const t of threatsDoc.threats) {
  riskIdsByThreat.set(t.threat_id, []);
}
for (const risk of risksDoc.risks) {
  for (const tid of risk.threat_ids || []) {
    if (!riskIdsByThreat.has(tid)) riskIdsByThreat.set(tid, []);
    riskIdsByThreat.get(tid).push(risk.risk_id);
  }
}
for (const t of threatsDoc.threats) {
  const ids = Array.from(new Set(riskIdsByThreat.get(t.threat_id) || [])).sort();
  t.mapped_risk_ids = ids;
}

risksDoc.version = '2.1.0';
threatsDoc.version = '1.1.0';

fs.writeFileSync(risksPath, JSON.stringify(risksDoc, null, 2) + '\n');
fs.writeFileSync(threatsPath, JSON.stringify(threatsDoc, null, 2) + '\n');

console.log(`Linked ${risksDoc.risks.length} risks and ${threatsDoc.threats.length} threats.`);
