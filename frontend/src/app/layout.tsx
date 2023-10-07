import NavBar from "@/components/NavBar/NavBar";
import "./globals.css";
import type { Metadata } from "next";
import { Open_Sans } from "next/font/google";
import ProviderComponent from "@/redux/provider";

const open_sans = Open_Sans({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Second Hand Cars",
  description: "The frontend of a second hand cars app",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={open_sans.className}>
        <ProviderComponent>
          <NavBar />
          {children}
        </ProviderComponent>
      </body>
    </html>
  );
}
