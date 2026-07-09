import { useLocation } from "react-router-dom";
import { useState } from "react";

export default function Navbar() {
  const location = useLocation();

  const [open, setOpen] = useState(false);

  const page =
    location.pathname
      .split("/")
      .pop()
      ?.replace("-", " ")
      ?.replace(/\b\w/g, (c) => c.toUpperCase()) || "Dashboard";

  const today = new Date().toLocaleDateString("en-US", {
    weekday: "long",
    month: "long",
    day: "numeric",
    year: "numeric",
  });

  return (
    <header className="flex h-20 items-center justify-between border-b bg-white px-8 shadow-sm">

      <div>

        <h2 className="text-2xl font-bold text-slate-800">
          {page}
        </h2>

        <p className="text-sm text-slate-500">
          {today}
        </p>

      </div>

      <div className="flex items-center gap-6">

        <input
          type="text"
          placeholder="Search..."
          className="w-72 rounded-xl border border-slate-300 px-4 py-2 outline-none transition focus:border-blue-500"
        />

        <button className="relative rounded-full bg-slate-100 p-3 transition hover:bg-slate-200">
          🔔
          <span className="absolute right-2 top-2 h-2 w-2 rounded-full bg-red-500"></span>
        </button>

        <div className="relative">

          <button
            onClick={() => setOpen(!open)}
            className="flex items-center gap-3 rounded-xl p-2 transition hover:bg-slate-100"
          >

            <div className="flex h-11 w-11 items-center justify-center rounded-full bg-blue-600 text-lg font-bold text-white">
              U
            </div>

            <div className="text-left">

              <p className="font-semibold">
                User
              </p>

              <p className="text-sm text-slate-500">
                AI Recruitment Platform
              </p>

            </div>

          </button>

          {open && (
              <div className="absolute right-0 mt-3 w-56 overflow-hidden rounded-xl border bg-white shadow-xl">

                <button
                  onClick={() => {
                  localStorage.removeItem("token");
                  window.location.href = "/login";
                  }}
                className="block w-full px-5 py-3 text-left text-red-600 hover:bg-red-50"
                >
                🚪 Logout
              </button>

              </div>
            )}

        </div>

      </div>

    </header>
  );
}