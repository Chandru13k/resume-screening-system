interface Props {
  message: string;
}

export default function EmptyState({
  message,
}: Props) {
  return (
    <div className="rounded-2xl border-2 border-dashed border-slate-300 bg-slate-50 py-16 text-center">

      <div className="text-6xl">
        📂
      </div>

      <h2 className="mt-5 text-xl font-semibold">
        Nothing Here
      </h2>

      <p className="mt-2 text-slate-500">
        {message}
      </p>

    </div>
  );
}