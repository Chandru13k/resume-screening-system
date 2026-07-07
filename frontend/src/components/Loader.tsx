export default function Loader() {
  return (
    <div className="flex h-[60vh] items-center justify-center">

      <div className="text-center">

        <div className="mx-auto h-16 w-16 animate-spin rounded-full border-4 border-blue-600 border-t-transparent"></div>

        <p className="mt-5 text-slate-500">
          Loading...
        </p>

      </div>

    </div>
  );
}