import { NavLink } from "react-router-dom";

interface Props {
  role: "candidate" | "recruiter";
}

export default function Sidebar({ role }: Props) {
  const candidateLinks = [
    {
      name: "Dashboard",
      path: "/candidate/dashboard",
    },
    {
      name: "Resume",
      path: "/candidate/resume",
    },
    {
      name: "Jobs",
      path: "/candidate/jobs",
    },
    {
      name: "Applications",
      path: "/candidate/applications",
    },
    {
      name: "Analysis",
      path: "/candidate/analysis",
    },
  ];

  const recruiterLinks = [
    {
      name: "Dashboard",
      path: "/recruiter/dashboard",
    },
    {
      name: "Manage Jobs",
      path: "/recruiter/jobs",
    },
    {
      name: "Applicants",
      path: "/recruiter/applicants",
    },
    {
    name: "Semantic Search",
    path: "/recruiter/search",
    },
    {
    name: "ATS Evaluation",
    path: "/recruiter/ats",
    },
    {
      name: "Analytics",
      path: "/recruiter/analytics",
    },
  ];

  const links =
    role === "candidate"
      ? candidateLinks
      : recruiterLinks;

  return (
    <aside className="flex h-screen w-64 flex-col bg-slate-900 text-white">

      <div className="border-b border-slate-700 p-6">

        <h1 className="text-3xl font-bold text-blue-400">
          HireAI
        </h1>

        <p className="mt-2 text-sm text-slate-400">
          Resume Screening Platform
        </p>

      </div>

      <nav className="flex-1 p-4">

        {links.map((item) => (

          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) =>
              `mb-3 block rounded-xl px-4 py-3 transition ${
                isActive
                  ? "bg-blue-600 text-white"
                  : "hover:bg-slate-800"
              }`
            }
          >
            {item.name}
          </NavLink>

        ))}

      </nav>

      <div className="border-t border-slate-700 p-5">

        <button
          onClick={() => {
            localStorage.removeItem("token");
            window.location.href = "/login";
          }}
          className="w-full rounded-xl bg-red-600 py-3 font-semibold hover:bg-red-700"
        >
          Logout
        </button>

      </div>

    </aside>
  );
}