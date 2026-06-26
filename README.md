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

### DefenderPi &nbsp;—&nbsp; Inline IPS with ML Anomaly Detection

Raspberry Pi 4 deployed inline on a live network. Traffic passes through the device; Suricata operates in NFQUEUE mode inspecting every packet. Blocks enforced via iptables and ipset. A secondary ML layer — K-Means clustering and Isolation Forest — detects behavioural patterns that static signatures miss: slow scans, unusual volumes, protocol anomalies. Redis caches enrichment data. Grafana dashboards the EVE JSON feed. Telegram delivers alerts. Pi-hole with Unbound handles DNS filtering and recursive resolution.

[![View repository](https://img.shields.io/badge/View_repository-DefenderPi-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/DefenderPi)

<br/>

### Wazuh Detection Engineering Lab &nbsp;—&nbsp; Windows Threat Simulation

Windows 11 lab with Sysmon feeding telemetry into Wazuh. Eight MITRE ATT&CK techniques simulated and detected end-to-end:

| # | Technique | Detection |
|---|-----------|-----------|
| 1 | Reconnaissance — port scan, ping sweep | Sysmon network events + Wazuh correlation |
| 2 | Encoded PowerShell execution | Event ID 4104, base64 pattern rules |
| 3 | Registry Run key persistence | Event ID 13, registry value creation |
| 4 | Startup folder abuse | Sysmon file creation in startup path |
| 5 | Malicious Windows service install | Event ID 7045, unusual binary path |
| 6 | PsExec lateral movement | Event IDs 4624 + 7045 + named pipe |
| 7 | SMB / NTLM auth monitoring | Event IDs 4624, 4625, 4634, 4672 |
| 8 | Privileged account abuse | Event ID 4672 + type-3 logon chain |

Each technique produced a Wazuh alert, a custom detection rule, and an SOC-style incident investigation report. Alerts delivered via Gmail SMTP and Telegram bot.

[![View repository](https://img.shields.io/badge/View_repository-Wazuh_SOC_Lab-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/Wazuh-SOC-Detection-Engineering-Lab)

<br/>

### Splunk Detection Engineering Lab &nbsp;—&nbsp; Full Kill Chain &nbsp;*(in progress)*

Splunk Enterprise environment. SPL-based detection across a complete attack chain: phishing initial access → WinRM lateral movement → LSASS credential dumping → C2 beaconing → staged exfiltration → ransomware detonation. Detections cover LOLBins (Certutil, MSHTA, Rundll32), encoded PowerShell, beaconing regularity, and ransomware file extension patterns. Capstone: executive-ready IR report from a full simulation run.

[![View repository](https://img.shields.io/badge/View_repository-Splunk_Lab-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/Splunk-SOC-Detection-Engineering-Lab)

<br/>

### ZeroTrace &nbsp;—&nbsp; AES-256 Encrypted Messenger

Flutter + Firebase + Node.js. AES-256 end-to-end encryption applied before transit. Messages auto-delete server-side on read — no residual data. Built to demonstrate that strong privacy doesn't require sacrificing usability.

[![View repository](https://img.shields.io/badge/View_repository-ZeroTrace-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/ZeroTrace-AES-Encrypted-Messaging-App-With-ServerSide-AutoDeletion)

---

## Stack

<div align="center">

![Wazuh](https://img.shields.io/badge/Wazuh-21262d?style=flat-square&logo=wazuh&logoColor=white)
![Splunk](https://img.shields.io/badge/Splunk-21262d?style=flat-square&logo=splunk&logoColor=white)
![Microsoft Sentinel](https://img.shields.io/badge/Microsoft_Sentinel-21262d?style=flat-square&logo=microsoftazure&logoColor=white)
![Suricata](https://img.shields.io/badge/Suricata-21262d?style=flat-square&logoColor=white)
![Sysmon](https://img.shields.io/badge/Sysmon-21262d?style=flat-square&logo=windows&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-21262d?style=flat-square&logo=wireshark&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-21262d?style=flat-square&logo=grafana&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-21262d?style=flat-square&logo=redis&logoColor=white)
![Metasploit](https://img.shields.io/badge/Metasploit-21262d?style=flat-square&logoColor=white)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-21262d?style=flat-square&logoColor=white)
![Autopsy](https://img.shields.io/badge/Autopsy-21262d?style=flat-square&logoColor=white)
![Nmap](https://img.shields.io/badge/Nmap-21262d?style=flat-square&logoColor=white)
![Pi-hole](https://img.shields.io/badge/Pi--hole-21262d?style=flat-square&logo=pi-hole&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-21262d?style=flat-square&logo=raspberrypi&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-21262d?style=flat-square&logo=kalilinux&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-21262d?style=flat-square&logo=linux&logoColor=white)
![Windows Server](https://img.shields.io/badge/Windows_Server-21262d?style=flat-square&logo=windows&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-21262d?style=flat-square&logoColor=white)
![Python](https://img.shields.io/badge/Python-21262d?style=flat-square&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-21262d?style=flat-square&logo=gnubash&logoColor=white)
![C++](https://img.shields.io/badge/C++-21262d?style=flat-square&logo=cplusplus&logoColor=white)
![SPL](https://img.shields.io/badge/Splunk_SPL-21262d?style=flat-square&logoColor=white)
![KQL](https://img.shields.io/badge/KQL-21262d?style=flat-square&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-21262d?style=flat-square&logo=flutter&logoColor=white)

</div>

---

## Activity

<div align="center">

<img height="160" src="https://github-readme-stats.vercel.app/api?username=edwii-78&show_icons=true&theme=github_dark&bg_color=0d1117&title_color=e6edf3&text_color=8b949e&icon_color=1f6feb&border_color=21262d&include_all_commits=true&count_private=true&border_radius=6"/>
&nbsp;
<img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=edwii-78&layout=compact&theme=github_dark&bg_color=0d1117&title_color=e6edf3&text_color=8b949e&border_color=21262d&langs_count=6&border_radius=6"/>

<br/><br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=edwii-78&background=0d1117&ring=1f6feb&fire=f85149&currStreakLabel=e6edf3&sideLabels=8b949e&dates=6e7681&border=21262d&stroke=21262d&currStreakNum=e6edf3&sideNums=c9d1d9&border_radius=6"/>

</div>

<br/>

**SIEM Log Stream &nbsp;·&nbsp; Contribution Activity**

> Each cell is a log event. The red scan line is the detection sweep — the same way a SIEM scans incoming telemetry.

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream.svg"/>
  <img alt="SOC Log Stream — Contribution Activity" src="https://raw.githubusercontent.com/edwii-78/edwii-78/output/soc-log-stream-dark.svg"/>
</picture>
</div>

<br/>

<div align="center">
<img src="https://github-readme-activity-graph.vercel.app/graph?username=edwii-78&bg_color=0d1117&color=8b949e&line=1f6feb&point=e6edf3&area=true&hide_border=false&border_color=21262d&area_color=0d2137&radius=6" alt="Contribution activity"/>
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

[![TryHackMe](https://img.shields.io/badge/TryHackMe-edwindominic7878-212C42?style=for-the-badge&logo=tryhackme&logoColor=white&labelColor=0d1117)](https://tryhackme.com/p/edwindominic7878)

<br/>

![](https://img.shields.io/badge/SOC_Level_1-In_Progress-1f6feb?style=flat-square&labelColor=0d1117)
![](https://img.shields.io/badge/AI_Security-In_Progress-1f6feb?style=flat-square&labelColor=0d1117)
![](https://img.shields.io/badge/Pre--Security-Completed-238636?style=flat-square&labelColor=0d1117)

</div>

---

<div align="center">
<img src="https://komarev.com/ghpvc/?username=edwii-78&color=1f6feb&style=flat-square&label=profile+views&labelColor=0d1117"/>
&nbsp;&nbsp;
<img src="https://img.shields.io/badge/open_to_work-globally-238636?style=flat-square&labelColor=0d1117"/>
</div>
