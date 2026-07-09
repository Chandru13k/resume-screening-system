// import { useEffect, useState } from "react";
// import DashboardLayout from "../components/DashboardLayout";
// import Card from "../components/Card";
// import Loader from "../components/Loader";
// import api from "../api/api";
// import { toast } from "sonner";
// import EmptyState from "../components/EmptyState";

// interface Job {
//   id: number;
//   title: string;
//   company_name: string;
//   location: string | null;
//   work_mode: string | null;
//   employment_type: string | null;
//   experience_required: string | null;
//   salary_min: string | null;
//   salary_max: string | null;
//   description: string;
// }

// interface Resume {
//   id: number;
//   original_filename: string;
// }

// export default function Jobs() {
//   const [jobs, setJobs] = useState<Job[]>([]);
//   const [resumes, setResumes] = useState<Resume[]>([]);
//   const [selectedResume, setSelectedResume] = useState<number>();
//   const [loading, setLoading] = useState(true);

//   async function loadData() {
//     try {
//       const [jobsRes, resumeRes] = await Promise.all([
//         api.get("/candidate/jobs"),
//         api.get("/resumes"),
//       ]);

//       setJobs(jobsRes.data);
//       setResumes(resumeRes.data);

//       if (resumeRes.data.length > 0) {
//         setSelectedResume(resumeRes.data[0].id);
//       }
//     } finally {
//       setLoading(false);
//     }
//   }

//   async function apply(jobId: number) {
//     if (!selectedResume) {
//       toast.warning("Please upload a resume first.");
//       return;
//     }

//     try {
//       await api.post(`/jobs/${jobId}/apply`, {
//         resume_id: selectedResume,
//       });

//       toast.success("Application submitted successfully.");
//     } catch (err: any) {
//       toast.error(err?.response?.data?.detail || "Application failed.");
//     }
//   }

//   useEffect(() => {
//     loadData();
//   }, []);

//   if (loading) {
//     return (
//       <DashboardLayout role="candidate" title="Browse Jobs">
//         <Loader />
//       </DashboardLayout>
//     );
//   }

//   return (
//     <DashboardLayout
//       role="candidate"
//       title="Browse Jobs"
//       subtitle="Discover opportunities matching your skills."
//     >
//       <div className="mb-8 flex items-center gap-4">

//         <label className="font-semibold">
//           Resume
//         </label>

//         <select
//           value={selectedResume}
//           onChange={(e) =>
//             setSelectedResume(Number(e.target.value))
//           }
//           className="rounded-xl border p-3"
//         >
//           {resumes.map((resume) => (
//             <option
//               key={resume.id}
//               value={resume.id}
//             >
//               {resume.original_filename}
//             </option>
//           ))}
//         </select>

//       </div>

//       <div className="grid gap-6">

//   {jobs.length === 0 ? (

//     <EmptyState message="No jobs available." />

//   ) : (

//     jobs.map((job) => (

//       <Card key={job.id}>

//         <div className="flex items-start justify-between">

//           <div>

//             <h2 className="text-2xl font-bold">
//               {job.title}
//             </h2>

//             <p className="mt-2 text-slate-500">
//               {job.company_name}
//             </p>

//           </div>

//           <button
//             onClick={() => apply(job.id)}
//             className="rounded-xl bg-blue-600 px-6 py-3 text-white hover:bg-blue-700"
//           >
//             Apply
//           </button>

//         </div>

//         <div className="mt-6 flex flex-wrap gap-3">

//           {job.location && (
//             <span className="rounded-full bg-slate-100 px-3 py-1">
//               📍 {job.location}
//             </span>
//           )}

//           {job.work_mode && (
//             <span className="rounded-full bg-blue-100 px-3 py-1">
//               {job.work_mode}
//             </span>
//           )}

//           {job.employment_type && (
//             <span className="rounded-full bg-green-100 px-3 py-1">
//               {job.employment_type}
//             </span>
//           )}

//           {job.experience_required && (
//             <span className="rounded-full bg-orange-100 px-3 py-1">
//               {job.experience_required}
//             </span>
//           )}

//         </div>

//         <p className="mt-6 leading-7 text-slate-600">
//           {job.description}
//         </p>

//         {(job.salary_min || job.salary_max) && (
//           <div className="mt-6 font-semibold text-green-600">
//             ₹ {job.salary_min ?? "-"} — ₹ {job.salary_max ?? "-"}
//           </div>
//         )}

//       </Card>

//     ))

//   )}

// </div>

//     </DashboardLayout>
//   );
// }



import { useEffect, useMemo, useState } from "react";
import DashboardLayout from "../components/DashboardLayout";
import Card from "../components/Card";
import Loader from "../components/Loader";
import EmptyState from "../components/EmptyState";
import api from "../api/api";
import { toast } from "sonner";

interface Job {
  id: number;
  title: string;
  company_name: string;
  location: string | null;
  work_mode: string | null;
  employment_type: string | null;
  experience_required: string | null;
  salary_min: string | null;
  salary_max: string | null;
  description: string;
  is_applied: boolean;
}

interface Resume {
  id: number;
  original_filename: string;
}

export default function Jobs() {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [resumes, setResumes] = useState<Resume[]>([]);
  const [selectedResume, setSelectedResume] = useState<number>();

  const [search, setSearch] = useState("");

  const [loading, setLoading] = useState(true);

  async function loadData() {
    try {
      const [jobsRes, resumeRes] = await Promise.all([
        api.get("/candidate/jobs"),
        api.get("/resumes"),
      ]);

      setJobs(jobsRes.data);

      setResumes(resumeRes.data);

      if (resumeRes.data.length > 0) {
        setSelectedResume(resumeRes.data[0].id);
      }
    } catch (err) {
      toast.error("Unable to load jobs.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadData();
  }, []);

  async function apply(jobId: number) {
    if (!selectedResume) {
      toast.warning("Please upload a resume first.");
      return;
    }

    try {
      await api.post(`/jobs/${jobId}/apply`, {
        resume_id: selectedResume,
      });

      toast.success("Application submitted successfully.");

      setJobs((prev) =>
        prev.map((job) =>
          job.id === jobId
            ? {
                ...job,
                is_applied: true,
              }
            : job
        )
      );
    } catch (err: any) {
      toast.error(
        err?.response?.data?.detail ??
          "Application failed."
      );
    }
  }

  const filteredJobs = useMemo(() => {
    return jobs.filter(
      (job) =>
        job.title
          .toLowerCase()
          .includes(search.toLowerCase()) ||
        job.company_name
          .toLowerCase()
          .includes(search.toLowerCase())
    );
  }, [jobs, search]);

  if (loading) {
    return (
      <DashboardLayout
        role="candidate"
        title="Browse Jobs"
      >
        <Loader />
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout
      role="candidate"
      title="Browse Jobs"
      subtitle="Discover opportunities matching your skills."
    >
      <div className="mb-8 flex flex-col gap-5 lg:flex-row lg:items-end lg:justify-between">

        <div>

          <label className="mb-2 block font-semibold">
            Select Resume
          </label>

          <select
            value={selectedResume}
            onChange={(e) =>
              setSelectedResume(Number(e.target.value))
            }
            className="w-full rounded-xl border border-slate-300 p-3 md:w-96"
          >
            {resumes.map((resume) => (
              <option
                key={resume.id}
                value={resume.id}
              >
                {resume.original_filename}
              </option>
            ))}
          </select>

        </div>

        <div>

          <label className="mb-2 block font-semibold">
            Search Jobs
          </label>

          <input
            type="text"
            placeholder="Search title or company..."
            value={search}
            onChange={(e) =>
              setSearch(e.target.value)
            }
            className="w-full rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500 md:w-96"
          />

        </div>

      </div>

      <div className="grid gap-6">

        {filteredJobs.length === 0 ? (

          <EmptyState message="No jobs available." />

        ) : (

          filteredJobs.map((job) => (

            <Card key={job.id}>

              <div className="flex flex-col gap-5 lg:flex-row lg:items-start lg:justify-between">

                <div>

                  <h2 className="text-2xl font-bold">
                    {job.title}
                  </h2>

                  <p className="mt-2 text-lg text-slate-500">
                    {job.company_name}
                  </p>

                </div>

                {job.is_applied ? (

                  <button
                    disabled
                    className="cursor-not-allowed rounded-xl bg-green-600 px-6 py-3 font-semibold text-white"
                  >
                    ✓ Applied
                  </button>

                ) : (

                  <button
                    onClick={() =>
                      apply(job.id)
                    }
                    className="rounded-xl bg-blue-600 px-6 py-3 font-semibold text-white transition hover:scale-105 hover:bg-blue-700"
                  >
                    Apply Now
                  </button>

                )}

              </div>

              <div className="mt-6 flex flex-wrap gap-3">

                {job.location && (
                  <span className="rounded-full bg-slate-100 px-4 py-2">
                    📍 {job.location}
                  </span>
                )}

                {job.work_mode && (
                  <span className="rounded-full bg-blue-100 px-4 py-2 text-blue-700">
                    {job.work_mode}
                  </span>
                )}

                {job.employment_type && (
                  <span className="rounded-full bg-green-100 px-4 py-2 text-green-700">
                    {job.employment_type}
                  </span>
                )}

                {job.experience_required && (
                  <span className="rounded-full bg-orange-100 px-4 py-2 text-orange-700">
                    {job.experience_required}
                  </span>
                )}

              </div>

              <p className="mt-6 leading-8 text-slate-600">
                {job.description}
              </p>

              {(job.salary_min || job.salary_max) && (

                <div className="mt-6 rounded-xl bg-green-50 p-4">

                  <p className="font-semibold text-green-700">
                    Salary Range
                  </p>

                  <p className="mt-1 text-lg font-bold text-green-600">
                    ₹ {job.salary_min ?? "-"} — ₹ {job.salary_max ?? "-"}
                  </p>

                </div>

              )}

            </Card>

          ))

        )}

      </div>

    </DashboardLayout>
  );
}