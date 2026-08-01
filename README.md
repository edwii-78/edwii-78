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

Building a detection engineering progression across **Wazuh → Splunk → Microsoft Defender XDR → Microsoft Sentinel**, each platform demonstrating a distinct SOC capability. Eight MITRE ATT&CK techniques detected end-to-end on Wazuh. A Raspberry Pi 4 runs as an inline IPS with ML anomaly detection on a production network.

Independent vulnerability research — 15+ disclosures to Indian government portals and institutions. IIT Madras acknowledged. CERT-In Hall of Fame nominated twice. Open to SOC analyst, detection engineer, and threat hunting roles — available to relocate anywhere.

<br/>

---

<br/>

## Proven Investigations

<sub>Complete, published SOC-grade case files — full methodology, evidence, and findings.</sub>

<br/>

<table><tr><td width="100%">

<img align="right" src="https://img.shields.io/badge/MALWARE_ANALYSIS-f85149?style=flat-square&labelColor=2d1010" alt=""/>

**`OP-001`** &nbsp;·&nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### AsyncRAT v0.5.8 — Behavioral Malware Analysis
`Triage Sandbox` &nbsp;·&nbsp; `Static Config Extraction` &nbsp;·&nbsp; `Dynamic Analysis` &nbsp;·&nbsp; `Splunk SPL`

Score **10 / 10**. Static extraction recovered AES key, mutex, 6 C2 hosts, install path — without execution. Dynamic detonation confirmed roaming-profile install, `OnLogon` scheduled task at highest privilege, `SeDebugPrivilege` acquisition, and 25 C2 connections. Persistence validated by the payload relaunching as an unparented process.

| Field | Detail |
|:---|:---|
| Static recovery | AES key · mutex `LtyEIcOsTiXq` · 6 C2 hosts · install path |
| Persistence | `schtasks /sc onlogon /rl highest` → `%AppData%\windown10.exe` |
| C2 observed | `34.76.205.124` — ports 80, 443, 4444, 5555 of 6 configured |
| Output | Full IR · IOC table · 3 Splunk SPL hunting queries |

![](https://img.shields.io/badge/T1059.003-f85149?style=flat-square&labelColor=2d1010)
![](https://img.shields.io/badge/T1053.005-f85149?style=flat-square&labelColor=2d1010)
![](https://img.shields.io/badge/T1082-f85149?style=flat-square&labelColor=2d1010)
![](https://img.shields.io/badge/T1614.001-f85149?style=flat-square&labelColor=2d1010)
![](https://img.shields.io/badge/SeDebugPrivilege-f85149?style=flat-square&labelColor=2d1010)

[![View repository](https://img.shields.io/badge/View_Repository-AsyncRAT_Analysis-1f6feb?style=flat-square&logo=github&logoColor=white&labelColor=0d1117)](https://github.com/edwii-78/AsyncRAT-Malware-Analysis-and-SOC-Investigation)

</td></tr></table>

<br/>

<table><tr><td width="100%">

<img align="right" src="https://img.shields.io/badge/PHISHING_INVESTIGATION-f85149?style=flat-square&labelColor=2d1010" alt=""/>

**`OP-002`** &nbsp;·&nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### Email Phishing IR — UPS Brand Impersonation
`Header Forensics` &nbsp;·&nbsp; `SPF/DKIM/DMARC` &nbsp;·&nbsp; `Threat Intel` &nbsp;·&nbsp; `IOC Analysis`

Core finding: attacker legitimately owned a Microsoft 365 tenant to inherit Microsoft's outbound IP reputation — SPF, DKIM, and ARC all passed, yet the email was malicious. Redirect chain `t.co → zoomertar.com` (VT 2/91, Redemption Period). Tracking pixels confirmed mailbox fingerprinting. 10-stage attack chain reconstructed.

| Field | Detail |
|:---|:---|
| Core finding | Authenticated M365 abuse — auth pass ≠ legitimacy |
| Phishing domain | `zoomertar.com` — VT 2/91 · Redemption Period |
| Tracking infra | `199.192.27.195` — 135 passive DNS resolutions |
| Output | IOC table · 10-stage attack chain · MITRE map · containment plan |

![](https://img.shields.io/badge/T1566-f85149?style=flat-square&labelColor=2d1010)
![](https://img.shields.io/badge/T1566.002-f85149?style=flat-square&labelColor=2d1010)
![](https://img.shields.io/badge/T1199-f85149?style=flat-square&labelColor=2d1010)
![](https://img.shields.io/badge/T1589-f85149?style=flat-square&labelColor=2d1010)
![](https://img.shields.io/badge/T1204-f85149?style=flat-square&labelColor=2d1010)

[![View repository](https://img.shields.io/badge/View_Repository-Phishing_IR-1f6feb?style=flat-square&logo=github&logoColor=white&labelColor=0d1117)](https://github.com/edwii-78/Phishing-Email-Investigation-)

</td></tr></table>

<br/>

---

<br/>

## Detection Engineering Labs

<sub>Environments built and operated end-to-end — not walkthroughs.</sub>

<br/>

<table><tr><td width="100%">

**`OP-003`** &nbsp;·&nbsp; ![](https://img.shields.io/badge/PRODUCTION-1f6feb?style=flat-square&labelColor=0d1117)

### DefenderPi — Inline IPS with ML Anomaly Detection
`Raspberry Pi 4` &nbsp;·&nbsp; `Suricata` &nbsp;·&nbsp; `scikit-learn` &nbsp;·&nbsp; `Redis` &nbsp;·&nbsp; `Grafana`

Raspberry Pi 4 deployed **inline on a live network**. Suricata in NFQUEUE mode inspects every packet; confirmed threats trigger automated iptables/ipset blocks. A secondary ML layer (K-Means + Isolation Forest) catches what signatures miss. Pi-hole + Unbound handles recursive DNS filtering.

| Component | Role |
|:---|:---|
| Suricata NFQUEUE | Inline inspection + rule-based detection |
| K-Means · Isolation Forest | Behavioural anomaly layer |
| iptables / ipset | Automated block enforcement |

![](https://img.shields.io/badge/Network_IDS-1f6feb?style=flat-square&labelColor=0d1520)
![](https://img.shields.io/badge/ML_Detection-1f6feb?style=flat-square&labelColor=0d1520)
![](https://img.shields.io/badge/Auto_Response-1f6feb?style=flat-square&labelColor=0d1520)

[![View repository](https://img.shields.io/badge/View_Repository-DefenderPi-1f6feb?style=flat-square&logo=github&logoColor=white&labelColor=0d1117)](https://github.com/edwii-78/DefenderPi)

</td></tr></table>

<br/>

<table><tr><td width="100%">

**`OP-004`** &nbsp;·&nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### Wazuh Detection Engineering Lab — Windows Threat Simulation
`Windows 11` &nbsp;·&nbsp; `Sysmon` &nbsp;·&nbsp; `Wazuh` &nbsp;·&nbsp; `MITRE ATT&CK`

Eight MITRE ATT&CK techniques simulated and detected end-to-end on a Windows 11 lab with Sysmon telemetry. Each produced a custom detection rule, a triggered alert, and a written incident report.

<details>
<summary><b>View all 8 techniques</b></summary>
<br/>

| # | Technique | Detection |
|:--|:----------|:----------|
| 1 | Reconnaissance | Sysmon net events + Wazuh correlation |
| 2 | Encoded PowerShell | Event ID 4104 · base64 rules |
| 3 | Registry persistence | Event ID 13 · registry value write |
| 4 | Startup folder abuse | Sysmon file creation in startup path |
| 5 | Malicious service | Event ID 7045 · unusual binary path |
| 6 | PsExec lateral movement | Event IDs 4624 + 7045 + named pipe |
| 7 | SMB / NTLM auth | Event IDs 4624, 4625, 4634, 4672 |
| 8 | Privileged account abuse | Event ID 4672 + type-3 logon chain |

</details>

![](https://img.shields.io/badge/T1046-1f6feb?style=flat-square&labelColor=0d1520)
![](https://img.shields.io/badge/T1059-1f6feb?style=flat-square&labelColor=0d1520)
![](https://img.shields.io/badge/T1547-1f6feb?style=flat-square&labelColor=0d1520)
![](https://img.shields.io/badge/T1021-1f6feb?style=flat-square&labelColor=0d1520)
![](https://img.shields.io/badge/T1078-1f6feb?style=flat-square&labelColor=0d1520)

[![View repository](https://img.shields.io/badge/View_Repository-Wazuh_SOC_Lab-1f6feb?style=flat-square&logo=github&logoColor=white&labelColor=0d1117)](https://github.com/edwii-78/Wazuh-SOC-Detection-Engineering-Lab)

</td></tr></table>

<br/>

---

<br/>

## Active Roadmap

<sub>Tracked publicly, updated as each investigation ships. Most portfolios show finished work only — this shows how the work gets built.</sub>

<br/>

| Platform | Focus | Progress | |
|:---|:---|:---|:---:|
| **Splunk** | SIEM detection engineering · SPL · threat hunting | `██████████░░░░░░░░░░` 6 / 13 | [Repo →](https://github.com/edwii-78/Splunk-SOC-Detection-Engineering-Lab) |
| **Defender XDR** | Enterprise endpoint investigation · KQL · live response | `░░░░░░░░░░░░░░░░░░░░` 0 / 6 | Planning |
| **Microsoft Sentinel** | Cross-domain SIEM/SOAR · automation | `░░░░░░░░░░░░░░░░░░░░` 0 / 6 | Planning |

<br/>

<details>
<summary><b>Splunk — 13-project roadmap, phase breakdown</b></summary>
<br/>

**Phase 1 — Authentication Monitoring**
| | Investigation | MITRE |
|:---|:---|:---|
| ✅ | Account Lockout Investigation | T1110 |
| ✅ | Unauthorized Local Administrator Creation | T1136 |

**Phase 2 — Initial Access & Execution (LOLBins)**
| | Investigation | MITRE |
|:---|:---|:---|
| ✅ | Certutil Download Activity | T1105 |
| ✅ | MSHTA Remote Script Execution | T1218.005 |
| ✅ | Office → PowerShell Execution Chain | T1204 · T1059.001 |

**Phase 3 — Credential Access & Lateral Movement**
| | Investigation | MITRE |
|:---|:---|:---|
| ✅ | Attempted LSASS Credential Dumping | T1003.001 · T1218.011 |
| 🔄 | BITSAdmin Abuse | T1197 |
| ⬜ | WMI Remote Execution Investigation | T1047 |
| ⬜ | Command & Control Beacon Detection | T1071 |

**Phase 4 — Impact & Defense Evasion**
| | Investigation | MITRE |
|:---|:---|:---|
| ⬜ | Data Exfiltration Detection | T1041 |
| ⬜ | Shadow Copy Deletion | T1490 |
| ⬜ | Ransomware Behavioral Detection | T1486 · T1490 |
| ⬜ | File Encryption Burst Detection | T1486 |

</details>

<details>
<summary><b>Microsoft Defender XDR — 6-project series</b></summary>
<br/>

| | Project |
|:---|:---|
| ⬜ | Endpoint Incident Investigation & Response |
| ⬜ | Automated Investigation & Attack Disruption |
| ⬜ | Threat Intelligence & IOC Management |
| ⬜ | Advanced Hunting & Proactive Threat Hunting (KQL) |
| ⬜ | Enterprise XDR Incident Correlation |
| ⬜ | Live Response & Enterprise Forensics |

</details>

<details>
<summary><b>Microsoft Sentinel — 6-project series</b></summary>
<br/>

| | Project |
|:---|:---|
| ⬜ | Phishing Email → Defender XDR → Sentinel Investigation |
| ⬜ | Cloud Identity Attack Investigation (Entra ID) |
| ⬜ | Business Email Compromise (BEC) Investigation |
| ⬜ | Cloud Account Takeover & OAuth Persistence |
| ⬜ | Defender XDR → Sentinel Incident Correlation |
| ⬜ | Sentinel Detection Engineering & SOAR |

</details>

<br/>

---

<br/>

## Applied Security Build

<br/>

<table><tr><td width="100%">

**`OP-005`** &nbsp;·&nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### ZeroTrace — AES-256 Encrypted Messenger
`Flutter` &nbsp;·&nbsp; `Firebase` &nbsp;·&nbsp; `Node.js` &nbsp;·&nbsp; `AES-256 E2E`

AES-256 encryption applied on-device before transit. The server handles only ciphertext. Messages auto-delete server-side on read — no persistent store, no forensic trace.

![](https://img.shields.io/badge/AES--256_E2E-6e7681?style=flat-square&labelColor=1a1f2a)
![](https://img.shields.io/badge/Zero_Plaintext-6e7681?style=flat-square&labelColor=1a1f2a)
![](https://img.shields.io/badge/Auto_Deletion-6e7681?style=flat-square&labelColor=1a1f2a)

[![View repository](https://img.shields.io/badge/View_Repository-ZeroTrace-1f6feb?style=flat-square&logo=github&logoColor=white&labelColor=0d1117)](https://github.com/edwii-78/ZeroTrace-AES-Encrypted-Messaging-App-With-ServerSide-AutoDeletion)

</td></tr></table>

<br/>

---

<br/>

## Stack

**Detection & SIEM** &nbsp;&nbsp; ![Wazuh](https://img.shields.io/badge/Wazuh-0d1a2d?style=flat-square&logo=wazuh&logoColor=79c0ff) ![Splunk](https://img.shields.io/badge/Splunk-0d1a2d?style=flat-square&logo=splunk&logoColor=79c0ff) ![Sentinel](https://img.shields.io/badge/Microsoft_Sentinel-0d1a2d?style=flat-square&logo=microsoftazure&logoColor=79c0ff) ![Defender XDR](https://img.shields.io/badge/Defender_XDR-0d1a2d?style=flat-square&logo=microsoftdefender&logoColor=79c0ff) ![Grafana](https://img.shields.io/badge/Grafana-0d1a2d?style=flat-square&logo=grafana&logoColor=79c0ff)

**Network & IDS/IPS** &nbsp;&nbsp; ![Suricata](https://img.shields.io/badge/Suricata-2d1010?style=flat-square&logoColor=ff7b72) ![Wireshark](https://img.shields.io/badge/Wireshark-2d1010?style=flat-square&logo=wireshark&logoColor=ff7b72) ![Nmap](https://img.shields.io/badge/Nmap-2d1010?style=flat-square&logoColor=ff7b72) ![Pi-hole](https://img.shields.io/badge/Pi--hole-2d1010?style=flat-square&logo=pi-hole&logoColor=ff7b72)

**Endpoint & Forensics** &nbsp;&nbsp; ![Sysmon](https://img.shields.io/badge/Sysmon-2a1f08?style=flat-square&logo=windows&logoColor=e3b341) ![Autopsy](https://img.shields.io/badge/Autopsy-2a1f08?style=flat-square&logoColor=e3b341) ![Triage](https://img.shields.io/badge/Triage_Sandbox-2a1f08?style=flat-square&logoColor=e3b341) ![Burp Suite](https://img.shields.io/badge/Burp_Suite-2a1f08?style=flat-square&logoColor=e3b341)

**Identity & Cloud** &nbsp;&nbsp; ![Entra ID](https://img.shields.io/badge/Entra_ID-160f2d?style=flat-square&logo=microsoftazure&logoColor=d2a8ff) ![Active Directory](https://img.shields.io/badge/Active_Directory-160f2d?style=flat-square&logo=windows&logoColor=d2a8ff) ![Logic Apps](https://img.shields.io/badge/Logic_Apps-160f2d?style=flat-square&logo=microsoftazure&logoColor=d2a8ff)

**Frameworks** &nbsp;&nbsp; ![MITRE](https://img.shields.io/badge/MITRE_ATT%26CK-1f2d1f?style=flat-square&logoColor=56d364) ![Linux](https://img.shields.io/badge/Linux-1f2d1f?style=flat-square&logo=linux&logoColor=56d364) ![Kali](https://img.shields.io/badge/Kali-1f2d1f?style=flat-square&logo=kalilinux&logoColor=56d364) ![Windows Server](https://img.shields.io/badge/Windows_Server-1f2d1f?style=flat-square&logo=windows&logoColor=56d364)

**Languages & Query** &nbsp;&nbsp; ![Python](https://img.shields.io/badge/Python-1f1a2d?style=flat-square&logo=python&logoColor=bc8cff) ![Bash](https://img.shields.io/badge/Bash-1f1a2d?style=flat-square&logo=gnubash&logoColor=bc8cff) ![SPL](https://img.shields.io/badge/SPL-1f1a2d?style=flat-square&logoColor=bc8cff) ![KQL](https://img.shields.io/badge/KQL-1f1a2d?style=flat-square&logoColor=bc8cff)

<br/>

---

<br/>

## Activity

> Stats update every 24 hours. Each committed detection rule, SPL/KQL query, or lab update moves these numbers.

<div align="center">

<img height="195" src="https://github-readme-stats.vercel.app/api?username=edwii-78&show_icons=true&theme=github_dark&bg_color=0d1117&title_color=e6edf3&text_color=8b949e&icon_color=1f6feb&border_color=21262d&include_all_commits=true&count_private=true&border_radius=6&rank_icon=github&card_width=740"/>

<br/><br/>

*Each cell is a log event. The red sweep is the detection scan.*

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream.svg"/>
  <img alt="SOC Log Stream" src="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream-dark.svg"/>
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
| IAM Job Simulation | Forage — TCS | `Active` |
| Cybersecurity Simulations | Forage — Deloitte · AIG · Mastercard | `Active` |

*Pursuing: CNSP · AWS Cloud Practitioner · TryHackMe SOC Level 1 · AI Security*

<br/>

---

<br/>

## Vulnerability Research

| | |
|:---|:---|
| **Scope** | Indian government portals, universities, public institutions |
| **Findings** | 15+ vulnerabilities responsibly disclosed |
| **Classes** | SQL injection · XSS · DNS cache poisoning · clickjacking · auth bypass |
| **Notable** | IIT Madras — verified and acknowledged |
| **Recognition** | CERT-In Hall of Fame — nominated twice, under review |

<br/>

---

<br/>

## TryHackMe

<div align="center">

<a href="https://tryhackme.com/p/edwindominic7878">
<img src="https://raw.githubusercontent.com/edwii-78/edwii-78/main/assets/thm-stats.svg"
     width="760" alt="TryHackMe — edwindominic7878"/>
</a>

<br/><br/>

![Pre-Security](https://img.shields.io/badge/Pre--Security-Completed-238636?style=flat-square&labelColor=0d1117)
![SOC Level 1](https://img.shields.io/badge/SOC_Level_1-In_Progress-1f6feb?style=flat-square&labelColor=0d1117)
![AI Security](https://img.shields.io/badge/AI_Security-In_Progress-1f6feb?style=flat-square&labelColor=0d1117)

</div>
