<div align="center">
<img src="https://raw.githubusercontent.com/edwii-78/edwii-78/main/header.svg" width="100%" alt="Edwin Dominic — Security Operations"/>
</div>

<br/>

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=ui-monospace%2CSFMono-Regular%2C+SF+Mono%2CConsolas%2Cmonospace&size=13&duration=3500&pause=1200&color=8B949E&background=0D111700&center=true&vCenter=true&width=680&height=28&lines=Turning+noise+into+signal%2C+signals+into+action.;Detection+rules+that+catch+what+scanners+miss.;Every+log+is+a+clue.+Every+alert+is+a+story." alt=""/>
</div>

<br/>

---

## About

SOC analyst building detection engineering labs from scratch — designing environments, simulating attacks, writing detection rules, and producing incident reports that mirror real SOC workflows.

Core stack: **Wazuh** and **Splunk** for SIEM, **Sysmon** for Windows telemetry, **Suricata** for network IDS, **MITRE ATT&CK** as the detection framework. Eight techniques validated end-to-end in a live Windows 11 lab. A Raspberry Pi 4 runs as an inline IPS with ML-backed anomaly detection on my home network — production, not a VM.

Independent vulnerability research across Indian government and institutional portals — 15+ disclosures, IIT Madras acknowledged, CERT-In Hall of Fame nominated twice.

Building toward **Microsoft Sentinel**, **CNSP**, and **AWS Cloud Practitioner**. Open to SOC analyst, detection engineer, and threat hunting roles — available to relocate anywhere.

```
edwindominic7878@gmail.com  ·  linkedin.com/in/edwin78  ·  Kerala, India
```

---

## Projects

<br/>

<!--  OP-001  -->
<table><tr><td>

**`OP-001`** &nbsp; ![](https://img.shields.io/badge/PRODUCTION-238636?style=flat-square&labelColor=0d1117) &nbsp; ![](https://img.shields.io/badge/Network_Security-1f6feb?style=flat-square&labelColor=0d1117)

### DefenderPi &nbsp;—&nbsp; Inline IPS with ML Anomaly Detection
`Raspberry Pi 4` &nbsp;·&nbsp; `Suricata` &nbsp;·&nbsp; `scikit-learn` &nbsp;·&nbsp; `Redis` &nbsp;·&nbsp; `Grafana` &nbsp;·&nbsp; `Pi-hole`

Raspberry Pi 4 deployed **inline on a live network** — not a VM, not a lab simulation. Suricata runs in NFQUEUE mode, inspecting every packet in real time. Confirmed threats trigger automated iptables/ipset block rules. A secondary ML layer (K-Means clustering + Isolation Forest) detects behavioural anomalies that static signatures miss: slow scans, unusual traffic volumes, protocol deviation. Redis caches threat intel enrichment. Grafana dashboards the EVE JSON feed. Telegram delivers real-time SOC alerts. Pi-hole + Unbound handles DNS filtering with recursive resolution.

| Field | Detail |
|:---|:---|
| Platform | Raspberry Pi 4B — edge deployment |
| IDS engine | Suricata (NFQUEUE inline mode) |
| ML detection | K-Means clustering · Isolation Forest |
| Enforcement | Automated iptables · ipset block rules |
| Intel pipeline | Redis enrichment → Telegram SOC bot |
| DNS layer | Pi-hole + Unbound (recursive resolver) |

![](https://img.shields.io/badge/Network_Monitoring-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Anomaly_Detection-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Threat_Intel-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/DNS_Defence-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Auto_Response-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/ML_Pipeline-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-DefenderPi-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/DefenderPi)

</td></tr></table>

<br/>

<!--  OP-002  -->
<table><tr><td>

**`OP-002`** &nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117) &nbsp; ![](https://img.shields.io/badge/Detection_Engineering-1f6feb?style=flat-square&labelColor=0d1117)

### Wazuh Detection Engineering Lab &nbsp;—&nbsp; Windows Threat Simulation
`Windows 11` &nbsp;·&nbsp; `Sysmon` &nbsp;·&nbsp; `Wazuh SIEM` &nbsp;·&nbsp; `MITRE ATT&CK` &nbsp;·&nbsp; `8 Techniques E2E`

Windows 11 lab with Sysmon feeding telemetry into Wazuh. Eight MITRE ATT&CK techniques simulated and detected **end-to-end** — each producing a custom detection rule, a triggered Wazuh alert, and an SOC-style incident investigation report with full attack chain timeline reconstruction. Alert delivery via Gmail SMTP and Telegram bot.

| Field | Detail |
|:---|:---|
| SIEM | Wazuh + Sysmon |
| OS lab | Windows 11 |
| Framework | MITRE ATT&CK — 8 techniques validated |
| Event IDs | 4624 · 4625 · 4634 · 4672 · 7045 · 4104 · 13 |
| Alerting | Gmail SMTP + Telegram real-time bot |
| Output | 8 SOC-style incident investigation reports |

| # | Technique | Detection Method |
|:--|:----------|:-----------------|
| 1 | Reconnaissance — port scan, ping sweep | Sysmon net events + Wazuh correlation |
| 2 | Encoded PowerShell execution | Event ID 4104 · base64 pattern rules |
| 3 | Registry Run key persistence | Event ID 13 · registry value creation |
| 4 | Startup folder abuse | Sysmon file creation in startup path |
| 5 | Malicious Windows service install | Event ID 7045 · unusual binary path |
| 6 | PsExec lateral movement | Event IDs 4624 + 7045 + named pipe |
| 7 | SMB / NTLM auth monitoring | Event IDs 4624, 4625, 4634, 4672 |
| 8 | Privileged account abuse | Event ID 4672 + type-3 logon chain |

![](https://img.shields.io/badge/T1046_Reconnaissance-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1059_PowerShell-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1547_Persistence-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1543_Service_Abuse-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1021_PsExec-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1550_NTLM-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1078_Accounts-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1078_Privilege_Abuse-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-Wazuh_SOC_Lab-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/Wazuh-SOC-Detection-Engineering-Lab)

</td></tr></table>

<br/>

<!--  OP-003  -->
<table><tr><td>

**`OP-003`** &nbsp; ![](https://img.shields.io/badge/IN_PROGRESS-d29922?style=flat-square&labelColor=0d1117) &nbsp; ![](https://img.shields.io/badge/Threat_Hunting-1f6feb?style=flat-square&labelColor=0d1117)

### Splunk Detection Engineering Lab &nbsp;—&nbsp; Full Kill Chain Simulation
`Splunk Enterprise` &nbsp;·&nbsp; `SPL` &nbsp;·&nbsp; `MITRE ATT&CK` &nbsp;·&nbsp; `LOLBins` &nbsp;·&nbsp; `Kill Chain`

Splunk Enterprise environment. SPL-based detection across a **complete attack chain**: phishing initial access → WinRM lateral movement → LSASS credential dumping → C2 beaconing → staged exfiltration → ransomware detonation. Detections cover LOLBins (Certutil, MSHTA, Rundll32), encoded PowerShell, beaconing regularity analysis, and ransomware file extension patterns. Capstone: executive-ready IR report from a full simulation run.

| Field | Detail |
|:---|:---|
| SIEM | Splunk Enterprise |
| Query language | SPL (Search Processing Language) |
| LOLBins targeted | Certutil · MSHTA · Rundll32 · WinRM abuse |
| Credential attacks | LSASS dump detection · Pass-the-Hash |
| C2 detection | Beaconing regularity · JA3 fingerprinting |
| Capstone | Full multi-stage simulation + executive IR report |

| Phase | Attack Technique | Detection Focus |
|:------|:----------------|:----------------|
| 1 | Phishing — initial access | Email header analysis · attachment heuristics |
| 2 | WinRM lateral movement | Event ID 4624 type-3 · WinRM service abuse |
| 3 | LSASS credential dump | Process access events · LSASS memory reads |
| 4 | C2 beacon establishment | Beaconing interval regularity · outbound JA3 |
| 5 | Staged data exfiltration | Large outbound transfers · Certutil abuse |
| 6 | Ransomware detonation | Mass file rename · shadow copy deletion |

![](https://img.shields.io/badge/T1566_Phishing-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1021_WinRM-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1003_LSASS_Dump-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1071_C2_Beacon-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1560_Exfiltration-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/T1486_Ransomware-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/LOLBins_Certutil-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/LOLBins_MSHTA-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-Splunk_Lab-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/Splunk-SOC-Detection-Engineering-Lab)

</td></tr></table>

<br/>

<!--  OP-004  -->
<table><tr><td>

**`OP-004`** &nbsp; ![](https://img.shields.io/badge/COMPLETED-238636?style=flat-square&labelColor=0d1117) &nbsp; ![](https://img.shields.io/badge/Secure_Development-1f6feb?style=flat-square&labelColor=0d1117)

### ZeroTrace &nbsp;—&nbsp; AES-256 Encrypted Messenger
`Flutter` &nbsp;·&nbsp; `Firebase` &nbsp;·&nbsp; `Node.js` &nbsp;·&nbsp; `AES-256 E2E` &nbsp;·&nbsp; `Server-Side Auto-Deletion`

Flutter + Firebase + Node.js messaging application built **security-first**. AES-256 end-to-end encryption applied before transit — the server never sees plaintext. Messages auto-delete server-side on read, leaving no forensic trace. Designed to prove that strong cryptographic privacy does not require sacrificing usability.

| Field | Detail |
|:---|:---|
| Stack | Flutter + Firebase + Node.js |
| Encryption | AES-256 end-to-end — applied pre-transit |
| Key design | Zero server-side plaintext access |
| Privacy mechanism | Server-side auto-deletion on read |
| Threat model | Interception · server compromise · forensic analysis |
| Platform | Android / iOS |

| Security Property | Implementation |
|:-----------------|:---------------|
| Confidentiality | AES-256 encryption before leaving device |
| Integrity | Message auth — tampering detected server-side |
| Availability | Firebase distributed backend |
| Non-repudiation | Deletion-on-read — no persistent message store |
| Forward secrecy | Per-session key derivation |

![](https://img.shields.io/badge/AES--256_E2E-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Zero_Plaintext-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Auto_Deletion-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Key_Management-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Threat_Modelling-f85149?style=flat-square&labelColor=2d1f1f)
![](https://img.shields.io/badge/Privacy_by_Design-f85149?style=flat-square&labelColor=2d1f1f)

[![View repository](https://img.shields.io/badge/View_repository-ZeroTrace-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/ZeroTrace-AES-Encrypted-Messaging-App-With-ServerSide-AutoDeletion)

</td></tr></table>
---

## Stack

<!-- Each category is a labelled group — no blob of flat badges -->

**Detection & SIEM**

![Wazuh](https://img.shields.io/badge/Wazuh-0d1117?style=flat-square&logo=wazuh&logoColor=79c0ff&labelColor=0d1117&color=0d2137)
![Splunk](https://img.shields.io/badge/Splunk-0d1117?style=flat-square&logo=splunk&logoColor=79c0ff&labelColor=0d1117&color=0d2137)
![Microsoft Sentinel](https://img.shields.io/badge/Microsoft_Sentinel-0d1117?style=flat-square&logo=microsoftazure&logoColor=79c0ff&labelColor=0d1117&color=0d2137)
![Grafana](https://img.shields.io/badge/Grafana-0d1117?style=flat-square&logo=grafana&logoColor=79c0ff&labelColor=0d1117&color=0d2137)
![Elastic](https://img.shields.io/badge/Elastic-0d1117?style=flat-square&logo=elastic&logoColor=79c0ff&labelColor=0d1117&color=0d2137)

**Network & IDS/IPS**

![Suricata](https://img.shields.io/badge/Suricata-0d1117?style=flat-square&logoColor=ff7b72&labelColor=0d1117&color=3d1f1f)
![Wireshark](https://img.shields.io/badge/Wireshark-0d1117?style=flat-square&logo=wireshark&logoColor=ff7b72&labelColor=0d1117&color=3d1f1f)
![Nmap](https://img.shields.io/badge/Nmap-0d1117?style=flat-square&logoColor=ff7b72&labelColor=0d1117&color=3d1f1f)
![Pi-hole](https://img.shields.io/badge/Pi--hole-0d1117?style=flat-square&logo=pi-hole&logoColor=ff7b72&labelColor=0d1117&color=3d1f1f)
![iptables](https://img.shields.io/badge/iptables-0d1117?style=flat-square&logo=linux&logoColor=ff7b72&labelColor=0d1117&color=3d1f1f)

**Endpoint & Forensics**

![Sysmon](https://img.shields.io/badge/Sysmon-0d1117?style=flat-square&logo=windows&logoColor=e3b341&labelColor=0d1117&color=2a1f08)
![Autopsy](https://img.shields.io/badge/Autopsy-0d1117?style=flat-square&logoColor=e3b341&labelColor=0d1117&color=2a1f08)
![Metasploit](https://img.shields.io/badge/Metasploit-0d1117?style=flat-square&logoColor=e3b341&labelColor=0d1117&color=2a1f08)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-0d1117?style=flat-square&logoColor=e3b341&labelColor=0d1117&color=2a1f08)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-0d1117?style=flat-square&logo=kalilinux&logoColor=e3b341&labelColor=0d1117&color=2a1f08)

**Frameworks & Platforms**

![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-0d1117?style=flat-square&logoColor=56d364&labelColor=0d1117&color=1f2d1f)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-0d1117?style=flat-square&logo=raspberrypi&logoColor=56d364&labelColor=0d1117&color=1f2d1f)
![Linux](https://img.shields.io/badge/Linux-0d1117?style=flat-square&logo=linux&logoColor=56d364&labelColor=0d1117&color=1f2d1f)
![Windows Server](https://img.shields.io/badge/Windows_Server-0d1117?style=flat-square&logo=windows&logoColor=56d364&labelColor=0d1117&color=1f2d1f)
![Redis](https://img.shields.io/badge/Redis-0d1117?style=flat-square&logo=redis&logoColor=56d364&labelColor=0d1117&color=1f2d1f)

**Languages & Query**

![Python](https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d)
![Bash](https://img.shields.io/badge/Bash-0d1117?style=flat-square&logo=gnubash&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d)
![C++](https://img.shields.io/badge/C++-0d1117?style=flat-square&logo=cplusplus&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d)
![SPL](https://img.shields.io/badge/Splunk_SPL-0d1117?style=flat-square&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d)
![KQL](https://img.shields.io/badge/KQL-0d1117?style=flat-square&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d)
![Flutter](https://img.shields.io/badge/Flutter-0d1117?style=flat-square&logo=flutter&logoColor=bc8cff&labelColor=0d1117&color=1f1a2d)

---

## Activity

> Stats update every 24 hours. Streak and languages update within 6 hours.

<div align="center">

<img height="200" src="https://github-readme-stats.vercel.app/api?username=edwii-78&show_icons=true&theme=github_dark&bg_color=0d1117&title_color=e6edf3&text_color=8b949e&icon_color=1f6feb&border_color=21262d&include_all_commits=true&count_private=true&border_radius=6&rank_icon=github&card_width=420"/>
&nbsp;
<img height="200" src="https://github-readme-stats.vercel.app/api/top-langs/?username=edwii-78&layout=compact&theme=github_dark&bg_color=0d1117&title_color=e6edf3&text_color=8b949e&border_color=21262d&langs_count=8&border_radius=6&card_width=320"/>

<br/><br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=edwii-78&background=0d1117&ring=1f6feb&fire=f85149&currStreakLabel=e6edf3&sideLabels=8b949e&dates=6e7681&border=21262d&stroke=21262d&currStreakNum=e6edf3&sideNums=c9d1d9&border_radius=6&date_format=j%20M%5B%20Y%5D&card_width=760"/>

</div>
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
| Job Simulations — TATA, Deloitte, AIG, Mastercard | Forage | Active |
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
