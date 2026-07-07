import { ReactNode } from "react";
import { motion } from "framer-motion";

import Sidebar from "./Sidebar";
import Navbar from "./Navbar";

interface DashboardLayoutProps {
  role: "candidate" | "recruiter";
  title: string;
  subtitle?: string;
  children: ReactNode;
}

export default function DashboardLayout({
  role,
  title,
  subtitle,
  children,
}: DashboardLayoutProps) {
  return (
    <div className="flex min-h-screen bg-gradient-to-br from-slate-100 via-slate-50 to-slate-200">

      <Sidebar role={role} />

      <div className="flex flex-1 flex-col overflow-hidden">

        <Navbar />

        <motion.main
          className="flex-1 overflow-y-auto p-8"
          initial={{
            opacity: 0,
            y: 15,
          }}
          animate={{
            opacity: 1,
            y: 0,
          }}
          transition={{
            duration: 0.35,
          }}
        >

          <div className="mb-8">

            <h1 className="text-4xl font-bold text-slate-800">
              {title}
            </h1>

            {subtitle && (
              <p className="mt-2 text-lg text-slate-500">
                {subtitle}
              </p>
            )}

          </div>

          {children}

        </motion.main>

      </div>

    </div>
  );
}