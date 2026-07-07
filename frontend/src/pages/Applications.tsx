// import { useEffect, useState } from "react";
// import DashboardLayout from "../components/DashboardLayout";
// import Card from "../components/Card";
// import Loader from "../components/Loader";
// import api from "../api/api";
// import EmptyState from "../components/EmptyState";


// interface Application {
//   application_id: number;
//   job_id: number;
//   job_title: string;
//   company_name: string;
//   location: string | null;
//   status: string;
//   applied_at: string;
// }

// export default function Applications() {
//   const [applications, setApplications] = useState<Application[]>([]);
//   const [loading, setLoading] = useState(true);

//   async function loadApplications() {
//     try {
//       const res = await api.get("/candidate/applications");
//       setApplications(res.data);
//     } catch (err) {
//       console.error(err);
//     } finally {
//       setLoading(false);
//     }
//   }

//   useEffect(() => {
//     loadApplications();
//   }, []);

//   if (loading) {
//     return (
//       <DashboardLayout
//         role="candidate"
//         title="My Applications"
//       >
//         <Loader />
//       </DashboardLayout>
//     );
//   }

//   return (
//     <DashboardLayout
//       role="candidate"
//       title="My Applications"
//       subtitle="Track every job you've applied for."
//     >
//       <Card title={`Applications (${applications.length})`}>

//         {applications.length === 0 ? (

//           <div className="py-12 text-center text-slate-500">
//             You haven't applied for any jobs yet.
//           </div>

//         ) : (

//           <table className="w-full">

//             <thead>

//               <tr className="border-b">

//                 <th className="py-4 text-left">
//                   Job
//                 </th>

//                 <th className="text-left">
//                   Company
//                 </th>

//                 <th className="text-left">
//                   Location
//                 </th>

//                 <th>
//                   Status
//                 </th>

//                 <th>
//                   Applied On
//                 </th>

//               </tr>

//             </thead>

//             <tbody>

//               {applications.map((application) => (

//                 <tr
//                   key={application.application_id}
//                   className="border-b hover:bg-slate-50"
//                 >

//                   <td className="py-5 font-semibold">
//                     {application.job_title}
//                   </td>

//                   <td>
//                     {application.company_name}
//                   </td>

//                   <td>
//                     {application.location ?? "-"}
//                   </td>

//                   <td>

//                     <span
//                       className={`rounded-lg px-3 py-1 text-sm font-medium
//                       ${
//                         application.status === "APPLIED"
//                           ? "bg-blue-100 text-blue-700"
//                           : ""
//                       }
//                       ${
//                         application.status === "SHORTLISTED"
//                           ? "bg-green-100 text-green-700"
//                           : ""
//                       }
//                       ${
//                         application.status === "INTERVIEW"
//                           ? "bg-purple-100 text-purple-700"
//                           : ""
//                       }
//                       ${
//                         application.status === "REJECTED"
//                           ? "bg-red-100 text-red-700"
//                           : ""
//                       }
//                       ${
//                         application.status === "HIRED"
//                           ? "bg-emerald-100 text-emerald-700"
//                           : ""
//                       }`}
//                     >
//                       {application.status}
//                     </span>

//                   </td>

//                   <td>
//                     {new Date(
//                       application.applied_at
//                     ).toLocaleDateString()}
//                   </td>

//                 </tr>

//               ))}

//             </tbody>

//           </table>

//         )}

//       </Card>
//     </DashboardLayout>
//   );
// }





import { useEffect, useMemo, useState } from "react";
import DashboardLayout from "../components/DashboardLayout";
import Card from "../components/Card";
import Loader from "../components/Loader";
import EmptyState from "../components/EmptyState";
import api from "../api/api";

interface Application {
  application_id: number;
  job_id: number;
  job_title: string;
  company_name: string;
  location: string | null;
  status: string;
  applied_at: string;
}

export default function Applications() {
  const [applications, setApplications] = useState<Application[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");

  async function loadApplications() {
    try {
      const res = await api.get("/candidate/applications");
      setApplications(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadApplications();
  }, []);

  const filteredApplications = useMemo(() => {
    return applications.filter(
      (application) =>
        application.job_title
          .toLowerCase()
          .includes(search.toLowerCase()) ||
        application.company_name
          .toLowerCase()
          .includes(search.toLowerCase())
    );
  }, [applications, search]);

  function getStatusColor(status: string) {
    switch (status) {
      case "APPLIED":
        return "bg-blue-100 text-blue-700";
      case "SHORTLISTED":
        return "bg-green-100 text-green-700";
      case "INTERVIEW":
        return "bg-purple-100 text-purple-700";
      case "REJECTED":
        return "bg-red-100 text-red-700";
      case "HIRED":
        return "bg-emerald-100 text-emerald-700";
      default:
        return "bg-slate-100 text-slate-700";
    }
  }

  if (loading) {
    return (
      <DashboardLayout
        role="candidate"
        title="My Applications"
      >
        <Loader />
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout
      role="candidate"
      title="My Applications"
      subtitle="Track every job you've applied for."
    >

      <div className="mb-6">

        <input
          type="text"
          placeholder="Search by job title or company..."
          value={search}
          onChange={(e) =>
            setSearch(e.target.value)
          }
          className="w-full max-w-md rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500"
        />

      </div>

      <Card
        title={`Applications (${filteredApplications.length})`}
      >

        {filteredApplications.length === 0 ? (

          <EmptyState message="You haven't applied for any jobs yet." />

        ) : (

          <div className="overflow-x-auto">

            <table className="min-w-full">

              <thead>

                <tr className="border-b bg-slate-100">

                  <th className="px-4 py-3 text-left font-semibold">
                    Job
                  </th>

                  <th className="px-4 py-3 text-left font-semibold">
                    Company
                  </th>

                  <th className="px-4 py-3 text-left font-semibold">
                    Location
                  </th>

                  <th className="px-4 py-3 text-left font-semibold">
                    Status
                  </th>

                  <th className="px-4 py-3 text-left font-semibold">
                    Applied On
                  </th>

                </tr>

              </thead>

              <tbody>

                {filteredApplications.map((application) => (

                  <tr
                    key={application.application_id}
                    className="border-b transition hover:bg-slate-50"
                  >

                    <td className="px-4 py-4 font-semibold">
                      {application.job_title}
                    </td>

                    <td className="px-4 py-4">
                      {application.company_name}
                    </td>

                    <td className="px-4 py-4">
                      {application.location ?? "-"}
                    </td>

                    <td className="px-4 py-4">

                      <span
                        className={`rounded-full px-4 py-1 text-sm font-medium ${getStatusColor(
                          application.status
                        )}`}
                      >
                        {application.status}
                      </span>

                    </td>

                    <td className="px-4 py-4">
                      {new Date(
                        application.applied_at
                      ).toLocaleDateString()}
                    </td>

                  </tr>

                ))}

              </tbody>

            </table>

          </div>

        )}

      </Card>

    </DashboardLayout>
  );
}