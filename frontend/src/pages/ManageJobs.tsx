// import { useEffect, useState } from "react";
// import DashboardLayout from "../components/DashboardLayout";
// import Card from "../components/Card";
// import Loader from "../components/Loader";
// import api from "../api/api";
// import { toast } from "sonner";


// interface Job {
//   id: number;
//   recruiter_id: number;
//   title: string;
//   company_name: string;
//   location: string | null;
//   work_mode: string | null;
//   employment_type: string | null;
//   experience_required: string | null;
//   salary_min: string | null;
//   salary_max: string | null;
//   total_positions: number;
//   application_deadline: string | null;
//   description: string;
//   status: string;
//   is_active: boolean;
// }

// const emptyJob = {
//   title: "",
//   company_name: "",
//   location: "",
//   work_mode: "",
//   employment_type: "",
//   experience_required: "",
//   salary_min: "",
//   salary_max: "",
//   total_positions: 1,
//   application_deadline: "",
//   description: "",
// };

// export default function ManageJobs() {
//   const [jobs, setJobs] = useState<Job[]>([]);
//   const [loading, setLoading] = useState(true);

//   const [showForm, setShowForm] = useState(false);

//   const [editingId, setEditingId] = useState<number | null>(null);

//   const [form, setForm] = useState<any>(emptyJob);

//   async function loadJobs() {
//     try {
//       const res = await api.get("/jobs");
//       setJobs(res.data);
//     } catch (err) {
//       console.error(err);
//     } finally {
//       setLoading(false);
//     }
//   }

//   useEffect(() => {
//     loadJobs();
//   }, []);

//   function handleChange(
//     e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
//   ) {
//     setForm({
//       ...form,
//       [e.target.name]: e.target.value,
//     });
//   }

//   async function saveJob() {
//     try {
//       if (editingId) {
//         await api.put(`/jobs/${editingId}`, form);
//       } else {
//         await api.post("/jobs", form);
//       }

//       setShowForm(false);
//       setEditingId(null);
//       setForm(emptyJob);

//       loadJobs();
//     } catch (err) {
//       console.error(err);
//       toast.error("Unable to save job.");
//     }
//   }

//   async function deleteJob(id: number) {
//     if (!window.confirm("Delete this job?")) return;

//     try {
//       await api.delete(`/jobs/${id}`);

//       loadJobs();
//     } catch (err) {
//       console.error(err);
//     }
//   }

//   function editJob(job: Job) {
//     setEditingId(job.id);

//     setForm(job);

//     setShowForm(true);
//   }

//   if (loading) {
//     return (
//       <DashboardLayout
//         role="recruiter"
//         title="Manage Jobs"
//       >
//         <Loader />
//       </DashboardLayout>
//     );
//   }
//     return (
//     <DashboardLayout
//       role="recruiter"
//       title="Manage Jobs"
//       subtitle="Create, edit and manage all your job postings."
//     >

//       <div className="mb-6 flex justify-end">

//         <button
//           onClick={() => {
//             setEditingId(null);
//             setForm(emptyJob);
//             setShowForm(true);
//           }}
//           className="rounded-xl bg-blue-600 px-6 py-3 font-semibold text-white hover:bg-blue-700"
//         >
//           + Create Job
//         </button>

//       </div>

//       <Card title="My Jobs">

//         <table className="w-full">

//           <thead>

//             <tr className="border-b">

//               <th className="py-3 text-left">Title</th>

//               <th>Company</th>

//               <th>Status</th>

//               <th>Actions</th>

//             </tr>

//           </thead>

//           <tbody>

//             {jobs.map((job) => (

//               <tr
//                 key={job.id}
//                 className="border-b"
//               >

//                 <td className="py-4">
//                   {job.title}
//                 </td>

//                 <td>
//                   {job.company_name}
//                 </td>

//                 <td>

//                   <span
//                     className={`rounded-lg px-3 py-1 text-sm ${
//                       job.is_active
//                         ? "bg-green-100 text-green-700"
//                         : "bg-red-100 text-red-700"
//                     }`}
//                   >
//                     {job.status}
//                   </span>

//                 </td>

//                 <td className="space-x-2">

//                   <button
//                     onClick={() => editJob(job)}
//                     className="rounded-lg bg-yellow-500 px-4 py-2 text-white hover:bg-yellow-600"
//                   >
//                     Edit
//                   </button>

//                   <button
//                     onClick={() => deleteJob(job.id)}
//                     className="rounded-lg bg-red-600 px-4 py-2 text-white hover:bg-red-700"
//                   >
//                     Delete
//                   </button>

//                 </td>

//               </tr>

//             ))}

//           </tbody>

//         </table>

//       </Card>

//       {showForm && (

//         <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">

//           <div className="max-h-[90vh] w-full max-w-3xl overflow-y-auto rounded-2xl bg-white p-8">

//             <h2 className="mb-6 text-3xl font-bold">

//               {editingId ? "Edit Job" : "Create Job"}

//             </h2>

//             <div className="grid gap-5 md:grid-cols-2">

//               <input
//                 name="title"
//                 placeholder="Job Title"
//                 value={form.title}
//                 onChange={handleChange}
//                 className="rounded-lg border p-3"
//               />

//               <input
//                 name="company_name"
//                 placeholder="Company"
//                 value={form.company_name}
//                 onChange={handleChange}
//                 className="rounded-lg border p-3"
//               />

//               <input
//                 name="location"
//                 placeholder="Location"
//                 value={form.location}
//                 onChange={handleChange}
//                 className="rounded-lg border p-3"
//               />

//               <input
//                 name="work_mode"
//                 placeholder="Work Mode"
//                 value={form.work_mode}
//                 onChange={handleChange}
//                 className="rounded-lg border p-3"
//               />

//               <input
//                 name="employment_type"
//                 placeholder="Employment Type"
//                 value={form.employment_type}
//                 onChange={handleChange}
//                 className="rounded-lg border p-3"
//               />

//               <input
//                 name="experience_required"
//                 placeholder="Experience"
//                 value={form.experience_required}
//                 onChange={handleChange}
//                 className="rounded-lg border p-3"
//               />

//               <input
//                 type="number"
//                 name="salary_min"
//                 placeholder="Minimum Salary"
//                 value={form.salary_min}
//                 onChange={handleChange}
//                 className="rounded-lg border p-3"
//               />

//               <input
//                 type="number"
//                 name="salary_max"
//                 placeholder="Maximum Salary"
//                 value={form.salary_max}
//                 onChange={handleChange}
//                 className="rounded-lg border p-3"
//               />

//               <input
//                 type="number"
//                 name="total_positions"
//                 placeholder="Positions"
//                 value={form.total_positions}
//                 onChange={handleChange}
//                 className="rounded-lg border p-3"
//               />

//               <input
//                 type="date"
//                 name="application_deadline"
//                 value={form.application_deadline}
//                 onChange={handleChange}
//                 className="rounded-lg border p-3"
//               />

//             </div>

//             <textarea
//               name="description"
//               rows={6}
//               placeholder="Job Description"
//               value={form.description}
//               onChange={handleChange}
//               className="mt-5 w-full rounded-lg border p-3"
//             />

//             <div className="mt-8 flex justify-end gap-4">

//               <button
//                 onClick={() => setShowForm(false)}
//                 className="rounded-lg border px-6 py-2"
//               >
//                 Cancel
//               </button>

//               <button
//                 onClick={saveJob}
//                 className="rounded-lg bg-blue-600 px-6 py-2 text-white hover:bg-blue-700"
//               >
//                 {editingId ? "Update Job" : "Create Job"}
//               </button>

//             </div>

//           </div>

//         </div>

//       )}

//     </DashboardLayout>
//   );
// }










import { useEffect, useMemo, useState } from "react";
import { toast } from "sonner";

import DashboardLayout from "../components/DashboardLayout";
import Card from "../components/Card";
import Loader from "../components/Loader";
import EmptyState from "../components/EmptyState";

import api from "../api/api";

interface Job {
  id: number;
  recruiter_id: number;
  title: string;
  company_name: string;
  location: string | null;
  work_mode: string |null;
  employment_type: string | null;
  experience_required: string | null;
  salary_min: string | null;
  salary_max: string | null;
  total_positions: number;
  application_deadline: string | null;
  description: string;
  status: string;
  is_active: boolean;
}

const emptyJob = {
  title: "",
  company_name: "",
  location: "",
  work_mode: "",
  employment_type: "",
  experience_required: "",
  salary_min: "",
  salary_max: "",
  total_positions: 1,
  application_deadline: "",
  description: "",
};

export default function ManageJobs() {

  const [jobs, setJobs] = useState<Job[]>([]);
  const [loading, setLoading] = useState(true);

  const [showForm, setShowForm] = useState(false);

  const [editingId, setEditingId] =
    useState<number | null>(null);

  const [search, setSearch] = useState("");

  const [form, setForm] =
    useState<any>(emptyJob);

  async function loadJobs() {

    try {

      const res = await api.get("/jobs");

      setJobs(res.data);

    } catch (err) {

      console.error(err);

      toast.error("Unable to load jobs.");

    } finally {

      setLoading(false);

    }

  }

  useEffect(() => {

    loadJobs();

  }, []);

  function handleChange(
    e: React.ChangeEvent<
      HTMLInputElement | HTMLTextAreaElement
    >
  ) {

    setForm({

      ...form,

      [e.target.name]: e.target.value,

    });

  }

  async function saveJob() {

    try {

      if (editingId) {

        await api.put(
          `/jobs/${editingId}`,
          form
        );

        toast.success(
          "Job updated successfully."
        );

      } else {

        await api.post(
          "/jobs",
          form
        );

        toast.success(
          "Job created successfully."
        );

      }

      setShowForm(false);

      setEditingId(null);

      setForm(emptyJob);

      loadJobs();

    } catch (err) {

      console.error(err);

      toast.error("Unable to save job.");

    }

  }

  async function deleteJob(
    id: number
  ) {

    if (
      !window.confirm(
        "Delete this job?"
      )
    )
      return;

    try {

      await api.delete(
        `/jobs/${id}`
      );

      toast.success(
        "Job deleted."
      );

      loadJobs();

    } catch (err) {

      console.error(err);

      toast.error(
        "Unable to delete job."
      );

    }

  }

  function editJob(job: Job) {

    setEditingId(job.id);

    setForm(job);

    setShowForm(true);

  }

  const filteredJobs = useMemo(() => {

    return jobs.filter((job) =>
      job.title
        .toLowerCase()
        .includes(search.toLowerCase())
    );

  }, [jobs, search]);
    if (loading) {
    return (
      <DashboardLayout
        role="recruiter"
        title="Manage Jobs"
      >
        <Loader />
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout
      role="recruiter"
      title="Manage Jobs"
      subtitle="Create, edit and manage all your job postings."
    >

      <div className="mb-8 flex flex-col gap-5 md:flex-row md:items-end md:justify-between">

        <div>

          <label className="mb-2 block font-semibold">
            Search Jobs
          </label>

          <input
            type="text"
            placeholder="Search by title..."
            value={search}
            onChange={(e) =>
              setSearch(e.target.value)
            }
            className="w-full rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500 md:w-80"
          />

        </div>

        <button
          onClick={() => {
            setEditingId(null);
            setForm(emptyJob);
            setShowForm(true);
          }}
          className="rounded-xl bg-blue-600 px-6 py-3 font-semibold text-white transition hover:scale-105 hover:bg-blue-700"
        >
          + Create Job
        </button>

      </div>

      <Card
        title={`My Jobs (${filteredJobs.length})`}
      >

        {filteredJobs.length === 0 ? (

          <EmptyState message="Create your first job posting." />

        ) : (

          <div className="overflow-x-auto">

            <table className="min-w-full">

              <thead>

                <tr className="border-b bg-slate-100">

                  <th className="px-4 py-3 text-left font-semibold">
                    Title
                  </th>

                  <th className="px-4 py-3 text-left font-semibold">
                    Company
                  </th>

                  <th className="px-4 py-3 text-left font-semibold">
                    Status
                  </th>

                  <th className="px-4 py-3 text-left font-semibold">
                    Actions
                  </th>

                </tr>

              </thead>

              <tbody>

                {filteredJobs.map((job) => (

                  <tr
                    key={job.id}
                    className="border-b transition hover:bg-slate-50"
                  >

                    <td className="px-4 py-4 font-semibold">
                      {job.title}
                    </td>

                    <td className="px-4 py-4">
                      {job.company_name}
                    </td>

                    <td className="px-4 py-4">

                      <span
                        className={`rounded-full px-4 py-1 text-sm font-medium ${
                          job.is_active
                            ? "bg-green-100 text-green-700"
                            : "bg-red-100 text-red-700"
                        }`}
                      >
                        {job.status}
                      </span>

                    </td>

                    <td className="space-x-2 px-4 py-4">

                      <button
                        onClick={() => editJob(job)}
                        className="rounded-lg bg-yellow-500 px-4 py-2 text-white transition hover:bg-yellow-600"
                      >
                        Edit
                      </button>

                      <button
                        onClick={() =>
                          deleteJob(job.id)
                        }
                        className="rounded-lg bg-red-600 px-4 py-2 text-white transition hover:bg-red-700"
                      >
                        Delete
                      </button>

                    </td>

                  </tr>

                ))}

              </tbody>

            </table>

          </div>

        )}

      </Card>

      {showForm && (
            

        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4">

          <div className="max-h-[90vh] w-full max-w-4xl overflow-y-auto rounded-2xl bg-white p-8 shadow-2xl">

            <div className="mb-8 flex items-center justify-between">

              <h2 className="text-3xl font-bold">

                {editingId
                  ? "Edit Job"
                  : "Create New Job"}

              </h2>

              <button
                onClick={() => {
                  setShowForm(false);
                  setEditingId(null);
                  setForm(emptyJob);
                }}
                className="rounded-lg bg-red-100 px-4 py-2 text-red-600 hover:bg-red-200"
              >
                ✕
              </button>

            </div>

            <div className="grid gap-5 md:grid-cols-2">

              <input
                name="title"
                placeholder="Job Title"
                value={form.title}
                onChange={handleChange}
                className="rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500"
              />

              <input
                name="company_name"
                placeholder="Company Name"
                value={form.company_name}
                onChange={handleChange}
                className="rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500"
              />

              <input
                name="location"
                placeholder="Location"
                value={form.location}
                onChange={handleChange}
                className="rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500"
              />

              <input
                name="work_mode"
                placeholder="Work Mode"
                value={form.work_mode}
                onChange={handleChange}
                className="rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500"
              />

              <input
                name="employment_type"
                placeholder="Employment Type"
                value={form.employment_type}
                onChange={handleChange}
                className="rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500"
              />

              <input
                name="experience_required"
                placeholder="Experience Required"
                value={form.experience_required}
                onChange={handleChange}
                className="rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500"
              />

              <input
                type="number"
                name="salary_min"
                placeholder="Minimum Salary"
                value={form.salary_min}
                onChange={handleChange}
                className="rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500"
              />

              <input
                type="number"
                name="salary_max"
                placeholder="Maximum Salary"
                value={form.salary_max}
                onChange={handleChange}
                className="rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500"
              />

              <input
                type="number"
                name="total_positions"
                placeholder="Total Positions"
                value={form.total_positions}
                onChange={handleChange}
                className="rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500"
              />

              <input
                type="date"
                name="application_deadline"
                value={form.application_deadline}
                onChange={handleChange}
                className="rounded-xl border border-slate-300 p-3 outline-none focus:border-blue-500"
              />

            </div>

            <textarea
              rows={7}
              name="description"
              placeholder="Enter detailed job description..."
              value={form.description}
              onChange={handleChange}
              className="mt-6 w-full rounded-xl border border-slate-300 p-4 outline-none focus:border-blue-500"
            />

            <div className="mt-8 flex justify-end gap-4">

              <button
                onClick={() => {
                  setShowForm(false);
                  setEditingId(null);
                  setForm(emptyJob);
                }}
                className="rounded-xl border border-slate-300 px-6 py-3 hover:bg-slate-100"
              >
                Cancel
              </button>

              <button
                onClick={saveJob}
                className="rounded-xl bg-blue-600 px-6 py-3 font-semibold text-white transition hover:bg-blue-700"
              >
                {editingId
                  ? "Update Job"
                  : "Create Job"}
              </button>

            </div>

          </div>

        </div>

      )}

    </DashboardLayout>
  );
}