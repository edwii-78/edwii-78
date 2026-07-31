<div align="center">
<img src="https://raw.githubusercontent.com/edwii-78/edwii-78/main/header.svg" width="100%" alt="Edwin Dominic — Security Operations"/>
</div>

<br/>

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=ui-monospace%2CSFMono-Regular%2C+SF+Mono%2CConsolas%2Cmonospace&size=13&duration=3200&pause=1200&color=8B949E&background=0D111700&center=true&vCenter=true&width=680&height=28&lines=SOC+Analyst+%C2%B7+Detection+Engineer+%C2%B7+Threat+Hunter;CEH+v13+%C2%B7+15%2B+CVEs+%C2%B7+CERT-In+HoF+%C2%B7+AsyncRAT+%2B+Phishing+IR;Open+to+roles+globally+%E2%80%94+relocation+ready." alt=""/>

<br/><br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-edwin78-0A66C2?style=flat-square&logo=linkedin&logoColor=white&labelColor=0d1117)](https://linkedin.com/in/edwin78)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-edwindominic7878-212C42?style=flat-square&logo=tryhackme&logoColor=white&labelColor=0d1117)](https://tryhackme.com/p/edwindominic7878)
[![Email](https://img.shields.io/badge/Email-edwindominic7878%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white&labelColor=0d1117)](mailto:edwindominic7878@gmail.com)

</div>

---

<br/>

## About

Produced professional-grade SOC investigation reports — a full behavioral malware analysis of AsyncRAT v0.5.8 and a credential phishing IR documenting authenticated Microsoft 365 tenant abuse to bypass SPF/DKIM. Both include MITRE ATT&CK mappings, IOC tables, containment plans, and Splunk SPL hunting queries.

Building a full detection engineering progression across **Wazuh → Splunk → Microsoft Defender XDR → Microsoft Sentinel** — each platform demonstrating a distinct SOC capability: endpoint telemetry and detection engineering, SIEM investigation and threat hunting, enterprise endpoint response, and cross-domain SIEM/SOAR correlation. Eight MITRE ATT&CK techniques detected end-to-end on Wazuh. A Raspberry Pi 4 runs as an inline IPS with ML anomaly detection on a production network.

Independent vulnerability research — 15+ disclosures to Indian government portals and institutions. IIT Madras acknowledged. CERT-In Hall of Fame nominated twice. Open to SOC analyst, detection engineer, and threat hunting roles — available to relocate anywhere.

<br/>

---

<br/>

## Investigations & Labs

<br/>

<table><tr><td>

**`OP-001`** &nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### AsyncRAT v0.5.8 — Behavioral Malware Analysis & SOC Investigation
`Triage Sandbox` &nbsp;·&nbsp; `Static Config Extraction` &nbsp;·&nbsp; `MITRE ATT&CK` &nbsp;·&nbsp; `Splunk SPL`

Sample `95dedfab...fd2b76a2` — malicious score **10/10**. Static configuration extraction recovered live C2 infrastructure, AES key, mutex `LtyEIcOsTiXq`, install path, and persistence filename without executing the sample. Dynamic detonation confirmed installation to roaming profile, `OnLogon` scheduled task at highest run level, `SeDebugPrivilege` acquisition, 25 outbound C2 connections across four ports. Persistence validated: payload relaunched as an unparented top-level process, confirming the scheduled task fired. Three Splunk SPL hunting queries written.

| Field | Detail |
|:---|:---|
| Static extraction | AES key · mutex `LtyEIcOsTiXq` · 6 C2 hosts · install path |
| Persistence | `schtasks /sc onlogon /rl highest` → `%AppData%\windown10.exe` |
| C2 | 6 domains · `34.76.205.124` · ports 80, 443, 4444, 5555 observed |
| Privilege | `SeDebugPrivilege` — arbitrary process handle access |
| Output | Full IR report · IOC table · 3 Splunk SPL hunting queries |

![](https://img.shields.io/badge/T1059.003-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1053.005-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1082-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1614.001-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Static_Config_Extraction-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/SeDebugPrivilege-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-AsyncRAT_Analysis-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/AsyncRAT-Malware-Analysis-and-SOC-Investigation)

</td></tr></table>

<br/>

<table><tr><td>

**`OP-002`** &nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### Email Phishing Investigation — UPS Brand Impersonation / Credential Harvesting
`Header Forensics` &nbsp;·&nbsp; `SPF/DKIM/DMARC` &nbsp;·&nbsp; `Threat Intel Enrichment` &nbsp;·&nbsp; `IOC Analysis`

Full SOC-grade credential phishing IR. Sender domain passed SPF, DKIM, and ARC — attacker legitimately owned a Microsoft 365 tenant to inherit Microsoft's IP reputation and bypass authentication-based filtering. Redirect chain: `t.co/f9tVtkdJm3` → `zoomertar.com` (VT 2/91, Redemption Period). Hidden tracking pixels on `199.192.27.195` (135 passive DNS resolutions, PayPal/Amazon phishing history) confirmed mailbox fingerprinting. Attack chain reconstructed across 10 stages.

| Field | Detail |
|:---|:---|
| Key finding | Authenticated M365 tenant abuse — SPF/DKIM pass ≠ legitimacy |
| Phishing domain | `zoomertar.com` — VT 2/91 · Redemption Period · IP churn across lifetime |
| Tracking server | `199.192.27.195` — 135 passive DNS resolutions · PayPal/Amazon phish history |
| Output | IOC table · 10-stage attack chain · MITRE mapping · containment plan |

![](https://img.shields.io/badge/T1566-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1566.002-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1199-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1589-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1204-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Header_Forensics-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-Phishing_IR-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/Phishing-Email-Investigation-)

</td></tr></table>

<br/>

<table><tr><td>

**`OP-003`** &nbsp; ![](https://img.shields.io/badge/PRODUCTION-1f6feb?style=flat-square&labelColor=0d1117)

### DefenderPi — Inline IPS with ML Anomaly Detection
`Raspberry Pi 4` &nbsp;·&nbsp; `Suricata` &nbsp;·&nbsp; `scikit-learn` &nbsp;·&nbsp; `Redis` &nbsp;·&nbsp; `Grafana` &nbsp;·&nbsp; `Pi-hole`

Raspberry Pi 4 deployed **inline on a live network** — not a VM. Suricata in NFQUEUE mode inspects every packet; confirmed threats trigger automated iptables/ipset block rules. A secondary ML layer (K-Means + Isolation Forest) catches behavioural anomalies that signatures miss. Redis caches enrichment data. Grafana dashboards the EVE JSON feed. Pi-hole + Unbound handles recursive DNS filtering. Telegram delivers real-time alerts.

| Component | Role |
|:---|:---|
| Suricata NFQUEUE | Inline packet inspection + rule-based detection |
| K-Means · Isolation Forest | Behavioural anomaly detection layer |
| iptables / ipset | Automated block enforcement |
| Redis | Threat intel enrichment cache |
| Pi-hole + Unbound | Malicious domain filtering + recursive DNS |

![](https://img.shields.io/badge/Network_IDS-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/ML_Anomaly_Detection-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Auto_Response-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/DNS_Defence-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-DefenderPi-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/DefenderPi)

</td></tr></table>

<br/>

<table><tr><td>

**`OP-004`** &nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### Wazuh Detection Engineering Lab — Windows Threat Simulation
`Windows 11` &nbsp;·&nbsp; `Sysmon` &nbsp;·&nbsp; `Wazuh` &nbsp;·&nbsp; `MITRE ATT&CK` &nbsp;·&nbsp; `8 TTPs E2E`

Windows 11 lab with Sysmon telemetry feeding Wazuh. Eight MITRE ATT&CK techniques simulated and detected end-to-end — each producing a custom detection rule, a triggered alert, and a written incident investigation report.

| # | Technique | Detection |
|:--|:----------|:----------|
| 1 | Reconnaissance — port scan, ping sweep | Sysmon net events + Wazuh correlation |
| 2 | Encoded PowerShell execution | Event ID 4104 · base64 pattern rules |
| 3 | Registry Run key persistence | Event ID 13 · registry value write |
| 4 | Startup folder abuse | Sysmon file creation in startup path |
| 5 | Malicious Windows service | Event ID 7045 · unusual binary path |
| 6 | PsExec lateral movement | Event IDs 4624 + 7045 + named pipe |
| 7 | SMB / NTLM auth monitoring | Event IDs 4624, 4625, 4634, 4672 |
| 8 | Privileged account abuse | Event ID 4672 + type-3 logon chain |

![](https://img.shields.io/badge/T1046-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1059-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1547-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1543-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1021-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1550-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1078-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-Wazuh_SOC_Lab-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/Wazuh-SOC-Detection-Engineering-Lab)

</td></tr></table>

<br/>

<table><tr><td>

**`OP-005`** &nbsp; ![](https://img.shields.io/badge/IN_PROGRESS-d29922?style=flat-square&labelColor=0d1117)

### Splunk Threat Hunting & Detection Engineering — 13-Project Roadmap
`Splunk Enterprise` &nbsp;·&nbsp; `SPL` &nbsp;·&nbsp; `Sysmon` &nbsp;·&nbsp; `MITRE ATT&CK` &nbsp;·&nbsp; `Timeline Reconstruction`

A structured, 13-investigation roadmap covering the full attack lifecycle — authentication, initial access, LOLBins, credential access, lateral movement, C2, and impact — each producing a standalone SOC investigation report with SPL detection logic, IOC extraction, and MITRE mapping. **6 of 13 completed.**

**Phase 1 — Authentication Monitoring**
| Status | Investigation | MITRE |
|:---|:---|:---|
| ✅ Completed | Account Lockout Investigation | T1110 |
| ✅ Completed | Unauthorized Local Administrator Creation | T1136 |

**Phase 2 — Initial Access & Execution (LOLBins)**
| Status | Investigation | MITRE |
|:---|:---|:---|
| ✅ Completed | Certutil Download Activity | T1105 |
| ✅ Completed | MSHTA Remote Script Execution | T1218.005 |
| ✅ Completed | Office → PowerShell Execution Chain | T1204 · T1059.001 |

**Phase 3 — Credential Access & Lateral Movement**
| Status | Investigation | MITRE |
|:---|:---|:---|
| ✅ Completed | Attempted LSASS Credential Dumping | T1003.001 · T1218.011 |
| 🔄 In progress | WMI Remote Execution Investigation | T1047 |
| ⬜ Planned | BITSAdmin Abuse | T1197 |
| ⬜ Planned | Command & Control Beacon Detection | T1071 |

**Phase 4 — Impact & Defense Evasion**
| Status | Investigation | MITRE |
|:---|:---|:---|
| ⬜ Planned | Data Exfiltration Detection | T1041 |
| ⬜ Planned | Shadow Copy Deletion | T1490 |
| ⬜ Planned | Ransomware Behavioral Detection | T1486 · T1490 |
| ⬜ Planned | File Encryption Burst Detection | T1486 |

[![View repository](https://img.shields.io/badge/View_repository-Splunk_Lab-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/Splunk-SOC-Detection-Engineering-Lab)

</td></tr></table>

<br/>

<table><tr><td>

**`OP-006`** &nbsp; ![](https://img.shields.io/badge/IN_PROGRESS-d29922?style=flat-square&labelColor=0d1117)

### Microsoft Defender XDR — Enterprise Endpoint Investigation Series
`Defender for Endpoint` &nbsp;·&nbsp; `Entra ID` &nbsp;·&nbsp; `KQL` &nbsp;·&nbsp; `MITRE ATT&CK`

A 6-project series focused on enterprise endpoint investigation and response — distinct from the Wazuh/Splunk work by covering Microsoft's automated investigation, threat intelligence operationalization, advanced hunting with KQL, cross-domain XDR correlation, and live response forensics.

| Status | Project |
|:---|:---|
| ⬜ Planned | Endpoint Incident Investigation & Response |
| ⬜ Planned | Automated Investigation & Attack Disruption |
| ⬜ Planned | Threat Intelligence & IOC Management |
| ⬜ Planned | Advanced Hunting & Proactive Threat Hunting (KQL) |
| ⬜ Planned | Enterprise XDR Incident Correlation |
| ⬜ Planned | Live Response & Enterprise Forensics |

![](https://img.shields.io/badge/KQL-1f6feb?style=flat-square&labelColor=0d1520)
![](https://img.shields.io/badge/Advanced_Hunting-1f6feb?style=flat-square&labelColor=0d1520)
![](https://img.shields.io/badge/Live_Response-1f6feb?style=flat-square&labelColor=0d1520)
![](https://img.shields.io/badge/XDR_Correlation-1f6feb?style=flat-square&labelColor=0d1520)

</td></tr></table>

<br/>

<table><tr><td>

**`OP-007`** &nbsp; ![](https://img.shields.io/badge/IN_PROGRESS-d29922?style=flat-square&labelColor=0d1117)

### Microsoft Sentinel — Enterprise SIEM & SOAR Series
`Microsoft Sentinel` &nbsp;·&nbsp; `KQL` &nbsp;·&nbsp; `Logic Apps` &nbsp;·&nbsp; `Automation Rules` &nbsp;·&nbsp; `ServiceNow SIR`

A 6-project series demonstrating enterprise SIEM operations — correlating telemetry from Defender XDR, Entra ID, and Microsoft 365 into unified incidents, building KQL analytics rules and watchlists, and automating response with Logic Apps and ServiceNow integration.

| Status | Project |
|:---|:---|
| ⬜ Planned | Phishing Email → Defender XDR → Sentinel Investigation |
| ⬜ Planned | Cloud Identity Attack Investigation (Entra ID) |
| ⬜ Planned | Business Email Compromise (BEC) Investigation |
| ⬜ Planned | Cloud Account Takeover & OAuth Persistence |
| ⬜ Planned | Defender XDR → Sentinel Incident Correlation |
| ⬜ Planned | Sentinel Detection Engineering & SOAR |

![](https://img.shields.io/badge/SIEM-1f6feb?style=flat-square&labelColor=0d1520)
![](https://img.shields.io/badge/SOAR-1f6feb?style=flat-square&labelColor=0d1520)
![](https://img.shields.io/badge/Cross_Domain_Correlation-1f6feb?style=flat-square&labelColor=0d1520)
![](https://img.shields.io/badge/Automation-1f6feb?style=flat-square&labelColor=0d1520)

</td></tr></table>

<br/>

<table><tr><td>

**`OP-008`** &nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### ZeroTrace — AES-256 Encrypted Messenger
`Flutter` &nbsp;·&nbsp; `Firebase` &nbsp;·&nbsp; `Node.js` &nbsp;·&nbsp; `AES-256 E2E`

Flutter + Firebase + Node.js messaging app built security-first. AES-256 encryption applied on-device before transit — the server never handles plaintext. Messages auto-delete server-side on read, leaving no forensic trace.

| Security Property | Implementation |
|:-----------------|:---------------|
| Confidentiality | AES-256 E2E — encrypted before leaving device |
| Server access | Zero plaintext — server handles ciphertext only |
| Persistence | Auto-deletion on read — no message store |

![](https://img.shields.io/badge/AES--256_E2E-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Zero_Plaintext-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Auto_Deletion-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-ZeroTrace-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/ZeroTrace-AES-Encrypted-Messaging-App-With-ServerSide-AutoDeletion)

</td></tr></table>

<br/>

---

<br/>

## Detection Engineering Progression

```text
Wazuh                    Splunk                    Defender XDR              Sentinel
────────                  ────────                   ──────────────            ──────────
Endpoint telemetry    →   SIEM + SPL threat      →   Enterprise endpoint   →   SIEM/SOAR,
Detection rules            hunting, timeline           investigation,            cross-domain
8 TTPs — completed         reconstruction               live response,           correlation,
                            6 / 13 — in progress         KQL hunting               automation
                                                          — planned                 — planned
```

<br/>

---

<br/>

## Stack

<br/>

**Detection & SIEM** &nbsp; — &nbsp; ![Wazuh](https://img.shields.io/badge/Wazuh-0d2137?style=flat-square&logo=wazuh&logoColor=79c0ff) ![Splunk](https://img.shields.io/badge/Splunk-0d2137?style=flat-square&logo=splunk&logoColor=79c0ff) ![Microsoft Sentinel](https://img.shields.io/badge/Microsoft_Sentinel-0d2137?style=flat-square&logo=microsoftazure&logoColor=79c0ff) ![Defender XDR](https://img.shields.io/badge/Defender_XDR-0d2137?style=flat-square&logo=microsoftdefender&logoColor=79c0ff) ![Grafana](https://img.shields.io/badge/Grafana-0d2137?style=flat-square&logo=grafana&logoColor=79c0ff)

**Network & IDS/IPS** &nbsp; — &nbsp; ![Suricata](https://img.shields.io/badge/Suricata-3d1f1f?style=flat-square&logoColor=ff7b72) ![Wireshark](https://img.shields.io/badge/Wireshark-3d1f1f?style=flat-square&logo=wireshark&logoColor=ff7b72) ![Nmap](https://img.shields.io/badge/Nmap-3d1f1f?style=flat-square&logoColor=ff7b72) ![Pi-hole](https://img.shields.io/badge/Pi--hole-3d1f1f?style=flat-square&logo=pi-hole&logoColor=ff7b72) ![iptables](https://img.shields.io/badge/iptables-3d1f1f?style=flat-square&logo=linux&logoColor=ff7b72)

**Endpoint & Forensics** &nbsp; — &nbsp; ![Sysmon](https://img.shields.io/badge/Sysmon-2a1f08?style=flat-square&logo=windows&logoColor=e3b341) ![Autopsy](https://img.shields.io/badge/Autopsy-2a1f08?style=flat-square&logoColor=e3b341) ![Triage Sandbox](https://img.shields.io/badge/Triage_Sandbox-2a1f08?style=flat-square&logoColor=e3b341) ![Burp Suite](https://img.shields.io/badge/Burp_Suite-2a1f08?style=flat-square&logoColor=e3b341)

**Identity & Cloud** &nbsp; — &nbsp; ![Entra ID](https://img.shields.io/badge/Entra_ID-160f2d?style=flat-square&logo=microsoftazure&logoColor=d2a8ff) ![Active Directory](https://img.shields.io/badge/Active_Directory-160f2d?style=flat-square&logo=windows&logoColor=d2a8ff) ![Logic Apps](https://img.shields.io/badge/Azure_Logic_Apps-160f2d?style=flat-square&logo=microsoftazure&logoColor=d2a8ff)

**Frameworks** &nbsp; — &nbsp; ![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-1f2d1f?style=flat-square&logoColor=56d364) ![Linux](https://img.shields.io/badge/Linux-1f2d1f?style=flat-square&logo=linux&logoColor=56d364) ![Kali](https://img.shields.io/badge/Kali_Linux-1f2d1f?style=flat-square&logo=kalilinux&logoColor=56d364) ![Windows Server](https://img.shields.io/badge/Windows_Server-1f2d1f?style=flat-square&logo=windows&logoColor=56d364)

**Languages & Query** &nbsp; — &nbsp; ![Python](https://img.shields.io/badge/Python-1f1a2d?style=flat-square&logo=python&logoColor=bc8cff) ![Bash](https://img.shields.io/badge/Bash-1f1a2d?style=flat-square&logo=gnubash&logoColor=bc8cff) ![SPL](https://img.shields.io/badge/Splunk_SPL-1f1a2d?style=flat-square&logoColor=bc8cff) ![KQL](https://img.shields.io/badge/KQL-1f1a2d?style=flat-square&logoColor=bc8cff) ![C++](https://img.shields.io/badge/C++-1f1a2d?style=flat-square&logo=cplusplus&logoColor=bc8cff)

<br/>

---

<br/>

## Activity

> Stats update every 24 hours. Commit regularly — each detection rule, lab update, or SPL/KQL query counts.

<div align="center">

<img height="195" src="https://github-readme-stats.vercel.app/api?username=edwii-78&show_icons=true&theme=github_dark&bg_color=0d1117&title_color=e6edf3&text_color=8b949e&icon_color=1f6feb&border_color=21262d&include_all_commits=true&count_private=true&border_radius=6&rank_icon=github&card_width=740"/>

<br/><br/>

**SIEM Log Stream &nbsp;·&nbsp; Contribution Activity**

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream.svg"/>
  <img alt="SOC Log Stream — Contribution Activity" src="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream-dark.svg"/>
</picture>

</div>

<br/>

---

<br/>

## Certifications

| Certification | Issuer | |
|:---|:---|:---:|
| Certified Ethical Hacker — CEH v13 | EC-Council | `Active` |
| Certified Secure Computer User — CSCU | EC-Council | `Active` |
| Introduction to Microsoft Sentinel | Microsoft | `Active` |
| Intro to Splunk | Splunk | `Active` |
| Cyber Threat Intelligence 101 | arcX | `Active` |
| TCS IAM Job Simulation | Forage — Tata Consultancy Services | `Active` |
| Job Simulations | Forage — Deloitte · AIG · Mastercard | `Active` |

*Currently pursuing: CNSP · AWS Cloud Practitioner · TryHackMe SOC Level 1 · AI Security*

<br/>

---

<br/>

## Vulnerability Research

| | |
|:---|:---|
| **Scope** | Indian government portals, universities, public institutions |
| **Findings** | 15+ vulnerabilities disclosed |
| **Classes** | SQL injection · stored/reflected XSS · DNS cache poisoning · clickjacking · auth bypass |
| **Notable** | IIT Madras — verified and acknowledged |
| **Recognition** | CERT-In Hall of Fame — nominated twice, under review |

<br/>

---

<br/>

## TryHackMe

<div align="center">

<a href="https://tryhackme.com/p/edwindominic7878">
  <img src="https://raw.githubusercontent.com/edwii-78/edwii-78/main/assets/thm-stats.svg"
       width="760" alt="TryHackMe stats — edwindominic7878"/>
</a>

<br/><br/>

![Pre-Security](https://img.shields.io/badge/Pre--Security-Completed-238636?style=flat-square&labelColor=0d1117)
![SOC Level 1](https://img.shields.io/badge/SOC_Level_1-In_Progress-1f6feb?style=flat-square&labelColor=0d1117)
![AI Security](https://img.shields.io/badge/AI_Security-In_Progress-1f6feb?style=flat-square&labelColor=0d1117)

</div>
