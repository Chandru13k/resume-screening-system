// import { useEffect, useState } from "react";
// import DashboardLayout from "../components/DashboardLayout";
// import Card from "../components/Card";
// import Loader from "../components/Loader";
// import api from "../api/api";
// import { toast } from "sonner";
// import EmptyState from "../components/EmptyState";
// import AIInsightsModal from "../components/AIInsightsModal";
// interface Job {
//   id: number;
//   title: string;
// }

// interface Applicant {
//   application_id: number;
//   candidate_id: number;
//   candidate_name: string;
//   candidate_email: string;
//   resume_id: number;
//   status: string;
//   applied_at: string;
// }

// const STATUS = [
//   "APPLIED",
//   "SHORTLISTED",
//   "INTERVIEW",
//   "REJECTED",
//   "HIRED",
// ];

// export default function Applicants() {
//   const [jobs, setJobs] = useState<Job[]>([]);
//   const [selectedJob, setSelectedJob] = useState<number>();

//   const [applicants, setApplicants] = useState<Applicant[]>([]);

//   const [loading, setLoading] = useState(true);
//   const [aiData, setAiData] = useState<any>(null);

//   const [showAI, setShowAI] = useState(false);
//   const [search, setSearch] = useState("");
//   async function loadJobs() {
//     const res = await api.get("/jobs");

//     setJobs(res.data);

//     if (res.data.length > 0) {
//       setSelectedJob(res.data[0].id);
//     }
//   }

//   async function loadApplicants(jobId: number) {
//     const res = await api.get(
//       `/jobs/${jobId}/applications`
//     );

//     setApplicants(res.data);
//   }

//   useEffect(() => {
//     async function load() {
//       await loadJobs();

//       setLoading(false);
//     }

//     load();
//   }, []);

//   useEffect(() => {
//     if (selectedJob) {
//       loadApplicants(selectedJob);
//     }
//   }, [selectedJob]);

//   async function updateStatus(
//     applicationId: number,
//     status: string
//   ) {
//     try {
//       await api.patch(
//         `/applications/${applicationId}/status`,
//         {
//           status,
//         }
//       );

//       if (selectedJob) {
//         loadApplicants(selectedJob);
//       }
//     } catch (err) {
//       console.error(err);
//     }
//   }

//   async function viewAI(applicationId: number) {
//     try {

//         const res = await api.get(
//         `/applications/${applicationId}/ai-insights`
//         );

//         setAiData(res.data);

//         setShowAI(true);

//     } catch (err) {
//         console.error(err);
//     }
//     }

//   if (loading) {
//     return (
//       <DashboardLayout
//         role="recruiter"
//         title="Applicants"
//       >
//         <Loader />
//       </DashboardLayout>
//     );
//   }
//     return (
//     <DashboardLayout
//       role="recruiter"
//       title="Applicants"
//       subtitle="Review applicants, update status and view AI insights."
//     >

//       <div className="mb-6">

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

//       <Card title="Applicants">

//         <table className="w-full">

//           <thead>

//             <tr className="border-b">

//               <th className="py-3 text-left">
//                 Candidate
//               </th>

//               <th>Email</th>

//               <th>Resume</th>

//               <th>Status</th>

//               <th>Applied</th>

//               <th>Actions</th>

//             </tr>

//           </thead>

//           <tbody>

//             {applicants.length === 0 && (
//              <tr>
//                <td colSpan={6}>
//                 <EmptyState message="No applicants found." />
//                </td>
//               </tr>
//             )}

//             {applicants.map((applicant) => (

//               <tr
//                 key={applicant.application_id}
//                 className="border-b"
//               >

//                 <td className="py-4 font-medium">
//                   {applicant.candidate_name}
//                 </td>

//                 <td>
//                   {applicant.candidate_email}
//                 </td>

//                 <td>
//                   #{applicant.resume_id}
//                 </td>

//                 <td>

//                   <select
//                     value={applicant.status}
//                     onChange={(e) =>
//                       updateStatus(
//                         applicant.application_id,
//                         e.target.value
//                       )
//                     }
//                     className="rounded-lg border p-2"
//                   >

//                     {STATUS.map((status) => (

//                       <option
//                         key={status}
//                         value={status}
//                       >
//                         {status}
//                       </option>

//                     ))}

//                   </select>

//                 </td>

//                 <td>
//                   {new Date(
//                     applicant.applied_at
//                   ).toLocaleDateString()}
//                 </td>

//                 <td>

//                   <button
//                     onClick={() =>
//                       viewAI(
//                         applicant.application_id
//                       )
//                     }
//                     className="rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
//                   >
//                     AI Insights
//                   </button>

//                 </td>

//               </tr>

//             ))}

//           </tbody>

//         </table>

//       </Card>

//       <AIInsightsModal
//       open={showAI}
//       data={aiData}
//       onClose={() => setShowAI(false)}
//     />

//     </DashboardLayout>
//   );
// }






import { useEffect, useMemo, useState } from "react";
import { toast } from "sonner";

import DashboardLayout from "../components/DashboardLayout";
import Card from "../components/Card";
import Loader from "../components/Loader";
import EmptyState from "../components/EmptyState";
import AIInsightsModal from "../components/AIInsightsModal";

import api from "../api/api";

interface Job {
  id: number;
  title: string;
}

interface Applicant {
  application_id: number;
  candidate_id: number;
  candidate_name: string;
  candidate_email: string;
  resume_id: number;
  status: string;
  applied_at: string;
}

const STATUS = [
  "APPLIED",
  "SHORTLISTED",
  "INTERVIEW",
  "REJECTED",
  "HIRED",
];

export default function Applicants() {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [selectedJob, setSelectedJob] = useState<number>();

  const [applicants, setApplicants] = useState<Applicant[]>([]);

  const [loading, setLoading] = useState(true);

  const [search, setSearch] = useState("");

  const [aiData, setAiData] = useState<any>(null);

  const [showAI, setShowAI] = useState(false);

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

  async function loadApplicants(jobId: number) {
    try {
      const res = await api.get(
        `/jobs/${jobId}/applications`
      );

      setApplicants(res.data);
    } catch (err) {
      console.error(err);
      toast.error("Unable to load applicants.");
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
      loadApplicants(selectedJob);
    }
  }, [selectedJob]);

  async function updateStatus(
    applicationId: number,
    status: string
  ) {
    try {
      await api.patch(
        `/applications/${applicationId}/status`,
        {
          status,
        }
      );

      toast.success("Status updated successfully.");

      if (selectedJob) {
        loadApplicants(selectedJob);
      }
    } catch (err) {
      console.error(err);
      toast.error("Unable to update status.");
    }
  }

  async function viewAI(
    applicationId: number
  ) {
    try {
      const res = await api.get(
        `/applications/${applicationId}/ai-insights`
      );

      setAiData(res.data);

      setShowAI(true);
    } catch (err) {
      console.error(err);
      toast.error("Unable to fetch AI insights.");
    }
  }

  const filteredApplicants = useMemo(() => {
    return applicants.filter((applicant) =>
      applicant.candidate_name
        .toLowerCase()
        .includes(search.toLowerCase())
    );
  }, [applicants, search]);
    if (loading) {
    return (
      <DashboardLayout
        role="recruiter"
        title="Applicants"
      >
        <Loader />
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout
      role="recruiter"
      title="Applicants"
      subtitle="Review applicants, update status and view AI insights."
    >

      <div className="mb-8 flex flex-col gap-5 md:flex-row md:items-end md:justify-between">

        <div>

          <label className="mb-2 block font-semibold">
            Select Job
          </label>

          <select
            value={selectedJob}
            onChange={(e) =>
              setSelectedJob(Number(e.target.value))
            }
            className="w-full rounded-xl border border-slate-300 p-3 md:w-96"
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

        <div>

          <label className="mb-2 block font-semibold">
            Search Candidate
          </label>

          <input
            type="text"
            placeholder="Search by name..."
            value={search}
            onChange={(e) =>
              setSearch(e.target.value)
            }
            className="w-full rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500 md:w-80"
          />

        </div>

      </div>

      <Card
        title={`Applicants (${filteredApplicants.length})`}
      >

        <div className="overflow-x-auto">

          <table className="min-w-full">

            <thead>

              <tr className="border-b bg-slate-100">

                <th className="px-4 py-3 text-left font-semibold">
                  Candidate
                </th>

                <th className="px-4 py-3 text-left font-semibold">
                  Email
                </th>

                <th className="px-4 py-3 text-left font-semibold">
                  Resume
                </th>

                <th className="px-4 py-3 text-left font-semibold">
                  Status
                </th>

                <th className="px-4 py-3 text-left font-semibold">
                  Applied
                </th>

                <th className="px-4 py-3 text-left font-semibold">
                  Actions
                </th>

              </tr>

            </thead>

            <tbody>
                              {filteredApplicants.length === 0 ? (

                <tr>

                  <td
                    colSpan={6}
                    className="py-8"
                  >
                    <EmptyState message="No applicants found." />
                  </td>

                </tr>

              ) : (

                filteredApplicants.map((applicant) => (

                  <tr
                    key={applicant.application_id}
                    className="border-b transition hover:bg-slate-50"
                  >

                    <td className="px-4 py-4">

                      <div className="font-semibold">
                        {applicant.candidate_name}
                      </div>

                    </td>

                    <td className="px-4 py-4">
                      {applicant.candidate_email}
                    </td>

                    <td className="px-4 py-4">
                      #{applicant.resume_id}
                    </td>

                    <td className="px-4 py-4">

                      <select
                        value={applicant.status}
                        onChange={(e) =>
                          updateStatus(
                            applicant.application_id,
                            e.target.value
                          )
                        }
                        className="rounded-lg border border-slate-300 p-2"
                      >

                        {STATUS.map((status) => (

                          <option
                            key={status}
                            value={status}
                          >
                            {status}
                          </option>

                        ))}

                      </select>

                    </td>

                    <td className="px-4 py-4">
                      {new Date(
                        applicant.applied_at
                      ).toLocaleDateString()}
                    </td>

                    <td className="px-4 py-4">

                      <button
                        onClick={() =>
                          viewAI(
                            applicant.application_id
                          )
                        }
                        className="rounded-lg bg-blue-600 px-4 py-2 text-white transition hover:scale-105 hover:bg-blue-700"
                      >
                        AI Insights
                      </button>

                    </td>

                  </tr>

                ))

              )}

            </tbody>

          </table>

        </div>

      </Card>

      <AIInsightsModal
        open={showAI}
        data={aiData}
        onClose={() => setShowAI(false)}
      />

    </DashboardLayout>
  );
}