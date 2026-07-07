// import { useState } from "react";
// import DashboardLayout from "../components/DashboardLayout";
// import Card from "../components/Card";
// import api from "../api/api";
// import { toast } from "sonner";
// import EmptyState from "../components/EmptyState";


// interface Candidate {
//   candidate_id: number;
//   resume_document_id: number;
//   full_name: string | null;
//   email: string | null;
//   location: string | null;
//   semantic_score: number;
//   skill_match_score: number;
//   overall_score: number;
//   matched_skills: string[];
//   missing_skills: string[];
// }

// export default function ATSEvaluation() {
//   const [jobDescription, setJobDescription] =
//     useState("");

//   const [candidateLimit, setCandidateLimit] =
//     useState(10);

//   const [loading, setLoading] =
//     useState(false);

//   const [results, setResults] =
//     useState<Candidate[]>([]);

//   async function evaluate() {
//     if (jobDescription.length < 20) {
//       toast.warning(
//         "Job description should contain at least 20 characters."
//       );
//       return;
//     }

//     setLoading(true);

//     try {
//       const res = await api.post(
//         "/ats/evaluate",
//         {
//           job_description: jobDescription,
//           candidate_limit: candidateLimit,
//         }
//       );

//       setResults(res.data.candidates);

//     } catch (err) {
//       console.error(err);
//       toast.error("ATS Evaluation failed.");
//     } finally {
//       setLoading(false);
//     }
//   }

//   return (
//     <DashboardLayout
//       role="recruiter"
//       title="ATS Evaluation"
//       subtitle="Evaluate candidates using AI and ATS scoring."
//     >

//       <Card title="Job Description">

//         <textarea
//           rows={10}
//           value={jobDescription}
//           onChange={(e) =>
//             setJobDescription(e.target.value)
//           }
//           placeholder="Paste complete job description..."
//           className="w-full rounded-xl border p-4"
//         />

//         <div className="mt-5 flex items-center gap-4">

//           <label>
//             Candidate Limit
//           </label>

//           <input
//             type="number"
//             min={1}
//             max={50}
//             value={candidateLimit}
//             onChange={(e) =>
//               setCandidateLimit(
//                 Number(e.target.value)
//               )
//             }
//             className="w-24 rounded-lg border p-2"
//           />

//           <button
//             onClick={evaluate}
//             disabled={loading}
//             className="rounded-xl bg-blue-600 px-6 py-2 text-white hover:bg-blue-700"
//           >
//             {loading
//               ? "Evaluating..."
//               : "Run ATS"}
//           </button>

//         </div>

//       </Card>

//       <div className="mt-8">

//         <Card title="Ranked Candidates">

//           {results.length === 0 ? (

//             <EmptyState message="Run ATS evaluation to see ranked candidates." />

//           ) : (

//             <table className="w-full">

//               <thead>

//                 <tr className="border-b">

//                   <th className="py-3 text-left">
//                     Candidate
//                   </th>

//                   <th>Email</th>

//                   <th>Semantic</th>

//                   <th>Skill</th>

//                   <th>Overall</th>

//                 </tr>

//               </thead>

//               <tbody>

//                 {results.map((candidate) => (

//                   <tr
//                     key={candidate.candidate_id}
//                     className="border-b"
//                   >

//                     <td className="py-4">

//                       <div>

//                         <div className="font-semibold">
//                           {candidate.full_name ??
//                             `Candidate #${candidate.candidate_id}`}
//                         </div>

//                         <div className="text-sm text-slate-500">
//                           {candidate.location ?? "-"}
//                         </div>

//                       </div>

//                     </td>

//                     <td>
//                       {candidate.email}
//                     </td>

//                     <td>
//                       {candidate.semantic_score.toFixed(1)}%
//                     </td>

//                     <td>
//                       {candidate.skill_match_score.toFixed(1)}%
//                     </td>

//                     <td>

//                       <span className="rounded-lg bg-green-100 px-3 py-1 font-semibold text-green-700">
//                         {candidate.overall_score.toFixed(1)}%
//                       </span>

//                     </td>

//                   </tr>

//                 ))}

//               </tbody>

//             </table>

//           )}

//         </Card>

//       </div>

//       {results.length > 0 && (

//         <div className="mt-8 grid gap-6 md:grid-cols-2">

//           <Card title="Matched Skills">

//             <div className="flex flex-wrap gap-2">

//               {results[0].matched_skills.map((skill) => (

//                 <span
//                   key={skill}
//                   className="rounded-full bg-green-100 px-3 py-1 text-green-700"
//                 >
//                   {skill}
//                 </span>

//               ))}

//             </div>

//           </Card>

//           <Card title="Missing Skills">

//             <div className="flex flex-wrap gap-2">

//               {results[0].missing_skills.map((skill) => (

//                 <span
//                   key={skill}
//                   className="rounded-full bg-red-100 px-3 py-1 text-red-700"
//                 >
//                   {skill}
//                 </span>

//               ))}

//             </div>

//           </Card>

//         </div>

//       )}

//     </DashboardLayout>
//   );
// }



import { useState } from "react";
import DashboardLayout from "../components/DashboardLayout";
import Card from "../components/Card";
import EmptyState from "../components/EmptyState";
import api from "../api/api";
import { toast } from "sonner";

interface Candidate {
  candidate_id: number;
  resume_document_id: number;
  full_name: string | null;
  email: string |null;
  location: string | null;
  semantic_score: number;
  skill_match_score: number;
  overall_score: number;
  matched_skills: string[];
  missing_skills: string[];
}

export default function ATSEvaluation() {
  const [jobDescription, setJobDescription] =
    useState("");

  const [candidateLimit, setCandidateLimit] =
    useState(10);

  const [loading, setLoading] =
    useState(false);

  const [results, setResults] =
    useState<Candidate[]>([]);

  async function evaluate() {
    if (jobDescription.trim().length < 20) {
      toast.warning(
        "Job description should contain at least 20 characters."
      );
      return;
    }

    setLoading(true);

    try {
      const res = await api.post(
        "/ats/evaluate",
        {
          job_description: jobDescription,
          candidate_limit: candidateLimit,
        }
      );

      setResults(res.data.candidates ?? []);

      toast.success(
        "ATS evaluation completed."
      );
    } catch (err) {
      console.error(err);
      toast.error(
        "ATS Evaluation failed."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <DashboardLayout
      role="recruiter"
      title="ATS Evaluation"
      subtitle="Evaluate candidates using AI-powered ATS scoring."
    >

      <Card title="Job Description">

        <textarea
          rows={10}
          value={jobDescription}
          placeholder="Paste complete job description..."
          onChange={(e) =>
            setJobDescription(e.target.value)
          }
          onKeyDown={(e) => {
            if (e.ctrlKey && e.key === "Enter") {
              evaluate();
            }
          }}
          className="w-full rounded-xl border border-slate-300 p-4 outline-none focus:border-blue-500"
        />

        <div className="mt-6 flex flex-col gap-4 md:flex-row md:items-center">

          <div>

            <label className="mb-2 block font-semibold">
              Candidate Limit
            </label>

            <input
              type="number"
              min={1}
              max={50}
              value={candidateLimit}
              onChange={(e) =>
                setCandidateLimit(
                  Number(e.target.value)
                )
              }
              className="w-28 rounded-lg border border-slate-300 p-2"
            />

          </div>

          <button
            onClick={evaluate}
            disabled={loading}
            className="rounded-xl bg-blue-600 px-8 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:opacity-60"
          >
            {loading
              ? "Evaluating..."
              : "Run ATS"}
          </button>

        </div>

      </Card>

      <div className="mt-8">

        <Card
          title={`Ranked Candidates (${results.length})`}
        >

          {results.length === 0 ? (

            <EmptyState message="Run ATS evaluation to view ranked candidates." />

          ) : (

            <div className="overflow-x-auto">

              <table className="min-w-full">

                <thead>

                  <tr className="border-b bg-slate-100">

                    <th className="px-4 py-3 text-left">
                      Candidate
                    </th>

                    <th className="px-4 py-3 text-left">
                      Email
                    </th>

                    <th className="px-4 py-3 text-left">
                      Semantic
                    </th>

                    <th className="px-4 py-3 text-left">
                      Skill
                    </th>

                    <th className="px-4 py-3 text-left">
                      Overall
                    </th>

                  </tr>

                </thead>

                <tbody>

                  {results.map((candidate) => (

                    <tr
                      key={candidate.candidate_id}
                      className="border-b hover:bg-slate-50"
                    >

                      <td className="px-4 py-4">

                        <div>

                          <div className="font-semibold">
                            {candidate.full_name ??
                              `Candidate #${candidate.candidate_id}`}
                          </div>

                          <div className="text-sm text-slate-500">
                            {candidate.location ??
                              "-"}
                          </div>

                        </div>

                      </td>

                      <td className="px-4 py-4">
                        {candidate.email ??
                          "-"}
                      </td>

                      <td className="px-4 py-4">
                        {candidate.semantic_score.toFixed(
                          1
                        )}
                        %
                      </td>

                      <td className="px-4 py-4">
                        {candidate.skill_match_score.toFixed(
                          1
                        )}
                        %
                      </td>

                      <td className="px-4 py-4">

                        <span className="rounded-full bg-green-100 px-4 py-1 font-semibold text-green-700">

                          {candidate.overall_score.toFixed(
                            1
                          )}
                          %

                        </span>

                      </td>

                    </tr>

                  ))}

                </tbody>

              </table>

            </div>

          )}

        </Card>

      </div>

      {results.length > 0 && (

        <div className="mt-8 grid gap-6 lg:grid-cols-2">

          <Card title="Matched Skills">

            <div className="flex flex-wrap gap-3">

              {results[0].matched_skills.length ===
              0 ? (
                <EmptyState message="No matched skills." />
              ) : (
                results[0].matched_skills.map(
                  (skill) => (
                    <span
                      key={skill}
                      className="rounded-full bg-green-100 px-4 py-2 text-green-700"
                    >
                      {skill}
                    </span>
                  )
                )
              )}

            </div>

          </Card>

          <Card title="Missing Skills">

            <div className="flex flex-wrap gap-3">

              {results[0].missing_skills.length ===
              0 ? (
                <EmptyState message="No missing skills." />
              ) : (
                results[0].missing_skills.map(
                  (skill) => (
                    <span
                      key={skill}
                      className="rounded-full bg-red-100 px-4 py-2 text-red-700"
                    >
                      {skill}
                    </span>
                  )
                )
              )}

            </div>

          </Card>

        </div>

      )}

    </DashboardLayout>
  );
}