// import { useEffect, useState } from "react";
// import {
//   Briefcase,
//   FolderOpen,
//   FileText,
//   TrendingUp,
// } from "lucide-react";

// import DashboardLayout from "../components/DashboardLayout";
// import StatsCard from "../components/StatsCard";
// import Card from "../components/Card";
// import Loader from "../components/Loader";
// import api from "../api/api";

// interface DashboardStats {
//   total_jobs: number;
//   active_jobs: number;
//   parsed_resumes: number;
// }

// interface RecentJob {
//   id: number;
//   title: string;
//   company_name: string;
//   status: string;
//   created_at: string;
// }

// interface DashboardResponse {
//   stats: DashboardStats;
//   recent_jobs: RecentJob[];
// }

// export default function RecruiterDashboard() {
//   const [dashboard, setDashboard] =
//     useState<DashboardResponse | null>(null);

//   const [loading, setLoading] = useState(true);

//   async function loadDashboard() {
//     try {
//       const res = await api.get("/dashboard/stats");
//       setDashboard(res.data);
//     } finally {
//       setLoading(false);
//     }
//   }

//   useEffect(() => {
//     loadDashboard();
//   }, []);

//   if (loading) {
//     return (
//       <DashboardLayout
//         role="recruiter"
//         title="Recruiter Dashboard"
//       >
//         <Loader />
//       </DashboardLayout>
//     );
//   }

//   if (!dashboard) return null;

//   return (
//     <DashboardLayout
//       role="recruiter"
//       title="Recruiter Dashboard"
//       subtitle="Overview of your hiring activities."
//     >
//       <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

//         <StatsCard
//           title="Total Jobs"
//           value={dashboard.stats.total_jobs}
//           color="text-blue-600"
//           icon={<Briefcase size={34} />}
//         />

//         <StatsCard
//           title="Active Jobs"
//           value={dashboard.stats.active_jobs}
//           color="text-green-600"
//           icon={<FolderOpen size={34} />}
//         />

//         <StatsCard
//           title="Parsed Resumes"
//           value={dashboard.stats.parsed_resumes}
//           color="text-purple-600"
//           icon={<FileText size={34} />}
//         />

//         <StatsCard
//           title="Hiring Progress"
//           value={`${dashboard.stats.active_jobs}/${dashboard.stats.total_jobs}`}
//           color="text-orange-600"
//           icon={<TrendingUp size={34} />}
//         />

//       </div>

//       <div className="mt-8 grid gap-6 lg:grid-cols-2">

//         <Card title="Recent Job Posts">

//           {dashboard.recent_jobs.length === 0 ? (

//             <p>No jobs created.</p>

//           ) : (

//             <div className="space-y-4">

//               {dashboard.recent_jobs.map((job) => (

//                 <div
//                   key={job.id}
//                   className="rounded-xl border border-slate-200 p-4 hover:bg-slate-50"
//                 >

//                   <div className="flex items-center justify-between">

//                     <div>

//                       <h3 className="font-semibold">
//                         {job.title}
//                       </h3>

//                       <p className="text-sm text-slate-500">
//                         {job.company_name}
//                       </p>

//                     </div>

//                     <span
//                       className={`rounded-lg px-3 py-1 text-sm font-medium ${
//                         job.status === "OPEN"
//                           ? "bg-green-100 text-green-700"
//                           : "bg-red-100 text-red-700"
//                       }`}
//                     >
//                       {job.status}
//                     </span>

//                   </div>

//                   <p className="mt-3 text-sm text-slate-500">
//                     Created :
//                     {" "}
//                     {new Date(job.created_at).toLocaleDateString()}
//                   </p>

//                 </div>

//               ))}

//             </div>

//           )}

//         </Card>

//         <Card title="Recruitment Summary">

//           <div className="space-y-6">

//             <div>

//               <p className="text-sm text-slate-500">
//                 Active Jobs
//               </p>

//               <div className="mt-2 h-3 rounded-full bg-slate-200">

//                 <div
//                   className="h-3 rounded-full bg-blue-600"
//                   style={{
//                     width: `${
//                       dashboard.stats.total_jobs === 0
//                         ? 0
//                         : (dashboard.stats.active_jobs /
//                             dashboard.stats.total_jobs) *
//                           100
//                     }%`,
//                   }}
//                 />

//               </div>

//             </div>

//             <div>

//               <p className="text-sm text-slate-500">
//                 Resume Parsing
//               </p>

//               <div className="mt-2 h-3 rounded-full bg-slate-200">

//                 <div
//                   className="h-3 rounded-full bg-green-600"
//                   style={{
//                     width: "80%",
//                   }}
//                 />

//               </div>

//             </div>

//             <div className="rounded-xl bg-blue-50 p-5">

//               <h3 className="font-semibold text-blue-700">
//                 AI Recruitment Summary
//               </h3>

//               <p className="mt-3 text-sm text-slate-600">

//                 Your recruitment platform has
//                 {" "}
//                 <strong>
//                   {dashboard.stats.active_jobs}
//                 </strong>
//                 {" "}
//                 active job postings and
//                 {" "}
//                 <strong>
//                   {dashboard.stats.parsed_resumes}
//                 </strong>
//                 {" "}
//                 parsed resumes ready for AI-powered matching and ranking.

//               </p>

//             </div>

//           </div>

//         </Card>

//       </div>

//     </DashboardLayout>
//   );
// }



import { useEffect, useState } from "react";
import {
  Briefcase,
  FolderOpen,
  FileText,
  TrendingUp,
} from "lucide-react";

import DashboardLayout from "../components/DashboardLayout";
import StatsCard from "../components/StatsCard";
import Card from "../components/Card";
import Loader from "../components/Loader";
import EmptyState from "../components/EmptyState";
import api from "../api/api";
import { toast } from "sonner";

interface DashboardStats {
  total_jobs: number;
  active_jobs: number;
  parsed_resumes: number;
}

interface RecentJob {
  id: number;
  title: string;
  company_name: string;
  status: string;
  created_at: string;
}

interface DashboardResponse {
  stats: DashboardStats;
  recent_jobs: RecentJob[];
}

export default function RecruiterDashboard() {
  const [dashboard, setDashboard] =
    useState<DashboardResponse | null>(null);

  const [loading, setLoading] =
    useState(true);

  async function loadDashboard() {
    try {
      const res = await api.get(
        "/dashboard/stats"
      );

      setDashboard(res.data);
    } catch (err) {
      console.error(err);

      toast.error(
        "Unable to load dashboard."
      );
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadDashboard();
  }, []);

  if (loading) {
    return (
      <DashboardLayout
        role="recruiter"
        title="Recruiter Dashboard"
      >
        <Loader />
      </DashboardLayout>
    );
  }

  if (!dashboard) {
    return (
      <DashboardLayout
        role="recruiter"
        title="Recruiter Dashboard"
      >
        <EmptyState message="Dashboard unavailable." />
      </DashboardLayout>
    );
  }

  const hiringProgress =
    dashboard.stats.total_jobs === 0
      ? 0
      : (
          dashboard.stats.active_jobs /
          dashboard.stats.total_jobs
        ) * 100;

  return (
    <DashboardLayout
      role="recruiter"
      title="Recruiter Dashboard"
      subtitle="Overview of your hiring activities."
    >
      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

        <StatsCard
          title="Total Jobs"
          value={dashboard.stats.total_jobs}
          color="text-blue-600"
          icon={<Briefcase size={34} />}
        />

        <StatsCard
          title="Active Jobs"
          value={dashboard.stats.active_jobs}
          color="text-green-600"
          icon={<FolderOpen size={34} />}
        />

        <StatsCard
          title="Parsed Resumes"
          value={dashboard.stats.parsed_resumes}
          color="text-purple-600"
          icon={<FileText size={34} />}
        />

        <StatsCard
          title="Hiring Progress"
          value={`${dashboard.stats.active_jobs}/${dashboard.stats.total_jobs}`}
          color="text-orange-600"
          icon={<TrendingUp size={34} />}
        />

      </div>

      <div className="mt-8 grid gap-6 lg:grid-cols-2">

        <Card title="Recent Job Posts">

          {dashboard.recent_jobs.length === 0 ? (

            <EmptyState message="No jobs created yet." />

          ) : (

            <div className="space-y-4">

              {dashboard.recent_jobs.map(
                (job) => (

                  <div
                    key={job.id}
                    className="rounded-xl border border-slate-200 p-4 transition hover:shadow-md"
                  >

                    <div className="flex items-center justify-between">

                      <div>

                        <h3 className="font-semibold">
                          {job.title}
                        </h3>

                        <p className="text-sm text-slate-500">
                          {job.company_name}
                        </p>

                      </div>

                      <span
                        className={`rounded-full px-4 py-1 text-sm font-medium ${
                          job.status ===
                          "OPEN"
                            ? "bg-green-100 text-green-700"
                            : "bg-red-100 text-red-700"
                        }`}
                      >
                        {job.status}
                      </span>

                    </div>

                    <p className="mt-3 text-sm text-slate-500">
                      Created on{" "}
                      {new Date(
                        job.created_at
                      ).toLocaleDateString()}
                    </p>

                  </div>

                )
              )}

            </div>

          )}

        </Card>

        <Card title="Recruitment Summary">

          <div className="space-y-8">

            <div>

              <div className="mb-2 flex justify-between text-sm">

                <span>
                  Active Jobs
                </span>

                <span>
                  {hiringProgress.toFixed(0)}%
                </span>

              </div>

              <div className="h-3 rounded-full bg-slate-200">

                <div
                  className="h-3 rounded-full bg-blue-600 transition-all"
                  style={{
                    width: `${hiringProgress}%`,
                  }}
                />

              </div>

            </div>

            <div>

              <div className="mb-2 flex justify-between text-sm">

                <span>
                  Resume Processing
                </span>

                <span>
                  {dashboard.stats.parsed_resumes}
                </span>

              </div>

              <div className="h-3 rounded-full bg-slate-200">

                <div
                  className="h-3 rounded-full bg-green-600"
                  style={{
                    width:
                      dashboard.stats.parsed_resumes > 0
                        ? "100%"
                        : "0%",
                  }}
                />

              </div>

            </div>

            <div className="rounded-xl border border-blue-100 bg-blue-50 p-5">

              <h3 className="text-lg font-semibold text-blue-700">
                AI Recruitment Summary
              </h3>

              <p className="mt-3 leading-7 text-slate-700">

                You currently have{" "}

                <strong>
                  {dashboard.stats.active_jobs}
                </strong>{" "}

                active jobs available for hiring.

                <br />

                AI has already processed{" "}

                <strong>
                  {dashboard.stats.parsed_resumes}
                </strong>{" "}

                resumes, making semantic search,
                ATS scoring and candidate ranking
                instantly available.

              </p>

            </div>

          </div>

        </Card>

      </div>

    </DashboardLayout>
  );
}