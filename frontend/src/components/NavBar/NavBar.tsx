import React from "react";
import Image from "next/image";

type Props = {};

const NavBar = (props: Props) => {
  return (
    <nav className="flex justify-between items-center p-4 bg-white h-[5rem]">
      <div className="">
        <Image
          src="/images/logo.jpg"
          alt="Company Logo"
          width={100}
          height={100}
        />
      </div>
      <div className=""></div>
      <div className=""></div>
    </nav>
  );
};

export default NavBar;
