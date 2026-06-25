<div align="center">
<img src="https://raw.githubusercontent.com/edwii-78/edwii-78/main/header.svg" width="100%" alt="Edwin Dominic"/>
</div>

<br/>

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=ui-monospace%2CSFMono-Regular%2C+SF+Mono%2CConsolas%2Cmonospace&size=13&duration=3000&pause=1000&color=8B949E&background=0D111700&center=true&vCenter=true&width=720&height=28&lines=Security+Operations+%E2%80%94+Turning+noise+into+signal%2C+signals+into+action.;Detection+Engineering+%E2%80%94+Building+rules+that+catch+what+matters.;Threat+Analysis+%E2%80%94+Every+log+is+a+clue.+Every+alert+tells+a+story." alt=""/>
</div>

<br/>

---

## About

SOC analyst with hands-on experience building and operating detection engineering labs from the ground up. My work centres on Wazuh and Splunk SIEM environments, writing detection rules mapped to MITRE ATT&CK, and validating them against real attack simulations — not just theory.

I've disclosed 15+ vulnerabilities to Indian government portals and institutions independently, with nominations to the CERT-In Hall of Fame. I build tools that work in production: a Raspberry Pi-based inline IPS running Suricata with ML-backed anomaly detection is currently live on my home network.

Currently deepening expertise in Microsoft Sentinel and cloud security while pursuing CNSP and AWS certifications. Open to roles in SOC analysis, detection engineering, or threat hunting — anywhere the work is meaningful.

```
Contact  →  edwindominic7878@gmail.com
LinkedIn →  linkedin.com/in/edwin78
Location →  Kerala, India — open to relocation globally
```

---

## Projects

These are labs built to simulate real environments, not toy setups. Each one produced investigation reports and detection artefacts.

<br/>

**DefenderPi — Inline IPS with ML Anomaly Detection**

A Raspberry Pi 4 deployed as an inline network security appliance using Suricata in NFQUEUE mode. Traffic flows through the device; suspicious packets trigger automated iptables/ipset block rules. A secondary ML layer — K-Means clustering and Isolation Forest — flags behavioural anomalies that signature rules miss. Threat intelligence is enriched via Redis and pushed to a Telegram alerting bot. DNS filtering runs through Pi-hole backed by Unbound for recursive resolution.

This is a production deployment on a live network, not a VM lab.

[![View →](https://img.shields.io/badge/View_Repository-DefenderPi-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/DefenderPi)

<br/>

**Wazuh Detection Engineering Lab — Windows Threat Simulation**

Built a detection engineering environment on Windows 11 with Sysmon feeding telemetry into Wazuh. Simulated and detected eight MITRE ATT&CK techniques end-to-end: reconnaissance, encoded PowerShell execution, registry and startup persistence, Windows service abuse, PsExec lateral movement, SMB/NTLM authentication monitoring, and privileged account tracking. Each technique produced a detection rule, triggered an alert, and was documented in an SOC-style incident report.

Alert delivery via Gmail SMTP and Telegram. Windows Event IDs 4624, 4625, 4634, 4672 correlated across the attack chain.

[![View →](https://img.shields.io/badge/View_Repository-Wazuh_SOC_Lab-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/Wazuh-SOC-Detection-Engineering-Lab)

<br/>

**Splunk Detection Engineering Lab — Full Kill Chain Simulation** *(in progress)*

Building a Splunk Enterprise environment with SPL-based detection engineering across a full attack chain: initial access, WinRM abuse, LSASS credential dumping, C2 beaconing, data exfiltration, and ransomware detonation. Detections target LOLBins, encoded PowerShell, Certutil, MSHTA, and Rundll32 abuse. Capstone: a full multi-stage simulation producing an executive-ready incident report.

[![View →](https://img.shields.io/badge/View_Repository-Splunk_Lab-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/Splunk-SOC-Detection-Engineering-Lab)

<br/>

**ZeroTrace — AES-256 Encrypted Messenger**

A mobile messaging application built with Flutter, Firebase, and Node.js. End-to-end AES-256 encryption with server-side auto-deletion of messages. Designed from the ground up with privacy as the primary constraint, not an afterthought.

[![View →](https://img.shields.io/badge/View_Repository-ZeroTrace-1f6feb?style=flat-square&logo=github&logoColor=white)](https://github.com/edwii-78/ZeroTrace-AES-Encrypted-Messaging-App-With-ServerSide-AutoDeletion)

---

## Skills & Tools

<div align="center">

**SIEM & Monitoring**

![Wazuh](https://img.shields.io/badge/Wazuh-0d1117?style=flat-square&logo=wazuh&logoColor=white&labelColor=0d1117&color=21262d)
![Splunk](https://img.shields.io/badge/Splunk-0d1117?style=flat-square&logo=splunk&logoColor=white&labelColor=0d1117&color=21262d)
![Microsoft Sentinel](https://img.shields.io/badge/Microsoft_Sentinel-0d1117?style=flat-square&logo=microsoftazure&logoColor=white&labelColor=0d1117&color=21262d)
![Grafana](https://img.shields.io/badge/Grafana-0d1117?style=flat-square&logo=grafana&logoColor=white&labelColor=0d1117&color=21262d)
![Elastic](https://img.shields.io/badge/Elastic-0d1117?style=flat-square&logo=elastic&logoColor=white&labelColor=0d1117&color=21262d)

**Network & Endpoint**

![Suricata](https://img.shields.io/badge/Suricata-0d1117?style=flat-square&logoColor=white&labelColor=0d1117&color=21262d)
![Wireshark](https://img.shields.io/badge/Wireshark-0d1117?style=flat-square&logo=wireshark&logoColor=white&labelColor=0d1117&color=21262d)
![Sysmon](https://img.shields.io/badge/Sysmon-0d1117?style=flat-square&logo=windows&logoColor=white&labelColor=0d1117&color=21262d)
![Nmap](https://img.shields.io/badge/Nmap-0d1117?style=flat-square&logoColor=white&labelColor=0d1117&color=21262d)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-0d1117?style=flat-square&logoColor=white&labelColor=0d1117&color=21262d)
![Metasploit](https://img.shields.io/badge/Metasploit-0d1117?style=flat-square&logoColor=white&labelColor=0d1117&color=21262d)
![Autopsy](https://img.shields.io/badge/Autopsy-0d1117?style=flat-square&logoColor=white&labelColor=0d1117&color=21262d)

**Languages & Scripting**

![Python](https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=white&labelColor=0d1117&color=21262d)
![Bash](https://img.shields.io/badge/Bash-0d1117?style=flat-square&logo=gnubash&logoColor=white&labelColor=0d1117&color=21262d)
![C++](https://img.shields.io/badge/C++-0d1117?style=flat-square&logo=cplusplus&logoColor=white&labelColor=0d1117&color=21262d)
![SPL](https://img.shields.io/badge/SPL-0d1117?style=flat-square&logoColor=white&labelColor=0d1117&color=21262d)
![KQL](https://img.shields.io/badge/KQL-0d1117?style=flat-square&logoColor=white&labelColor=0d1117&color=21262d)
![Flutter](https://img.shields.io/badge/Flutter-0d1117?style=flat-square&logo=flutter&logoColor=white&labelColor=0d1117&color=21262d)

**Frameworks & Platforms**

![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-0d1117?style=flat-square&logoColor=white&labelColor=0d1117&color=21262d)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-0d1117?style=flat-square&logo=raspberrypi&logoColor=white&labelColor=0d1117&color=21262d)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-0d1117?style=flat-square&logo=kalilinux&logoColor=white&labelColor=0d1117&color=21262d)
![Linux](https://img.shields.io/badge/Linux-0d1117?style=flat-square&logo=linux&logoColor=white&labelColor=0d1117&color=21262d)
![Windows Server](https://img.shields.io/badge/Windows_Server-0d1117?style=flat-square&logo=windows&logoColor=white&labelColor=0d1117&color=21262d)

</div>

---

## GitHub Activity

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=edwii-78&show_icons=true&theme=github_dark&bg_color=0d1117&title_color=e6edf3&text_color=8b949e&icon_color=1f6feb&border_color=21262d&include_all_commits=true&count_private=true&hide_border=false&border_radius=6&ring_color=1f6feb"/>
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=edwii-78&layout=compact&theme=github_dark&bg_color=0d1117&title_color=e6edf3&text_color=8b949e&border_color=21262d&langs_count=6&border_radius=6"/>

<br/><br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=edwii-78&background=0d1117&ring=1f6feb&fire=f85149&currStreakLabel=e6edf3&sideLabels=8b949e&dates=6e7681&border=21262d&stroke=21262d&currStreakNum=e6edf3&sideNums=c9d1d9&border_radius=6"/>

</div>

<br/>

**Contribution / Threat Path**

> The red trace is the threat actor path through your contribution graph — moving through every cell your commits occupy. Red on blue: attack surface mapped, monitored, and owned.

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/edwii-78/edwii-78/blob/output/threat-path-dark.svg?raw=true"/>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/edwii-78/edwii-78/blob/output/threat-path.svg?raw=true"/>
  <img alt="Threat Path — Contribution Graph" src="https://github.com/edwii-78/edwii-78/blob/output/threat-path-dark.svg?raw=true"/>
</picture>
</div>

<br/>

<div align="center">
<img src="https://github-readme-activity-graph.vercel.app/graph?username=edwii-78&bg_color=0d1117&color=8b949e&line=1f6feb&point=e6edf3&area=true&hide_border=false&border_color=21262d&area_color=1a2d50&radius=6" alt="Activity Graph"/>
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
| Cybersecurity Job Simulations | Forage — TATA, Deloitte, AIG, Mastercard | Active |
| Certified Network Security Practitioner — CNSP | SecOps Group | In Progress |
| AWS Cloud Practitioner | Amazon Web Services | In Progress |
| SOC Level 1 | TryHackMe | In Progress |
| AI Security | TryHackMe | In Progress |

---

## Responsible Disclosure

Independent vulnerability research targeting public-sector and institutional infrastructure.

- **15+ vulnerabilities** disclosed across Indian government portals and academic institutions
- Vulnerability classes: SQL injection, reflected and stored XSS, DNS spoofing, clickjacking, authentication bypass
- **IIT Madras** — verified and acknowledged disclosure
- **CERT-In Hall of Fame** — nominated twice (under review)
- All disclosures made through official channels. Zero malicious use.

---

## TryHackMe

<div align="center">
<a href="https://tryhackme.com/p/edwindominic7878">
<img src="https://tryhackme-badges.s3.amazonaws.com/edwindominic7878.png" alt="TryHackMe Profile"/>
</a>
</div>

---

<div align="center">
<sub>
<img src="https://komarev.com/ghpvc/?username=edwii-78&color=1f6feb&style=flat-square&label=profile+views&labelColor=0d1117"/>
&nbsp;&nbsp;
<img src="https://img.shields.io/badge/open_to_work-globally-238636?style=flat-square&labelColor=0d1117"/>
</sub>
</div>
