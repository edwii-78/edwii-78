<div align="center">
<img src="https://raw.githubusercontent.com/edwii-78/edwii-78/main/header.svg" width="100%" alt="Edwin Dominic — Security Operations"/>
</div>

<br/>

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=ui-monospace%2CSFMono-Regular%2C+SF+Mono%2CConsolas%2Cmonospace&size=13&duration=3200&pause=1000&color=8B949E&background=0D111700&center=true&vCenter=true&width=680&height=28&lines=SOC+Analyst+%E2%80%94+Detection+Engineering+%C2%B7+Threat+Analysis+%C2%B7+Malware+IR;AsyncRAT+v0.5.8+%E2%80%94+10%2F10+sandbox+%C2%B7+live+C2+%C2%B7+SPL+hunting+queries+written.;UPS+phishing+IR+%E2%80%94+M365+tenant+abuse+bypassing+SPF%2FDKIM+%E2%80%94+documented." alt=""/>

<br/><br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-edwin78-0A66C2?style=flat-square&logo=linkedin&logoColor=white&labelColor=0d1117)](https://linkedin.com/in/edwin78)
[![Email](https://img.shields.io/badge/Email-edwindominic7878%40gmail.com-1f6feb?style=flat-square&logo=gmail&logoColor=white&labelColor=0d1117)](mailto:edwindominic7878@gmail.com)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-edwindominic7878-212C42?style=flat-square&logo=tryhackme&logoColor=white&labelColor=0d1117)](https://tryhackme.com/p/edwindominic7878)
[![Location](https://img.shields.io/badge/Kerala%2C_India-Open_to_Relocation-238636?style=flat-square&labelColor=0d1117)](mailto:edwindominic7878@gmail.com)

</div>

---

<br/>

## About

Produced professional-grade SOC investigation reports — a full behavioral malware analysis of AsyncRAT v0.5.8 and a credential phishing IR documenting authenticated Microsoft 365 tenant abuse to bypass SPF/DKIM filters. Both include MITRE ATT&CK mappings, IOC tables, and Splunk SPL hunting queries.

Detection engineering on Wazuh and Splunk — eight MITRE ATT&CK techniques detected end-to-end in a live Windows 11 lab. Raspberry Pi 4 running as an inline IPS with ML anomaly detection on a production network.

Independent vulnerability research — 15+ disclosures to Indian government portals and institutions, IIT Madras acknowledged, CERT-In Hall of Fame nominated twice.

Open to SOC analyst, detection engineer, and threat hunting roles — available to relocate anywhere.

<br/>

---

<br/>

## Investigations & Labs

<br/>

<table><tr><td>

**`OP-001`** &nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### AsyncRAT v0.5.8 — Behavioral Malware Analysis & SOC Investigation
`Triage Sandbox` &nbsp;·&nbsp; `Static Config Extraction` &nbsp;·&nbsp; `MITRE ATT&CK` &nbsp;·&nbsp; `Splunk SPL Hunting`

Sample `95dedfab...fd2b76a2` — malicious score **10/10**. Static configuration extraction recovered live C2 infrastructure, AES key, mutex `LtyEIcOsTiXq`, install path, and persistence filename without executing the sample. Dynamic detonation confirmed installation to roaming profile, `OnLogon` scheduled task at highest run level, `SeDebugPrivilege` acquisition, and 25 C2 connections across four ports. Persistence validated — payload observed relaunching as an unparented top-level process. Three Splunk SPL hunting queries written: task name, C2 domain/IP, installer-batch pattern.

| Field | Detail |
|:---|:---|
| Static extraction | AES key · mutex `LtyEIcOsTiXq` · 6 C2 hosts · install path |
| Persistence | `schtasks /sc onlogon /rl highest` → `%AppData%\windown10.exe` |
| C2 | 6 domains · `34.76.205.124` · ports 80, 443, 4444, 5555 of 6 configured |
| Privilege | `SeDebugPrivilege` — arbitrary process handle access |
| Hunting | 3 SPL queries: task name · C2 indicators · installer-batch pattern |

![](https://img.shields.io/badge/T1059.003-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1053.005-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1082-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1614.001-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/SeDebugPrivilege-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Static_Config_Extraction-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-AsyncRAT_Analysis-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/AsyncRAT-Malware-Analysis-and-SOC-Investigation)

</td></tr></table>

<br/>

<table><tr><td>

**`OP-002`** &nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### Email Phishing Investigation — UPS Brand Impersonation / Credential Harvesting
`Header Forensics` &nbsp;·&nbsp; `SPF/DKIM/DMARC` &nbsp;·&nbsp; `Threat Intel Enrichment` &nbsp;·&nbsp; `IOC Analysis`

Full SOC-grade credential phishing IR. Sender domain `ali001.sarakzit.za.com` passed SPF, DKIM, and ARC — attacker legitimately owned a Microsoft 365 tenant to inherit Microsoft's IP reputation and bypass authentication-based filtering. Redirect chain: `t.co/f9tVtkdJm3` → `zoomertar.com` (VT 2/91, Redemption Period). Hidden tracking pixels on `199.192.27.195` (135 passive DNS resolutions, PayPal/Amazon phishing history) confirmed mailbox fingerprinting. Attack chain reconstructed across 10 stages.

| Field | Detail |
|:---|:---|
| Key finding | Authenticated M365 tenant abuse — SPF/DKIM pass ≠ legitimacy |
| Phishing domain | `zoomertar.com` — VT 2/91 · Redemption Period · IP churn |
| Tracking infra | `199.192.27.195` — 135 passive DNS resolutions · PayPal/Amazon phish history |
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

**`OP-003`** &nbsp; ![](https://img.shields.io/badge/PRODUCTION-238636?style=flat-square&labelColor=0d1117)

### DefenderPi — Inline IPS with ML Anomaly Detection
`Raspberry Pi 4` &nbsp;·&nbsp; `Suricata` &nbsp;·&nbsp; `scikit-learn` &nbsp;·&nbsp; `Redis` &nbsp;·&nbsp; `Grafana` &nbsp;·&nbsp; `Pi-hole`

Raspberry Pi 4 deployed **inline on a live network** — not a VM. Suricata in NFQUEUE mode inspects every packet; confirmed threats trigger automated iptables/ipset block rules. Secondary ML layer (K-Means + Isolation Forest) catches behavioural anomalies signatures miss. Redis caches enrichment data. Grafana dashboards the EVE JSON feed. Pi-hole + Unbound handles recursive DNS filtering. Telegram delivers real-time alerts.

| Component | Role |
|:---|:---|
| Suricata NFQUEUE | Inline packet inspection + rule-based detection |
| K-Means · Isolation Forest | Behavioural anomaly detection layer |
| iptables / ipset | Automated block enforcement |
| Redis | Threat intel enrichment cache |
| Pi-hole + Unbound | Malicious domain filtering + recursive DNS |

![](https://img.shields.io/badge/Anomaly_Detection-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Network_IDS-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Auto_Response-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Threat_Intel-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/DNS_Defence-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-DefenderPi-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/DefenderPi)

</td></tr></table>

<br/>

<table><tr><td>

**`OP-004`** &nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### Wazuh Detection Engineering Lab — Windows Threat Simulation
`Windows 11` &nbsp;·&nbsp; `Sysmon` &nbsp;·&nbsp; `Wazuh` &nbsp;·&nbsp; `MITRE ATT&CK` &nbsp;·&nbsp; `8 TTPs E2E`

Windows 11 lab with Sysmon telemetry feeding Wazuh. Eight MITRE ATT&CK techniques simulated and detected end-to-end — each producing a custom detection rule, a triggered alert, and a written incident report.

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

**`OP-005`** &nbsp; ![](https://img.shields.io/badge/BUILDING-d29922?style=flat-square&labelColor=0d1117)

### Splunk Detection Engineering Lab — Full Kill Chain Simulation
`Splunk Enterprise` &nbsp;·&nbsp; `SPL` &nbsp;·&nbsp; `MITRE ATT&CK` &nbsp;·&nbsp; `LOLBins`

SPL-based detection across a complete attack chain — each phase has a detection built and validated before moving to the next. Capstone: full simulation producing an executive-ready IR report.

| Phase | Attack | Detection |
|:------|:-------|:----------|
| 1 | Phishing — initial access | Attachment heuristics · email header analysis |
| 2 | WinRM lateral movement | Event ID 4624 type-3 · WinRM service abuse |
| 3 | LSASS credential dump | Process access events · LSASS memory reads |
| 4 | C2 beacon establishment | Beaconing interval regularity · JA3 fingerprinting |
| 5 | Staged data exfiltration | Large outbound transfers · Certutil / MSHTA abuse |
| 6 | Ransomware detonation | Mass file rename · shadow copy deletion |

![](https://img.shields.io/badge/T1566-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1021-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1003-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1071-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1560-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1486-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-Splunk_Lab-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/Splunk-SOC-Detection-Engineering-Lab)

</td></tr></table>

<br/>

<table><tr><td>

**`OP-006`** &nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### ZeroTrace — AES-256 Encrypted Messenger
`Flutter` &nbsp;·&nbsp; `Firebase` &nbsp;·&nbsp; `Node.js` &nbsp;·&nbsp; `AES-256 E2E`

Flutter + Firebase + Node.js messaging app built security-first. AES-256 encryption applied on-device before transit — server never handles plaintext. Messages auto-delete server-side on read, leaving no persistent store and no forensic trace.

| Security Property | Implementation |
|:-----------------|:---------------|
| Confidentiality | AES-256 E2E — encrypted before leaving device |
| Server access | Zero plaintext — server only handles ciphertext |
| Persistence | Auto-deletion on read — no message store |

![](https://img.shields.io/badge/AES--256_E2E-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Zero_Plaintext-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Auto_Deletion-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Privacy_by_Design-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-ZeroTrace-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/ZeroTrace-AES-Encrypted-Messaging-App-With-ServerSide-AutoDeletion)

</td></tr></table>

<br/>

---

<br/>

## Stack

<br/>

**Detection & SIEM** &nbsp;—&nbsp; ![Wazuh](https://img.shields.io/badge/Wazuh-0d1117?style=flat-square&logo=wazuh&logoColor=79c0ff&labelColor=0d1117&color=0d2137) ![Splunk](https://img.shields.io/badge/Splunk-0d1117?style=flat-square&logo=splunk&logoColor=79c0ff&labelColor=0d1117&color=0d2137) ![Microsoft Sentinel](https://img.shields.io/badge/Microsoft_Sentinel-0d1117?style=flat-square&logo=microsoftazure&logoColor=79c0ff&labelColor=0d1117&color=0d2137) ![Grafana](https://img.shields.io/badge/Grafana-0d1117?style=flat-square&logo=grafana&logoColor=79c0ff&labelColor=0d1117&color=0d2137)

**Network & IDS/IPS** &nbsp;—&nbsp; ![Suricata](https://img.shields.io/badge/Suricata-0d1117?style=flat-square&logoColor=ff7b72&labelColor=0d1117&color=3d1f1f) ![Wireshark](https://img.shields.io/badge/Wireshark-0d1117?style=flat-square&logo=wireshark&logoColor=ff7b72&labelColor=0d1117&color=3d1f1f) ![Nmap](https://img.shields.io/badge/Nmap-0d1117?style=flat-square&logoColor=ff7b72&labelColor=0d1117&color=3d1f1f) ![Pi-hole](https://img.shields.io/badge/Pi--hole-0d1117?style=flat-square&logo=pi-hole&logoColor=ff7b72&labelColor=0d1117&color=3d1f1f)

**Endpoint & Forensics** &nbsp;—&nbsp; ![Sysmon](https://img.shields.io/badge/Sysmon-0d1117?style=flat-square&logo=windows&logoColor=e3b341&labelColor=0d1117&color=2a1f08) ![Autopsy](https://img.shields.io/badge/Autopsy-0d1117?style=flat-square&logoColor=e3b341&labelColor=0d1117&color=2a1f08) ![Triage Sandbox](https://img.shields.io/badge/Triage_Sandbox-0d1117?style=flat-square&logoColor=e3b341&labelColor=0d1117&color=2a1f08) ![Burp Suite](https://img.shields.io/badge/Burp_Suite-0d1117?style=flat-square&logoColor=e3b341&labelColor=0d1117&color=2a1f08)

**Frameworks & OS** &nbsp;—&nbsp; ![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-0d1117?style=flat-square&logoColor=56d364&labelColor=0d1117&color=1f2d1f) ![Linux](https://img.shields.io/badge/Linux-0d1117?style=flat-square&logo=linux&logoColor=56d364&labelColor=0d1117&color=1f2d1f) ![Kali Linux](https://img.shields.io/badge/Kali-0d1117?style=flat-square&logo=kalilinux&logoColor=56d364&labelColor=0d1117&color=1f2d1f) ![Windows Server](https://img.shields.io/badge/Windows_Server-0d1117?style=flat-square&logo=windows&logoColor=56d364&labelColor=0d1117&color=1f2d1f)

**Languages & Query** &nbsp;—&nbsp; ![Python](https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d) ![Bash](https://img.shields.io/badge/Bash-0d1117?style=flat-square&logo=gnubash&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d) ![SPL](https://img.shields.io/badge/SPL-0d1117?style=flat-square&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d) ![KQL](https://img.shields.io/badge/KQL-0d1117?style=flat-square&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d) ![C++](https://img.shields.io/badge/C++-0d1117?style=flat-square&logo=cplusplus&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d)

<br/>

---

<br/>

## Activity

<div align="center">

<img height="195" src="https://github-readme-stats.vercel.app/api?username=edwii-78&show_icons=true&theme=github_dark&bg_color=0d1117&title_color=e6edf3&text_color=8b949e&icon_color=1f6feb&border_color=21262d&include_all_commits=true&count_private=true&border_radius=6&rank_icon=github&card_width=760"/>

<br/><br/>

**SIEM Log Stream &nbsp;·&nbsp; Contribution Activity**

> Each cell is a log event. The red scan line is the detection sweep.

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

| Certification | Issuer |
|:---|:---|
| Certified Ethical Hacker — CEH v13 | EC-Council |
| Certified Secure Computer User — CSCU | EC-Council |
| Introduction to Microsoft Sentinel | Microsoft |
| Intro to Splunk | Splunk |
| Cyber Threat Intelligence 101 | arcX |
| Job Simulations — TATA · Deloitte · AIG · Mastercard | Forage |

*Currently pursuing: CNSP (SecOps Group) · AWS Cloud Practitioner · TryHackMe SOC Level 1 · AI Security*

<br/>

---

<br/>

## Vulnerability Research

| | |
|:---|:---|
| Scope | Indian government portals · universities · public institutions |
| Findings | 15+ vulnerabilities — SQLi · XSS · DNS cache poisoning · clickjacking · auth bypass |
| Recognition | IIT Madras — verified · CERT-In Hall of Fame — nominated twice, under review |

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

[![TryHackMe](https://img.shields.io/badge/TryHackMe-edwindominic7878-212C42?style=flat-square&logo=tryhackme&logoColor=white&labelColor=0d1117)](https://tryhackme.com/p/edwindominic7878)
&nbsp;
![Pre-Security](https://img.shields.io/badge/Pre--Security-Completed-238636?style=flat-square&labelColor=0d1117)
![SOC Level 1](https://img.shields.io/badge/SOC_Level_1-In_Progress-1f6feb?style=flat-square&labelColor=0d1117)
![AI Security](https://img.shields.io/badge/AI_Security-In_Progress-1f6feb?style=flat-square&labelColor=0d1117)

</div>

Done

You are out of free mess
