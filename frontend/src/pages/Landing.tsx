import { Link } from "react-router-dom";

export default function Landing() {
  return (
    <div className="min-h-screen bg-slate-50">

      {/* Navbar */}

      <nav className="border-b bg-white shadow-sm">

        <div className="mx-auto flex max-w-7xl items-center justify-between px-8 py-5">

          <h1 className="text-3xl font-bold text-blue-600">
            HireAI
          </h1>

          <div className="flex gap-4">

            <Link
              to="/login"
              className="rounded-lg border px-5 py-2 font-semibold hover:bg-slate-100"
            >
              Login
            </Link>

            <Link
              to="/register"
              className="rounded-lg bg-blue-600 px-5 py-2 font-semibold text-white hover:bg-blue-700"
            >
              Register
            </Link>

          </div>

        </div>

      </nav>

      {/* Hero */}

      <section className="mx-auto grid max-w-7xl items-center gap-10 px-8 py-20 lg:grid-cols-2">

        <div>

          <h1 className="text-6xl font-bold leading-tight text-slate-900">

            AI Powered

            <br />

            Recruitment Platform

          </h1>

          <p className="mt-8 text-xl text-slate-600">

            Hire smarter using AI Resume Screening,
            ATS Scoring, Semantic Search,
            Candidate Ranking and Intelligent Analytics.

          </p>

          <div className="mt-10 flex gap-5">

            <Link
              to="/register"
              className="rounded-xl bg-blue-600 px-8 py-4 text-lg font-semibold text-white hover:bg-blue-700"
            >
              Get Started
            </Link>

            <Link
              to="/login"
              className="rounded-xl border px-8 py-4 text-lg font-semibold hover:bg-white"
            >
              Login
            </Link>

          </div>

        </div>

        <div className="rounded-3xl bg-gradient-to-r from-blue-600 to-indigo-600 p-12 text-white shadow-xl">

          <h2 className="text-4xl font-bold">
            Platform Highlights
          </h2>

          <div className="mt-10 space-y-5 text-lg">

            <p>✓ Resume Parsing</p>

            <p>✓ ATS Evaluation</p>

            <p>✓ Semantic Candidate Search</p>

            <p>✓ AI Resume Ranking</p>

            <p>✓ Recruiter Dashboard</p>

            <p>✓ Candidate Dashboard</p>

            <p>✓ AI Insights</p>

          </div>

        </div>

      </section>

      {/* Features */}

      <section className="mx-auto max-w-7xl px-8 py-20">

        <h2 className="mb-12 text-center text-4xl font-bold">
          Everything You Need
        </h2>

        <div className="grid gap-8 md:grid-cols-2 xl:grid-cols-4">

          <div className="rounded-2xl bg-white p-8 shadow">

            <h3 className="text-2xl font-bold">
              Resume Screening
            </h3>

            <p className="mt-4 text-slate-600">
              Upload and automatically parse resumes using AI.
            </p>

          </div>

          <div className="rounded-2xl bg-white p-8 shadow">

            <h3 className="text-2xl font-bold">
              ATS Matching
            </h3>

            <p className="mt-4 text-slate-600">
              Evaluate candidates with ATS scoring.
            </p>

          </div>

          <div className="rounded-2xl bg-white p-8 shadow">

            <h3 className="text-2xl font-bold">
              Recruiter Analytics
            </h3>

            <p className="mt-4 text-slate-600">
              View AI insights and hiring statistics.
            </p>

          </div>

          <div className="rounded-2xl bg-white p-8 shadow">

            <h3 className="text-2xl font-bold">
              Candidate Ranking
            </h3>

            <p className="mt-4 text-slate-600">
              Rank applicants automatically using Hybrid AI.
            </p>

          </div>

        </div>

      </section>

      {/* Workflow */}

      <section className="bg-white py-20">

        <div className="mx-auto max-w-7xl px-8">

          <h2 className="mb-12 text-center text-4xl font-bold">
            Recruitment Workflow
          </h2>

          <div className="grid gap-8 md:grid-cols-5">

            {[
              "Register",
              "Upload Resume",
              "Apply Job",
              "AI Screening",
              "Hire Best Candidate",
            ].map((step, index) => (

              <div
                key={index}
                className="rounded-2xl border bg-slate-50 p-8 text-center shadow-sm"
              >

                <div className="mx-auto flex h-14 w-14 items-center justify-center rounded-full bg-blue-600 text-xl font-bold text-white">

                  {index + 1}

                </div>

                <h3 className="mt-5 font-bold">
                  {step}
                </h3>

              </div>

            ))}

          </div>

        </div>

      </section>

      {/* Stats */}

      <section className="bg-blue-600 py-20 text-white">

        <div className="mx-auto grid max-w-6xl gap-8 text-center md:grid-cols-4">

          <div>

            <h2 className="text-5xl font-bold">
              AI
            </h2>

            <p className="mt-3">
              Powered Matching
            </p>

          </div>

          <div>

            <h2 className="text-5xl font-bold">
              ATS
            </h2>

            <p className="mt-3">
              Resume Evaluation
            </p>

          </div>

          <div>

            <h2 className="text-5xl font-bold">
              100%
            </h2>

            <p className="mt-3">
              Digital Hiring
            </p>

          </div>

          <div>

            <h2 className="text-5xl font-bold">
              FastAPI
            </h2>

            <p className="mt-3">
              Backend Powered
            </p>

          </div>

        </div>

      </section>

      {/* Footer */}

      <footer className="bg-slate-900 py-10 text-center text-white">

        <h2 className="text-2xl font-bold">
          HireAI Recruitment Platform
        </h2>

        <p className="mt-3 text-slate-400">
          AI Powered Resume Screening System
        </p>

      </footer>

    </div>
  );
}