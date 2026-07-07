import { ReactNode } from "react";

interface Props {
  title: string;
  value: string | number;
  color: string;
  icon: ReactNode;
}

export default function StatsCard({
  title,
  value,
  color,
  icon,
}: Props) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">

      <div className="flex items-center justify-between">

        <div>

          <p className="text-sm text-slate-500">
            {title}
          </p>

          <h2 className={`mt-3 text-4xl font-bold ${color}`}>
            {value}
          </h2>

        </div>

        <div className="rounded-2xl bg-slate-100 p-5">
          {icon}
        </div>

      </div>

    </div>
  );
}