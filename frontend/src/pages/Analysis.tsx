import { useEffect, useState } from "react";
import DashboardLayout from "../components/DashboardLayout";
import Card from "../components/Card";
import Loader from "../components/Loader";
import api from "../api/api";

interface Resume {
  id: number;
  original_filename: string;
}

interface ResumeAnalysis {
  id: number;
  candidate_id: number;
  original_filename: string;
  stored_filename: string;
  file_path: string;
  file_type: string;
  file_size: number;
  upload_status: string;
  parsing_completed: boolean;
  extracted_text: string | null;
  created_at: string;
}

export default function Analysis() {
  const [resumes, setResumes] = useState<Resume[]>([]);
  const [selectedResume, setSelectedResume] = useState<number>();

  const [analysis, setAnalysis] =
    useState<ResumeAnalysis>();

  const [loading, setLoading] = useState(true);

  async function loadResumes() {
    const res = await api.get("/resumes");

    setResumes(res.data);

    if (res.data.length > 0) {
      setSelectedResume(res.data[0].id);
    }
  }

  async function parseResume(id: number) {
    try {
      await api.post(`/resume-profile/${id}`);
    } catch (err) {
      console.log(err);
    }

    const res = await api.get(`/resumes/${id}`);

    setAnalysis(res.data);
  }

  useEffect(() => {
    async function init() {
      await loadResumes();
      setLoading(false);
    }

    init();
  }, []);

  useEffect(() => {
    if (selectedResume) {
      parseResume(selectedResume);
    }
  }, [selectedResume]);

  if (loading) {
    return (
      <DashboardLayout
        role="candidate"
        title="Resume Analysis"
      >
        <Loader />
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout
      role="candidate"
      title="Resume Analysis"
      subtitle="AI Resume Parsing & Analysis"
    >
      <div className="mb-8">

        <label className="mb-2 block font-semibold">
          Select Resume
        </label>

        <select
          value={selectedResume}
          onChange={(e) =>
            setSelectedResume(Number(e.target.value))
          }
          className="w-96 rounded-lg border p-3"
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

      {analysis && (

        <div className="grid gap-6">

          <Card title="Resume Details">

            <div className="grid gap-4 md:grid-cols-2">

              <p>
                <strong>Filename:</strong>
                {" "}
                {analysis.original_filename}
              </p>

              <p>
                <strong>Type:</strong>
                {" "}
                {analysis.file_type}
              </p>

              <p>
                <strong>Size:</strong>
                {" "}
                {analysis.file_size}
                {" "}bytes
              </p>

              <p>
                <strong>Status:</strong>
                {" "}
                {analysis.upload_status}
              </p>

              <p>
                <strong>Parsed:</strong>
                {" "}
                {analysis.parsing_completed
                  ? "Yes"
                  : "No"}
              </p>

              <p>
                <strong>Uploaded:</strong>
                {" "}
                {new Date(
                  analysis.created_at
                ).toLocaleString()}
              </p>

            </div>

          </Card>

          <Card title="Extracted Resume Text">

            <div className="max-h-[500px] overflow-auto rounded-xl bg-slate-50 p-5 whitespace-pre-wrap text-sm leading-7">

              {analysis.extracted_text ||
                "No extracted text available."}

            </div>

          </Card>

        </div>

      )}

    </DashboardLayout>
  );
}