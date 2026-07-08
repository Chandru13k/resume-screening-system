// import { FormEvent, useState } from "react";
// import { Link, useNavigate } from "react-router-dom";
// import api from "../api/api";
// import { toast } from "sonner";

// export default function Register() {
//   const navigate = useNavigate();

//   const [role, setRole] = useState("candidate");
//   const [name, setName] = useState("");
//   const [companyName, setCompanyName] = useState("");
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [confirmPassword, setConfirmPassword] = useState("");

//   const [loading, setLoading] = useState(false);
//   const [error, setError] = useState("");
//   const [success, setSuccess] = useState("");

//   async function handleRegister(e: FormEvent) {
//     e.preventDefault();

//     setError("");
//     setSuccess("");

//     if (password !== confirmPassword) {
//       setError("Passwords do not match.");
//       return;
//     }

//     setLoading(true);

//     try {
//       const endpoint =
//         role === "candidate"
//           ? "/auth/register/candidate"
//           : "/auth/register/recruiter";

//       const payload =
//         role === "candidate"
//           ? {
//               name,
//               email,
//               password,
//             }
//           : {
//               name,
//               company_name: companyName,
//               email,
//               password,
//             };

//       await api.post(endpoint, payload);

//       setSuccess("Registration Successful!");

//       setTimeout(() => {
//         navigate("/login");
//       }, 1200);
//     } catch (err: any) {
//       setError(err?.response?.data?.detail || "Registration Failed");
//     } finally {
//       setLoading(false);
//     }
//   }

//   return (
//     <div className="flex min-h-screen items-center justify-center bg-slate-100 py-10">
//       <div className="w-full max-w-lg rounded-2xl bg-white p-8 shadow-xl">
//         <h1 className="mb-2 text-center text-3xl font-bold">
//           Create Account
//         </h1>

//         <p className="mb-8 text-center text-gray-500">
//           AI Recruitment Platform
//         </p>

//         <form onSubmit={handleRegister} className="space-y-5">

//           <div>
//             <label className="mb-2 block font-medium">Register As</label>

//             <select
//               className="w-full rounded-lg border p-3"
//               value={role}
//               onChange={(e) => setRole(e.target.value)}
//             >
//               <option value="candidate">Candidate</option>
//               <option value="recruiter">Recruiter</option>
//             </select>
//           </div>

//           <div>
//             <label className="mb-2 block font-medium">Full Name</label>

//             <input
//               className="w-full rounded-lg border p-3"
//               value={name}
//               onChange={(e) => setName(e.target.value)}
//               placeholder="Enter Full Name"
//               required
//             />
//           </div>

//           {role === "recruiter" && (
//             <div>
//               <label className="mb-2 block font-medium">
//                 Company Name
//               </label>

//               <input
//                 className="w-full rounded-lg border p-3"
//                 value={companyName}
//                 onChange={(e) => setCompanyName(e.target.value)}
//                 placeholder="Company Name"
//                 required
//               />
//             </div>
//           )}

//           <div>
//             <label className="mb-2 block font-medium">Email</label>

//             <input
//               type="email"
//               className="w-full rounded-lg border p-3"
//               value={email}
//               onChange={(e) => setEmail(e.target.value)}
//               placeholder="Enter Email"
//               required
//             />
//           </div>

//           <div>
//             <label className="mb-2 block font-medium">Password</label>

//             <input
//               type="password"
//               className="w-full rounded-lg border p-3"
//               value={password}
//               onChange={(e) => setPassword(e.target.value)}
//               placeholder="Minimum 8 characters"
//               required
//             />
//           </div>

//           <div>
//             <label className="mb-2 block font-medium">
//               Confirm Password
//             </label>

//             <input
//               type="password"
//               className="w-full rounded-lg border p-3"
//               value={confirmPassword}
//               onChange={(e) => setConfirmPassword(e.target.value)}
//               placeholder="Confirm Password"
//               required
//             />
//           </div>

//           {error && (
//             <div className="rounded-lg bg-red-100 p-3 text-red-600">
//               {error}
//             </div>
//           )}

//           {success && (
//             <div className="rounded-lg bg-green-100 p-3 text-green-700">
//               {success}
//             </div>
//           )}

//           <button
//             type="submit"
//             disabled={loading}
//             className="w-full rounded-lg bg-blue-600 py-3 font-semibold text-white hover:bg-blue-700"
//           >
//             {loading ? "Creating Account..." : "Create Account"}
//           </button>
//         </form>

//         <div className="mt-8 text-center">
//           <p className="text-gray-600">Already have an account?</p>

//           <Link
//             to="/login"
//             className="font-semibold text-blue-600 hover:underline"
//           >
//             Login
//           </Link>
//         </div>
//       </div>
//     </div>
//   );
// }



import { FormEvent, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../api/api";
import { toast } from "sonner";

export default function Register() {
  const navigate = useNavigate();

  const [role, setRole] = useState("candidate");

  // Common
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] =
    useState("");

  // Candidate
  const [fullName, setFullName] = useState("");
  const [phone, setPhone] = useState("");
  const [location, setLocation] = useState("");
  const [github, setGithub] = useState("");
  const [linkedin, setLinkedin] = useState("");
  const [portfolio, setPortfolio] = useState("");

  // Recruiter
  const [recruiterName, setRecruiterName] =
    useState("");

  const [companyName, setCompanyName] =
    useState("");

  const [designation, setDesignation] =
    useState("");

  const [companyWebsite, setCompanyWebsite] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  async function handleRegister(
    e: FormEvent
  ) {
    e.preventDefault();

    if (password !== confirmPassword) {
      toast.error(
        "Passwords do not match."
      );
      return;
    }

    setLoading(true);

    try {

      const endpoint =
        role === "candidate"
          ? "/auth/register/candidate"
          : "/auth/register/recruiter";

      const payload =
        role === "candidate"
          ? {

              full_name: fullName,

              email,

              password,

              phone:
                phone || null,

              location:
                location || null,

              github_url:
                github || null,

              linkedin_url:
                linkedin || null,

              portfolio_url:
                portfolio || null,

              coding_profiles: {},

            }
          : {

              recruiter_name:
                recruiterName,

              company_name:
                companyName,

              designation,

              company_website:
                companyWebsite || null,

              email,

              password,

            };

      await api.post(
        endpoint,
        payload
      );

      toast.success(
        "Registration successful."
      );

      setTimeout(() => {
        navigate("/login");
      }, 1200);

    } catch (err: any) {

      toast.error(
        err?.response?.data?.detail ??
        "Registration failed."
      );

    } finally {

      setLoading(false);

    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-slate-100 py-10">

      <div className="w-full max-w-2xl rounded-2xl bg-white p-8 shadow-xl">

        <h1 className="mb-2 text-center text-3xl font-bold">
          Create Account
        </h1>

        <p className="mb-8 text-center text-slate-500">
          AI Recruitment Platform
        </p>

        <form
          onSubmit={handleRegister}
          className="space-y-5"
        >

          <div>

            <label className="mb-2 block font-medium">
              Register As
            </label>

            <select
              value={role}
              onChange={(e) =>
                setRole(e.target.value)
              }
              className="w-full rounded-lg border p-3"
            >

              <option value="candidate">
                Candidate
              </option>

              <option value="recruiter">
                Recruiter
              </option>

            </select>

          </div>
                    {role === "candidate" && (
            <>

              <div>

                <label className="mb-2 block font-medium">
                  Full Name
                </label>

                <input
                  value={fullName}
                  onChange={(e) =>
                    setFullName(e.target.value)
                  }
                  placeholder="Enter full name"
                  className="w-full rounded-lg border p-3"
                  required
                />

              </div>

              <div className="grid gap-5 md:grid-cols-2">

                <div>

                  <label className="mb-2 block font-medium">
                    Phone
                  </label>

                  <input
                    value={phone}
                    onChange={(e) =>
                      setPhone(e.target.value)
                    }
                    placeholder="Phone Number"
                    className="w-full rounded-lg border p-3"
                  />

                </div>

                <div>

                  <label className="mb-2 block font-medium">
                    Location
                  </label>

                  <input
                    value={location}
                    onChange={(e) =>
                      setLocation(e.target.value)
                    }
                    placeholder="City"
                    className="w-full rounded-lg border p-3"
                  />

                </div>

              </div>

              <div>

                <label className="mb-2 block font-medium">
                  GitHub URL
                </label>

                <input
                  value={github}
                  onChange={(e) =>
                    setGithub(e.target.value)
                  }
                  placeholder="https://github.com/username"
                  className="w-full rounded-lg border p-3"
                />

              </div>

              <div>

                <label className="mb-2 block font-medium">
                  LinkedIn URL
                </label>

                <input
                  value={linkedin}
                  onChange={(e) =>
                    setLinkedin(e.target.value)
                  }
                  placeholder="https://linkedin.com/in/username"
                  className="w-full rounded-lg border p-3"
                />

              </div>

              <div>

                <label className="mb-2 block font-medium">
                  Portfolio URL
                </label>

                <input
                  value={portfolio}
                  onChange={(e) =>
                    setPortfolio(e.target.value)
                  }
                  placeholder="https://portfolio.com"
                  className="w-full rounded-lg border p-3"
                />

              </div>

            </>
          )}

          {role === "recruiter" && (
            <>
                          <div>

                <label className="mb-2 block font-medium">
                  Recruiter Name
                </label>

                <input
                  value={recruiterName}
                  onChange={(e) =>
                    setRecruiterName(e.target.value)
                  }
                  placeholder="Enter recruiter name"
                  className="w-full rounded-lg border p-3"
                  required
                />

              </div>

              <div>

                <label className="mb-2 block font-medium">
                  Company Name
                </label>

                <input
                  value={companyName}
                  onChange={(e) =>
                    setCompanyName(e.target.value)
                  }
                  placeholder="Company Name"
                  className="w-full rounded-lg border p-3"
                  required
                />

              </div>

              <div>

                <label className="mb-2 block font-medium">
                  Designation
                </label>

                <input
                  value={designation}
                  onChange={(e) =>
                    setDesignation(e.target.value)
                  }
                  placeholder="HR Manager / Recruiter"
                  className="w-full rounded-lg border p-3"
                  required
                />

              </div>

              <div>

                <label className="mb-2 block font-medium">
                  Company Website
                </label>

                <input
                  value={companyWebsite}
                  onChange={(e) =>
                    setCompanyWebsite(e.target.value)
                  }
                  placeholder="https://company.com"
                  className="w-full rounded-lg border p-3"
                />

              </div>

            </>
          )}

          <div>

            <label className="mb-2 block font-medium">
              Email
            </label>

            <input
              type="email"
              value={email}
              onChange={(e) =>
                setEmail(e.target.value)
              }
              placeholder="Enter Email"
              className="w-full rounded-lg border p-3"
              required
            />

          </div>

          <div className="grid gap-5 md:grid-cols-2">

            <div>

              <label className="mb-2 block font-medium">
                Password
              </label>

              <input
                type="password"
                value={password}
                onChange={(e) =>
                  setPassword(e.target.value)
                }
                placeholder="Minimum 8 characters"
                className="w-full rounded-lg border p-3"
                required
              />

            </div>

            <div>

              <label className="mb-2 block font-medium">
                Confirm Password
              </label>

              <input
                type="password"
                value={confirmPassword}
                onChange={(e) =>
                  setConfirmPassword(
                    e.target.value
                  )
                }
                placeholder="Confirm Password"
                className="w-full rounded-lg border p-3"
                required
              />

            </div>

          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full rounded-xl bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:opacity-60"
          >
            {loading
              ? "Creating Account..."
              : "Create Account"}
          </button>

        </form>

        <div className="mt-8 text-center">

          <p className="text-slate-600">
            Already have an account?
          </p>

          <Link
            to="/login"
            className="font-semibold text-blue-600 hover:underline"
          >
            Login
          </Link>

        </div>

      </div>

    </div>
  );
}