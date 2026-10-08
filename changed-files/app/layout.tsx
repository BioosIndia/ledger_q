import PresentationMotion from '@/components/presentation-motion';
import type { Metadata } from "next";
import "./globals.css";
import "./ledger.css";
import "./ledger-reference.css";
import "./presentation-motion.css";

export const metadata: Metadata = {
  title: "LEDGER-Q | Quality evidence. Accountable decisions.",
  description: "PRAMANEX quality records and AI assurance with source evidence and named human review.",
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased"><PresentationMotion revealSelector=".landing .reveal" stageSelector=".hero-mechanism, .scene-art" accent="#5a86b8"/><a className="skip-link" href="#main-content">Skip to content</a>{children}</body>
    </html>
  );
}
