<div align="center">
<img src="https://raw.githubusercontent.com/edwii-78/edwii-78/main/header.svg" width="100%" alt="Edwin Dominic — Security Operations"/>
</div>

<br/>

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=ui-monospace%2CSFMono-Regular%2C+SF+Mono%2CConsolas%2Cmonospace&size=13&duration=3000&pause=1000&color=8B949E&background=0D111700&center=true&vCenter=true&width=720&height=28&lines=AsyncRAT+v0.5.8+analysed+%E2%80%94+static+config+extraction+%2B+live+C2+confirmed.;UPS+phishing+IR+%E2%80%94+SPF%2FDKIM+bypass+via+M365+tenant+abuse.;Wazuh+lab+%E2%80%94+8+MITRE+ATT%26CK+techniques+detected+end-to-end.;15%2B+CVEs+disclosed+%E2%80%94+IIT+Madras+%C2%B7+CERT-In+HoF+nominated+2%C3%97.;CEH+v13+%C2%B7+CSCU+%C2%B7+Splunk+%C2%B7+Microsoft+Sentinel+%C2%B7+arcX+CTI." alt=""/>
</div>

<br/>

---

## About

Produced professional-grade SOC investigation reports — a full behavioral malware analysis of AsyncRAT v0.5.8 using Triage Sandbox, and a credential phishing IR documenting authenticated Microsoft 365 tenant abuse to bypass SPF/DKIM filters. Both reports include MITRE ATT&CK mappings, IOC tables, containment recommendations, and Splunk SPL hunting queries.

Detection engineering labs built on **Wazuh** and **Splunk**, with **Sysmon** telemetry, **Suricata** inline IDS, and **MITRE ATT&CK** as the validation framework. Eight techniques detected end-to-end in a live Windows 11 lab. A Raspberry Pi 4 runs as an inline IPS with ML anomaly detection on a production network.

Independent vulnerability research — 15+ disclosures to Indian government portals and institutions, IIT Madras acknowledged, CERT-In Hall of Fame nominated twice.

Open to SOC analyst, detection engineer, and threat hunting roles — available to relocate anywhere.

```
edwindominic7878@gmail.com  ·  linkedin.com/in/edwin78  ·  Kerala, India
```

---

## Investigations & Labs

<br/>

<!--  OP-001  -->
<table><tr><td>

**`OP-001`** &nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### AsyncRAT v0.5.8 — Behavioral Malware Analysis & SOC Investigation
`Triage Sandbox` &nbsp;·&nbsp; `Static Config Extraction` &nbsp;·&nbsp; `MITRE ATT&CK` &nbsp;·&nbsp; `Splunk SPL Hunting`

Sample `95dedfab...fd2b76a2` — malicious score **10/10**. Static configuration extraction recovered live C2 infrastructure, AES encryption key, mutex `LtyEIcOsTiXq`, install path, and persistence filename without executing the sample. Dynamic detonation on Triage (Windows 11 21H2 x64) confirmed installation to roaming profile, `OnLogon` scheduled task requesting highest run level, `SeDebugPrivilege` acquisition, host/locale reconnaissance, and 25 outbound C2 connections across four ports. Persistence validated: payload observed relaunching as an unparented top-level process, confirming the scheduled task fired. Three Splunk SPL hunting queries written: scheduled task by name, C2 domain/IP, and installer-batch pattern.

| Field | Detail |
|:---|:---|
| Static extraction | AES key · mutex `LtyEIcOsTiXq` · 6 C2 hosts · install path recovered |
| Persistence | `schtasks /sc onlogon /rl highest` → `%AppData%\windown10.exe` |
| C2 | 6 domains · `34.76.205.124` · ports 80, 443, 4444, 5555 observed of 6 configured |
| Privilege escalation | `SeDebugPrivilege` — arbitrary process handle access |
| Hunting | 3 Splunk SPL queries: task name · C2 indicators · installer-batch pattern |

![](https://img.shields.io/badge/T1059.003_CMD-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1053.005_Sched_Task-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1082_Sys_Discovery-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1614.001_Lang_Discovery-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/SeDebugPrivilege-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Static_Config_Extraction-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-AsyncRAT_Analysis-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/AsyncRAT-Malware-Analysis-and-SOC-Investigation)

</td></tr></table>

<br/>

<!--  OP-002  -->
<table><tr><td>

**`OP-002`** &nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### Email Phishing Investigation — UPS Brand Impersonation / Credential Harvesting
`Header Forensics` &nbsp;·&nbsp; `SPF/DKIM/DMARC` &nbsp;·&nbsp; `Threat Intel Enrichment` &nbsp;·&nbsp; `IOC Analysis`

Full SOC-grade credential phishing IR. Sender domain `ali001.sarakzit.za.com` passed SPF, DKIM, and ARC — the attacker legitimately owned a Microsoft 365 tenant to inherit Microsoft's IP reputation and bypass authentication-based filtering. Redirect chain: `t.co/f9tVtkdJm3` → `zoomertar.com` (2/91 VT, Redemption Period — disposable infrastructure). Hidden tracking pixels on `199.192.27.195` (135 passive DNS resolutions, PayPal/Amazon phishing history) confirmed mailbox fingerprinting. Attack chain reconstructed across 10 stages. IOC table, MITRE mapping, containment plan, and detection opportunities produced.

| Field | Detail |
|:---|:---|
| Key finding | Authenticated M365 tenant abuse — SPF/DKIM pass ≠ legitimacy |
| Phishing domain | `zoomertar.com` — VT 2/91 · Redemption Period · IP churn across lifetime |
| Tracking infra | `199.192.27.195` — Namecheap · 135 historical resolutions · PayPal/Amazon phish |
| Redirect | `t.co` shortener → `zoomertar.com` (offline at investigation — standard for phish) |
| Output | IOC table · 10-stage attack chain · MITRE mapping · containment + hunting plan |

![](https://img.shields.io/badge/T1566_Phishing-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1566.002_Spearphishing-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1199_Trusted_Relationship-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1589_Victim_Recon-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1204_User_Execution-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Header_Forensics-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-Phishing_IR-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/Phishing-Email-Investigation-)

</td></tr></table>

<br/>

<!--  OP-003  -->
<table><tr><td>

**`OP-003`** &nbsp; ![](https://img.shields.io/badge/PRODUCTION-238636?style=flat-square&labelColor=0d1117)

### DefenderPi &nbsp;—&nbsp; Inline IPS with ML Anomaly Detection
`Raspberry Pi 4` &nbsp;·&nbsp; `Suricata` &nbsp;·&nbsp; `scikit-learn` &nbsp;·&nbsp; `Redis` &nbsp;·&nbsp; `Grafana` &nbsp;·&nbsp; `Pi-hole`

Raspberry Pi 4 deployed **inline on a live network** — not a VM. Suricata in NFQUEUE mode inspects every packet; confirmed threats trigger automated iptables/ipset block rules. A secondary ML layer (K-Means + Isolation Forest) catches behavioural anomalies that signatures miss. Redis caches enrichment data. Grafana dashboards the EVE JSON feed. Pi-hole + Unbound handles recursive DNS filtering. Telegram delivers real-time alerts.

| Component | Role |
|:---|:---|
| Suricata NFQUEUE | Inline packet inspection + rule-based detection |
| K-Means · Isolation Forest | Behavioural anomaly detection layer |
| iptables / ipset | Automated block enforcement |
| Redis | Threat intel enrichment cache |
| Pi-hole + Unbound | Malicious domain filtering + recursive DNS |
| Grafana | EVE JSON telemetry dashboard |

![](https://img.shields.io/badge/Anomaly_Detection-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Network_IDS-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Auto_Response-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Threat_Intel-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/DNS_Defence-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-DefenderPi-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/DefenderPi)

</td></tr></table>

<br/>

<!--  OP-004  -->
<table><tr><td>

**`OP-004`** &nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### Wazuh Detection Engineering Lab &nbsp;—&nbsp; Windows Threat Simulation
`Windows 11` &nbsp;·&nbsp; `Sysmon` &nbsp;·&nbsp; `Wazuh` &nbsp;·&nbsp; `MITRE ATT&CK` &nbsp;·&nbsp; `8 TTPs E2E`

Windows 11 lab with Sysmon telemetry feeding Wazuh. Eight MITRE ATT&CK techniques simulated and detected end-to-end — each producing a custom detection rule, a triggered alert, and a written incident investigation report. Alert delivery via Gmail SMTP and Telegram.

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

![](https://img.shields.io/badge/T1046_Recon-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1059_PowerShell-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1547_Persistence-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1543_Service-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1021_PsExec-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1550_NTLM-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1078_Accounts-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-Wazuh_SOC_Lab-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/Wazuh-SOC-Detection-Engineering-Lab)

</td></tr></table>

<br/>

<!--  OP-005  -->
<table><tr><td>

**`OP-005`** &nbsp; ![](https://img.shields.io/badge/IN_PROGRESS-d29922?style=flat-square&labelColor=0d1117)

### Splunk Detection Engineering Lab &nbsp;—&nbsp; Full Kill Chain Simulation
`Splunk Enterprise` &nbsp;·&nbsp; `SPL` &nbsp;·&nbsp; `MITRE ATT&CK` &nbsp;·&nbsp; `LOLBins` &nbsp;·&nbsp; `Kill Chain`

Splunk Enterprise environment. SPL-based detection across a complete attack chain — each phase has a detection built and validated before moving to the next. Capstone: full simulation producing an executive-ready IR report.

| Phase | Attack | Detection |
|:------|:-------|:----------|
| 1 | Phishing — initial access | Attachment heuristics · email header analysis |
| 2 | WinRM lateral movement | Event ID 4624 type-3 · WinRM service abuse |
| 3 | LSASS credential dump | Process access events · LSASS memory reads |
| 4 | C2 beacon establishment | Beaconing interval regularity · JA3 fingerprinting |
| 5 | Staged data exfiltration | Large outbound transfers · Certutil / MSHTA abuse |
| 6 | Ransomware detonation | Mass file rename · shadow copy deletion |

![](https://img.shields.io/badge/T1566_Phishing-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1021_Lateral_Move-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1003_Cred_Dump-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1071_C2-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1560_Exfil-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1486_Ransomware-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-Splunk_Lab-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/Splunk-SOC-Detection-Engineering-Lab)

</td></tr></table>

<br/>

<!--  OP-006  -->
<table><tr><td>

**`OP-006`** &nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117)

### ZeroTrace &nbsp;—&nbsp; AES-256 Encrypted Messenger
`Flutter` &nbsp;·&nbsp; `Firebase` &nbsp;·&nbsp; `Node.js` &nbsp;·&nbsp; `AES-256 E2E` &nbsp;·&nbsp; `Auto-Deletion`

Flutter + Firebase + Node.js messaging app built security-first. AES-256 encryption applied on-device before transit — the server never handles plaintext. Messages auto-delete server-side on read, leaving no persistent store and no forensic trace.

| Security Property | Implementation |
|:-----------------|:---------------|
| Confidentiality | AES-256 E2E — encrypted before leaving device |
| Server access | Zero plaintext — server only handles ciphertext |
| Persistence | Auto-deletion on read — no message store |
| Integrity | Server-side tamper detection |

![](https://img.shields.io/badge/AES--256_E2E-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Zero_Plaintext-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Auto_Deletion-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Privacy_by_Design-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-ZeroTrace-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/ZeroTrace-AES-Encrypted-Messaging-App-With-ServerSide-AutoDeletion)

</td></tr></table>

---

## Stack

**Detection & SIEM**

![Wazuh](https://img.shields.io/badge/Wazuh-0d1117?style=flat-square&logo=wazuh&logoColor=79c0ff&labelColor=0d1117&color=0d2137)
![Splunk](https://img.shields.io/badge/Splunk-0d1117?style=flat-square&logo=splunk&logoColor=79c0ff&labelColor=0d1117&color=0d2137)
![Microsoft Sentinel](https://img.shields.io/badge/Microsoft_Sentinel-0d1117?style=flat-square&logo=microsoftazure&logoColor=79c0ff&labelColor=0d1117&color=0d2137)
![Grafana](https://img.shields.io/badge/Grafana-0d1117?style=flat-square&logo=grafana&logoColor=79c0ff&labelColor=0d1117&color=0d2137)

**Network & IDS/IPS**

![Suricata](https://img.shields.io/badge/Suricata-0d1117?style=flat-square&logoColor=ff7b72&labelColor=0d1117&color=3d1f1f)
![Wireshark](https://img.shields.io/badge/Wireshark-0d1117?style=flat-square&logo=wireshark&logoColor=ff7b72&labelColor=0d1117&color=3d1f1f)
![Nmap](https://img.shields.io/badge/Nmap-0d1117?style=flat-square&logoColor=ff7b72&labelColor=0d1117&color=3d1f1f)
![Pi-hole](https://img.shields.io/badge/Pi--hole-0d1117?style=flat-square&logo=pi-hole&logoColor=ff7b72&labelColor=0d1117&color=3d1f1f)
![iptables](https://img.shields.io/badge/iptables-0d1117?style=flat-square&logo=linux&logoColor=ff7b72&labelColor=0d1117&color=3d1f1f)

**Endpoint & Forensics**

![Sysmon](https://img.shields.io/badge/Sysmon-0d1117?style=flat-square&logo=windows&logoColor=e3b341&labelColor=0d1117&color=2a1f08)
![Autopsy](https://img.shields.io/badge/Autopsy-0d1117?style=flat-square&logoColor=e3b341&labelColor=0d1117&color=2a1f08)
![Triage Sandbox](https://img.shields.io/badge/Triage_Sandbox-0d1117?style=flat-square&logoColor=e3b341&labelColor=0d1117&color=2a1f08)
![Metasploit](https://img.shields.io/badge/Metasploit-0d1117?style=flat-square&logoColor=e3b341&labelColor=0d1117&color=2a1f08)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-0d1117?style=flat-square&logoColor=e3b341&labelColor=0d1117&color=2a1f08)

**Frameworks & Platforms**

![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-0d1117?style=flat-square&logoColor=56d364&labelColor=0d1117&color=1f2d1f)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-0d1117?style=flat-square&logo=raspberrypi&logoColor=56d364&labelColor=0d1117&color=1f2d1f)
![Linux](https://img.shields.io/badge/Linux-0d1117?style=flat-square&logo=linux&logoColor=56d364&labelColor=0d1117&color=1f2d1f)
![Windows Server](https://img.shields.io/badge/Windows_Server-0d1117?style=flat-square&logo=windows&logoColor=56d364&labelColor=0d1117&color=1f2d1f)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-0d1117?style=flat-square&logo=kalilinux&logoColor=56d364&labelColor=0d1117&color=1f2d1f)

**Languages & Query**

![Python](https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d)
![Bash](https://img.shields.io/badge/Bash-0d1117?style=flat-square&logo=gnubash&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d)
![SPL](https://img.shields.io/badge/Splunk_SPL-0d1117?style=flat-square&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d)
![KQL](https://img.shields.io/badge/KQL-0d1117?style=flat-square&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d)
![C++](https://img.shields.io/badge/C++-0d1117?style=flat-square&logo=cplusplus&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d)
![Flutter](https://img.shields.io/badge/Flutter-0d1117?style=flat-square&logo=flutter&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d)

---

## Activity

> Stats update every 24 hours · Streak updates within 6 hours · Commit regularly — each lab update, detection rule, or query addition counts.

<div align="center">

<img height="200" src="https://github-readme-stats.vercel.app/api?username=edwii-78&show_icons=true&theme=github_dark&bg_color=0d1117&title_color=e6edf3&text_color=8b949e&icon_color=1f6feb&border_color=21262d&include_all_commits=true&count_private=true&border_radius=6&rank_icon=github&card_width=420"/>
&nbsp;
<img height="200" src="https://github-readme-stats.vercel.app/api/top-langs/?username=edwii-78&layout=compact&theme=github_dark&bg_color=0d1117&title_color=e6edf3&text_color=8b949e&border_color=21262d&langs_count=8&border_radius=6&card_width=320"/>

<br/><br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=edwii-78&background=0d1117&ring=1f6feb&fire=f85149&currStreakLabel=e6edf3&sideLabels=8b949e&dates=6e7681&border=21262d&stroke=21262d&currStreakNum=e6edf3&sideNums=c9d1d9&border_radius=6&date_format=j%20M%5B%20Y%5D&card_width=760"/>

</div>

<br/>

**SIEM Log Stream &nbsp;·&nbsp; Contribution Activity**

> Each cell is a log event. The red scan line is the detection sweep — same way a SIEM scans incoming telemetry.

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream.svg"/>
  <img alt="SOC Log Stream — Contribution Activity" src="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream-dark.svg"/>
</picture>
</div>

---

## Certifications

| Certification | Issuer | Status |
|:---|:---|:---:|
| Certified Ethical Hacker — CEH v13 | EC-Council | Active |
| Certified Secure Computer User — CSCU | EC-Council | Active |
| Introduction to Microsoft Sentinel | Microsoft | Active |
| Intro to Splunk | Splunk | Active |
| Cyber Threat Intelligence 101 | arcX | Active |
| Job Simulations — TATA · Deloitte · AIG · Mastercard | Forage | Active |
| Certified Network Security Practitioner — CNSP | SecOps Group | In progress |
| AWS Cloud Practitioner | Amazon Web Services | In progress |
| SOC Level 1 | TryHackMe | In progress |
| AI Security | TryHackMe | In progress |

---

## Vulnerability Research

Independent security research across Indian public-sector and institutional infrastructure.

- **15+ vulnerabilities** disclosed to government portals, universities, and public institutions
- Classes: SQL injection, stored/reflected XSS, DNS cache poisoning, clickjacking, authentication bypass
- IIT Madras — verified and acknowledged
- CERT-In Hall of Fame — nominated twice, under review
- All disclosures made through official channels before any public mention

---

## TryHackMe

<div align="center">

<a href="https://tryhackme.com/p/edwindominic7878">
  <img src="https://raw.githubusercontent.com/edwii-78/edwii-78/main/assets/thm-stats.svg"
       width="740" alt="TryHackMe stats — edwindominic7878"/>
</a>

<br/><br/>

[![TryHackMe Profile](https://img.shields.io/badge/TryHackMe-edwindominic7878-212C42?style=flat-square&logo=tryhackme&logoColor=white&labelColor=0d1117)](https://tryhackme.com/p/edwindominic7878)
&nbsp;
![Pre-Security](https://img.shields.io/badge/Pre--Security-Completed-238636?style=flat-square&labelColor=0d1117)
![SOC Level 1](https://img.shields.io/badge/SOC_Level_1-In_Progress-1f6feb?style=flat-square&labelColor=0d1117)
![AI Security](https://img.shields.io/badge/AI_Security-In_Progress-1f6feb?style=flat-square&labelColor=0d1117)

</div>
