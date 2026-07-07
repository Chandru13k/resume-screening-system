// import { useEffect, useState } from "react";
// import { FileText, Briefcase, Send, Award } from "lucide-react";

// import DashboardLayout from "../components/DashboardLayout";
// import StatsCard from "../components/StatsCard";
// import Card from "../components/Card";
// import Loader from "../components/Loader";
// import api from "../api/api";

// interface Profile {
//   full_name: string;
//   phone: string | null;
//   location: string | null;
//   github_url: string | null;
//   linkedin_url: string | null;
//   portfolio_url: string | null;
// }

// interface Resume {
//   id: number;
//   original_filename: string;
//   parsing_completed: boolean;
//   created_at: string;
// }

// interface Dashboard {
//   profile: Profile;
//   resumes: Resume[];
// }

// export default function CandidateDashboard() {
//   const [dashboard, setDashboard] = useState<Dashboard | null>(null);
//   const [loading, setLoading] = useState(true);

//   async function loadDashboard() {
//     try {
//       const res = await api.get("/candidate/dashboard");
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
//         role="candidate"
//         title="Dashboard"
//       >
//         <Loader />
//       </DashboardLayout>
//     );
//   }

//   if (!dashboard) {
//     return null;
//   }

//   return (
//     <DashboardLayout
//       role="candidate"
//       title={`Welcome ${dashboard.profile.full_name}`}
//       subtitle="Manage your profile and job applications."
//     >
//       <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

//         <StatsCard
//           title="Uploaded Resumes"
//           value={dashboard.resumes.length}
//           color="text-blue-600"
//           icon={<FileText size={34} />}
//         />

//         <StatsCard
//           title="Parsed Resumes"
//           value={
//             dashboard.resumes.filter(r => r.parsing_completed).length
//           }
//           color="text-green-600"
//           icon={<Award size={34} />}
//         />

//         <StatsCard
//           title="Applications"
//           value="-"
//           color="text-purple-600"
//           icon={<Send size={34} />}
//         />

//         <StatsCard
//           title="Jobs Available"
//           value="-"
//           color="text-orange-600"
//           icon={<Briefcase size={34} />}
//         />

//       </div>

//       <div className="mt-8 grid gap-6 lg:grid-cols-2">

//         <Card title="Profile">

//           <div className="space-y-3">

//             <p><strong>Name:</strong> {dashboard.profile.full_name}</p>

//             <p><strong>Phone:</strong> {dashboard.profile.phone ?? "-"}</p>

//             <p><strong>Location:</strong> {dashboard.profile.location ?? "-"}</p>

//             <p><strong>GitHub:</strong> {dashboard.profile.github_url ?? "-"}</p>

//             <p><strong>LinkedIn:</strong> {dashboard.profile.linkedin_url ?? "-"}</p>

//             <p><strong>Portfolio:</strong> {dashboard.profile.portfolio_url ?? "-"}</p>

//           </div>

//         </Card>

//         <Card title="Recent Resumes">

//           {dashboard.resumes.length === 0 ? (

//             <p>No resumes uploaded.</p>

//           ) : (

//             <div className="space-y-4">

//               {dashboard.resumes.map((resume) => (

//                 <div
//                   key={resume.id}
//                   className="rounded-xl border p-4"
//                 >

//                   <h3 className="font-semibold">
//                     {resume.original_filename}
//                   </h3>

//                   <p className="mt-2 text-sm text-slate-500">
//                     {new Date(resume.created_at).toLocaleDateString()}
//                   </p>

//                   <span
//                     className={`mt-3 inline-block rounded-lg px-3 py-1 text-sm ${
//                       resume.parsing_completed
//                         ? "bg-green-100 text-green-700"
//                         : "bg-yellow-100 text-yellow-700"
//                     }`}
//                   >
//                     {resume.parsing_completed ? "Parsed" : "Pending"}
//                   </span>

//                 </div>

//               ))}

//             </div>

//           )}

//         </Card>

//       </div>

//     </DashboardLayout>
//   );
// }





import { useEffect, useState } from "react";
import { FileText, Briefcase, Send, Award } from "lucide-react";

import DashboardLayout from "../components/DashboardLayout";
import StatsCard from "../components/StatsCard";
import Card from "../components/Card";
import Loader from "../components/Loader";
import api from "../api/api";

interface Profile {
  full_name: string;
  phone: string | null;
  location: string | null;
  github_url: string | null;
  linkedin_url: string | null;
  portfolio_url: string | null;
}

interface Resume {
  id: number;
  original_filename: string;
  parsing_completed: boolean;
  created_at: string;
}

interface Dashboard {
  profile: Profile;
  resumes: Resume[];
}

export default function CandidateDashboard() {
  const [dashboard, setDashboard] = useState<Dashboard | null>(null);
  const [loading, setLoading] = useState(true);

  async function loadDashboard() {
    try {
      const res = await api.get("/candidate/dashboard");
      setDashboard(res.data);
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
        role="candidate"
        title="Dashboard"
      >
        <Loader />
      </DashboardLayout>
    );
  }

  if (!dashboard) {
    return null;
  }

  return (
    <DashboardLayout
      role="candidate"
      title={`Welcome ${dashboard.profile.full_name}`}
      subtitle="Manage your profile and job applications."
    >
      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

        <StatsCard
          title="Uploaded Resumes"
          value={dashboard.resumes.length}
          color="text-blue-600"
          icon={<FileText size={34} />}
        />

        <StatsCard
          title="Parsed Resumes"
          value={
            dashboard.resumes.filter(r => r.parsing_completed).length
          }
          color="text-green-600"
          icon={<Award size={34} />}
        />

        <StatsCard
          title="Applications"
          value="-"
          color="text-purple-600"
          icon={<Send size={34} />}
        />

        <StatsCard
          title="Jobs Available"
          value="-"
          color="text-orange-600"
          icon={<Briefcase size={34} />}
        />

      </div>

      <div className="mt-8 grid gap-6 lg:grid-cols-2">

        <Card title="Profile">

          <div className="space-y-3">

            <p><strong>Name:</strong> {dashboard.profile.full_name}</p>

            <p><strong>Phone:</strong> {dashboard.profile.phone ?? "-"}</p>

            <p><strong>Location:</strong> {dashboard.profile.location ?? "-"}</p>

            <p><strong>GitHub:</strong> {dashboard.profile.github_url ?? "-"}</p>

            <p><strong>LinkedIn:</strong> {dashboard.profile.linkedin_url ?? "-"}</p>

            <p><strong>Portfolio:</strong> {dashboard.profile.portfolio_url ?? "-"}</p>

          </div>

        </Card>

        <Card title="Recent Resumes">

          {dashboard.resumes.length === 0 ? (

            <p>No resumes uploaded.</p>

          ) : (

            <div className="space-y-4">

              {dashboard.resumes.map((resume) => (

                <div
                  key={resume.id}
                  className="rounded-xl border p-4"
                >

                  <h3 className="font-semibold">
                    {resume.original_filename}
                  </h3>

                  <p className="mt-2 text-sm text-slate-500">
                    {new Date(resume.created_at).toLocaleDateString()}
                  </p>

                  <span
                    className={`mt-3 inline-block rounded-lg px-3 py-1 text-sm ${
                      resume.parsing_completed
                        ? "bg-green-100 text-green-700"
                        : "bg-yellow-100 text-yellow-700"
                    }`}
                  >
                    {resume.parsing_completed ? "Parsed" : "Pending"}
                  </span>

                </div>

              ))}

            </div>

          )}

        </Card>

      </div>

    </DashboardLayout>
  );
}