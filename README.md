<div align="center">
<img src="https://raw.githubusercontent.com/edwii-78/edwii-78/main/header.svg" width="100%" alt="Edwin Dominic — Security Operations"/>
</div>

<br/>

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=ui-monospace%2CSFMono-Regular%2C+SF+Mono%2CConsolas%2Cmonospace&size=13&duration=3500&pause=1200&color=8B949E&background=0D111700&center=true&vCenter=true&width=700&height=28&lines=Detection+Engineering+%E2%80%94+turning+noise+into+signal.;Threat+Simulation+%E2%80%94+attack+to+understand%2C+defend+to+protect.;Every+log+is+a+clue.+Every+alert+is+a+story." alt=""/>
</div>

<br/>

---

## About

SOC analyst building detection engineering environments from scratch — designing labs, simulating attacks, writing SIEM rules, and producing incident reports that mirror real-world SOC workflows.

Core stack: **Wazuh** and **Splunk** for SIEM, **Sysmon** for Windows endpoint telemetry, **Suricata** for network IDS/IPS, **MITRE ATT&CK** as the detection framework. Eight techniques validated end-to-end in a live Windows 11 lab. Running a Raspberry Pi 4 as a production inline IPS with ML-backed anomaly detection on my home network.

Independent vulnerability researcher — 15+ disclosures to Indian government and institutional infrastructure, IIT Madras acknowledged, CERT-In Hall of Fame nominated twice.

Deepening expertise in **Microsoft Sentinel**, **CNSP**, and **AWS** cloud security. Open to SOC analyst, detection engineering, or threat hunting roles — anywhere.

```
edwindominic7878@gmail.com  ·  linkedin.com/in/edwin78  ·  Kerala, India  ·  Open to relocation globally
```

---

## Projects

<br/>

### DefenderPi &nbsp;·&nbsp; Inline IPS with ML Anomaly Detection

Raspberry Pi 4 deployed **inline on a live network** — not a lab VM. Traffic flows through the device; Suricata runs in NFQUEUE mode intercepting every packet before it hits the LAN. Confirmed threat blocks enforced in real time via iptables and ipset rule injection.

A secondary ML layer — K-Means clustering and Isolation Forest — detects behavioural anomalies that static Suricata signatures miss: slow port scans, abnormal traffic volumes, protocol misuse. Redis caches threat enrichment. Grafana dashboards the EVE JSON feed. Telegram delivers SOC-style alerts. Pi-hole with Unbound handles DNS filtering and recursive resolution.

[![View →](https://img.shields.io/badge/DefenderPi-View_Repository-1f6feb?style=flat-square&logo=github&logoColor=white&labelColor=0d1117)](https://github.com/edwii-78/DefenderPi)

<br/>

### Wazuh Detection Engineering Lab &nbsp;·&nbsp; Windows Threat Simulation

Windows 11 lab with Sysmon feeding telemetry into Wazuh. Simulated and detected **eight MITRE ATT&CK techniques end-to-end** — from attack execution through alert generation to incident report.

| Technique | ATT&CK ID | Key Event IDs |
|:---|:---|:---|
| Reconnaissance — port scan, ping sweep | T1046 / T1018 | Sysmon net events |
| Encoded PowerShell execution | T1059.001 | 4104, ScriptBlock |
| Registry Run key persistence | T1547.001 | Sysmon ID 13 |
| Startup folder abuse | T1547.001 | Sysmon file creation |
| Malicious Windows service install | T1543.003 | 7045 |
| PsExec lateral movement | T1570 | 4624 + 7045 + pipe |
| SMB / NTLM authentication monitoring | T1550.002 | 4624, 4625, 4634 |
| Privileged account abuse | T1078.003 | 4672 + 4624 type 3 |

Alert delivery via Gmail SMTP and Telegram bot. SOC-style incident investigation report produced per technique.

[![View →](https://img.shields.io/badge/Wazuh_SOC_Lab-View_Repository-1f6feb?style=flat-square&logo=github&logoColor=white&labelColor=0d1117)](https://github.com/edwii-78/Wazuh-SOC-Detection-Engineering-Lab)

<br/>

### Splunk Detection Engineering Lab &nbsp;·&nbsp; Full Kill Chain &nbsp;*(in progress)*

Splunk Enterprise environment. SPL-based detection across a complete attack chain:

```
Initial Access → WinRM Lateral Movement → LSASS Credential Dump
→ C2 Beaconing → Staged Exfiltration → Ransomware Detonation
```

Detections: LOLBins (Certutil, MSHTA, Rundll32), encoded PowerShell, credential dumping patterns, beaconing regularity analysis, ransomware file extension behaviour. Capstone: full simulation run producing an executive-ready incident report.

[![View →](https://img.shields.io/badge/Splunk_Lab-View_Repository-1f6feb?style=flat-square&logo=github&logoColor=white&labelColor=0d1117)](https://github.com/edwii-78/Splunk-SOC-Detection-Engineering-Lab)

<br/>

### ZeroTrace &nbsp;·&nbsp; AES-256 Encrypted Messenger

Flutter + Firebase + Node.js. AES-256 end-to-end encryption applied client-side before transit. Messages auto-delete server-side on read — no residual data, no forensic trace. Built security-first from the ground up.

[![View →](https://img.shields.io/badge/ZeroTrace-View_Repository-1f6feb?style=flat-square&logo=github&logoColor=white&labelColor=0d1117)](https://github.com/edwii-78/ZeroTrace-AES-Encrypted-Messaging-App-With-ServerSide-AutoDeletion)

---

## Stack

<div align="center">

**SIEM · Detection · Monitoring**

![Wazuh](https://img.shields.io/badge/Wazuh-161b22?style=flat-square&logo=wazuh&logoColor=58a6ff)
![Splunk](https://img.shields.io/badge/Splunk-161b22?style=flat-square&logo=splunk&logoColor=58a6ff)
![Microsoft Sentinel](https://img.shields.io/badge/Microsoft_Sentinel-161b22?style=flat-square&logo=microsoftazure&logoColor=58a6ff)
![Grafana](https://img.shields.io/badge/Grafana-161b22?style=flat-square&logo=grafana&logoColor=58a6ff)

**Network · Endpoint · Forensics**

![Suricata](https://img.shields.io/badge/Suricata-161b22?style=flat-square&logoColor=f85149)
![Wireshark](https://img.shields.io/badge/Wireshark-161b22?style=flat-square&logo=wireshark&logoColor=58a6ff)
![Sysmon](https://img.shields.io/badge/Sysmon-161b22?style=flat-square&logo=windows&logoColor=58a6ff)
![Nmap](https://img.shields.io/badge/Nmap-161b22?style=flat-square&logoColor=58a6ff)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-161b22?style=flat-square&logoColor=f85149)
![Metasploit](https://img.shields.io/badge/Metasploit-161b22?style=flat-square&logoColor=58a6ff)
![Autopsy](https://img.shields.io/badge/Autopsy-161b22?style=flat-square&logoColor=58a6ff)

**OS · Infrastructure**

![Kali Linux](https://img.shields.io/badge/Kali_Linux-161b22?style=flat-square&logo=kalilinux&logoColor=58a6ff)
![Linux](https://img.shields.io/badge/Linux-161b22?style=flat-square&logo=linux&logoColor=e3b341)
![Windows Server](https://img.shields.io/badge/Windows_Server-161b22?style=flat-square&logo=windows&logoColor=58a6ff)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-161b22?style=flat-square&logo=raspberrypi&logoColor=f85149)
![Pi-hole](https://img.shields.io/badge/Pi--hole-161b22?style=flat-square&logo=pi-hole&logoColor=f85149)

**Languages · Query**

![Python](https://img.shields.io/badge/Python-161b22?style=flat-square&logo=python&logoColor=58a6ff)
![Bash](https://img.shields.io/badge/Bash-161b22?style=flat-square&logo=gnubash&logoColor=58a6ff)
![C++](https://img.shields.io/badge/C++-161b22?style=flat-square&logo=cplusplus&logoColor=58a6ff)
![SPL](https://img.shields.io/badge/Splunk_SPL-161b22?style=flat-square&logoColor=58a6ff)
![KQL](https://img.shields.io/badge/KQL-161b22?style=flat-square&logoColor=58a6ff)
![Flutter](https://img.shields.io/badge/Flutter-161b22?style=flat-square&logo=flutter&logoColor=58a6ff)

**Frameworks**

![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-161b22?style=flat-square&logoColor=f85149)

</div>

---

## GitHub Activity

<div align="center">

<img height="160" src="https://github-readme-stats.vercel.app/api?username=edwii-78&show_icons=true&theme=github_dark&bg_color=0d1117&title_color=e6edf3&text_color=8b949e&icon_color=1f6feb&border_color=21262d&include_all_commits=true&count_private=true&border_radius=6"/>
&nbsp;
<img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=edwii-78&layout=compact&theme=github_dark&bg_color=0d1117&title_color=e6edf3&text_color=8b949e&border_color=21262d&langs_count=6&border_radius=6"/>

<br/><br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=edwii-78&background=0d1117&ring=1f6feb&fire=f85149&currStreakLabel=e6edf3&sideLabels=8b949e&dates=6e7681&border=21262d&stroke=21262d&currStreakNum=e6edf3&sideNums=c9d1d9&border_radius=6"/>

</div>

<br/>

**SOC Log Stream &nbsp;·&nbsp; Contribution Activity**

> Contribution cells visualised as SIEM log events. The red sweep is the detection scan — same motion as a SIEM ingesting and correlating incoming telemetry.

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream.svg"/>
  <img alt="SOC Log Stream" src="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream-dark.svg"/>
</picture>
</div>

<br/>

<div align="center">
<img src="https://github-readme-activity-graph.vercel.app/graph?username=edwii-78&bg_color=0d1117&color=8b949e&line=1f6feb&point=e6edf3&area=true&hide_border=false&border_color=21262d&area_color=0d2137&radius=6" alt="Activity graph"/>
</div>

---

## Certifications

| | Certification | Issuer | Status |
|:---:|:---|:---|:---:|
| | Certified Ethical Hacker — CEH v13 | EC-Council | `Active` |
| | Certified Secure Computer User — CSCU | EC-Council | `Active` |
| | Introduction to Microsoft Sentinel | Microsoft | `Active` |
| | Intro to Splunk | Splunk | `Active` |
| | Cyber Threat Intelligence 101 | arcX | `Active` |
| | Job Simulations — TATA, Deloitte, AIG, Mastercard | Forage | `Active` |
| | Certified Network Security Practitioner — CNSP | SecOps Group | `In progress` |
| | AWS Cloud Practitioner | AWS | `In progress` |
| | SOC Level 1 | TryHackMe | `In progress` |
| | AI Security | TryHackMe | `In progress` |

---

## Vulnerability Research

Independent research targeting Indian public-sector and institutional infrastructure.

- **15+ vulnerabilities** disclosed to government portals and universities
- SQL injection · stored/reflected XSS · DNS cache poisoning · clickjacking · auth bypass
- **IIT Madras** — verified and acknowledged
- **CERT-In Hall of Fame** — nominated twice, under review
- All disclosures through official channels before any public mention

---

## TryHackMe

<div align="center">

<a href="https://tryhackme.com/p/edwindominic7878">
<img src="https://raw.githubusercontent.com/edwii-78/edwii-78/main/assets/thm-badge.png"
     alt="TryHackMe — edwindominic7878"
     height="120"/>
</a>

> *Badge auto-fetched and committed daily via GitHub Actions · [View profile](https://tryhackme.com/p/edwindominic7878)*

</div>

---

<div align="center">
<img src="https://komarev.com/ghpvc/?username=edwii-78&color=1f6feb&style=flat-square&label=profile+views&labelColor=0d1117"/>
&nbsp;&nbsp;
<img src="https://img.shields.io/badge/open_to_work-globally-238636?style=flat-square&labelColor=0d1117"/>
</div>
