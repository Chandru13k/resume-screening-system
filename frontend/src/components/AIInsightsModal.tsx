interface Props {
  open: boolean;
  onClose: () => void;
  data: any;
}

export default function AIInsightsModal({
  open,
  onClose,
  data,
}: Props) {
  if (!open) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">

      <div className="max-h-[85vh] w-full max-w-4xl overflow-auto rounded-2xl bg-white p-8 shadow-2xl">

        <div className="mb-6 flex items-center justify-between">

          <h2 className="text-3xl font-bold">
            AI Candidate Insights
          </h2>

          <button
            onClick={onClose}
            className="rounded-lg bg-red-500 px-4 py-2 text-white"
          >
            Close
          </button>

        </div>

        {!data ? (

          <div className="text-center">
            No AI insights available.
          </div>

        ) : (

          <div className="space-y-6">

            {Object.entries(data).map(([key, value]) => (

              <div
                key={key}
                className="rounded-xl border p-5"
              >

                <h3 className="mb-3 text-lg font-bold capitalize">
                  {key.replaceAll("_", " ")}
                </h3>

                <p className="whitespace-pre-wrap text-slate-600">
                  {Array.isArray(value)
                    ? value.join(", ")
                    : String(value)}
                </p>

              </div>

            ))}

          </div>

        )}

      </div>

    </div>
  );
}