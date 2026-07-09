// import { useState } from "react";
// import DashboardLayout from "../components/DashboardLayout";
// import Card from "../components/Card";
// import api from "../api/api";
// import { toast } from "sonner";
// import EmptyState from "../components/EmptyState";

// export default function SemanticSearch() {
//   const [query, setQuery] = useState("");
//   const [loading, setLoading] = useState(false);
//   const [results, setResults] = useState<any[]>([]);

//   async function search() {
//     if (!query.trim()) return;

//     setLoading(true);

//     try {
//       const res = await api.post(
//         "/search/candidates",
//         {
//           query,
//         }
//       );

//       setResults(
//         res.data.candidates ||
//         res.data.results ||
//         []
//       );
//     } catch (err) {
//       console.error(err);
//       toast.error("Search failed.");
//     } finally {
//       setLoading(false);
//     }
//   }

//   return (
//     <DashboardLayout
//       role="recruiter"
//       title="Semantic Candidate Search"
//       subtitle="Find candidates using natural language."
//     >

//       <Card title="Search">

//         <textarea
//           rows={6}
//           placeholder="Example:

// Looking for a Python Backend Developer with FastAPI, PostgreSQL, Docker and AWS experience..."
//           value={query}
//           onChange={(e) =>
//             setQuery(e.target.value)
//           }
//           className="w-full rounded-xl border p-4"
//         />

//         <button
//           onClick={search}
//           disabled={loading}
//           className="mt-5 rounded-xl bg-blue-600 px-8 py-3 text-white hover:bg-blue-700"
//         >
//           {loading
//             ? "Searching..."
//             : "Search Candidates"}
//         </button>

//       </Card>

//       <div className="mt-8">

//         <Card title="Results">

//           {results.length === 0 ? (

//             <EmptyState message="No matching candidates found." />

//           ) : (

//             <table className="w-full">

//               <thead>

//                 <tr className="border-b">

//                   <th className="py-3 text-left">
//                     Candidate
//                   </th>

//                   <th>
//                     Resume
//                   </th>

//                   <th>
//                     Score
//                   </th>

//                 </tr>

//               </thead>

//               <tbody>

//                 {results.map(
//                   (candidate: any, index) => (

//                     <tr
//                       key={index}
//                       className="border-b"
//                     >

//                       <td className="py-4">
//                         {candidate.name ??
//                           candidate.candidate_name ??
//                           candidate.candidate_id}
//                       </td>

//                       <td>
//                         {candidate.resume_id}
//                       </td>

//                       <td>
//                         {candidate.score ??
//                           candidate.similarity_score ??
//                           "-"}
//                       </td>

//                     </tr>

//                   )
//                 )}

//               </tbody>

//             </table>

//           )}

//         </Card>

//       </div>

//     </DashboardLayout>
//   );
// }


import { useState } from "react";
import DashboardLayout from "../components/DashboardLayout";
import Card from "../components/Card";
import EmptyState from "../components/EmptyState";
import api from "../api/api";
import { toast } from "sonner";

interface SearchResult {
  candidate_id: number;
  candidate_name?: string;
  name?: string;
  resume_id: number;
  score?: number;
  similarity_score?: number;
}

export default function SemanticSearch() {
  const [query, setQuery] = useState("");

  const [loading, setLoading] =
    useState(false);

  const [results, setResults] =
    useState<SearchResult[]>([]);

  async function search() {
    if (!query.trim()) {
      toast.warning(
        "Please enter a search query."
      );
      return;
    }

    setLoading(true);

    try {
      const res = await api.post(
        "/search/candidates",
        {
          query,
        }
      );

      setResults(
        res.data.candidates ??
          res.data.results ??
          []
      );
    } catch (err) {
      console.error(err);

      toast.error("Search failed.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <DashboardLayout
      role="recruiter"
      title="Semantic Candidate Search"
      subtitle="Find candidates using natural language."
    >
      <Card title="AI Search">

        <textarea
          rows={6}
          value={query}
          placeholder={`Example:

Looking for a Python Backend Developer with FastAPI,
PostgreSQL, Docker, Redis and AWS experience...`}
          onChange={(e) =>
            setQuery(e.target.value)
          }
          onKeyDown={(e) => {
            if (
              e.key === "Enter" &&
              e.ctrlKey
            ) {
              search();
            }
          }}
          className="w-full rounded-xl border border-slate-300 p-4 outline-none focus:border-blue-500"
        />

        <div className="mt-4 flex items-center justify-between">

          <p className="text-sm text-slate-500">
            Press Ctrl + Enter to search
          </p>

          <button
            onClick={search}
            disabled={loading}
            className="rounded-xl bg-blue-600 px-8 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:opacity-60"
          >
            {loading
              ? "Searching..."
              : "Search Candidates"}
          </button>

        </div>

      </Card>

      <div className="mt-8">

        <Card
          title={`Results (${results.length})`}
        >

          {results.length === 0 ? (

            <EmptyState message="No matching candidates found." />

          ) : (

            <div className="overflow-x-auto">

              <table className="min-w-full">

                <thead>

                  <tr className="border-b bg-slate-100">

                    <th className="px-4 py-3 text-left font-semibold">
                      Candidate
                    </th>

                    <th className="px-4 py-3 text-left font-semibold">
                      Resume
                    </th>

                    <th className="px-4 py-3 text-left font-semibold">
                      Match Score
                    </th>

                  </tr>

                </thead>

                <tbody>

                  {results.map(
                    (candidate) => (

                      <tr
                        key={candidate.candidate_id}
                        className="border-b transition hover:bg-slate-50"
                      >

                        <td className="px-4 py-4 font-medium">
                          {candidate.full_name || `Candidate #${candidate.candidate_id}`}
                        </td>

                        <td className="px-4 py-4">
                          #{candidate.resume_id}
                        </td>

                        <td className="px-4 py-4">

                          <span className="rounded-full bg-green-100 px-4 py-1 font-semibold text-green-700">

                            {(
                              candidate.score ??
                              candidate.similarity_score ??
                              0
                            ).toFixed(2)}

                          </span>

                        </td>

                      </tr>

                    )
                  )}

                </tbody>

              </table>

            </div>

          )}

        </Card>

      </div>

    </DashboardLayout>
  );
}