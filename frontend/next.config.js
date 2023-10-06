/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "pin.it",
      },
    ],
  },
};

module.exports = nextConfig;
