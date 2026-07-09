// import { useEffect, useState } from "react";
// import DashboardLayout from "../components/DashboardLayout";
// import Card from "../components/Card";
// import Loader from "../components/Loader";
// import api from "../api/api";
// import StatsCard from "../components/StatsCard";
// import ApplicationStatusChart from "../components/ApplicationStatusChart";
// import ScoreChart from "../components/ScoreChart";

// import {
//   Users,
//   Trophy,
//   Star,
//   UserCheck,
// } from "lucide-react";


// interface Job {
//   id: number;
//   title: string;
// }

// interface AnalyticsResponse {
//   job_id: number;
//   job_title: string;
//   total_candidates: number;
//   average_match_score: number;
//   top_score: number;
//   recommended_for_interview: number;
// }

// interface DashboardResponse {
//   job: {
//     id: number;
//     title: string;
//     company: string;
//     status: string;
//   };
//   statistics: {
//     applications: number;
//     shortlisted: number;
//     interview: number;
//     rejected: number;
//     hired: number;
//   };
//   ranking: any[];
// }

// export default function Analytics() {
//   const [jobs, setJobs] = useState<Job[]>([]);
//   const [selectedJob, setSelectedJob] = useState<number>();

//   const [analytics, setAnalytics] =
//     useState<AnalyticsResponse>();

//   const [dashboard, setDashboard] =
//     useState<DashboardResponse>();

//   const [loading, setLoading] = useState(true);

//   async function loadJobs() {
//     const res = await api.get("/jobs");

//     setJobs(res.data);

//     if (res.data.length > 0) {
//       setSelectedJob(res.data[0].id);
//     }
//   }

//   async function loadAnalytics(jobId: number) {
//     const [analyticsRes, dashboardRes] =
//       await Promise.all([
//         api.get(`/dashboard/job/${jobId}`),
//         api.get(`/recruiter-dashboard/jobs/${jobId}`),
//       ]);

//     setAnalytics(analyticsRes.data);

//     setDashboard(dashboardRes.data);
//   }

//   useEffect(() => {
//     async function init() {
//       await loadJobs();

//       setLoading(false);
//     }

//     init();
//   }, []);

//   useEffect(() => {
//     if (selectedJob) {
//       loadAnalytics(selectedJob);
//     }
//   }, [selectedJob]);

//   if (loading) {
//     return (
//       <DashboardLayout
//         role="recruiter"
//         title="Analytics"
//       >
//         <Loader />
//       </DashboardLayout>
//     );
//   }

//   return (
//     <DashboardLayout
//       role="recruiter"
//       title="Recruitment Analytics"
//       subtitle="AI-powered recruitment insights."
//     >
//       <div className="mb-8">

//         <label className="mb-2 block font-semibold">
//           Select Job
//         </label>

//         <select
//           value={selectedJob}
//           onChange={(e) =>
//             setSelectedJob(Number(e.target.value))
//           }
//           className="w-96 rounded-lg border p-3"
//         >
//           {jobs.map((job) => (
//             <option
//               key={job.id}
//               value={job.id}
//             >
//               {job.title}
//             </option>
//           ))}
//         </select>

//       </div>

//       {analytics && (

//     <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

//         <StatsCard
//         title="Candidates"
//         value={analytics.total_candidates}
//         color="text-blue-600"
//         icon={<Users size={34} />}
//         />

//     <StatsCard
//         title="Average Match"
//         value={`${analytics.average_match_score.toFixed(1)}%`}
//         color="text-green-600"
//         icon={<Star size={34} />}
//     />

//     <StatsCard
//         title="Top Score"
//         value={`${analytics.top_score.toFixed(1)}%`}
//         color="text-purple-600"
//         icon={<Trophy size={34} />}
//     />

//     <StatsCard
//         title="Interview Ready"
//         value={analytics.recommended_for_interview}
//         color="text-orange-600"
//         icon={<UserCheck size={34} />}
//     />

//     </div>

//       )}

//       {dashboard && (

//         <div className="mt-8 grid gap-6 lg:grid-cols-2">

//           <Card title="Application Statistics">

//             <ApplicationStatusChart
//             data={[
//             {
//             name: "Applied",
//             value: dashboard.statistics.applications,
//             },
//             {
//             name: "Shortlisted",
//             value: dashboard.statistics.shortlisted,
//             },
//             {
//             name: "Interview",
//             value: dashboard.statistics.interview,
//             },
//             {
//             name: "Rejected",
//             value: dashboard.statistics.rejected,
//             },
//             {
//             name: "Hired",
//             value: dashboard.statistics.hired,
//             },
//            ]}
//         />

//         </Card>

//           <Card title="AI Ranking">

//             <ScoreChart
//               data={dashboard.ranking.map((candidate: any) => ({
//               name: `C${candidate.candidate_id}`,
//               score: candidate.overall_score,
//               }))}
//             />

//           </Card>

//         </div>

//       )}

//     </DashboardLayout>
//   );
// }



import { useEffect, useState } from "react";
import {
  Users,
  Trophy,
  Star,
  UserCheck,
} from "lucide-react";
import { toast } from "sonner";

import DashboardLayout from "../components/DashboardLayout";
import Card from "../components/Card";
import Loader from "../components/Loader";
import StatsCard from "../components/StatsCard";
import EmptyState from "../components/EmptyState";
import ApplicationStatusChart from "../components/ApplicationStatusChart";
import ScoreChart from "../components/ScoreChart";
import api from "../api/api";

interface Job {
  id: number;
  title: string;
}

interface AnalyticsResponse {
  job_id: number;
  job_title: string;
  total_candidates: number;
  average_match_score: number;
  top_score: number;
  recommended_for_interview: number;
}

interface RankingCandidate {
  candidate_id: number;
  overall_score: number;
  status: string;
}

interface DashboardResponse {
  job: {
    id: number;
    title: string;
    company: string;
    status: string;
  };

  statistics: {
    applications: number;
    shortlisted: number;
    interview: number;
    rejected: number;
    hired: number;
  };

  ranking: RankingCandidate[];
}

export default function Analytics() {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [selectedJob, setSelectedJob] =
    useState<number>();

  const [analytics, setAnalytics] =
    useState<AnalyticsResponse>();

  const [dashboard, setDashboard] =
    useState<DashboardResponse>();

  const [loading, setLoading] =
    useState(true);

  async function loadJobs() {
    try {
      const res = await api.get("/jobs");

      setJobs(res.data);

      if (res.data.length > 0) {
        setSelectedJob(res.data[0].id);
      }
    } catch (err) {
      console.error(err);
      toast.error("Unable to load jobs.");
    }
  }

  async function loadAnalytics(jobId: number) {
    try {
      const [analyticsRes, dashboardRes] =
        await Promise.all([
          api.get(`/dashboard/job/${jobId}`),
          api.get(
            `/recruiter-dashboard/jobs/${jobId}`
          ),
        ]);

      setAnalytics(analyticsRes.data);
      setDashboard(dashboardRes.data);
    } catch (err) {
      console.error(err);
      toast.error(
        "Unable to load analytics."
      );
    }
  }

  useEffect(() => {
    async function init() {
      await loadJobs();
      setLoading(false);
    }

    init();
  }, []);

  useEffect(() => {
    if (selectedJob) {
      loadAnalytics(selectedJob);
    }
  }, [selectedJob]);

  if (loading) {
    return (
      <DashboardLayout
        role="recruiter"
        title="Analytics"
      >
        <Loader />
      </DashboardLayout>
    );
  }

  if (jobs.length === 0) {
    return (
      <DashboardLayout
        role="recruiter"
        title="Analytics"
      >
        <EmptyState message="Create a job to view analytics." />
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout
      role="recruiter"
      title="Recruitment Analytics"
      subtitle="AI-powered recruitment insights."
    >
      <div className="mb-8">

        <label className="mb-2 block font-semibold">
          Select Job
        </label>

        <select
          value={selectedJob}
          onChange={(e) =>
            setSelectedJob(
              Number(e.target.value)
            )
          }
          className="w-full max-w-md rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500"
        >
          {jobs.map((job) => (
            <option
              key={job.id}
              value={job.id}
            >
              {job.title}
            </option>
          ))}
        </select>

      </div>

      {analytics && (

        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

          <StatsCard
            title="Candidates"
            value={analytics.total_candidates}
            color="text-blue-600"
            icon={<Users size={34} />}
          />

          <StatsCard
            title="Average Match"
            value={`${analytics.average_match_score.toFixed(
              1
            )}%`}
            color="text-green-600"
            icon={<Star size={34} />}
          />

          <StatsCard
            title="Top Score"
            value={`${analytics.top_score.toFixed(
              1
            )}%`}
            color="text-purple-600"
            icon={<Trophy size={34} />}
          />

          <StatsCard
            title="Interview Ready"
            value={
              analytics.recommended_for_interview
            }
            color="text-orange-600"
            icon={<UserCheck size={34} />}
          />

        </div>

      )}

      {dashboard && (

        <div className="mt-8 grid gap-6 lg:grid-cols-2">

          <Card title="Application Statistics">

            <ApplicationStatusChart
              data={[
                {
                  name: "Applied",
                  value:
                    dashboard.statistics
                      .applications,
                },
                {
                  name: "Shortlisted",
                  value:
                    dashboard.statistics
                      .shortlisted,
                },
                {
                  name: "Interview",
                  value:
                    dashboard.statistics
                      .interview,
                },
                {
                  name: "Rejected",
                  value:
                    dashboard.statistics
                      .rejected,
                },
                {
                  name: "Hired",
                  value:
                    dashboard.statistics
                      .hired,
                },
              ]}
            />

          </Card>

          <Card title="AI Ranking">
            console.log(dashboard.ranking);

            <ScoreChart
              data={dashboard.ranking.map((candidate: any) => ({
                name: candidate.candidate_name,
                score: candidate.overall_score,
              }))}
            />

          </Card>

        </div>

      )}

    </DashboardLayout>
  );
}