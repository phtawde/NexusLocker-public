// Footer module JSX code to be reused by every page

export default function Footer() {
  return (
      <div className="footer-container">
        <ul className="disclaimers">
          <li>
            <h2>
              Purpose & Character
            </h2>
            <p>
              This website is a non-commercial school project 
              created strictly for educational demonstration 
              and evaluation purposes. No actual products are 
              for sale, and no monetary transactions occur on 
              this site.
            </p>
          </li>
          <li>
            <h2>
              Copyright & Fair Use
            </h2>
            <p>
              This site utilizes certain copyrighted materials, 
              including press and product photography, under the 
              Fair Use doctrine of U.S. Copyright Law (17 U.S.C. § 107). 
              This material is displayed solely for contextual, 
              criticism, and instructional purposes within an academic 
              framework.
            </p>
          </li>
          <li>
            <h2>
              No Endorsement
            </h2>
            <p>
              All brand names, logos, trademarks, and press images 
              displayed on this site remain the sole property of their 
              respective copyright owners. Their inclusion does not imply 
              any affiliation with, endorsement by, or sponsorship from 
              the brands or creators.
            </p>
          </li>
        </ul>
      </div>
  );
}