// import { useEffect, useRef, useState } from "react";
// import Sidebar from "../components/Sidebar";
// import api from "../api/api";
// import { toast } from "sonner";
// interface Resume {
//   id: number;
//   original_filename: string;
//   created_at: string;
// }

// export default function Resume() {
//   const fileRef = useRef<HTMLInputElement>(null);

//   const [file, setFile] = useState<File | null>(null);
//   const [resumes, setResumes] = useState<Resume[]>([]);
//   const [loading, setLoading] = useState(false);
//   const [message, setMessage] = useState("");

//   async function loadResumes() {
//     try {
//       const res = await api.get("/resumes");
//       setResumes(res.data);
//     } catch (err) {
//       console.error(err);
//     }
//   }

//   useEffect(() => {
//     loadResumes();
//   }, []);

//   async function uploadResume() {
//     if (!file) return;

//     setLoading(true);
//     setMessage("");

//     try {
//       const formData = new FormData();
//       formData.append("file", file);

//       await api.post("/resumes/upload", formData, {
//         headers: {
//           "Content-Type": "multipart/form-data",
//         },
//       });

//       setMessage("Resume uploaded successfully.");

//       setFile(null);

//       if (fileRef.current) {
//         fileRef.current.value = "";
//       }

//       loadResumes();
//     } catch (err) {
//       console.error(err);
//       setMessage("Upload failed.");
//     }

//     setLoading(false);
//   }

//   async function parseResume(id: number) {
//     try {
//       await api.post(`/resume-profile/${id}`);

//       toast.success("Resume parsed successfully.");
//     } catch (err) {
//       console.error(err);
//       toast.error("Failed to parse resume.");
//     }
//   }

//   async function deleteResume(id: number) {
//     try {
//       await api.delete(`/resumes/${id}`);

//       loadResumes();
//     } catch (err) {
//       console.error(err);
//     }
//   }

//   return (
//     <div className="flex bg-slate-100">
//       <Sidebar role="candidate" />

//       <main className="flex-1 p-8">

//         <h1 className="mb-8 text-4xl font-bold">
//           Resume Management
//         </h1>

//         <div className="rounded-2xl bg-white p-8 shadow">

//           <h2 className="mb-6 text-2xl font-semibold">
//             Upload Resume
//           </h2>

//           <input
//             ref={fileRef}
//             type="file"
//             accept=".pdf,.doc,.docx"
//             onChange={(e) => {
//               if (e.target.files)
//                 setFile(e.target.files[0]);
//             }}
//           />

//           <button
//             onClick={uploadResume}
//             disabled={loading}
//             className="ml-5 rounded-lg bg-blue-600 px-6 py-2 text-white hover:bg-blue-700"
//           >
//             {loading ? "Uploading..." : "Upload"}
//           </button>

//           {message && (
//             <p className="mt-4 text-green-600">
//               {message}
//             </p>
//           )}

//         </div>

//         <div className="mt-10 rounded-2xl bg-white p-8 shadow">

//           <h2 className="mb-6 text-2xl font-semibold">
//             Uploaded Resumes
//           </h2>

//           <table className="w-full">

//             <thead>

//               <tr className="border-b">

//                 <th className="py-3 text-left">
//                   Resume
//                 </th>

//                 <th className="py-3 text-left">
//                   Uploaded
//                 </th>

//                 <th className="py-3 text-left">
//                   Actions
//                 </th>

//               </tr>

//             </thead>

//             <tbody>

//               {resumes.map((resume) => (

//                 <tr
//                   key={resume.id}
//                   className="border-b"
//                 >

//                   <td className="py-4">
//                     {resume.original_filename}
//                   </td>

//                   <td>
//                     {new Date(
//                       resume.created_at
//                     ).toLocaleString()}
//                   </td>

//                   <td className="space-x-3">

//                     <button
//                       onClick={() =>
//                         parseResume(resume.id)
//                       }
//                       className="rounded bg-green-600 px-4 py-2 text-white"
//                     >
//                       Analyze
//                     </button>

//                     <button
//                       onClick={() =>
//                         deleteResume(resume.id)
//                       }
//                       className="rounded bg-red-600 px-4 py-2 text-white"
//                     >
//                       Delete
//                     </button>

//                   </td>

//                 </tr>

//               ))}

//             </tbody>

//           </table>

//         </div>

//       </main>
//     </div>
//   );
// }





import { useEffect, useRef, useState } from "react";
import DashboardLayout from "../components/DashboardLayout";
import Card from "../components/Card";
import EmptyState from "../components/EmptyState";
import api from "../api/api";
import { toast } from "sonner";

interface Resume {
  id: number;
  original_filename: string;
  created_at: string;
}

export default function Resume() {
  const fileRef = useRef<HTMLInputElement>(null);

  const [file, setFile] = useState<File | null>(null);
  const [resumes, setResumes] = useState<Resume[]>([]);
  const [loading, setLoading] = useState(false);

  async function loadResumes() {
    try {
      const res = await api.get("/resumes");
      setResumes(res.data);
    } catch (err) {
      console.error(err);
      toast.error("Unable to load resumes.");
    }
  }

  useEffect(() => {
    loadResumes();
  }, []);

  async function uploadResume() {
    if (!file) {
      toast.warning("Please choose a resume first.");
      return;
    }

    setLoading(true);

    try {
      const formData = new FormData();

      formData.append("file", file);

      await api.post(
        "/resumes/upload",
        formData,
        {
          headers: {
            "Content-Type":
              "multipart/form-data",
          },
        }
      );

      toast.success(
        "Resume uploaded successfully."
      );

      setFile(null);

      if (fileRef.current) {
        fileRef.current.value = "";
      }

      loadResumes();
    } catch (err) {
      console.error(err);

      toast.error(
        "Failed to upload resume."
      );
    }

    setLoading(false);
  }

  async function parseResume(
    id: number
  ) {
    try {
      await api.post(
        `/resume-profile/${id}`
      );

      toast.success(
        "Resume parsed successfully."
      );

      loadResumes();
    } catch (err) {
      console.error(err);

      toast.error(
        "Failed to parse resume."
      );
    }
  }

  async function deleteResume(
    id: number
  ) {
    if (
      !window.confirm(
        "Delete this resume?"
      )
    )
      return;

    try {
      await api.delete(
        `/resumes/${id}`
      );

      toast.success(
        "Resume deleted."
      );

      loadResumes();
    } catch (err) {
      console.error(err);

      toast.error(
        "Failed to delete resume."
      );
    }
  }

  return (
    <DashboardLayout
      role="candidate"
      title="Resume Management"
      subtitle="Upload, analyse and manage your resumes."
    >
      <Card title="Upload Resume">

        <div className="flex flex-col gap-4 md:flex-row md:items-center">

          <input
            ref={fileRef}
            type="file"
            accept=".pdf,.doc,.docx"
            onChange={(e) => {
              if (e.target.files) {
                setFile(
                  e.target.files[0]
                );
              }
            }}
            className="rounded-lg border border-slate-300 p-2"
          />

          <button
            onClick={uploadResume}
            disabled={loading}
            className="rounded-xl bg-blue-600 px-6 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:opacity-60"
          >
            {loading
              ? "Uploading..."
              : "Upload Resume"}
          </button>

        </div>

      </Card>

      <div className="mt-8">

        <Card
          title={`Uploaded Resumes (${resumes.length})`}
        >

          {resumes.length === 0 ? (

            <EmptyState message="No resumes uploaded yet." />

          ) : (

            <div className="overflow-x-auto">

              <table className="min-w-full">

                <thead>

                  <tr className="border-b bg-slate-100">

                    <th className="px-4 py-3 text-left font-semibold">
                      Resume
                    </th>

                    <th className="px-4 py-3 text-left font-semibold">
                      Uploaded
                    </th>

                    <th className="px-4 py-3 text-left font-semibold">
                      Actions
                    </th>

                  </tr>

                </thead>

                <tbody>

                  {resumes.map((resume) => (

                    <tr
                      key={resume.id}
                      className="border-b transition hover:bg-slate-50"
                    >

                      <td className="px-4 py-4 font-medium">
                        {resume.original_filename}
                      </td>

                      <td className="px-4 py-4">
                        {new Date(
                          resume.created_at
                        ).toLocaleString()}
                      </td>

                      <td className="space-x-2 px-4 py-4">

                        <button
                          onClick={() =>
                            parseResume(
                              resume.id
                            )
                          }
                          className="rounded-lg bg-green-600 px-4 py-2 text-white transition hover:bg-green-700"
                        >
                          Analyze
                        </button>

                        <button
                          onClick={() =>
                            deleteResume(
                              resume.id
                            )
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

      </div>

    </DashboardLayout>
  );
}