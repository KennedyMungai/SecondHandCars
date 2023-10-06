import React from "react";
import Image from "next/image";
import Link from "next/link";
import { BsFillPersonFill } from "react-icons/bs";

type Props = {};

const NavBar = (props: Props) => {
  return (
    <nav className="flex justify-between items-center p-[1rem] bg-zinc-100 h-[5rem] text-black shadow-md sticky">
      <div className="rounded-full">
        <Image
          src="/images/logo.jpg"
          alt="Company Logo"
          width={100}
          height={100}
        />
      </div>
      <div className="">
        <h1 className="font-bold text-xl uppercase">Second Hand Cars</h1>
      </div>
      <div>
        <Link href={"/signin"} className="flex flex-row gap-2 items-center">
          <BsFillPersonFill className="text-xl" />
          <p className="text-bold">Sign In</p>
        </Link>
      </div>
    </nav>
  );
};

export default NavBar;
