import React from "react";
<<<<<<< HEAD

export default function IndexPage(props) {
  return (
    <div className="text-center h-screen flex justify-center flex-col items-center p-4">
      <img
        className="w-full lg:w-[60%]"
        src="/static/django_breeze/django-breeze-logo.jpg"
        alt=""
      />
      <h1 className="text-3xl font-bold">Welcome, Django Breeze</h1>
      <p className="text-green-600 mb-5">Your project is setup successfully!</p>
      <h3 className="text-slate-500">Powered by:</h3>
      <div className="lg:flex space-y-2 lg:space-y-0 lg:space-x-3 mt-3">
        {props.packages.map((framework, i) => (
          <PackageCard key={i} framework={framework} />
        ))}
      </div>
    </div>
  );
}

function PackageCard({ framework }) {
  return (
    <div className="px-12 py-6 border border-purple-500 text-purple-600 rounded-lg hover:scale-105 transition-all cursor-pointer duration-200">
      <p>{framework}</p>
=======
import { DjangoHeader, DjangoMain, DjangoFooter } from "../Layout/Fullstack";

export default function IndexPage(props) {
  const version = "0.4.0";

  return (
    <div>
      <DjangoHeader version={version} />
      <DjangoMain version={version} />
      <DjangoFooter version={version} />
>>>>>>> a784bf9 (two commit)
    </div>
  );
}
