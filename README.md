# Brother DCP-L2665DW Manager for Linux

**Unofficial open-source GTK3 frontend for Brother DCP-L2665DW network printers, using standard CUPS commands and Brother's own Web Based Management interface.**

**Latest version:** 0.2.1 · **Languages:** Italian and English · **License:** GPL-3.0-or-later · **Platform:** Linux / Debian-family systems

[Debian downloads](https://github.com/giuxlab-hub/brother-dcp-l2665dw-manager/releases/latest) · [Giux-Lab](https://giux-lab.it/) · [Original project README](README.original.md)

This is an **independent project created by Giux-Lab**. It is not affiliated with, sponsored by or endorsed by Brother Industries, Ltd. The program does not attempt undocumented or proprietary device maintenance operations.

## Features

- **CUPS printer status:** inspect the configured printer queue, connection details, queued jobs, and current printing options.
- **Editable connection settings:** enter the local CUPS queue name and printer IP address or hostname.
- **Print diagnostics:** inspect printer options and submit an A4 text diagnostic page after explicit confirmation, selecting Draft, Normal or High quality.
- **Duplex options:** choose single-sided, two-sided long-edge or two-sided short-edge printing for the test job.
- **Official Brother Web Based Management:** open the printer's web interface for status, toner information and supported device management.
- **Documentation and scanning:** open the official Brother support/manual page and launch XSane when installed.
- **Bilingual interface:** choose Italian or English automatically from the desktop locale, or switch language directly in the application header. The language change retains the selected CUPS queue, hostname and print options.
- **Noninvasive operation:** no automated firmware changes, undocumented cleaning commands or password modifications.

**Driver-dependent behavior:** The printing quality and duplex settings are passed through CUPS. Whether the driver implements them, and how they map to the physical printer, depends on the configured queue/driver. The application is not a replacement for the manufacturer's print or scanner drivers.

## Install on Debian

Download `brother-dcp-l2665dw-manager_0.2.1_all.deb` from [the latest GitHub release](https://github.com/giuxlab-hub/brother-dcp-l2665dw-manager/releases/tag/v0.2.1), then:

```bash
sudo apt install ./brother-dcp-l2665dw-manager_0.2.1_all.deb
```

The package declares these dependencies: `python3`, `python3-gi`, `gir1.2-gtk-3.0`, `cups-client`, `xdg-utils`; `xsane` is recommended, but optional. A working GTK3 graphical session, configured CUPS printer queue and network access to the device are necessary for the respective functionality.

Start the application from the system menu or run:

```bash
brother-dcp-l2665dw-manager
```

### Configure your own printer

The original application provides initial example values from its development environment:

```text
CUPS queue: Brother_DCP_L2665DW
Printer host: 192.168.1.112
```

**These are not automatically discovered printer settings.** Enter the correct queue and IP/hostname for your own Linux computer and printer.

## Build from source

The repository contains the Python application, Debian builder and the original launcher/icon/packaging metadata:

```bash
git clone https://github.com/giuxlab-hub/brother-dcp-l2665dw-manager.git
cd brother-dcp-l2665dw-manager
./build-deb.sh
```

Requires `dpkg-deb` (typically supplied by `dpkg-dev` or the Debian package tools). The repository's builder produces `./brother-dcp-l2665dw-manager_0.2.1_all.deb` without installing or launching the application.

The **original, unchanged** .deb and source tarballs for versions 0.1.0, 0.2.0 and 0.2.1 are retained under their corresponding [GitHub releases](https://github.com/giuxlab-hub/brother-dcp-l2665dw-manager/releases). The public repository uses the exact v0.2.1 Python source; only the builder's fixed output path was adapted to a local relative path for portable rebuilding. See [SOURCE_PROVENANCE.md](SOURCE_PROVENANCE.md).

## Limitations and notes

- Version 0.2.0 is preserved as a historical pre-release: its executable has no interpreter shebang. **Install v0.2.1** instead.
- Version 0.2.1 has Italian/English controls and tab labels, but some informational strings and the diagnostic-print confirmation remain in Italian in the supplied source. The repository preserves the original 0.2.1 application without silently rewriting its behavior.
- Device status and toner information rely on the printer's official web interface. The utility does not independently query toner levels through a private protocol.
- No installer modifies printer settings, firmware or CUPS queues automatically.

## License

GNU General Public License **version 3 or later** (`GPL-3.0-or-later`). See [LICENSE](LICENSE).

Copyright © 2026 Giux-Lab. **Not affiliated with Brother Industries, Ltd.** Brother and DCP-L2665DW are used solely for product identification.

---

## Italiano

**Brother DCP-L2665DW Manager** è un'applicazione indipendente Giux-Lab realizzata in **Python 3 e GTK3** per gestire la stampa tramite CUPS e accedere alla gestione web ufficiale della stampante Brother DCP-L2665DW.

### Funzionalità

- Visualizzazione dello stato della stampante, della coda CUPS, dei lavori e delle opzioni disponibili.
- Modifica diretta di nome coda e indirizzo IP/hostname della stampante.
- Stampa diagnostica A4 dopo conferma, con qualità Draft/Normal/High e selezione fronte-retro (l'effetto dipende dal driver CUPS).
- Accesso al servizio ufficiale Brother Web Based Management, ai manuali e a XSane quando disponibile.
- Interfaccia italiano/inglese con selezione automatica basata sulla lingua del sistema e cambio lingua dall'intestazione.
- Nessuna gestione proprietaria non documentata, modifica del firmware o pulizia automatica.

### Installazione

Scaricare `brother-dcp-l2665dw-manager_0.2.1_all.deb` dalla [release v0.2.1](https://github.com/giuxlab-hub/brother-dcp-l2665dw-manager/releases/tag/v0.2.1):

```bash
sudo apt install ./brother-dcp-l2665dw-manager_0.2.1_all.deb
```

Avviare dal menu grafico o mediante il comando `brother-dcp-l2665dw-manager`. Modificare la coda CUPS e l'indirizzo della stampante con i valori reali della propria rete.

I pacchetti originali delle versioni precedenti sono conservati, comprese le corrispondenti sorgenti. Il codice applicativo della v0.2.1 è riprodotto senza modifiche; lo script di compilazione è stato reso portabile soltanto nel percorso di destinazione del pacchetto.

**Licenza:** GNU GPL v3 o successiva. Progetto indipendente, **non affiliato a Brother Industries, Ltd.**

[Sito Giux-Lab](https://giux-lab.it/) · [Provenienza dei sorgenti](SOURCE_PROVENANCE.md)
