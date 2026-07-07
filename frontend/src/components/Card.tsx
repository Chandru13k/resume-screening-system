import type { ReactNode } from "react";

interface CardProps {
  title?: string;
  children: ReactNode;
}

export default function Card({
  title,
  children,
}: CardProps) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-2 hover:shadow-xl">

      {title && (
        <div className="mb-5 flex items-center justify-between">

          <h2 className="text-xl font-bold text-slate-800">
            {title}
          </h2>

          <div className="h-2 w-2 rounded-full bg-blue-500"></div>

        </div>
      )}

      {children}

    </div>
  );
}