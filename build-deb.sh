#!/bin/sh
set -eu
cd "$(dirname "$0")"
VERSION=0.1.0
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT
mkdir -p "$STAGE/DEBIAN" "$STAGE/usr/bin" "$STAGE/usr/share/applications" "$STAGE/usr/share/icons/hicolor/scalable/apps" "$STAGE/usr/share/doc/brother-dcp-l2665dw-manager"
install -m 755 brother-dcp-l2665dw-manager "$STAGE/usr/bin/brother-dcp-l2665dw-manager"
cat > "$STAGE/DEBIAN/control" <<'CONTROL'
Package: brother-dcp-l2665dw-manager
Version: 0.1.0
Section: utils
Priority: optional
Architecture: all
Maintainer: GiuxLab <noreply@giux-lab.it>
Depends: python3, python3-gi, gir1.2-gtk-3.0, cups-client, xdg-utils
Recommends: xsane
Description: Brother DCP-L2665DW series print and maintenance frontend
 GTK3 interface for CUPS printing and official Brother Web Based Management.
 Includes printer diagnostics, print quality selection, and access
 to maintenance through Brother's own web interface.
CONTROL
cat > "$STAGE/usr/share/applications/brother-dcp-l2665dw-manager.desktop" <<'DESKTOP'
[Desktop Entry]
Type=Application
Name=Brother DCP-L2665DW Manager
Name[it]=Gestione Brother DCP-L2665DW
Comment=Manage Brother DCP-L2665DW printing and access official maintenance
Comment[it]=Gestisci stampa Brother DCP-L2665DW e manutenzione ufficiale
Exec=brother-dcp-l2665dw-manager
Icon=brother-dcp-l2665dw-manager
Terminal=false
Categories=System;GTK;
Keywords=Brother;CUPS;Printer;Maintenance;Stampante;
StartupNotify=true
DESKTOP
cat > "$STAGE/usr/share/icons/hicolor/scalable/apps/brother-dcp-l2665dw-manager.svg" <<'SVG'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#263b50"/><rect x="10" y="21" width="44" height="29" rx="5" fill="#e6ebef"/><rect x="17" y="9" width="30" height="23" rx="2" fill="#fff"/><path d="M22 15h20M22 20h20M22 25h13" stroke="#566b7b" stroke-width="2"/><rect x="17" y="39" width="30" height="16" rx="2" fill="#fff"/><rect x="22" y="44" width="6" height="7" fill="#28c6dd"/><rect x="29" y="44" width="6" height="7" fill="#d840a8"/><rect x="36" y="44" width="6" height="7" fill="#f4c542"/><circle cx="47" cy="28" r="2" fill="#48ba6a"/></svg>
SVG
install -m 644 README.md "$STAGE/usr/share/doc/brother-dcp-l2665dw-manager/README.md"
find "$STAGE" -type d -exec chmod 755 {} +
dpkg-deb --build --root-owner-group "$STAGE" "/home/giu/brother-dcp-l2665dw-manager_0.1.0_all.deb"
